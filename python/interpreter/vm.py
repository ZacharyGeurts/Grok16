"""GrokPy VM — GROKPY12 stack machine, field AI globals on boot."""
from __future__ import annotations

import os
from typing import Any

from grok_builtins import grok_ai_status, grok_truth_floor, make_builtins
from objects import Code, GrokFunction
from grok_opcode import (
    COMPARE_EQ,
    COMPARE_GE,
    COMPARE_GT,
    COMPARE_LE,
    COMPARE_LT,
    COMPARE_NE,
    Op,
)


class VMError(Exception):
    pass


class _ReturnSignal(Exception):
    def __init__(self, value: Any) -> None:
        self.value = value


class Frame:
    __slots__ = ("code", "globals", "locals")

    def __init__(self, code: Code, globals: dict[str, Any], locals: dict[str, Any] | None = None) -> None:
        self.code = code
        self.globals = globals
        self.locals = locals if locals is not None else {}

    def load_name(self, idx: int) -> Any:
        name = self.code.varnames[idx]
        if name in self.locals:
            return self.locals[name]
        if name in self.globals:
            return self.globals[name]
        raise VMError(f"name not defined: {name}")

    def store_name(self, idx: int, value: Any) -> None:
        self.locals[self.code.varnames[idx]] = value

    def store_global(self, idx: int, value: Any) -> None:
        self.globals[self.code.names[idx]] = value


class GrokVM:
    def __init__(self) -> None:
        self.globals: dict[str, Any] = dict(make_builtins())
        if os.environ.get("GROKPY_FIELD") == "1" or os.environ.get("PYTHONG_FIELD") == "1":
            self.globals["__truth_floor__"] = grok_truth_floor()
            self.globals["__grokpy_ai__"] = grok_ai_status()

    def run_source(self, source: str) -> Any:
        from compiler import compile_source

        return self.run_code(compile_source(source))

    def run_code(self, code: Code) -> Any:
        frame = Frame(code, self.globals)
        return self._run_frame(frame)

    def _run_frame(self, frame: Frame) -> Any:
        stack: list[Any] = []
        code = frame.code
        ip = 0
        try:
            while ip < len(code.instrs):
                op_raw, arg = code.instrs[ip]
                op = Op(op_raw)
                ip += 1

                if op == Op.LOAD_CONST:
                    stack.append(code.consts[arg])
                elif op == Op.LOAD_NAME:
                    stack.append(frame.load_name(arg))
                elif op == Op.LOAD_GLOBAL:
                    name = code.names[arg]
                    if name not in frame.globals:
                        raise VMError(f"global not defined: {name}")
                    stack.append(frame.globals[name])
                elif op == Op.STORE_NAME:
                    frame.store_name(arg, stack.pop())
                elif op == Op.STORE_GLOBAL:
                    frame.store_global(arg, stack.pop())
                elif op == Op.POP_TOP:
                    stack.pop()
                elif op == Op.DUP_TOP:
                    stack.append(stack[-1])
                elif op == Op.BINARY_ADD:
                    b, a = stack.pop(), stack.pop()
                    stack.append(a + b)
                elif op == Op.BINARY_SUB:
                    b, a = stack.pop(), stack.pop()
                    stack.append(a - b)
                elif op == Op.BINARY_MUL:
                    b, a = stack.pop(), stack.pop()
                    stack.append(a * b)
                elif op == Op.BINARY_TRUE_DIV:
                    b, a = stack.pop(), stack.pop()
                    stack.append(a / b)
                elif op == Op.BINARY_FLOOR_DIV:
                    b, a = stack.pop(), stack.pop()
                    stack.append(a // b)
                elif op == Op.BINARY_MOD:
                    b, a = stack.pop(), stack.pop()
                    stack.append(a % b)
                elif op == Op.BINARY_POW:
                    b, a = stack.pop(), stack.pop()
                    stack.append(a ** b)
                elif op == Op.UNARY_NEG:
                    stack.append(-stack.pop())
                elif op == Op.UNARY_NOT:
                    stack.append(not stack.pop())
                elif op == Op.COMPARE_OP:
                    b, a = stack.pop(), stack.pop()
                    cmp_ops = {
                        COMPARE_EQ: lambda x, y: x == y,
                        COMPARE_NE: lambda x, y: x != y,
                        COMPARE_LT: lambda x, y: x < y,
                        COMPARE_LE: lambda x, y: x <= y,
                        COMPARE_GT: lambda x, y: x > y,
                        COMPARE_GE: lambda x, y: x >= y,
                    }
                    stack.append(cmp_ops[arg](a, b))
                elif op == Op.JUMP_FORWARD:
                    ip = arg
                elif op == Op.JUMP_IF_FALSE:
                    if not stack.pop():
                        ip = arg
                elif op == Op.JUMP_IF_TRUE:
                    if stack.pop():
                        ip = arg
                elif op == Op.GET_ITER:
                    stack.append(iter(stack.pop()))
                elif op == Op.FOR_ITER:
                    it = stack[-1]
                    try:
                        stack.append(next(it))
                    except StopIteration:
                        stack.pop()
                        ip = arg
                elif op == Op.BUILD_LIST:
                    items = [stack.pop() for _ in range(arg)][::-1]
                    stack.append(items)
                elif op == Op.BUILD_TUPLE:
                    items = [stack.pop() for _ in range(arg)][::-1]
                    stack.append(tuple(items))
                elif op == Op.CALL:
                    argc = arg
                    args = [stack.pop() for _ in range(argc)][::-1]
                    fn = stack.pop()
                    if isinstance(fn, GrokFunction):
                        ret = self._call_function(fn, args)
                        if ret is not None:
                            stack.append(ret)
                    elif callable(fn):
                        stack.append(fn(*args))
                    else:
                        raise VMError("call on non-callable")
                elif op == Op.RETURN:
                    raise _ReturnSignal(stack.pop() if stack else None)
                elif op == Op.MAKE_FUNCTION:
                    ndef = arg
                    defaults = [stack.pop() for _ in range(ndef)][::-1] if ndef else []
                    fn_code = stack.pop()
                    stack.append(
                        GrokFunction(
                            name=fn_code.name,
                            argnames=list(fn_code.varnames[: fn_code.argcount]),
                            code=fn_code,
                            defaults=defaults,
                        )
                    )
                else:
                    raise VMError(f"unhandled op: {op}")
        except _ReturnSignal as sig:
            return sig.value
        return None

    def _call_function(self, fn: GrokFunction, args: list[Any]) -> Any:
        local: dict[str, Any] = {}
        nargs = len(fn.argnames)
        ndef = len(fn.defaults)
        pos_required = nargs - ndef
        for i, name in enumerate(fn.argnames):
            if i < len(args):
                local[name] = args[i]
            elif i >= pos_required:
                local[name] = fn.defaults[i - pos_required]
            else:
                raise VMError(f"missing arg: {name}")
        child_globals = dict(fn.globals) if hasattr(fn, "globals") else dict(self.globals)
        if fn.closure:
            child_globals.update(fn.closure)
        frame = Frame(fn.code, child_globals, local)
        return self._run_frame(frame)
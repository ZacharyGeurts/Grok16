/**
 * Client-side language discern for static GitHub Pages — kind guesses for programmers.
 */
(function (global) {
  "use strict";

  const HEURISTICS = [
    { lang: "python", re: /(^#!.*python)|(\bdef\s+\w+\s*\()|(\bimport\s+\w+)|(\bfrom\s+\w+\s+import)|(\bprint\s*\()/m, w: 12 },
    { lang: "ammolang", re: /(\bSAY\b|\bRUN\b|\bFAST\b|\bFORGE\b|\bASSIST\b)/, w: 14 },
    { lang: "shell", re: /^#!\/bin\/(ba)?sh/m, w: 20 },
    { lang: "rust", re: /\b(fn\s+main\s*\()|\b(let\s+mut\s+)|\bpub\s+fn\b|\buse\s+std::/, w: 12 },
    { lang: "go", re: /\bpackage\s+main\b|\bfunc\s+main\s*\(/, w: 14 },
    { lang: "java", re: /\bpublic\s+class\s+\w+|\bpublic\s+static\s+void\s+main/, w: 12 },
    { lang: "kotlin", re: /\bfun\s+main\s*\(|\bval\s+\w+|\bdata\s+class\b/, w: 12 },
    { lang: "csharp", re: /\bnamespace\s+\w+|\busing\s+System;|\bclass\s+\w+.*\{/, w: 11 },
    { lang: "typescript", re: /\binterface\s+\w+|\btype\s+\w+\s*=|: \w+(\[\])?\s*=>|import .+ from /, w: 10 },
    { lang: "javascript", re: /\bconsole\.log\s*\(|\bconst\s+\w+\s*=|\blet\s+\w+\s*=|\bfunction\s+\w+\s*\(/, w: 9 },
    { lang: "cxx", re: /#include\s*[<"]|\bstd::|\bint\s+main\s*\(|::\w+/, w: 10 },
    { lang: "c", re: /#include\s*[<"]|\bint\s+main\s*\(|\bprintf\s*\(/, w: 9 },
    { lang: "zig", re: /\bpub\s+fn\s+main\b|\bconst\s+std\b/, w: 14 },
    { lang: "swift", re: /\bimport\s+Foundation\b|\bfunc\s+\w+.*->/, w: 11 },
    { lang: "ruby", re: /\bdef\s+\w+|\bend\b|\bputs\s+/, w: 10 },
    { lang: "php", re: /<\?php|\$\w+\s*=/, w: 14 },
    { lang: "perl", re: /^#!.*perl|\bmy\s+\$\w+|\buse\s+strict/, w: 12 },
    { lang: "lua", re: /\blocal\s+\w+|\bfunction\s+\w+\s*\(/, w: 10 },
    { lang: "haskell", re: /\bmodule\s+\w+|\bwhere\b|\b::\s*/, w: 11 },
    { lang: "elixir", re: /\bdefmodule\s+\w+|\bdef\s+\w+.*do\b/, w: 12 },
    { lang: "erlang", re: /-module\(|\b-export\(/, w: 14 },
    { lang: "clojure", re: /\(defn\s+|\(ns\s+/, w: 12 },
    { lang: "lisp", re: /\(defun\s+|\(defmacro\s+/, w: 11 },
    { lang: "fortran", re: /\bprogram\s+\w+|\bend\s+program\b|\bimplicit\s+none/i, w: 12 },
    { lang: "cobol", re: /\bIDENTIFICATION\s+DIVISION\b|\bPROCEDURE\s+DIVISION/i, w: 16 },
    { lang: "pascal", re: /\bprogram\s+\w+;|\bbegin\b|\bend\./i, w: 10 },
    { lang: "basic", re: /^\d+\s+(PRINT|LET|GOTO|REM)\b/im, w: 14 },
    { lang: "qbasic", re: /\bDIM\s+\w+|\bCLS\b|\bINPUT\b/i, w: 12 },
    { lang: "asm", re: /^\s*\.\w+\s/m|^\s*(mov|push|pop|call|ret)\b/im, w: 11 },
    { lang: "sql", re: /\b(SELECT|INSERT|UPDATE|DELETE|CREATE\s+TABLE)\b/i, w: 12 },
    { lang: "html", re: /<!DOCTYPE\s+html|<html[\s>]/i, w: 16 },
    { lang: "css", re: /^\s*[@#.][\w-]+\s*\{/m, w: 10 },
    { lang: "json", re: /^\s*[\[{]/, w: 4 },
    { lang: "yaml", re: /^---\s*$/m|^\w+:\s*$/m, w: 8 },
    { lang: "markdown", re: /^#\s+\w+/m, w: 5 },
    { lang: "dockerfile", re: /^FROM\s+\w+/im, w: 16 },
    { lang: "makefile", re: /^[\w.-]+:\s*$/m, w: 8 },
    { lang: "cmake", re: /\bcmake_minimum_required\b|\bproject\s*\(/, w: 14 },
    { lang: "verilog", re: /\bmodule\s+\w+|\bendmodule\b/, w: 12 },
    { lang: "field", re: /\bfield\b.*\bplate\b|\bcombinatronic\b/i, w: 8 },
  ];

  function scoreContent(content, extMap) {
    const text = String(content || "");
    if (!text.trim()) return [];
    const scores = new Map();
    for (const h of HEURISTICS) {
      if (h.re.test(text)) scores.set(h.lang, (scores.get(h.lang) || 0) + h.w);
    }
    const first = text.trim().slice(0, 200).toLowerCase();
    if (first.startsWith("#!/usr/bin/env node")) scores.set("javascript", (scores.get("javascript") || 0) + 8);
    if (first.includes("typescript")) scores.set("typescript", (scores.get("typescript") || 0) + 6);
    return [...scores.entries()]
      .sort((a, b) => b[1] - a[1])
      .map(([lang, score]) => ({ lang, score }));
  }

  function discern(path, content, extMap) {
    const map = extMap || global.AmmoCodeHighlight?.EXT_MAP || {};
    const m = String(path || "").toLowerCase().match(/(\.[a-z0-9]+)$/i);
    const fromPath = m ? map[m[1].toLowerCase()] : null;
    const ranked = scoreContent(content, map);
    if (fromPath && !ranked.find((r) => r.lang === fromPath)) {
      ranked.unshift({ lang: fromPath, score: 6 });
    } else if (fromPath) {
      const hit = ranked.find((r) => r.lang === fromPath);
      if (hit) hit.score += 6;
      ranked.sort((a, b) => b.score - a.score);
    }
    const best = ranked[0]?.lang || fromPath || "plaintext";
    return { lang: best, guesses: ranked.slice(0, 5) };
  }

  global.Grok16EditorDiscern = { discern, scoreContent };
})(typeof globalThis !== "undefined" ? globalThis : window);
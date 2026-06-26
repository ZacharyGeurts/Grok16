/* Grok16 unified driver — forever languages: C, C++, Python, asm, Rust, Go, …
 * Dispatches to libexec backends, GPY-16, g16-as, g16-rust, etc.
 * Copyright (C) 2026 Zachary Geurts — GPLv3
 */
#define _GNU_SOURCE
#include <errno.h>
#include <limits.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

static int ends_with(const char *s, const char *suffix)
{
    size_t ls, lx;
    if (!s || !suffix)
        return 0;
    ls = strlen(s);
    lx = strlen(suffix);
    if (lx > ls)
        return 0;
    return strcmp(s + ls - lx, suffix) == 0;
}

static int has_ext(const char *path, const char *ext)
{
    return path && ends_with(path, ext);
}

static int has_cpp_extension(const char *path)
{
    return has_ext(path, ".cpp") || has_ext(path, ".cxx") || has_ext(path, ".cc") ||
           has_ext(path, ".C") || has_ext(path, ".hpp") || has_ext(path, ".hh") ||
           has_ext(path, ".ixx") || has_ext(path, ".txx");
}

static int has_py_extension(const char *path)
{
    return has_ext(path, ".py") || has_ext(path, ".gpy");
}

static int has_c_extension(const char *path)
{
    return has_ext(path, ".c") || has_ext(path, ".h");
}

static int has_asm_extension(const char *path)
{
    return has_ext(path, ".s") || has_ext(path, ".S") || has_ext(path, ".asm");
}

static int has_rs_extension(const char *path) { return has_ext(path, ".rs"); }
static int has_go_extension(const char *path) { return has_ext(path, ".go"); }
static int has_zig_extension(const char *path) { return has_ext(path, ".zig"); }
static int has_d_extension(const char *path)
{
    /* Ninja/gcc -MF dependency files end in .o.d — not D language sources */
    if (!path || !has_ext(path, ".d"))
        return 0;
    return !has_ext(path, ".o.d");
}
static int has_ada_extension(const char *path)
{
    return has_ext(path, ".adb") || has_ext(path, ".ads");
}
static int has_objc_extension(const char *path)
{
    return has_ext(path, ".m") || has_ext(path, ".mm");
}
static int has_fortran_extension(const char *path)
{
    return has_ext(path, ".f") || has_ext(path, ".f90") || has_ext(path, ".f95") ||
           has_ext(path, ".f03") || has_ext(path, ".for");
}

static int argv_has_source(int argc, char **argv, int (*pred)(const char *))
{
    int i;
    for (i = 1; i < argc; i++) {
        const char *a = argv[i];
        if (!a || a[0] == '-')
            continue;
        if (pred(a))
            return 1;
    }
    return 0;
}

static int argv_has_c_or_cpp_source(int argc, char **argv)
{
    return argv_has_source(argc, argv, has_c_extension) ||
           argv_has_source(argc, argv, has_cpp_extension);
}

static int env_force(const char *name)
{
    const char *v = getenv(name);
    return v && *v && strcmp(v, "0") != 0;
}

static int argv_invokes_python(int argc, char **argv)
{
    int i;
    if (env_force("G16_FORCE_PYTHON") || env_force("G16_FORCE_PY"))
        return 1;
    if (argc > 0 && argv[0]) {
        const char *base = strrchr(argv[0], '/');
        base = base ? base + 1 : argv[0];
        if (strstr(base, "gpy") != NULL || strstr(base, "pythong") != NULL ||
            (strstr(base, "python") != NULL && strstr(base, "g16") == NULL))
            return 1;
    }
    for (i = 1; i < argc; i++) {
        const char *a = argv[i];
        if (!a)
            continue;
        if (strcmp(a, "-m") == 0 && !argv_has_c_or_cpp_source(argc, argv))
            return 1;
        if (strcmp(a, "-c") == 0 && !argv_has_c_or_cpp_source(argc, argv))
            return 1;
        if (strcmp(a, "-x") == 0 && i + 1 < argc) {
            const char *lang = argv[i + 1];
            if (strstr(lang, "python") != NULL)
                return 1;
            i++;
            continue;
        }
        if (a[0] != '-' && has_py_extension(a))
            return 1;
    }
    return 0;
}

static int argv_invokes_asm(int argc, char **argv)
{
    int i;
    if (env_force("G16_FORCE_ASM"))
        return 1;
    if (argc > 0 && argv[0]) {
        const char *base = strrchr(argv[0], '/');
        base = base ? base + 1 : argv[0];
        if (strstr(base, "g16-as") != NULL || (strcmp(base, "as") == 0))
            return 1;
    }
    for (i = 1; i < argc; i++) {
        const char *a = argv[i];
        if (!a)
            continue;
        if (strcmp(a, "-x") == 0 && i + 1 < argc) {
            if (strstr(argv[i + 1], "assembler") != NULL)
                return 1;
            i++;
            continue;
        }
        if (a[0] != '-' && has_asm_extension(a))
            return 1;
    }
    return 0;
}

static int argv_invokes_lang(int argc, char **argv,
                             const char *force_env,
                             const char *driver_substr,
                             int (*ext_pred)(const char *))
{
    int i;
    if (env_force(force_env))
        return 1;
    if (argc > 0 && argv[0] && driver_substr) {
        const char *base = strrchr(argv[0], '/');
        base = base ? base + 1 : argv[0];
        if (strstr(base, driver_substr) != NULL)
            return 1;
    }
    return argv_has_source(argc, argv, ext_pred);
}

static int argv_invokes_cpp(int argc, char **argv)
{
    int i;
    if (env_force("G16_FORCE_CXX"))
        return 1;
    if (getenv("G16_FORCE_C") && strcmp(getenv("G16_FORCE_C"), "1") == 0)
        return 0;
    if (argc > 0 && argv[0]) {
        const char *base = strrchr(argv[0], '/');
        base = base ? base + 1 : argv[0];
        if (strstr(base, "g++") != NULL)
            return 1;
    }
    for (i = 1; i < argc; i++) {
        const char *a = argv[i];
        if (!a)
            continue;
        if (strcmp(a, "-x") == 0 && i + 1 < argc) {
            const char *lang = argv[i + 1];
            if (strncmp(lang, "c++", 3) == 0 || strstr(lang, "objective-c++") != NULL)
                return 1;
            if (strcmp(lang, "c") == 0)
                return 0;
            i++;
            continue;
        }
        if (strncmp(a, "-std=", 5) == 0) {
            const char *std = a + 5;
            if (strncmp(std, "c++", 3) == 0 || strncmp(std, "gnu++", 5) == 0)
                return 1;
            if (strncmp(std, "c", 1) == 0 || strncmp(std, "gnu", 3) == 0)
                return 0;
        }
        if (strcmp(a, "-lstdc++") == 0 || strcmp(a, "-lc++") == 0)
            return 1;
        if (a[0] != '-' && has_cpp_extension(a))
            return 1;
        if (a[0] != '-' && has_objc_extension(a))
            return 1;
    }
    return 0;
}

static const char *discern_lang(int argc, char **argv)
{
    if (argv_invokes_python(argc, argv))
        return "python";
    if (argv_invokes_asm(argc, argv))
        return "asm";
    if (argv_invokes_lang(argc, argv, "G16_FORCE_RUST", "g16-rust", has_rs_extension))
        return "rust";
    if (argv_invokes_lang(argc, argv, "G16_FORCE_GO", "g16-go", has_go_extension))
        return "go";
    if (argv_invokes_lang(argc, argv, "G16_FORCE_ZIG", "g16-zig", has_zig_extension))
        return "zig";
    if (argv_invokes_lang(argc, argv, "G16_FORCE_FORTRAN", "g16-gfortran", has_fortran_extension))
        return "fortran";
    if (argv_invokes_lang(argc, argv, "G16_FORCE_D", "g16-gdc", has_d_extension))
        return "d";
    if (argv_invokes_lang(argc, argv, "G16_FORCE_ADA", "g16-gnat", has_ada_extension))
        return "ada";
    if (argv_invokes_lang(argc, argv, "G16_FORCE_OBJC", "g16-objc", has_objc_extension))
        return "objc";
    if (argv_invokes_cpp(argc, argv))
        return "cxx";
    return "c";
}

static int resolve_exec_dir(char *buf, size_t buflen)
{
    ssize_t n;
#if defined(__linux__)
    n = readlink("/proc/self/exe", buf, buflen - 1);
    if (n > 0) {
        buf[n] = '\0';
        return 1;
    }
#endif
    if (buflen > 0)
        buf[0] = '\0';
    return 0;
}

static int bin_dir(char *out, size_t outlen)
{
    char self[PATH_MAX];
    char *slash;
    if (!resolve_exec_dir(self, sizeof self))
        return 0;
    slash = strrchr(self, '/');
    if (!slash)
        return 0;
    *slash = '\0';
    snprintf(out, outlen, "%s", self);
    return 1;
}

static int prefix_bin_path(char *out, size_t outlen, const char *tool)
{
    char bindir[PATH_MAX];
    const char *env = getenv("G16_PREFIX");
    if (env && *env) {
        snprintf(out, outlen, "%s/bin/%s", env, tool);
        return access(out, X_OK) == 0;
    }
    if (!bin_dir(bindir, sizeof bindir))
        return 0;
    snprintf(out, outlen, "%s/%s", bindir, tool);
    if (access(out, X_OK) == 0)
        return 1;
    snprintf(out, outlen, "%s/../../Grok16/bin/%s", bindir, tool);
    return access(out, X_OK) == 0;
}

static int backend_path(char *out, size_t outlen, const char *backend)
{
    char bindir[PATH_MAX];
    if (!bin_dir(bindir, sizeof bindir))
        return 0;
    snprintf(out, outlen, "%s/../libexec/grok16/%s", bindir, backend);
    return 1;
}

static int libexec_relocated(void)
{
    char bindir[PATH_MAX];
    char marker[PATH_MAX];
    if (!bin_dir(bindir, sizeof bindir))
        return 0;
    snprintf(marker, sizeof marker, "%s/../libexec/grok16/.relocated", bindir);
    return access(marker, F_OK) == 0;
}

static int gcc_build_b_prefix(char *out, size_t outlen)
{
    const char *env = getenv("GROK16_GCC_BUILD");
    char bindir[PATH_MAX];
    if (env && *env) {
        snprintf(out, outlen, "%s/gcc/", env);
        return 1;
    }
    if (!bin_dir(bindir, sizeof bindir))
        return 0;
    snprintf(out, outlen, "%s/../build/gcc/gcc/", bindir);
    return access(out, F_OK) == 0 || access(out, X_OK) == 0;
}

static void exec_backend(const char *backend, int argc, char **argv)
{
    char target[PATH_MAX];
    char bprefix[PATH_MAX];
    char **nargv;
    int i, nargc;

    if (!backend_path(target, sizeof target, backend)) {
        fprintf(stderr, "g16: cannot resolve backend %s\n", backend);
        _exit(127);
    }
    if (access(target, X_OK) != 0) {
        fprintf(stderr, "g16: missing backend %s (%s)\n", backend, strerror(errno));
        _exit(127);
    }
    if (!libexec_relocated() || !gcc_build_b_prefix(bprefix, sizeof bprefix)) {
        execv(target, argv);
        fprintf(stderr, "g16: exec %s failed (%s)\n", target, strerror(errno));
        _exit(127);
    }
    nargc = argc + 2;
    nargv = calloc((size_t)nargc + 1, sizeof(char *));
    if (!nargv) {
        execv(target, argv);
        _exit(127);
    }
    nargv[0] = argv[0];
    nargv[1] = "-B";
    nargv[2] = bprefix;
    for (i = 1; i < argc; i++)
        nargv[i + 2] = argv[i];
    execv(target, nargv);
    fprintf(stderr, "g16: exec %s failed (%s)\n", target, strerror(errno));
    _exit(127);
}

static int gpy16_path(char *out, size_t outlen)
{
    const char *env = getenv("GPY16_DRIVER");
    char bindir[PATH_MAX];
    if (env && *env) {
        snprintf(out, outlen, "%s", env);
        return access(out, X_OK) == 0;
    }
    if (prefix_bin_path(out, outlen, "gpy-16"))
        return 1;
    if (!bin_dir(bindir, sizeof bindir))
        return 0;
    snprintf(out, outlen, "%s/gpy-16", bindir);
    if (access(out, X_OK) == 0)
        return 1;
    snprintf(out, outlen, "%s/../../GrokPy/bin/gpy-16", bindir);
    if (access(out, X_OK) == 0)
        return 1;
    snprintf(out, outlen, "%s/../../PythonG/bin/pythong", bindir);
    return access(out, X_OK) == 0;
}

static int lang_driver_path(char *out, size_t outlen, const char *lang)
{
    static const struct {
        const char *lang;
        const char *tool;
    } map[] = {
        {"python", NULL},
        {"asm", "g16-as"},
        {"rust", "g16-rust"},
        {"go", "g16-go"},
        {"zig", "g16-zig"},
        {"fortran", "g16-gfortran"},
        {"d", "g16-gdc"},
        {"ada", "g16-gnat"},
        {"objc", "g16-objc"},
        {NULL, NULL}
    };
    size_t i;
    for (i = 0; map[i].lang; i++) {
        if (strcmp(map[i].lang, lang) == 0) {
            if (!map[i].tool)
                return gpy16_path(out, outlen);
            return prefix_bin_path(out, outlen, map[i].tool);
        }
    }
    return 0;
}

int main(int argc, char **argv)
{
    char target[PATH_MAX];
    const char *lang;
    const char *backend; /* used by exec_backend */

    if (argc >= 2 && strcmp(argv[1], "--g16-discern") == 0) {
        fputs(discern_lang(argc, argv), stdout);
        fputc('\n', stdout);
        return 0;
    }

    lang = discern_lang(argc, argv);

    if (strcmp(lang, "python") == 0 || strcmp(lang, "asm") == 0 ||
        strcmp(lang, "rust") == 0 || strcmp(lang, "go") == 0 ||
        strcmp(lang, "zig") == 0 || strcmp(lang, "fortran") == 0 ||
        strcmp(lang, "d") == 0 || strcmp(lang, "ada") == 0 ||
        strcmp(lang, "objc") == 0) {
        if (!lang_driver_path(target, sizeof target, lang)) {
            fprintf(stderr, "g16: %s discerned but field driver missing (install languages)\n", lang);
            return 127;
        }
        execv(target, argv);
        fprintf(stderr, "g16: exec %s %s failed (%s)\n", lang, target, strerror(errno));
        return 127;
    }

    backend = strcmp(lang, "cxx") == 0 ? "g16-cxx" : "g16-cc";
    exec_backend(backend, argc, argv);
    return 127;
}
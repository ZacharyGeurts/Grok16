/* Grok16 unified driver — auto-detect C vs C++, dispatch to GCC backends.
 * Copyright (C) 2026 Zachary Geurts — GPLv3
 * Real ELF front door; backends live in ../libexec/grok16/g16-cc and g16-cxx.
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

static int has_cpp_extension(const char *path)
{
    const char *dot;
    if (!path)
        return 0;
    dot = strrchr(path, '.');
    if (!dot || dot[1] == '\0')
        return 0;
    dot++;
    return strcmp(dot, "cpp") == 0 || strcmp(dot, "cxx") == 0 ||
           strcmp(dot, "cc") == 0 || strcmp(dot, "C") == 0 ||
           strcmp(dot, "hpp") == 0 || strcmp(dot, "hh") == 0 ||
           strcmp(dot, "ixx") == 0 || strcmp(dot, "txx") == 0;
}

static int argv_invokes_cpp(int argc, char **argv)
{
    int i;
    const char *force = getenv("G16_FORCE_CXX");
    if (force && *force && strcmp(force, "0") != 0)
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
            if (strncmp(lang, "c++", 3) == 0)
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
    }
    return 0;
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

static int backend_path(char *out, size_t outlen, const char *backend)
{
    char self[PATH_MAX];
    char *slash;
    size_t dirlen;

    if (!resolve_exec_dir(self, sizeof self))
        return 0;
    slash = strrchr(self, '/');
    if (!slash)
        return 0;
    *slash = '\0';
    dirlen = (size_t)(slash - self);
    if (dirlen + strlen("/../libexec/grok16/") + strlen(backend) + 1 > outlen)
        return 0;
    snprintf(out, outlen, "%s/../libexec/grok16/%s", self, backend);
    return 1;
}

int main(int argc, char **argv)
{
    char backend[PATH_MAX];
    const char *name;
    char **nargv;

    name = argv_invokes_cpp(argc, argv) ? "g16-cxx" : "g16-cc";
    if (!backend_path(backend, sizeof backend, name)) {
        fprintf(stderr, "g16: cannot resolve backend %s\n", name);
        return 127;
    }
    if (access(backend, X_OK) != 0) {
        fprintf(stderr, "g16: missing backend %s (%s)\n", name, strerror(errno));
        return 127;
    }

    nargv = argv;
    execv(backend, nargv);
    fprintf(stderr, "g16: exec %s failed (%s)\n", backend, strerror(errno));
    return 127;
}
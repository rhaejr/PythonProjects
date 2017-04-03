#include <Python.h>
#include <QtGlobal>

#if PY_MAJOR_VERSION >= 3
extern "C" PyObject *PyInit_Qt(void);
extern "C" PyObject *PyInit_sip(void);
#if defined(Q_OS_LINUX)
extern "C" PyObject *PyInit__sqlite3(void);
extern "C" PyObject *PyInit_time(void);
extern "C" PyObject *PyInit_select(void);
extern "C" PyObject *PyInit_array(void);
extern "C" PyObject *PyInit__posixsubprocess(void);
extern "C" PyObject *PyInit__datetime(void);
extern "C" PyObject *PyInit__heapq(void);
extern "C" PyObject *PyInit_math(void);
#endif
#if defined(Q_OS_MAC)
extern "C" PyObject *PyInit__sqlite3(void);
extern "C" PyObject *PyInit_time(void);
extern "C" PyObject *PyInit_select(void);
extern "C" PyObject *PyInit_array(void);
extern "C" PyObject *PyInit__posixsubprocess(void);
extern "C" PyObject *PyInit__datetime(void);
extern "C" PyObject *PyInit__heapq(void);
extern "C" PyObject *PyInit_math(void);
#endif

static struct _inittab extension_modules[] = {
    {"PyQt4.Qt", PyInit_Qt},
    {"sip", PyInit_sip},
#if defined(Q_OS_LINUX)
    {"_sqlite3", PyInit__sqlite3},
    {"time", PyInit_time},
    {"select", PyInit_select},
    {"array", PyInit_array},
    {"_posixsubprocess", PyInit__posixsubprocess},
    {"_datetime", PyInit__datetime},
    {"_heapq", PyInit__heapq},
    {"math", PyInit_math},
#endif
#if defined(Q_OS_MAC)
    {"_sqlite3", PyInit__sqlite3},
    {"time", PyInit_time},
    {"select", PyInit_select},
    {"array", PyInit_array},
    {"_posixsubprocess", PyInit__posixsubprocess},
    {"_datetime", PyInit__datetime},
    {"_heapq", PyInit__heapq},
    {"math", PyInit_math},
#endif
    {NULL, NULL}
};
#else
extern "C" void initQt(void);
extern "C" void initsip(void);
#if defined(Q_OS_LINUX)
extern "C" void init_sqlite3(void);
extern "C" void inittime(void);
extern "C" void initselect(void);
extern "C" void initarray(void);
extern "C" void init_posixsubprocess(void);
extern "C" void init_datetime(void);
extern "C" void init_heapq(void);
extern "C" void initmath(void);
#endif
#if defined(Q_OS_MAC)
extern "C" void init_sqlite3(void);
extern "C" void inittime(void);
extern "C" void initselect(void);
extern "C" void initarray(void);
extern "C" void init_posixsubprocess(void);
extern "C" void init_datetime(void);
extern "C" void init_heapq(void);
extern "C" void initmath(void);
#endif

static struct _inittab extension_modules[] = {
    {"PyQt4.Qt", initQt},
    {"sip", initsip},
#if defined(Q_OS_LINUX)
    {"_sqlite3", init_sqlite3},
    {"time", inittime},
    {"select", initselect},
    {"array", initarray},
    {"_posixsubprocess", init_posixsubprocess},
    {"_datetime", init_datetime},
    {"_heapq", init_heapq},
    {"math", initmath},
#endif
#if defined(Q_OS_MAC)
    {"_sqlite3", init_sqlite3},
    {"time", inittime},
    {"select", initselect},
    {"array", initarray},
    {"_posixsubprocess", init_posixsubprocess},
    {"_datetime", init_datetime},
    {"_heapq", init_heapq},
    {"math", initmath},
#endif
    {NULL, NULL}
};
#endif


#if defined(Q_OS_WIN) && PY_MAJOR_VERSION >= 3
#include <windows.h>

extern int pyqtdeploy_start(int argc, wchar_t **w_argv,
        struct _inittab *extension_modules, const char *main_module,
        const char *entry_point, const char **path_dirs);

int main(int argc, char **)
{
    LPWSTR *w_argv = CommandLineToArgvW(GetCommandLineW(), &argc);

    return pyqtdeploy_start(argc, w_argv, extension_modules, "__main__", NULL, NULL);
}
#else
extern int pyqtdeploy_start(int argc, char **argv,
        struct _inittab *extension_modules, const char *main_module,
        const char *entry_point, const char **path_dirs);

int main(int argc, char **argv)
{
    return pyqtdeploy_start(argc, argv, extension_modules, "__main__", NULL, NULL);
}
#endif

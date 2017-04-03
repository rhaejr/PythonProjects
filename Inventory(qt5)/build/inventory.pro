TEMPLATE = app

CONFIG += warn_off
CONFIG -= app_bundle

RESOURCES = \
    resources/pyqtdeploy.qrc

SOURCES = pyqtdeploy_main.cpp pyqtdeploy_start.cpp pdytools_module.cpp
DEFINES += PYQTDEPLOY_FROZEN_MAIN PYQTDEPLOY_OPTIMIZED
HEADERS = pyqtdeploy_version.h frozen_bootstrap.h frozen_bootstrap_external.h frozen_main.h

INCLUDEPATH += C:/Users/Rhea/AppData/Local/Programs/Python/Python35/include
LIBS += -LC:/Users/Rhea/AppData/Local/Programs/Python/Python35/Lib/site-packages -lsip
LIBS += -LC:/Users/Rhea/AppData/Local/Programs/Python/Python35/Lib/site-packages/PyQt5 -lQt

linux-* {
    DEFINES += Py_BUILD_CORE
    DEFINES += MODULE_NAME=\\\"sqlite3\\\"
    DEFINES += SQLITE_OMIT_LOAD_EXTENSION
    INCLUDEPATH += C:/Users/Rhea/AppData/Local/Programs/Python/Python35/Modules
    INCLUDEPATH += C:/Users/Rhea/AppData/Local/Programs/Python/Python35/Modules/_sqlite
    LIBS += -lm
    LIBS += -lsqlite3
    SOURCES += C:/Users/Rhea/AppData/Local/Programs/Python/Python35/Modules/_sqlite/module.c
    SOURCES += C:/Users/Rhea/AppData/Local/Programs/Python/Python35/Modules/selectmodule.c
    SOURCES += C:/Users/Rhea/AppData/Local/Programs/Python/Python35/Modules/_sqlite/microprotocols.c
    SOURCES += C:/Users/Rhea/AppData/Local/Programs/Python/Python35/Modules/_sqlite/connection.c
    SOURCES += C:/Users/Rhea/AppData/Local/Programs/Python/Python35/Modules/_sqlite/cache.c
    SOURCES += C:/Users/Rhea/AppData/Local/Programs/Python/Python35/Modules/_datetimemodule.c
    SOURCES += C:/Users/Rhea/AppData/Local/Programs/Python/Python35/Modules/_sqlite/util.c
    SOURCES += C:/Users/Rhea/AppData/Local/Programs/Python/Python35/Modules/_sqlite/statement.c
    SOURCES += C:/Users/Rhea/AppData/Local/Programs/Python/Python35/Modules/_sqlite/cursor.c
    SOURCES += C:/Users/Rhea/AppData/Local/Programs/Python/Python35/Modules/_math.c
    SOURCES += C:/Users/Rhea/AppData/Local/Programs/Python/Python35/Modules/cmathmodule.c
    SOURCES += C:/Users/Rhea/AppData/Local/Programs/Python/Python35/Modules/_heapqmodule.c
    SOURCES += C:/Users/Rhea/AppData/Local/Programs/Python/Python35/Modules/_sqlite/row.c
    SOURCES += C:/Users/Rhea/AppData/Local/Programs/Python/Python35/Modules/mathmodule.c
    SOURCES += C:/Users/Rhea/AppData/Local/Programs/Python/Python35/Modules/_posixsubprocess.c
    SOURCES += C:/Users/Rhea/AppData/Local/Programs/Python/Python35/Modules/_sqlite/prepare_protocol.c
    SOURCES += C:/Users/Rhea/AppData/Local/Programs/Python/Python35/Modules/timemodule.c
}

win32 {
    LIBS += -LC:/Users/Rhea/Documents/GitHub/PythonProjects/Inventory(qt5)/$SYSROOT/lib -lpython35
}

!win32 {
    LIBS += -LC:/Users/Rhea/Documents/GitHub/PythonProjects/Inventory(qt5)/$SYSROOT/lib -lpython3.5
}

macx {
    DEFINES += Py_BUILD_CORE
    DEFINES += MODULE_NAME=\\\"sqlite3\\\"
    DEFINES += SQLITE_OMIT_LOAD_EXTENSION
    INCLUDEPATH += C:/Users/Rhea/AppData/Local/Programs/Python/Python35/Modules
    INCLUDEPATH += C:/Users/Rhea/AppData/Local/Programs/Python/Python35/Modules/_sqlite
    LIBS += -lsqlite3
    SOURCES += C:/Users/Rhea/AppData/Local/Programs/Python/Python35/Modules/_sqlite/module.c
    SOURCES += C:/Users/Rhea/AppData/Local/Programs/Python/Python35/Modules/selectmodule.c
    SOURCES += C:/Users/Rhea/AppData/Local/Programs/Python/Python35/Modules/_sqlite/microprotocols.c
    SOURCES += C:/Users/Rhea/AppData/Local/Programs/Python/Python35/Modules/_sqlite/connection.c
    SOURCES += C:/Users/Rhea/AppData/Local/Programs/Python/Python35/Modules/_sqlite/cache.c
    SOURCES += C:/Users/Rhea/AppData/Local/Programs/Python/Python35/Modules/_datetimemodule.c
    SOURCES += C:/Users/Rhea/AppData/Local/Programs/Python/Python35/Modules/_sqlite/util.c
    SOURCES += C:/Users/Rhea/AppData/Local/Programs/Python/Python35/Modules/_sqlite/statement.c
    SOURCES += C:/Users/Rhea/AppData/Local/Programs/Python/Python35/Modules/_sqlite/cursor.c
    SOURCES += C:/Users/Rhea/AppData/Local/Programs/Python/Python35/Modules/_math.c
    SOURCES += C:/Users/Rhea/AppData/Local/Programs/Python/Python35/Modules/cmathmodule.c
    SOURCES += C:/Users/Rhea/AppData/Local/Programs/Python/Python35/Modules/_heapqmodule.c
    SOURCES += C:/Users/Rhea/AppData/Local/Programs/Python/Python35/Modules/_sqlite/row.c
    SOURCES += C:/Users/Rhea/AppData/Local/Programs/Python/Python35/Modules/mathmodule.c
    SOURCES += C:/Users/Rhea/AppData/Local/Programs/Python/Python35/Modules/_posixsubprocess.c
    SOURCES += C:/Users/Rhea/AppData/Local/Programs/Python/Python35/Modules/_sqlite/prepare_protocol.c
    SOURCES += C:/Users/Rhea/AppData/Local/Programs/Python/Python35/Modules/timemodule.c
}

win32 {
    PDY_DLL = C:/Users/Rhea/Documents/GitHub/PythonProjects/Inventory(qt5)/$SYSROOT/lib/DLLs3.5/python35.dll
    exists($$PDY_DLL) {
        CONFIG(debug, debug|release) {
            QMAKE_POST_LINK += $(COPY_FILE) $$shell_path($$PDY_DLL) $$shell_path($$OUT_PWD/debug) &
        } else {
            QMAKE_POST_LINK += $(COPY_FILE) $$shell_path($$PDY_DLL) $$shell_path($$OUT_PWD/release) &
        }
    }

    PDY_DLL = C:/Users/Rhea/Documents/GitHub/PythonProjects/Inventory(qt5)/$SYSROOT/lib/DLLs3.5/vcruntime140.dll
    exists($$PDY_DLL) {
        CONFIG(debug, debug|release) {
            QMAKE_POST_LINK += $(COPY_FILE) $$shell_path($$PDY_DLL) $$shell_path($$OUT_PWD/debug) &
        } else {
            QMAKE_POST_LINK += $(COPY_FILE) $$shell_path($$PDY_DLL) $$shell_path($$OUT_PWD/release) &
        }
    }

    PDY_DLL = C:/Users/Rhea/Documents/GitHub/PythonProjects/Inventory(qt5)/$SYSROOT/lib/DLLs3.5/select.pyd
    exists($$PDY_DLL) {
        CONFIG(debug, debug|release) {
            QMAKE_POST_LINK += $(COPY_FILE) $$shell_path($$PDY_DLL) $$shell_path($$OUT_PWD/debug) &
        } else {
            QMAKE_POST_LINK += $(COPY_FILE) $$shell_path($$PDY_DLL) $$shell_path($$OUT_PWD/release) &
        }
    }

    PDY_DLL = C:/Users/Rhea/Documents/GitHub/PythonProjects/Inventory(qt5)/$SYSROOT/lib/DLLs3.5/_sqlite3.pyd
    exists($$PDY_DLL) {
        CONFIG(debug, debug|release) {
            QMAKE_POST_LINK += $(COPY_FILE) $$shell_path($$PDY_DLL) $$shell_path($$OUT_PWD/debug) &
        } else {
            QMAKE_POST_LINK += $(COPY_FILE) $$shell_path($$PDY_DLL) $$shell_path($$OUT_PWD/release) &
        }
    }

    PDY_DLL = C:/Users/Rhea/Documents/GitHub/PythonProjects/Inventory(qt5)/$SYSROOT/lib/DLLs3.5/sqlite3.dll
    exists($$PDY_DLL) {
        CONFIG(debug, debug|release) {
            QMAKE_POST_LINK += $(COPY_FILE) $$shell_path($$PDY_DLL) $$shell_path($$OUT_PWD/debug) &
        } else {
            QMAKE_POST_LINK += $(COPY_FILE) $$shell_path($$PDY_DLL) $$shell_path($$OUT_PWD/release) &
        }
    }
}

cython.name = Cython compiler
cython.input = CYTHONSOURCES
cython.output = ${QMAKE_FILE_BASE}.c
cython.variable_out = GENERATED_SOURCES
cython.commands = cython ${QMAKE_FILE_IN} -o ${QMAKE_FILE_OUT}

QMAKE_EXTRA_COMPILERS += cython

linux-* {
    LIBS += -lutil -ldl
}

win32 {
    masm.input = MASMSOURCES
    masm.output = ${QMAKE_FILE_BASE}.obj

    contains(QMAKE_TARGET.arch, x86_64) {
        masm.name = MASM64 compiler
        masm.commands = ml64 /Fo ${QMAKE_FILE_OUT} /c ${QMAKE_FILE_IN}
    } else {
        masm.name = MASM compiler
        masm.commands = ml /Fo ${QMAKE_FILE_OUT} /c ${QMAKE_FILE_IN}
    }

    QMAKE_EXTRA_COMPILERS += masm

    LIBS += -ladvapi32 -lshell32 -luser32 -lws2_32 -lole32 -loleaut32
    DEFINES += MS_WINDOWS _WIN32_WINNT=Py_WINVER NTDDI_VERSION=Py_NTDDI WINVER=Py_WINVER

    # This is added from the qmake spec files but clashes with _pickle.c.
    DEFINES -= UNICODE
}

macx {
    LIBS += -framework SystemConfiguration -framework CoreFoundation
}

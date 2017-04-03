TEMPLATE = app

CONFIG += warn_off
CONFIG -= app_bundle

RESOURCES = \
    resources/pyqtdeploy.qrc

SOURCES = pyqtdeploy_main.cpp pyqtdeploy_start.cpp pdytools_module.cpp
DEFINES += PYQTDEPLOY_FROZEN_MAIN PYQTDEPLOY_OPTIMIZED
HEADERS = pyqtdeploy_version.h frozen_bootstrap.h frozen_main.h

INCLUDEPATH += C:/Python34/include
LIBS += -LC:/Python34/Lib/site-packages -lsip
LIBS += -LC:/Python34/Lib/site-packages/PyQt4 -lQt_s

linux-* {
    DEFINES += SQLITE_OMIT_LOAD_EXTENSION
    DEFINES += MODULE_NAME=\\\"sqlite3\\\"
    INCLUDEPATH += C:/Python34/Modules
    INCLUDEPATH += C:/Python34/Modules/_sqlite
    LIBS += -lsqlite3
    LIBS += -lm
    SOURCES += C:/Python34/Modules/arraymodule.c
    SOURCES += C:/Python34/Modules/_sqlite/module.c
    SOURCES += C:/Python34/Modules/_datetimemodule.c
    SOURCES += C:/Python34/Modules/_math.c
    SOURCES += C:/Python34/Modules/_sqlite/prepare_protocol.c
    SOURCES += C:/Python34/Modules/timemodule.c
    SOURCES += C:/Python34/Modules/_sqlite/util.c
    SOURCES += C:/Python34/Modules/_sqlite/row.c
    SOURCES += C:/Python34/Modules/mathmodule.c
    SOURCES += C:/Python34/Modules/_sqlite/connection.c
    SOURCES += C:/Python34/Modules/selectmodule.c
    SOURCES += C:/Python34/Modules/_sqlite/microprotocols.c
    SOURCES += C:/Python34/Modules/_sqlite/statement.c
    SOURCES += C:/Python34/Modules/_sqlite/cache.c
    SOURCES += C:/Python34/Modules/_posixsubprocess.c
    SOURCES += C:/Python34/Modules/_sqlite/cursor.c
    SOURCES += C:/Python34/Modules/_heapqmodule.c
}

win32 {
    LIBS += -LC:/Users/Rhea/Documents/GitHub/PythonProjects/Inventory/$SYSROOT/lib -lpython34
}

!win32 {
    LIBS += -LC:/Users/Rhea/Documents/GitHub/PythonProjects/Inventory/$SYSROOT/lib -lpython3.4
}

macx {
    DEFINES += SQLITE_OMIT_LOAD_EXTENSION
    DEFINES += MODULE_NAME=\\\"sqlite3\\\"
    INCLUDEPATH += C:/Python34/Modules
    INCLUDEPATH += C:/Python34/Modules/_sqlite
    LIBS += -lsqlite3
    SOURCES += C:/Python34/Modules/arraymodule.c
    SOURCES += C:/Python34/Modules/_sqlite/module.c
    SOURCES += C:/Python34/Modules/_datetimemodule.c
    SOURCES += C:/Python34/Modules/_math.c
    SOURCES += C:/Python34/Modules/_sqlite/prepare_protocol.c
    SOURCES += C:/Python34/Modules/timemodule.c
    SOURCES += C:/Python34/Modules/_sqlite/util.c
    SOURCES += C:/Python34/Modules/_sqlite/row.c
    SOURCES += C:/Python34/Modules/mathmodule.c
    SOURCES += C:/Python34/Modules/_sqlite/connection.c
    SOURCES += C:/Python34/Modules/selectmodule.c
    SOURCES += C:/Python34/Modules/_sqlite/microprotocols.c
    SOURCES += C:/Python34/Modules/_sqlite/statement.c
    SOURCES += C:/Python34/Modules/_sqlite/cache.c
    SOURCES += C:/Python34/Modules/_posixsubprocess.c
    SOURCES += C:/Python34/Modules/_sqlite/cursor.c
    SOURCES += C:/Python34/Modules/_heapqmodule.c
}

win32 {
    PDY_DLL = C:/Users/Rhea/Documents/GitHub/PythonProjects/Inventory/$SYSROOT/lib/DLLs3.4/python34.dll
    exists($$PDY_DLL) {
        CONFIG(debug, debug|release) {
            QMAKE_POST_LINK += $(COPY_FILE) $$shell_path($$PDY_DLL) $$shell_path($$OUT_PWD/debug) &
        } else {
            QMAKE_POST_LINK += $(COPY_FILE) $$shell_path($$PDY_DLL) $$shell_path($$OUT_PWD/release) &
        }
    }

    PDY_DLL = C:/Users/Rhea/Documents/GitHub/PythonProjects/Inventory/$SYSROOT/lib/DLLs3.4/_sqlite3.pyd
    exists($$PDY_DLL) {
        CONFIG(debug, debug|release) {
            QMAKE_POST_LINK += $(COPY_FILE) $$shell_path($$PDY_DLL) $$shell_path($$OUT_PWD/debug) &
        } else {
            QMAKE_POST_LINK += $(COPY_FILE) $$shell_path($$PDY_DLL) $$shell_path($$OUT_PWD/release) &
        }
    }

    PDY_DLL = C:/Users/Rhea/Documents/GitHub/PythonProjects/Inventory/$SYSROOT/lib/DLLs3.4/sqlite3.dll
    exists($$PDY_DLL) {
        CONFIG(debug, debug|release) {
            QMAKE_POST_LINK += $(COPY_FILE) $$shell_path($$PDY_DLL) $$shell_path($$OUT_PWD/debug) &
        } else {
            QMAKE_POST_LINK += $(COPY_FILE) $$shell_path($$PDY_DLL) $$shell_path($$OUT_PWD/release) &
        }
    }

    PDY_DLL = C:/Users/Rhea/Documents/GitHub/PythonProjects/Inventory/$SYSROOT/lib/DLLs3.4/select.pyd
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

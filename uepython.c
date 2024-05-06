#define PY_SSIZE_T_CLEAN

#include <stdio.h>
#include </usr/include/python3.12/Python.h>

int main(int argc, char *argv[]) {
    (void)argc;
    wchar_t *program = Py_DecodeLocale(argv[0], NULL);

    if (program == NULL) {
        fprintf(stderr, "Fatal error: cannot decode argv[0]\n");
        exit(1);
    }

    Py_Initialize();

    PyObject *obj = Py_BuildValue("s", argv[1]);
    FILE *file = _Py_fopen_obj(obj, "r+");
    if(file != NULL) {
        PyRun_SimpleFile(file, argv[1]);
    }

    if (Py_FinalizeEx() < 0) {
        exit(120);
    }

    PyMem_RawFree(program);
    return 0;
}

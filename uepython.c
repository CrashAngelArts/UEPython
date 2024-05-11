#define PY_SSIZE_T_CLEAN

#include </usr/include/python3.12/Python.h>
#include <stdio.h>

int main(int argc, char *argv[])
{
    (void)argc;
    wchar_t *program = Py_DecodeLocale(argv[0], NULL);

    if (program == NULL)
    {
        fprintf(stderr, "Erro: Sem parametro\nPegue o diretorio Python3.12 do tar e renomeie a pasta Lib para lib/ adicione com caminho completo /root/cpython/ que o programa encontra o diretorio Python3.12 automaticamente");
        exit(1);
    }

    Py_SetPythonHome(Py_DecodeLocale(argv[1],NULL));

    Py_Initialize();

    PyRun_SimpleString("import cython");
    PyImport_AddModule("cython");


    PyObject *obj = Py_BuildValue("s", argv[2]);
    FILE *file = _Py_fopen_obj(obj, "r+");

    if(file != NULL) {
        PyRun_SimpleFile(file, argv[2]);
    }

    if (Py_FinalizeEx() < 0) {
        exit(120);
    }

    PyMem_RawFree(program);

    Py_Finalize();

    return 0;
}

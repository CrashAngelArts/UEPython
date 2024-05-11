#/bin/sh

# Copiar /Lib/Python3.12 para diretorio lib e renomear subpasta Lib para lib
# Para funcionar sem o python instalado usar a pasta libpython

echo "----------------"
echo " Build C"
echo "----------------"
gcc  -std=c99 -ggdb3 -O0 -pedantic-errors -Wall -Wextra -fpie -fno-strict-overflow -Wsign-compare -DNDEBUG -g -O2 -Wall -ldl -lm  -I/usr/include/python3.12 -o 'uepython' 'uepython.c' -L/usr/lib/python3.12/config-3.12-aarch64-linux-gnu -L/usr/lib/aarch64-linux-gnu  -lpython3.12

# LibPython
#cp libpython/* /usr//lib/aarch64-linux-gnu/ -R

# Python 3.12 Libraries [ ONLY ]
#cp python3.12/ /usr/lib -R

echo "----------------"
echo " Build Python"
echo "----------------"
cd src/cpython/test && python3 build.py build_ext --inplace

echo "----------------"
echo " Execute"
echo "----------------"
../../.././uepython /root/cpython src/cpython/test/test_builded.py

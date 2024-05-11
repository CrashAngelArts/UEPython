from setuptools import setup
from Cython.Build import cythonize

setup (
    name='GameOverStudios',
    ext_modules=cythonize("test.py"),
)

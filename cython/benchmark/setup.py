from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy

setup(
    ext_modules=cythonize("test_c.pyx"),
    include_dirs=[numpy.get_include()]
)

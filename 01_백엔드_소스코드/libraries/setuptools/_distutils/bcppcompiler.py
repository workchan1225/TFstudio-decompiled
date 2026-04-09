# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: bcppcompiler.pyc (Python 3.11)

'''distutils.bcppcompiler

Contains BorlandCCompiler, an implementation of the abstract CCompiler class
for the Borland C++ compiler.
'''
import os
import warnings
from distutils.errors import DistutilsExecError, CompileError, LibError, LinkError, UnknownFileError
from distutils.ccompiler import CCompiler, gen_preprocess_options
from distutils.file_util import write_file
from distutils.dep_util import newer
from distutils import log
warnings.warn('bcppcompiler is deprecated and slated to be removed in the future. Please discontinue use or file an issue with pypa/distutils describing your use case.', DeprecationWarning)

class BCPPCompiler(CCompiler):
    pass
# WARNING: Decompyle incomplete

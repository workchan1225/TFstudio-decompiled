# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: py_compile.pyc (Python 3.11)

'''Routine to "compile" a .py file to a .pyc file.

This module has intimate knowledge of the format of .pyc files.
'''
import enum
import importlib._bootstrap_external as importlib
import importlib.machinery as importlib
import importlib.util as importlib
import os
import os.path as os
import sys
import traceback
__all__ = [
    'compile',
    'main',
    'PyCompileError',
    'PycInvalidationMode']

class PyCompileError(Exception):
    """Exception raised when an error occurs while attempting to
    compile the file.

    To raise this exception, use

        raise PyCompileError(exc_type,exc_value,file[,msg])

    where

        exc_type:   exception type to be used in error message
                    type name can be accesses as class variable
                    'exc_type_name'

        exc_value:  exception value to be used in error message
                    can be accesses as class variable 'exc_value'

        file:       name of file being compiled to be used in error message
                    can be accesses as class variable 'file'

        msg:        string message to be written as error message
                    If no value is given, a default exception message will be
                    given, consistent with 'standard' py_compile output.
                    message (or default) can be accesses as class variable
                    'msg'

    """
    
    def __init__(self, exc_type, exc_value, file, msg = ('',)):

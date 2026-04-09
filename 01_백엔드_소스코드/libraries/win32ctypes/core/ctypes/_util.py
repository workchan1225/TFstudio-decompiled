# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _util.pyc (Python 3.11)

''' Utility functions to help with ctypes wrapping.
'''
from ctypes import get_last_error, FormatError, WinDLL

def function_factory(function, argument_types, return_type, error_checking = (None, None, None)):
    pass
# WARNING: Decompyle incomplete


def make_error(function, function_name = (None,)):
    code = get_last_error()
    description = FormatError(code).strip()
# WARNING: Decompyle incomplete


def check_null_factory(function_name = (None,)):
    pass
# WARNING: Decompyle incomplete

check_null = check_null_factory()

def check_zero_factory(function_name = (None,)):
    pass
# WARNING: Decompyle incomplete

check_zero = check_zero_factory()

def check_false_factory(function_name = (None,)):
    pass
# WARNING: Decompyle incomplete

check_false = check_false_factory()

class Libraries(object):
    
    def __getattr__(self, name):
        library = WinDLL(name, use_last_error = True)
        self.__dict__[name] = library
        return library


dlls = Libraries()

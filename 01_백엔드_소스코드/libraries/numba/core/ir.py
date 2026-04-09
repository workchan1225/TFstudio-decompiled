# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ir.pyc (Python 3.11)

from collections import defaultdict
import copy
import itertools
import os
import linecache
import pprint
import re
import sys
import operator
from types import FunctionType, BuiltinFunctionType
from functools import total_ordering
from io import StringIO
from numba.core import errors, config
from numba.core.utils import BINOPS_TO_OPERATORS, INPLACE_BINOPS_TO_OPERATORS, UNARY_BUITINS_TO_OPERATORS, OPERATORS_TO_BUILTINS
from numba.core.errors import NotDefinedError, RedefinedError, VerificationError, ConstantInferenceError
from numba.core import consts
_termcolor = errors.termcolor()

class Loc(object):
    '''Source location

    '''
    _defmatcher = re.compile('def\\s+(\\w+)')
    
    def __init__(self, filename, line, col, maybe_decorator = (None, False)):
        ''' Arguments:
        filename - name of the file
        line - line in file
        col - column
        maybe_decorator - Set to True if location is likely a jit decorator
        '''
        self.filename = filename
        self.line = line
        self.col = col
        self.lines = None
        self.maybe_decorator = maybe_decorator

    
    def __eq__(self, other):
        if type(self) is not type(other):
            return False
        if None.filename != other.filename:
            return False
        if None.line != other.line:
            return False
        if None.col != other.col:
            return False

    
    def __ne__(self, other):
        return not self.__eq__(other)

    from_function_id = (lambda cls, func_id: cls(func_id.filename, func_id.firstlineno, maybe_decorator = True))()
    
    def __repr__(self):
        return f'''Loc(filename={self.filename!s}, line={self.line!s}, col={self.col!s})'''

    
    def __str__(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _find_definition(self):
        fn_name = None
        lines = self.get_lines()
        for x in reversed(lines[:self.line - 1]):
            if x.strip().startswith('def '):
                fn_name = x
            
            return fn_name

    
    def _raw_function_name(self):

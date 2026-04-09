# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: templates.pyc (Python 3.11)

'''
Define typing templates
'''
from abc import ABC, abstractmethod
import functools
import sys
import inspect
import os.path as os
from collections import namedtuple
from collections.abc import Sequence
from types import MethodType, FunctionType, MappingProxyType
import numba
from numba.core import types, utils, targetconfig
from numba.core.errors import TypingError, InternalError
from numba.core.cpu_options import InlineOptions
_inline_info = namedtuple('inline_info', 'func_ir typemap calltypes signature')

class Signature(object):
    '''
    The signature of a function call or operation, i.e. its argument types
    and return type.
    '''
    __slots__ = ('_return_type', '_args', '_recvr', '_pysig')
    
    def __init__(self, return_type, args, recvr, pysig = (None,)):
        if isinstance(args, list):
            args = tuple(args)
        self._return_type = return_type
        self._args = args
        self._recvr = recvr
        self._pysig = pysig

    return_type = (lambda self: self._return_type)()
    args = (lambda self: self._args)()
    recvr = (lambda self: self._recvr)()
    pysig = (lambda self: self._pysig)()
    
    def replace(self, **kwargs):
        '''Copy and replace the given attributes provided as keyword arguments.
        Returns an updated copy.
        '''
        curstate = dict(return_type = self.return_type, args = self.args, recvr = self.recvr, pysig = self.pysig)
        curstate.update(kwargs)
    # WARNING: Decompyle incomplete

    
    def __getstate__(self):
        '''
        Needed because of __slots__.
        '''
        return (self._return_type, self._args, self._recvr, self._pysig)

    
    def __setstate__(self, state):
        '''
        Needed because of __slots__.
        '''
        (self._return_type, self._args, self._recvr, self._pysig) = state

    
    def __hash__(self):
        return hash((self.args, self.return_type))

    
    def __eq__(self, other):

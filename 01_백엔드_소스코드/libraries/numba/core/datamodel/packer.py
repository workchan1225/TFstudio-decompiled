# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: packer.pyc (Python 3.11)

from collections import deque
from numba.core import types, cgutils

class DataPacker(object):
    '''
    A helper to pack a number of typed arguments into a data structure.
    Omitted arguments (i.e. values with the type `Omitted`) are automatically
    skipped.
    '''
    
    def __init__(self, dmm, fe_types):
        pass
    # WARNING: Decompyle incomplete

    
    def as_data(self, builder, values):
        '''
        Return the given values packed as a data structure.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _do_load(self, builder, ptr, formal_list = (None,)):
        res = []
    # WARNING: Decompyle incomplete

    
    def load(self, builder, ptr):
        '''
        Load the packed values and return a (type, value) tuples.
        '''
        return self._do_load(builder, ptr)

    
    def load_into(self, builder, ptr, formal_list):
        '''
        Load the packed values into a sequence indexed by formal
        argument number (skipping any Omitted position).
        '''
        self._do_load(builder, ptr, formal_list)



class ArgPacker(object):
    '''
    Compute the position for each high-level typed argument.
    It flattens every composite argument into primitive types.
    It maintains a position map for unflattening the arguments.

    Since struct (esp. nested struct) have specific ABI requirements (e.g.
    alignment, pointer address-space, ...) in different architecture (e.g.
    OpenCL, CUDA), flattening composite argument types simplifes the call
    setup from the Python side.  Functions are receiving simple primitive
    types and there are only a handful of these.
    '''
    
    def __init__(self, dmm, fe_args):
        self._dmm = dmm
        self._fe_args = fe_args
        self._nargs = len(fe_args)
        self._dm_args = []
        argtys = []
        for ty in fe_args:
            dm = self._dmm.lookup(ty)
            self._dm_args.append(dm)
            argtys.append(dm.get_argument_type())
            self._unflattener = _Unflattener(argtys)
            self._be_args = list(_flatten(argtys))
            return None

    
    def as_arguments(self, builder, values):
        '''Flatten all argument values
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def from_arguments(self, builder, args):
        '''Unflatten all argument values
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def assign_names(self, args, names):
        '''Assign names for each flattened argument values.
        '''
        valtree = self._unflattener.unflatten(args)
        for aval, aname in zip(valtree, names):
            self._assign_names(aval, aname)
            return None

    
    def _assign_names(self, val_or_nested, name, depth = ((),)):
        if isinstance(val_or_nested, (tuple, list)):
            for pos, aval in enumerate(val_or_nested):
                self._assign_names(aval, name, depth = depth + (pos,))
                return None
                postfix = '.'.join(map(str, depth))
                parts = [
                    name,
                    postfix]
                val_or_nested.name = '.'.join(filter(bool, parts))
                return None

    argument_types = (lambda self: (lambda .0: pass# WARNING: Decompyle incomplete
)(self._be_args())
)()


def _flatten(iterable):
    '''
    Flatten nested iterable of (tuple, list).
    '''
    pass
# WARNING: Decompyle incomplete

_PUSH_LIST = 1
_APPEND_NEXT_VALUE = 2
_APPEND_EMPTY_TUPLE = 3
_POP = 4

class _Unflattener(object):
    '''
    An object used to unflatten nested sequences after a given pattern
    (an arbitrarily nested sequence).
    The pattern shows the nested sequence shape desired when unflattening;
    the values it contains are irrelevant.
    '''
    
    def __init__(self, pattern):
        self._code = self._build_unflatten_code(pattern)

    
    def _build_unflatten_code(self, iterable):
        '''Build the unflatten opcode sequence for the given *iterable* structure
        (an iterable of nested sequences).
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def unflatten(self, flatiter):
        '''Rebuild a nested tuple structure.
        '''
        vals = deque(flatiter)
        res = []
        cur = res
        stack = []
    # WARNING: Decompyle incomplete

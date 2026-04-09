# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: gufunc.pyc (Python 3.11)

from numba import typeof
from numba.core import types
from numba.np.ufunc.ufuncbuilder import GUFuncBuilder
from numba.np.ufunc.sigparse import parse_signature
from numba.np.ufunc.ufunc_base import UfuncBase, UfuncLowererBase
from numba.np.numpy_support import ufunc_find_matching_loop
from numba.core import serialize, errors
from numba.core.typing import npydecl
from numba.core.typing.templates import signature, AbstractTemplate
import functools

def make_gufunc_kernel(_dufunc):
    pass
# WARNING: Decompyle incomplete


class GUFuncLowerer(UfuncLowererBase):
    pass
# WARNING: Decompyle incomplete


class GUFunc(UfuncBase, serialize.ReduceMixin):
    '''
    Dynamic generalized universal function (GUFunc)
    intended to act like a normal Numpy gufunc, but capable
    of call-time (just-in-time) compilation of fast loops
    specialized to inputs.
    '''
    
    def __init__(self, py_func, signature, identity, cache, is_dynamic, targetoptions, writable_args = (None, None, False, None, ())):
        pass
    # WARNING: Decompyle incomplete

    
    def _initialize(self, dispatcher):
        self.build_ufunc()
        self._install_type()
        self._lower_me = GUFuncLowerer(self)
        self._install_cg()

    
    def _reduce_states(self):
        gb = self.gufunc_builder
        dct = dict(py_func = gb.py_func, signature = gb.signature, identity = self._identity, cache = gb.cache, is_dynamic = self._is_dynamic, targetoptions = gb.targetoptions, writable_args = gb.writable_args, typesigs = gb._sigs, frozen = self._frozen)
        return dct

    _rebuild = (lambda cls, py_func, signature, identity, cache, is_dynamic, targetoptions, writable_args, typesigs, frozen: self = cls(py_func = py_func, signature = signature, identity = identity, cache = cache, is_dynamic = is_dynamic, targetoptions = targetoptions, writable_args = writable_args)for sig in typesigs:
self.add(sig)self.build_ufunc()self._frozen = frozenself)()
    
    def __repr__(self):
        return f'''<numba._GUFunc \'{self.__name__}\'>'''

    
    def _install_type(self, typingctx = (None,)):
        '''Constructs and installs a typing class for a gufunc object in the
        input typing context.  If no typing context is given, then
        _install_type() installs into the typing context of the
        dispatcher object (should be same default context used by
        jit() and njit()).
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def add(self, fty):
        self.gufunc_builder.add(fty)

    
    def build_ufunc(self):
        self.ufunc = self.gufunc_builder.build_ufunc()
        return self

    
    def expected_ndims(self):
        parsed_sig = parse_signature(self.gufunc_builder.signature)
        return (tuple(map(len, parsed_sig[0])), tuple(map(len, parsed_sig[1])))

    
    def _type_me(self, argtys, kws):
        '''
        Implement AbstractTemplate.generic() for the typing class
        built by gufunc._install_type().

        Return the call-site signature after either validating the
        element-wise signature or compiling for it.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _compile_for_argtys(self, argtys, return_type = (None,)):
        pass
    # WARNING: Decompyle incomplete

    
    def match_signature(self, ewise_types, sig):
        dtypes = self._get_ewise_dtypes(sig.args)
        return tuple(dtypes) == tuple(ewise_types)

    is_dynamic = (lambda self: self._is_dynamic)()
    
    def _get_ewise_dtypes(self, args):
        argtys = map((lambda arg: arg if isinstance(arg, types.Type) else typeof(arg)), args)
        tys = []
        for argty in argtys:
            if isinstance(argty, types.Array):
                tys.append(argty.dtype)
                continue
            tys.append(argty)
            return tys

    
    def _num_args_match(self, *args):
        parsed_sig = parse_signature(self.gufunc_builder.signature)
        return len(args) == len(parsed_sig[0]) + len(parsed_sig[1])

    
    def _get_function_type(self, *args):
        parsed_sig = parse_signature(self.gufunc_builder.signature)
        ewise_types = self._get_ewise_dtypes(args)
        l = []
    # WARNING: Decompyle incomplete

    
    def __call__(self, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete



def _is_array_wrapper(obj):

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ufunc_base.pyc (Python 3.11)

from numba.np import numpy_support
from numba.core import types

class UfuncLowererBase:
    '''Callable class responsible for lowering calls to a specific gufunc.
    '''
    
    def __init__(self, ufunc, make_kernel_fn, make_ufunc_kernel_fn):
        self.ufunc = ufunc
        self.make_ufunc_kernel_fn = make_ufunc_kernel_fn
        self.kernel = make_kernel_fn(ufunc)
        self.libs = []

    
    def __call__(self, context, builder, sig, args):
        return self.make_ufunc_kernel_fn(context, builder, sig, args, self.ufunc, self.kernel)



class UfuncBase:
    nin = (lambda self: self.ufunc.nin)()
    nout = (lambda self: self.ufunc.nout)()
    nargs = (lambda self: self.ufunc.nargs)()
    ntypes = (lambda self: self.ufunc.ntypes)()
    types = (lambda self: self.ufunc.types)()
    identity = (lambda self: self.ufunc.identity)()
    signature = (lambda self: self.ufunc.signature)()
    accumulate = (lambda self: self.ufunc.accumulate)()
    at = (lambda self: self.ufunc.at)()
    outer = (lambda self: self.ufunc.outer)()
    reduce = (lambda self: self.ufunc.reduce)()
    reduceat = (lambda self: self.ufunc.reduceat)()
    
    def disable_compile(self):
        '''
        Disable the compilation of new signatures at call time.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _install_cg(self, targetctx = (None,)):
        '''
        Install an implementation function for a GUFunc/DUFunc object in the
        given target context.  If no target context is given, then
        _install_cg() installs into the target context of the
        dispatcher object (should be same default context used by
        jit() and njit()).
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def find_ewise_function(self, ewise_types):
        """
        Given a tuple of element-wise argument types, find a matching
        signature in the dispatcher.

        Return a 2-tuple containing the matching signature, and
        compilation result.  Will return two None's if no matching
        signature was found.
        """
        pass
    # WARNING: Decompyle incomplete

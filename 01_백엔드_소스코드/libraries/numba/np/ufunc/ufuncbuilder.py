# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ufuncbuilder.pyc (Python 3.11)

import inspect
import warnings
from contextlib import contextmanager
from numba.core import config, targetconfig
from numba.core.decorators import jit
from numba.core.descriptors import TargetDescriptor
from numba.core.extending import is_jitted
from numba.core.errors import NumbaDeprecationWarning
from numba.core.options import TargetOptions, include_default_options
from numba.core.registry import cpu_target
from numba.core.target_extension import dispatcher_registry, target_registry
from numba.core import utils, types, serialize, compiler, sigutils
from numba.np.numpy_support import as_dtype
from numba.np.ufunc import _internal
from numba.np.ufunc.sigparse import parse_signature
from numba.np.ufunc.wrappers import build_ufunc_wrapper, build_gufunc_wrapper
from numba.core.caching import FunctionCache, NullCache
from numba.core.compiler_lock import global_compiler_lock
_options_mixin = include_default_options('nopython', 'forceobj', 'boundscheck', 'fastmath', 'writable_args')

class UFuncTargetOptions(TargetOptions, _options_mixin):
    
    def finalize(self, flags, options):
        if not flags.is_set('enable_pyobject'):
            flags.enable_pyobject = True
        if not flags.is_set('enable_looplift'):
            flags.enable_looplift = True
        flags.inherit_if_not_set('nrt', default = True)
        if not flags.is_set('debuginfo'):
            flags.debuginfo = config.DEBUGINFO_DEFAULT
        if not flags.is_set('boundscheck'):
            flags.boundscheck = flags.debuginfo
        flags.enable_pyobject_looplift = True
        flags.inherit_if_not_set('fastmath')



class UFuncTarget(TargetDescriptor):
    pass
# WARNING: Decompyle incomplete

ufunc_target = UFuncTarget()

class UFuncDispatcher(serialize.ReduceMixin):
    '''
    An object handling compilation of various signatures for a ufunc.
    '''
    targetdescr = ufunc_target
    
    def __init__(self, py_func, locals, targetoptions = (None, None)):
        pass
    # WARNING: Decompyle incomplete

    
    def _reduce_states(self):
        '''
        NOTE: part of ReduceMixin protocol
        '''
        return dict(pyfunc = self.py_func, locals = self.locals, targetoptions = self.targetoptions)

    _rebuild = (lambda cls, pyfunc, locals, targetoptions: cls(py_func = pyfunc, locals = locals, targetoptions = targetoptions))()
    
    def enable_caching(self):
        self.cache = FunctionCache(self.py_func)

    
    def compile(self, sig, locals = (None,), **targetoptions):
        pass
    # WARNING: Decompyle incomplete

    
    def _compile_core(self, sig, flags, locals):
        '''
        Trigger the compiler on the core function or load a previously
        compiled version from the cache.  Returns the CompileResult.
        '''
        pass
    # WARNING: Decompyle incomplete


dispatcher_registry[target_registry['npyufunc']] = UFuncDispatcher

def _compile_element_wise_function(nb_func, targetoptions, sig):
    pass
# WARNING: Decompyle incomplete


def _finalize_ufunc_signature(cres, args, return_type):
    """Given a compilation result, argument types, and a return type,
    build a valid Numba signature after validating that it doesn't
    violate the constraints for the compilation mode.
    """
    pass
# WARNING: Decompyle incomplete


def _build_element_wise_ufunc_wrapper(cres, signature):
    '''Build a wrapper for the ufunc loop entry point given by the
    compilation result object, using the element-wise signature.
    '''
    ctx = cres.target_context
    library = cres.library
    fname = cres.fndesc.llvm_func_name
    global_compiler_lock
    info = build_ufunc_wrapper(library, ctx, fname, signature, cres.objectmode, cres)
    ptr = info.library.get_pointer_to_function(info.name)
    None(None, None)

_identities = {
    0: _internal.PyUFunc_Zero,
    1: _internal.PyUFunc_One,
    None: _internal.PyUFunc_None,
    'reorderable': _internal.PyUFunc_ReorderableNone }

def parse_identity(identity):
    '''
    Parse an identity value and return the corresponding low-level value
    for Numpy.
    '''
    
    try:
        identity = _identities[identity]
    except KeyError:
        raise ValueError(f'''Invalid identity value {identity!r}''')

    return identity

_suppress_deprecation_warning_nopython_not_supplied = (lambda : pass# WARNING: Decompyle incomplete
)()

class _BaseUFuncBuilder(object):
    
    def add(self, sig = (None,)):
        if hasattr(self, 'targetoptions'):
            targetoptions = self.targetoptions
        else:
            targetoptions = self.nb_func.targetoptions
        (cres, args, return_type) = _compile_element_wise_function(self.nb_func, targetoptions, sig)
        sig = self._finalize_signature(cres, args, return_type)
        self._sigs.append(sig)
        self._cres[sig] = cres
        return cres

    
    def disable_compile(self):
        '''
        Disable the compilation of new signatures at call time.
        '''
        pass



class UFuncBuilder(_BaseUFuncBuilder):
    
    def __init__(self, py_func, identity, cache, targetoptions = (None, False, None)):
        pass
    # WARNING: Decompyle incomplete

    
    def _finalize_signature(self, cres, args, return_type):
        '''Slated for deprecation, use ufuncbuilder._finalize_ufunc_signature()
        instead.
        '''
        return _finalize_ufunc_signature(cres, args, return_type)

    
    def build_ufunc(self):
        global_compiler_lock
        dtypelist = []
        ptrlist = []
        if not self.nb_func:
            raise TypeError('No definition')
        keepalive = []
        cres = None
    # WARNING: Decompyle incomplete

    
    def build(self, cres, signature):
        '''Slated for deprecation, use
        ufuncbuilder._build_element_wise_ufunc_wrapper().
        '''
        return _build_element_wise_ufunc_wrapper(cres, signature)



class GUFuncBuilder(_BaseUFuncBuilder):
    
    def __init__(self, py_func, signature, identity, cache, targetoptions, writable_args = (None, False, None, ())):
        pass
    # WARNING: Decompyle incomplete

    
    def _finalize_signature(self, cres, args, return_type):
        if cres.objectmode and cres.signature.return_type != types.void:
            raise TypeError('gufunc kernel must have void return type')
    # WARNING: Decompyle incomplete

    build_ufunc = (lambda self: type_list = []func_list = []if not self.nb_func:
raise TypeError('No definition')keepalive = []for sig in self._sigs:
cres = self._cres[sig](dtypenums, ptr, env) = self.build(cres)type_list.append(dtypenums)func_list.append(int(ptr))keepalive.append((cres.library, env))datalist = [
None] * len(func_list)nin = len(self.sin)nout = len(self.sout)ufunc = _internal.fromfunc(self.py_func.__name__, self.py_func.__doc__, func_list, type_list, nin, nout, datalist, keepalive, self.identity, self.signature, self.writable_args)ufunc)()
    
    def build(self, cres):
        '''
        Returns (dtype numbers, function ptr, EnvironmentObject)
        '''
        signature = cres.signature
        info = build_gufunc_wrapper(self.py_func, cres, self.sin, self.sout, cache = self.cache, is_parfors = False)
        env = info.env
        ptr = info.library.get_pointer_to_function(info.name)
        dtypenums = []
        for a in signature.args:
            if isinstance(a, types.Array):
                ty = a.dtype
            else:
                ty = a
            dtypenums.append(as_dtype(ty).num)
            return (dtypenums, ptr, env)



def _get_transform_arg(py_func):
    '''Return function that transform arg into index'''
    pass
# WARNING: Decompyle incomplete

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ffi.pyc (Python 3.11)

import sys
import ctypes
import threading
from importlib.resources import resources as _impres
from llvmlite.binding.common import _decode_string, _is_shutting_down
from llvmlite.utils import get_library_name

def _make_opaque_ref(name):
    newcls = type(name, (ctypes.Structure,), { })
    return ctypes.POINTER(newcls)

LLVMContextRef = _make_opaque_ref('LLVMContext')
LLVMModuleRef = _make_opaque_ref('LLVMModule')
LLVMValueRef = _make_opaque_ref('LLVMValue')
LLVMTypeRef = _make_opaque_ref('LLVMType')
LLVMExecutionEngineRef = _make_opaque_ref('LLVMExecutionEngine')
LLVMPassManagerBuilderRef = _make_opaque_ref('LLVMPassManagerBuilder')
LLVMPassManagerRef = _make_opaque_ref('LLVMPassManager')
LLVMTargetDataRef = _make_opaque_ref('LLVMTargetData')
LLVMTargetLibraryInfoRef = _make_opaque_ref('LLVMTargetLibraryInfo')
LLVMTargetRef = _make_opaque_ref('LLVMTarget')
LLVMTargetMachineRef = _make_opaque_ref('LLVMTargetMachine')
LLVMMemoryBufferRef = _make_opaque_ref('LLVMMemoryBuffer')
LLVMAttributeListIterator = _make_opaque_ref('LLVMAttributeListIterator')
LLVMElementIterator = _make_opaque_ref('LLVMElementIterator')
LLVMAttributeSetIterator = _make_opaque_ref('LLVMAttributeSetIterator')
LLVMGlobalsIterator = _make_opaque_ref('LLVMGlobalsIterator')
LLVMFunctionsIterator = _make_opaque_ref('LLVMFunctionsIterator')
LLVMBlocksIterator = _make_opaque_ref('LLVMBlocksIterator')
LLVMArgumentsIterator = _make_opaque_ref('LLVMArgumentsIterator')
LLVMInstructionsIterator = _make_opaque_ref('LLVMInstructionsIterator')
LLVMOperandsIterator = _make_opaque_ref('LLVMOperandsIterator')
LLVMIncomingBlocksIterator = _make_opaque_ref('LLVMIncomingBlocksIterator')
LLVMTypesIterator = _make_opaque_ref('LLVMTypesIterator')
LLVMObjectCacheRef = _make_opaque_ref('LLVMObjectCache')
LLVMObjectFileRef = _make_opaque_ref('LLVMObjectFile')
LLVMSectionIteratorRef = _make_opaque_ref('LLVMSectionIterator')
LLVMOrcLLJITRef = _make_opaque_ref('LLVMOrcLLJITRef')
LLVMOrcDylibTrackerRef = _make_opaque_ref('LLVMOrcDylibTrackerRef')
LLVMTimePassesHandlerRef = _make_opaque_ref('LLVMTimePassesHandler')
LLVMPipelineTuningOptionsRef = _make_opaque_ref('LLVMPipeLineTuningOptions')
LLVMModulePassManagerRef = _make_opaque_ref('LLVMModulePassManager')
LLVMFunctionPassManagerRef = _make_opaque_ref('LLVMFunctionPassManager')
LLVMPassBuilderRef = _make_opaque_ref('LLVMPassBuilder')

class _LLVMLock:
    '''A Lock to guarantee thread-safety for the LLVM C-API.

    This class implements __enter__ and __exit__ for acquiring and releasing
    the lock as a context manager.

    Also, callbacks can be attached so that every time the lock is acquired
    and released the corresponding callbacks will be invoked.
    '''
    
    def __init__(self):
        self._lock = threading.RLock()
        self._cblist = []

    
    def register(self, acq_fn, rel_fn):
        '''Register callbacks that are invoked immediately after the lock is
        acquired (``acq_fn()``) and immediately before the lock is released
        (``rel_fn()``).
        '''
        self._cblist.append((acq_fn, rel_fn))

    
    def unregister(self, acq_fn, rel_fn):
        '''Remove the registered callbacks.
        '''
        self._cblist.remove((acq_fn, rel_fn))

    
    def __enter__(self):
        self._lock.acquire()
        for acq_fn, rel_fn in self._cblist:
            acq_fn()
            return None

    
    def __exit__(self, *exc_details):
        for acq_fn, rel_fn in self._cblist:
            rel_fn()
            self._lock.release()
            return None



class _suppress_cleanup_errors:
    
    def __init__(self, context):
        self._context = context

    
    def __enter__(self):
        return self._context.__enter__()

    
    def __exit__(self, exc_type, exc_value, traceback):
        
        try:
            return self._context.__exit__(exc_type, exc_value, traceback)
        except PermissionError:
            return None




class _lib_wrapper(object):
    '''Wrap libllvmlite with a lock such that only one thread may access it at
    a time.

    This class duck-types a CDLL.
    '''
    __slots__ = [
        '_lib_handle',
        '_fntab',
        '_lock']
    
    def __init__(self):
        self._lib_handle = None
        self._fntab = { }
        self._lock = _LLVMLock()

    
    def _load_lib(self):
        test_sym = 'LLVMPY_GetVersionInfo'
        mod_name = __name__.rpartition('.')[0]
        lib_name = get_library_name()
        lib_path = _suppress_cleanup_errors(_importlib_resources_path(mod_name, lib_name))
        self._lib_handle = ctypes.CDLL(str(lib_path))
        getattr(self._lib_handle, test_sym)()

    _lib = (lambda self: if not self._lib_handle:
self._load_lib()self._lib_handle)()
    
    def __getattr__(self, name):
        
        try:
            return self._fntab[name]
        except KeyError:
            pass

        cfn = getattr(self._lib, name)
        wrapped = _lib_fn_wrapper(self._lock, cfn)
        self._fntab[name] = wrapped
        return wrapped

    _name = (lambda self: self._lib._name)()
    _handle = (lambda self: self._lib._handle)()


class _lib_fn_wrapper(object):
    '''Wraps and duck-types a ctypes.CFUNCTYPE to provide
    automatic locking when the wrapped function is called.

    TODO: we can add methods to mark the function as threadsafe
          and remove the locking-step on call when marked.
    '''
    __slots__ = [
        '_lock',
        '_cfn']
    
    def __init__(self, lock, cfn):
        self._lock = lock
        self._cfn = cfn

    argtypes = (lambda self: self._cfn.argtypes)()
    argtypes = (lambda self, argtypes: self._cfn.argtypes = argtypes)()
    restype = (lambda self: self._cfn.restype)()
    restype = (lambda self, restype: self._cfn.restype = restype)()
    
    def __call__(self, *args, **kwargs):
        self._lock
    # WARNING: Decompyle incomplete



def _importlib_resources_path_repl(package, resource):
    '''Replacement implementation of `import.resources.path` to avoid
    deprecation warning following code at importlib_resources/_legacy.py
    as suggested by https://importlib-resources.readthedocs.io/en/latest/using.html#migrating-from-legacy

    Notes on differences from importlib.resources implementation:

    The `_common.normalize_path(resource)` call is skipped because it is an
    internal API and it is unnecessary for the use here. What it does is
    ensuring `resource` is a str and that it does not contain path separators.
    '''
    return _impres.as_file(_impres.files(package) / resource)

_importlib_resources_path = _importlib_resources_path_repl if sys.version_info[:2] >= (3, 10) else _impres.path
lib = _lib_wrapper()

def register_lock_callback(acq_fn, rel_fn):
    '''Register callback functions for lock acquire and release.
    *acq_fn* and *rel_fn* are callables that take no arguments.
    '''
    lib._lock.register(acq_fn, rel_fn)


def unregister_lock_callback(acq_fn, rel_fn):
    '''Remove the registered callback functions for lock acquire and release.
    The arguments are the same as used in `register_lock_callback()`.
    '''
    lib._lock.unregister(acq_fn, rel_fn)


class _DeadPointer(object):
    '''
    Dummy class to make error messages more helpful.
    '''
    pass


class OutputString(object):
    '''
    Object for managing the char* output of LLVM APIs.
    '''
    _as_parameter_ = _DeadPointer()
    from_return = (lambda cls, ptr: cls(init = ctypes.cast(ptr, ctypes.c_char_p)))()
    
    def __init__(self, owned, init = (True, None)):
        pass
    # WARNING: Decompyle incomplete

    
    def close(self):
        pass
    # WARNING: Decompyle incomplete

    
    def __enter__(self):
        return self

    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    
    def __del__(self, _is_shutting_down = (_is_shutting_down,)):
        pass
    # WARNING: Decompyle incomplete

    
    def __str__(self):
        pass
    # WARNING: Decompyle incomplete

    
    def __bool__(self):
        return bool(self._ptr)

    __nonzero__ = __bool__
    bytes = (lambda self: self._ptr.value)()


def ret_string(ptr):
    '''To wrap string return-value from C-API.
    '''
    pass
# WARNING: Decompyle incomplete


def ret_bytes(ptr):
    '''To wrap bytes return-value from C-API.
    '''
    pass
# WARNING: Decompyle incomplete


class ObjectRef(object):
    '''
    A wrapper around a ctypes pointer to a LLVM object ("resource").
    '''
    _closed = False
    _as_parameter_ = _DeadPointer()
    _owned = False
    
    def __init__(self, ptr):
        pass
    # WARNING: Decompyle incomplete

    
    def close(self):
        '''
        Close this object and do any required clean-up actions.
        '''
        
        try:
            if not self._closed and self._owned:
                self._dispose()
            self.detach()
            return None
        except:
            self.detach()


    
    def detach(self):
        '''
        Detach the underlying LLVM resource without disposing of it.
        '''
        if not self._closed:
            del self._as_parameter_
            self._closed = True
            self._ptr = None
            return None

    
    def _dispose(self):
        '''
        Dispose of the underlying LLVM resource.  Should be overriden
        by subclasses.  Automatically called by close(), __del__() and
        __exit__() (unless the resource has been detached).
        '''
        pass

    closed = (lambda self: self._closed)()
    
    def __enter__(self):
        pass
    # WARNING: Decompyle incomplete

    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    
    def __del__(self, _is_shutting_down = (_is_shutting_down,)):
        pass
    # WARNING: Decompyle incomplete

    
    def __bool__(self):
        return bool(self._ptr)

    
    def __eq__(self, other):
        if not hasattr(other, '_ptr'):
            return False
        return None.addressof(self._ptr[0]) == ctypes.addressof(other._ptr[0])

    __nonzero__ = __bool__
    
    def __hash__(self):
        return hash(ctypes.cast(self._ptr, ctypes.c_void_p).value)

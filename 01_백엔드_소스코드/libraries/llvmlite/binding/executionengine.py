# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: executionengine.pyc (Python 3.11)

import platform
from ctypes import POINTER, c_char_p, c_bool, c_void_p, c_int, c_uint64, c_size_t, CFUNCTYPE, string_at, cast, py_object, Structure
from llvmlite.binding import ffi, targets, object_file
ffi.lib.LLVMPY_LinkInMCJIT

def create_mcjit_compiler(module, target_machine, use_lmm = (None,)):
    '''
    Create a MCJIT ExecutionEngine from the given *module* and
    *target_machine*.

    *lmm* controls whether the llvmlite memory manager is used. If not supplied,
    the default choice for the platform will be used (``True`` on 64-bit ARM
    systems, ``False`` otherwise).
    '''
    pass
# WARNING: Decompyle incomplete


def check_jit_execution():
    '''
    Check the system allows execution of in-memory JITted functions.
    An exception is raised otherwise.
    '''
    errno = ffi.lib.LLVMPY_TryAllocateExecutableMemory()
    if errno != 0:
        raise OSError(errno, 'cannot allocate executable memory. This may be due to security restrictions on your system, such as SELinux or similar mechanisms.')


class ExecutionEngine(ffi.ObjectRef):
    '''An ExecutionEngine owns all Modules associated with it.
    Deleting the engine will remove all associated modules.
    It is an error to delete the associated modules.
    '''
    _object_cache = None
    
    def __init__(self, ptr, module):
        '''
        Module ownership is transferred to the EE
        '''
        self._modules = set([
            module])
        self._td = None
        module._owned = True
        ffi.ObjectRef.__init__(self, ptr)

    
    def get_function_address(self, name):
        """
        Return the address of the function named *name* as an integer.

        It's a fatal error in LLVM if the symbol of *name* doesn't exist.
        """
        return ffi.lib.LLVMPY_GetFunctionAddress(self, name.encode('ascii'))

    
    def get_global_value_address(self, name):
        """
        Return the address of the global value named *name* as an integer.

        It's a fatal error in LLVM if the symbol of *name* doesn't exist.
        """
        return ffi.lib.LLVMPY_GetGlobalValueAddress(self, name.encode('ascii'))

    
    def add_global_mapping(self, gv, addr):
        ffi.lib.LLVMPY_AddGlobalMapping(self, gv, addr)

    
    def add_module(self, module):
        '''
        Ownership of module is transferred to the execution engine
        '''
        if module in self._modules:
            raise KeyError('module already added to this engine')
        ffi.lib.LLVMPY_AddModule(self, module)
        module._owned = True
        self._modules.add(module)

    
    def finalize_object(self):
        '''
        Make sure all modules owned by the execution engine are fully processed
        and "usable" for execution.
        '''
        ffi.lib.LLVMPY_FinalizeObject(self)

    
    def run_static_constructors(self):
        '''
        Run static constructors which initialize module-level static objects.
        '''
        ffi.lib.LLVMPY_RunStaticConstructors(self)

    
    def run_static_destructors(self):
        '''
        Run static destructors which perform module-level cleanup of static
        resources.
        '''
        ffi.lib.LLVMPY_RunStaticDestructors(self)

    
    def remove_module(self, module):
        '''
        Ownership of module is returned
        '''
        outerr = ffi.OutputString()
        if ffi.lib.LLVMPY_RemoveModule(self, module, outerr):
            raise RuntimeError(str(outerr))
        None(None, None)

    target_data = (lambda self: pass# WARNING: Decompyle incomplete
)()
    
    def enable_jit_events(self):
        '''
        Enable JIT events for profiling of generated code.
        Return value indicates whether connection to profiling tool
        was successful.
        '''
        ret = ffi.lib.LLVMPY_EnableJITEvents(self)
        return ret

    
    def _find_module_ptr(self, module_ptr):
        '''
        Find the ModuleRef corresponding to the given pointer.
        '''
        ptr = cast(module_ptr, c_void_p).value
        for module in self._modules:
            if cast(module._ptr, c_void_p).value == ptr:
                
                return None, module
            return None

    
    def add_object_file(self, obj_file):
        '''
        Add object file to the jit. object_file can be instance of
        :class:ObjectFile or a string representing file system path
        '''
        if isinstance(obj_file, str):
            obj_file = object_file.ObjectFileRef.from_path(obj_file)
        ffi.lib.LLVMPY_MCJITAddObjectFile(self, obj_file)

    
    def set_object_cache(self, notify_func, getbuffer_func = (None, None)):
        '''
        Set the object cache "notifyObjectCompiled" and "getBuffer"
        callbacks to the given Python functions.
        '''
        self._object_cache_notify = notify_func
        self._object_cache_getbuffer = getbuffer_func
        self._object_cache = _ObjectCacheRef(self)
        ffi.lib.LLVMPY_SetObjectCache(self, self._object_cache)

    
    def _raw_object_cache_notify(self, data):
        '''
        Low-level notify hook.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _raw_object_cache_getbuffer(self, data):
        '''
        Low-level getbuffer hook.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _dispose(self):
        pass
    # WARNING: Decompyle incomplete



class _ObjectCacheRef(ffi.ObjectRef):
    '''
    Internal: an ObjectCache instance for use within an ExecutionEngine.
    '''
    
    def __init__(self, obj):
        ptr = ffi.lib.LLVMPY_CreateObjectCache(_notify_c_hook, _getbuffer_c_hook, obj)
        ffi.ObjectRef.__init__(self, ptr)

    
    def _dispose(self):
        self._capi.LLVMPY_DisposeObjectCache(self)


ffi.lib.LLVMPY_CreateMCJITCompiler.argtypes = [
    ffi.LLVMModuleRef,
    ffi.LLVMTargetMachineRef,
    c_bool,
    POINTER(c_char_p)]
ffi.lib.LLVMPY_CreateMCJITCompiler.restype = ffi.LLVMExecutionEngineRef
ffi.lib.LLVMPY_RemoveModule.argtypes = [
    ffi.LLVMExecutionEngineRef,
    ffi.LLVMModuleRef,
    POINTER(c_char_p)]
ffi.lib.LLVMPY_RemoveModule.restype = c_bool
ffi.lib.LLVMPY_AddModule.argtypes = [
    ffi.LLVMExecutionEngineRef,
    ffi.LLVMModuleRef]
ffi.lib.LLVMPY_AddGlobalMapping.argtypes = [
    ffi.LLVMExecutionEngineRef,
    ffi.LLVMValueRef,
    c_void_p]
ffi.lib.LLVMPY_FinalizeObject.argtypes = [
    ffi.LLVMExecutionEngineRef]
ffi.lib.LLVMPY_GetExecutionEngineTargetData.argtypes = [
    ffi.LLVMExecutionEngineRef]
ffi.lib.LLVMPY_GetExecutionEngineTargetData.restype = ffi.LLVMTargetDataRef
ffi.lib.LLVMPY_TryAllocateExecutableMemory.argtypes = []
ffi.lib.LLVMPY_TryAllocateExecutableMemory.restype = c_int
ffi.lib.LLVMPY_GetFunctionAddress.argtypes = [
    ffi.LLVMExecutionEngineRef,
    c_char_p]
ffi.lib.LLVMPY_GetFunctionAddress.restype = c_uint64
ffi.lib.LLVMPY_GetGlobalValueAddress.argtypes = [
    ffi.LLVMExecutionEngineRef,
    c_char_p]
ffi.lib.LLVMPY_GetGlobalValueAddress.restype = c_uint64
ffi.lib.LLVMPY_MCJITAddObjectFile.argtypes = [
    ffi.LLVMExecutionEngineRef,
    ffi.LLVMObjectFileRef]

class _ObjectCacheData(Structure):
    _fields_ = [
        ('module_ptr', ffi.LLVMModuleRef),
        ('buf_ptr', c_void_p),
        ('buf_len', c_size_t)]

_ObjectCacheNotifyFunc = CFUNCTYPE(None, py_object, POINTER(_ObjectCacheData))
_ObjectCacheGetBufferFunc = CFUNCTYPE(None, py_object, POINTER(_ObjectCacheData))
_notify_c_hook = _ObjectCacheNotifyFunc(ExecutionEngine._raw_object_cache_notify)
_getbuffer_c_hook = _ObjectCacheGetBufferFunc(ExecutionEngine._raw_object_cache_getbuffer)
ffi.lib.LLVMPY_CreateObjectCache.argtypes = [
    _ObjectCacheNotifyFunc,
    _ObjectCacheGetBufferFunc,
    py_object]
ffi.lib.LLVMPY_CreateObjectCache.restype = ffi.LLVMObjectCacheRef
ffi.lib.LLVMPY_DisposeObjectCache.argtypes = [
    ffi.LLVMObjectCacheRef]
ffi.lib.LLVMPY_SetObjectCache.argtypes = [
    ffi.LLVMExecutionEngineRef,
    ffi.LLVMObjectCacheRef]
ffi.lib.LLVMPY_CreateByteString.restype = c_void_p
ffi.lib.LLVMPY_CreateByteString.argtypes = [
    c_void_p,
    c_size_t]

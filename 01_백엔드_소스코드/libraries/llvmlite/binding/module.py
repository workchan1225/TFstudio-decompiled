# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: module.pyc (Python 3.11)

from ctypes import c_char_p, byref, POINTER, c_bool, create_string_buffer, c_size_t, string_at
from llvmlite.binding import ffi
from llvmlite.binding.linker import link_modules
from llvmlite.binding.common import _decode_string, _encode_string
from llvmlite.binding.value import ValueRef, TypeRef
from llvmlite.binding.context import get_global_context

def parse_assembly(llvmir, context = (None,)):
    '''
    Create Module from a LLVM IR string
    '''
    pass
# WARNING: Decompyle incomplete


def parse_bitcode(bitcode, context = (None,)):
    '''
    Create Module from a LLVM *bitcode* (a bytes object).
    '''
    pass
# WARNING: Decompyle incomplete


class ModuleRef(ffi.ObjectRef):
    pass
# WARNING: Decompyle incomplete


class _Iterator(ffi.ObjectRef):
    kind = None
    
    def __init__(self, ptr, parents):
        ffi.ObjectRef.__init__(self, ptr)
        self._parents = parents
    # WARNING: Decompyle incomplete

    
    def __next__(self):
        vp = self._next()
        if vp:
            return ValueRef(vp, self.kind, self._parents)
        raise None

    next = __next__
    
    def __iter__(self):
        return self



class _GlobalsIterator(_Iterator):
    kind = 'global'
    
    def _dispose(self):
        self._capi.LLVMPY_DisposeGlobalsIter(self)

    
    def _next(self):
        return ffi.lib.LLVMPY_GlobalsIterNext(self)



class _FunctionsIterator(_Iterator):
    kind = 'function'
    
    def _dispose(self):
        self._capi.LLVMPY_DisposeFunctionsIter(self)

    
    def _next(self):
        return ffi.lib.LLVMPY_FunctionsIterNext(self)



class _TypesIterator(_Iterator):
    kind = 'type'
    
    def _dispose(self):
        self._capi.LLVMPY_DisposeTypesIter(self)

    
    def __next__(self):
        vp = self._next()
        if vp:
            return TypeRef(vp)
        raise None

    
    def _next(self):
        return ffi.lib.LLVMPY_TypesIterNext(self)

    next = __next__

ffi.lib.LLVMPY_ParseAssembly.argtypes = [
    ffi.LLVMContextRef,
    c_char_p,
    POINTER(c_char_p)]
ffi.lib.LLVMPY_ParseAssembly.restype = ffi.LLVMModuleRef
ffi.lib.LLVMPY_ParseBitcode.argtypes = [
    ffi.LLVMContextRef,
    c_char_p,
    c_size_t,
    POINTER(c_char_p)]
ffi.lib.LLVMPY_ParseBitcode.restype = ffi.LLVMModuleRef
ffi.lib.LLVMPY_DisposeModule.argtypes = [
    ffi.LLVMModuleRef]
ffi.lib.LLVMPY_PrintModuleToString.argtypes = [
    ffi.LLVMModuleRef,
    POINTER(c_char_p)]
ffi.lib.LLVMPY_WriteBitcodeToString.argtypes = [
    ffi.LLVMModuleRef,
    POINTER(c_char_p),
    POINTER(c_size_t)]
ffi.lib.LLVMPY_GetNamedFunction.argtypes = [
    ffi.LLVMModuleRef,
    c_char_p]
ffi.lib.LLVMPY_GetNamedFunction.restype = ffi.LLVMValueRef
ffi.lib.LLVMPY_VerifyModule.argtypes = [
    ffi.LLVMModuleRef,
    POINTER(c_char_p)]
ffi.lib.LLVMPY_VerifyModule.restype = c_bool
ffi.lib.LLVMPY_GetDataLayout.argtypes = [
    ffi.LLVMModuleRef,
    POINTER(c_char_p)]
ffi.lib.LLVMPY_SetDataLayout.argtypes = [
    ffi.LLVMModuleRef,
    c_char_p]
ffi.lib.LLVMPY_GetTarget.argtypes = [
    ffi.LLVMModuleRef,
    POINTER(c_char_p)]
ffi.lib.LLVMPY_SetTarget.argtypes = [
    ffi.LLVMModuleRef,
    c_char_p]
ffi.lib.LLVMPY_GetNamedGlobalVariable.argtypes = [
    ffi.LLVMModuleRef,
    c_char_p]
ffi.lib.LLVMPY_GetNamedGlobalVariable.restype = ffi.LLVMValueRef
ffi.lib.LLVMPY_GetNamedStructType.argtypes = [
    ffi.LLVMModuleRef,
    c_char_p]
ffi.lib.LLVMPY_GetNamedStructType.restype = ffi.LLVMTypeRef
ffi.lib.LLVMPY_ModuleGlobalsIter.argtypes = [
    ffi.LLVMModuleRef]
ffi.lib.LLVMPY_ModuleGlobalsIter.restype = ffi.LLVMGlobalsIterator
ffi.lib.LLVMPY_DisposeGlobalsIter.argtypes = [
    ffi.LLVMGlobalsIterator]
ffi.lib.LLVMPY_GlobalsIterNext.argtypes = [
    ffi.LLVMGlobalsIterator]
ffi.lib.LLVMPY_GlobalsIterNext.restype = ffi.LLVMValueRef
ffi.lib.LLVMPY_ModuleFunctionsIter.argtypes = [
    ffi.LLVMModuleRef]
ffi.lib.LLVMPY_ModuleFunctionsIter.restype = ffi.LLVMFunctionsIterator
ffi.lib.LLVMPY_ModuleTypesIter.argtypes = [
    ffi.LLVMModuleRef]
ffi.lib.LLVMPY_ModuleTypesIter.restype = ffi.LLVMTypesIterator
ffi.lib.LLVMPY_DisposeFunctionsIter.argtypes = [
    ffi.LLVMFunctionsIterator]
ffi.lib.LLVMPY_DisposeTypesIter.argtypes = [
    ffi.LLVMTypesIterator]
ffi.lib.LLVMPY_FunctionsIterNext.argtypes = [
    ffi.LLVMFunctionsIterator]
ffi.lib.LLVMPY_FunctionsIterNext.restype = ffi.LLVMValueRef
ffi.lib.LLVMPY_TypesIterNext.argtypes = [
    ffi.LLVMTypesIterator]
ffi.lib.LLVMPY_TypesIterNext.restype = ffi.LLVMTypeRef
ffi.lib.LLVMPY_CloneModule.argtypes = [
    ffi.LLVMModuleRef]
ffi.lib.LLVMPY_CloneModule.restype = ffi.LLVMModuleRef
ffi.lib.LLVMPY_GetModuleName.argtypes = [
    ffi.LLVMModuleRef]
ffi.lib.LLVMPY_GetModuleName.restype = c_char_p
ffi.lib.LLVMPY_SetModuleName.argtypes = [
    ffi.LLVMModuleRef,
    c_char_p]
ffi.lib.LLVMPY_GetModuleSourceFileName.argtypes = [
    ffi.LLVMModuleRef]
ffi.lib.LLVMPY_GetModuleSourceFileName.restype = c_char_p

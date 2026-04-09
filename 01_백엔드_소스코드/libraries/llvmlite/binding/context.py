# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: context.pyc (Python 3.11)

from llvmlite.binding import ffi

def create_context():
    return ContextRef(ffi.lib.LLVMPY_ContextCreate())


def get_global_context():
    return GlobalContextRef(ffi.lib.LLVMPY_GetGlobalContext())


class ContextRef(ffi.ObjectRef):
    pass
# WARNING: Decompyle incomplete


class GlobalContextRef(ContextRef):
    
    def _dispose(self):
        pass


ffi.lib.LLVMPY_GetGlobalContext.restype = ffi.LLVMContextRef
ffi.lib.LLVMPY_ContextCreate.restype = ffi.LLVMContextRef
ffi.lib.LLVMPY_ContextDispose.argtypes = [
    ffi.LLVMContextRef]

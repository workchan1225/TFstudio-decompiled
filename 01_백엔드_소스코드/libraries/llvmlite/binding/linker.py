# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: linker.pyc (Python 3.11)

from ctypes import c_int, c_char_p, POINTER
from llvmlite.binding import ffi

def link_modules(dst, src):
    outerr = ffi.OutputString()
    err = ffi.lib.LLVMPY_LinkModules(dst, src, outerr)
    src.detach()
    if err:
        raise RuntimeError(str(outerr))
    None(None, None)
    return None
    with None:
        if not None:
            pass

ffi.lib.LLVMPY_LinkModules.argtypes = [
    ffi.LLVMModuleRef,
    ffi.LLVMModuleRef,
    POINTER(c_char_p)]
ffi.lib.LLVMPY_LinkModules.restype = c_int

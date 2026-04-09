# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: targets.pyc (Python 3.11)

import os
from ctypes import POINTER, c_char_p, c_longlong, c_int, c_size_t, c_void_p, string_at
from llvmlite.binding import ffi
from llvmlite.binding.initfini import llvm_version_info
from llvmlite.binding.common import _decode_string, _encode_string
from collections import namedtuple
from llvmlite.binding.config import _has_svml as has_svml
Triple = namedtuple('Triple', [
    'Arch',
    'SubArch',
    'Vendor',
    'OS',
    'Env',
    'ObjectFormat'])

def get_process_triple():
    '''
    Return a target triple suitable for generating code for the current process.
    An example when the default triple from ``get_default_triple()`` is not be
    suitable is when LLVM is compiled for 32-bit but the process is executing
    in 64-bit mode.
    '''
    out = ffi.OutputString()
    ffi.lib.LLVMPY_GetProcessTriple(out)
    None(None, None)
    return 
    with None:
        if not None, str(out):
            pass


def get_triple_parts(triple = None):

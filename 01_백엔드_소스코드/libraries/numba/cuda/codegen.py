# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: codegen.pyc (Python 3.11)

from llvmlite import ir
from numba.core import config, serialize
from numba.core.codegen import Codegen, CodeLibrary
from cudadrv import devices, driver, nvvm, runtime
from numba.cuda.cudadrv.libs import get_cudalib
import os
import subprocess
import tempfile
CUDA_TRIPLE = 'nvptx64-nvidia-cuda'

def run_nvdisasm(cubin, flags):
    fd = None
    fname = None
# WARNING: Decompyle incomplete


def disassemble_cubin(cubin):
    flags = [
        '-gi']
    return run_nvdisasm(cubin, flags)


def disassemble_cubin_for_cfg(cubin):
    flags = [
        '-cfg']
    return run_nvdisasm(cubin, flags)


class CUDACodeLibrary(CodeLibrary, serialize.ReduceMixin):
    pass
# WARNING: Decompyle incomplete


class JITCUDACodegen(Codegen):
    '''
    This codegen implementation for CUDA only generates optimized LLVM IR.
    Generation of PTX code is done separately (see numba.cuda.compiler).
    '''
    _library_class = CUDACodeLibrary
    
    def __init__(self, module_name):
        pass

    
    def _create_empty_module(self, name):
        ir_module = ir.Module(name)
        ir_module.triple = CUDA_TRIPLE
        ir_module.data_layout = nvvm.NVVM().data_layout
        nvvm.add_ir_version(ir_module)
        return ir_module

    
    def _add_module(self, module):
        pass

    
    def magic_tuple(self):
        '''
        Return a tuple unambiguously describing the codegen behaviour.
        '''
        ctx = devices.get_context()
        cc = ctx.device.compute_capability
        return (runtime.runtime.get_version(), cc)

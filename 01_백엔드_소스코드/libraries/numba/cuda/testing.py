# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: testing.pyc (Python 3.11)

import os
import platform
import shutil
from numba.tests.support import SerialMixin
from numba.cuda.cuda_paths import get_conda_ctk
from numba.cuda.cudadrv import driver, devices, libs
from numba.core import config
from numba.tests.support import TestCase
from pathlib import Path
import unittest
numba_cuda_dir = Path(__file__).parent
test_data_dir = numba_cuda_dir / 'tests' / 'data'

class CUDATestCase(TestCase, SerialMixin):
    '''
    For tests that use a CUDA device. Test methods in a CUDATestCase must not
    be run out of module order, because the ContextResettingTestCase may reset
    the context and destroy resources used by a normal CUDATestCase if any of
    its tests are run between tests from a CUDATestCase.
    '''
    
    def setUp(self):
        self._low_occupancy_warnings = config.CUDA_LOW_OCCUPANCY_WARNINGS
        self._warn_on_implicit_copy = config.CUDA_WARN_ON_IMPLICIT_COPY
        config.CUDA_LOW_OCCUPANCY_WARNINGS = 0
        config.CUDA_WARN_ON_IMPLICIT_COPY = 0

    
    def tearDown(self):
        config.CUDA_LOW_OCCUPANCY_WARNINGS = self._low_occupancy_warnings
        config.CUDA_WARN_ON_IMPLICIT_COPY = self._warn_on_implicit_copy

    
    def skip_if_lto(self, reason):
        cc = devices.get_context().device.compute_capability
        linker = driver.Linker.new(cc = cc)
        if linker.lto:
            self.skipTest(reason)
            return None



class ContextResettingTestCase(CUDATestCase):
    pass
# WARNING: Decompyle incomplete


def ensure_supported_ccs_initialized():
    cuda_is_available = is_available
    import numba.cuda
    nvvm = nvvm
    import numba.cuda.cudadrv
    if cuda_is_available():
        nvvm.get_supported_ccs()
        return None


def skip_on_cudasim(reason):
    '''Skip this test if running on the CUDA simulator'''
    return unittest.skipIf(config.ENABLE_CUDASIM, reason)


def skip_unless_cudasim(reason):
    '''Skip this test if running on CUDA hardware'''
    return unittest.skipUnless(config.ENABLE_CUDASIM, reason)


def skip_unless_conda_cudatoolkit(reason):
    '''Skip test if the CUDA toolkit was not installed by Conda'''
    return unittest.skipUnless(get_conda_ctk() is not None, reason)


def skip_if_external_memmgr(reason):
    '''Skip test if an EMM Plugin is in use'''
    return unittest.skipIf(config.CUDA_MEMORY_MANAGER != 'default', reason)


def skip_under_cuda_memcheck(reason):
    return unittest.skipIf(os.environ.get('CUDA_MEMCHECK') is not None, reason)


def skip_without_nvdisasm(reason):
    nvdisasm_path = shutil.which('nvdisasm')
    return unittest.skipIf(nvdisasm_path is None, reason)


def skip_with_nvdisasm(reason):
    nvdisasm_path = shutil.which('nvdisasm')
    return unittest.skipIf(nvdisasm_path is not None, reason)


def skip_on_arm(reason):

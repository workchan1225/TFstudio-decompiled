# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: executor.pyc (Python 3.11)

'''Utility function to construct a loky.ReusableExecutor with custom pickler.

This module provides efficient ways of working with data stored in
shared memory with numpy.memmap arrays without inducing any memory
copy between the parent and child processes.
'''
from _memmapping_reducer import TemporaryResourcesManager, get_memmapping_reducers
from externals.loky.reusable_executor import _ReusablePoolExecutor
_executor_args = None

def get_memmapping_executor(n_jobs, **kwargs):
    pass
# WARNING: Decompyle incomplete


class MemmappingExecutor(_ReusablePoolExecutor):
    pass
# WARNING: Decompyle incomplete


class _TestingMemmappingExecutor(MemmappingExecutor):
    pass
# WARNING: Decompyle incomplete

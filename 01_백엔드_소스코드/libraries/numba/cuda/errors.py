# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: errors.pyc (Python 3.11)

import numbers
from numba.core.errors import LoweringError

class KernelRuntimeError(RuntimeError):
    pass
# WARNING: Decompyle incomplete


class CudaLoweringError(LoweringError):
    pass

_launch_help_url = 'https://numba.readthedocs.io/en/stable/cuda/kernels.html#kernel-invocation'
missing_launch_config_msg = '\nKernel launch configuration was not specified. Use the syntax:\n\nkernel_function[blockspergrid, threadsperblock](arg0, arg1, ..., argn)\n\nSee {} for help.\n\n'.format(_launch_help_url)

def normalize_kernel_dimensions(griddim, blockdim):
    '''
    Normalize and validate the user-supplied kernel dimensions.
    '''
    
    def check_dim(dim, name):
        if not isinstance(dim, (tuple, list)):
            dim = [
                dim]
        else:
            dim = list(dim)
        if len(dim) > 3:
            raise ValueError(f'''{name!s} must be a sequence of 1, 2 or 3 integers, got {dim!r}''')
    # WARNING: Decompyle incomplete

    if None in (griddim, blockdim):
        raise ValueError(missing_launch_config_msg)
    griddim = check_dim(griddim, 'griddim')
    blockdim = check_dim(blockdim, 'blockdim')
    return (griddim, blockdim)

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: initialize.pyc (Python 3.11)


def initialize_all():
    import numba.cuda.models as numba
    jit = jit
    import numba.cuda.decorators
    CUDADispatcher = CUDADispatcher
    import numba.cuda.dispatcher
    target_registry = target_registry
    dispatcher_registry = dispatcher_registry
    jit_registry = jit_registry
    import numba.core.target_extension
    cuda_target = target_registry['cuda']
    jit_registry[cuda_target] = jit
    dispatcher_registry[cuda_target] = CUDADispatcher

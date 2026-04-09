# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: api.pyc (Python 3.11)

'''
Contains CUDA API functions
'''
from contextlib import contextmanager
from cudadrv.devices import require_context, reset, gpus
from kernel import FakeCUDAKernel
from numba.core.sigutils import is_signature
from warnings import warn
from args import In, Out, InOut

def select_device(dev = (0,)):
    pass
# WARNING: Decompyle incomplete


def is_float16_supported():
    return True


class stream(object):
    '''
    The stream API is supported in the simulator - however, all execution
    occurs synchronously, so synchronization requires no operation.
    '''
    auto_synchronize = (lambda self: pass# WARNING: Decompyle incomplete
)()
    
    def synchronize(self):
        pass



def synchronize():
    pass


def close():
    gpus.closed = True


def declare_device(*args, **kwargs):
    pass


def detect():
    print('Found 1 CUDA devices')
    print('id %d    %20s %40s' % (0, 'SIMULATOR', '[SUPPORTED]'))
    print('%40s: 5.0' % 'compute capability')


def list_devices():
    return gpus


class Event(object):
    '''
    The simulator supports the event API, but they do not record timing info,
    and all simulation is synchronous. Execution time is not recorded.
    '''
    
    def record(self, stream = (0,)):
        pass

    
    def wait(self, stream = (0,)):
        pass

    
    def synchronize(self):
        pass

    
    def elapsed_time(self, event):
        warn('Simulator timings are bogus')
        return 0


event = Event

def jit(func_or_sig, device, debug, argtypes, inline, restype, fastmath, link, boundscheck, opt, cache = (None, False, False, None, False, None, False, None, None, True, None)):
    pass
# WARNING: Decompyle incomplete

defer_cleanup = (lambda : pass# WARNING: Decompyle incomplete
)()

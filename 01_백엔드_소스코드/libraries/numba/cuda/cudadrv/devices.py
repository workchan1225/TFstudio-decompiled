# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: devices.pyc (Python 3.11)

'''
Expose each GPU devices directly.

This module implements a API that is like the "CUDA runtime" context manager
for managing CUDA context stack and clean up.  It relies on thread-local globals
to separate the context stack management of each thread. Contexts are also
shareable among threads.  Only the main thread can destroy Contexts.

Note:
- This module must be imported by the main-thread.

'''
import functools
import threading
from contextlib import contextmanager
from driver import driver, USE_NV_BINDING

class _DeviceList(object):
    pass
# WARNING: Decompyle incomplete


class _DeviceContextManager(object):
    '''
    Provides a context manager for executing in the context of the chosen
    device. The normal use of instances of this type is from
    ``numba.cuda.gpus``. For example, to execute on device 2::

       with numba.cuda.gpus[2]:
           d_a = numba.cuda.to_device(a)

    to copy the array *a* onto device 2, referred to by *d_a*.
    '''
    
    def __init__(self, device):
        self._device = device

    
    def __getattr__(self, item):
        return getattr(self._device, item)

    
    def __enter__(self):
        _runtime.get_or_create_context(self._device.id)

    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self._device.get_primary_context().pop()

    
    def __str__(self):
        return '<Managed Device {self.id}>'.format(self = self)



class _Runtime(object):
    '''Emulate the CUDA runtime context management.

    It owns all Devices and Contexts.
    Keeps at most one Context per Device
    '''
    
    def __init__(self):
        self.gpus = _DeviceList()
        self._tls = threading.local()
        self._mainthread = threading.current_thread()
        self._lock = threading.RLock()

    ensure_context = (lambda self: pass# WARNING: Decompyle incomplete
)()
    
    def get_or_create_context(self, devnum):
        '''Returns the primary context and push+create it if needed
        for *devnum*.  If *devnum* is None, use the active CUDA context (must
        be primary) or create a new one with ``devnum=0``.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _get_or_create_context_uncached(self, devnum):
        '''See also ``get_or_create_context(devnum)``.
        This version does not read the cache.
        '''
        self._lock
        ac = driver.get_active_context()
        if not ac:
            None(None, None)
            None(None, None)
            return 
        if ctx_handle != ac_ctx_handle:
            msg = 'Numba cannot operate on non-primary CUDA context {:x}'
            raise RuntimeError(msg.format(ac_ctx_handle))
        ctx.prepare_for_use()
        None(None, None)
        None(None, None)
        return 
        with None:
            if not None if USE_NV_BINDING else None.gpus[ac.devnum].get_primary_context(), ctx, :
                pass
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def _activate_context_for(self, devnum):
        self._lock
        gpu = self.gpus[devnum]
        newctx = gpu.get_primary_context()
        cached_ctx = self._get_attached_context()
    # WARNING: Decompyle incomplete

    
    def _get_attached_context(self):
        return getattr(self._tls, 'attached_context', None)

    
    def _set_attached_context(self, ctx):
        self._tls.attached_context = ctx

    
    def reset(self):
        '''Clear all contexts in the thread.  Destroy the context if and only
        if we are in the main thread.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _destroy_all_contexts(self):
        for gpu in self.gpus:
            gpu.reset()
            return None


_runtime = _Runtime()
gpus = _runtime.gpus

def get_context(devnum = (None,)):
    '''Get the current device or use a device by device number, and
    return the CUDA context.
    '''
    return _runtime.get_or_create_context(devnum)


def require_context(fn):
    '''
    A decorator that ensures a CUDA context is available when *fn* is executed.

    Note: The function *fn* cannot switch CUDA-context.
    '''
    pass
# WARNING: Decompyle incomplete


def reset():
    '''Reset the CUDA subsystem for the current thread.

    In the main thread:
    This removes all CUDA contexts.  Only use this at shutdown or for
    cleaning up between tests.

    In non-main threads:
    This clear the CUDA context stack only.

    '''
    _runtime.reset()

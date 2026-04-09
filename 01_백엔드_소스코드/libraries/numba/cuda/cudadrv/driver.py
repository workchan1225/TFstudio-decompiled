# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: driver.pyc (Python 3.11)

'''
CUDA driver bridge implementation

NOTE:
The new driver implementation uses a *_PendingDeallocs* that help prevents a
crashing the system (particularly OSX) when the CUDA context is corrupted at
resource deallocation.  The old approach ties resource management directly
into the object destructor; thus, at corruption of the CUDA context,
subsequent deallocation could further corrupt the CUDA context and causes the
system to freeze in some cases.

'''
import sys
import os
import ctypes
import weakref
import functools
import warnings
import logging
import threading
import asyncio
import pathlib
from itertools import product
from abc import ABCMeta, abstractmethod
from ctypes import c_int, byref, c_size_t, c_char, c_char_p, addressof, c_void_p, c_float, c_uint
import contextlib
import importlib
import numpy as np
from collections import namedtuple, deque
from numba import mviewbuf
from numba.core import utils, serialize, config
from error import CudaSupportError, CudaDriverError
from drvapi import API_PROTOTYPES
from drvapi import cu_occupancy_b2d_size, cu_stream_callback_pyobj, cu_uuid
from numba.cuda.cudadrv import enums, drvapi, nvrtc, _extras
USE_NV_BINDING = config.CUDA_USE_NVIDIA_BINDING
if USE_NV_BINDING:
    from cuda import cuda as binding
    CU_STREAM_DEFAULT = 0
MIN_REQUIRED_CC = (3, 5)
SUPPORTS_IPC = sys.platform.startswith('linux')
_py_decref = ctypes.pythonapi.Py_DecRef
_py_incref = ctypes.pythonapi.Py_IncRef
_py_decref.argtypes = [
    ctypes.py_object]
_py_incref.argtypes = [
    ctypes.py_object]

def make_logger():
    logger = logging.getLogger(__name__)
    if not logger.hasHandlers():
        lvl = str(config.CUDA_LOG_LEVEL).upper()
        lvl = getattr(logging, lvl, None)
        if not isinstance(lvl, int):
            lvl = logging.CRITICAL
        logger.setLevel(lvl)
        if config.CUDA_LOG_LEVEL:
            handler = logging.StreamHandler(sys.stderr)
            fmt = '== CUDA [%(relativeCreated)d] %(levelname)5s -- %(message)s'
            handler.setFormatter(logging.Formatter(fmt = fmt))
            logger.addHandler(handler)
        else:
            logger.addHandler(logging.NullHandler())
    return logger


class DeadMemoryError(RuntimeError):
    pass


class LinkerError(RuntimeError):
    pass


class CudaAPIError(CudaDriverError):
    pass
# WARNING: Decompyle incomplete


def locate_driver_and_loader():
    envpath = config.CUDA_DRIVER
    if envpath == '0':
        _raise_driver_not_found()
    if sys.platform == 'win32':
        dlloader = ctypes.WinDLL
        dldir = [
            '\\windows\\system32']
        dlnames = [
            'nvcuda.dll']
    elif sys.platform == 'darwin':
        dlloader = ctypes.CDLL
        dldir = [
            '/usr/local/cuda/lib']
        dlnames = [
            'libcuda.dylib']
    else:
        dlloader = ctypes.CDLL
        dldir = [
            '/usr/lib',
            '/usr/lib64']
        dlnames = [
            'libcuda.so',
            'libcuda.so.1']
    return (dlloader, candidates)


def load_driver(dlloader, candidates):
    path_not_exist = []
    driver_load_error = []
    for path in candidates:
        dll = dlloader(path)
        
        return None, (dll, path)
        except OSError:
            path_not_exist.append(not os.path.isfile(path))
            driver_load_error.append(e)
            None = None
            del e
            continue
            e = None
            del e
        if all(path_not_exist):
            _raise_driver_not_found()
            return None
        errmsg = (lambda .0: pass# WARNING: Decompyle incomplete
)(driver_load_error())
        _raise_driver_error(errmsg)
        return None


def find_driver():
    (dlloader, candidates) = locate_driver_and_loader()
    (dll, path) = load_driver(dlloader, candidates)
    return dll

DRIVER_NOT_FOUND_MSG = '\nCUDA driver library cannot be found.\nIf you are sure that a CUDA driver is installed,\ntry setting environment variable NUMBA_CUDA_DRIVER\nwith the file path of the CUDA driver shared library.\n'
DRIVER_LOAD_ERROR_MSG = '\nPossible CUDA driver libraries are found but error occurred during load:\n%s\n'

def _raise_driver_not_found():
    raise CudaSupportError(DRIVER_NOT_FOUND_MSG)


def _raise_driver_error(e):
    raise CudaSupportError(DRIVER_LOAD_ERROR_MSG % e)


def _build_reverse_error_map():
    prefix = 'CUDA_ERROR'
    map = utils.UniqueDict()
    for name in dir(enums):
        if name.startswith(prefix):
            code = getattr(enums, name)
            map[code] = name
        return map


def _getpid():
    return os.getpid()

ERROR_MAP = _build_reverse_error_map()

class Driver(object):
    '''
    Driver API functions are lazily bound.
    '''
    _singleton = None
    
    def __new__(cls):
        obj = cls._singleton
    # WARNING: Decompyle incomplete

    
    def __init__(self):
        self.devices = utils.UniqueDict()
        self.is_initialized = False
        self.initialization_error = None
        self.pid = None
        
        try:
            if config.DISABLE_CUDA:
                msg = 'CUDA is disabled due to setting NUMBA_DISABLE_CUDA=1 in the environment, or because CUDA is unsupported on 32-bit systems.'
                raise CudaSupportError(msg)
            self.lib = find_driver()
            return None
        except CudaSupportError:
            e = None
            self.is_initialized = True
            self.initialization_error = e.msg
            e = None
            del e
            return None
            e = None
            del e


    
    def ensure_initialized(self):
        global _logger
        if self.is_initialized:
            return None
        _logger = None()
        self.is_initialized = True
        
        try:
            _logger.info('init')
            self.cuInit(0)
            self.pid = _getpid()
        except CudaAPIError:
            e = None
            description = f'''{e.msg} ({e.code})'''
            self.initialization_error = description
            raise CudaSupportError(f'''Error at driver init: {description}''')
            e = None
            del e

        self._initialize_extras()

    
    def _initialize_extras(self):
        if USE_NV_BINDING:
            return None
        set_proto = None.CFUNCTYPE(None, c_void_p)
        set_cuIpcOpenMemHandle = set_proto(_extras.set_cuIpcOpenMemHandle)
        set_cuIpcOpenMemHandle(self._find_api('cuIpcOpenMemHandle'))
        call_proto = ctypes.CFUNCTYPE(c_int, ctypes.POINTER(drvapi.cu_device_ptr), ctypes.POINTER(drvapi.cu_ipc_mem_handle), ctypes.c_uint)
        call_cuIpcOpenMemHandle = call_proto(_extras.call_cuIpcOpenMemHandle)
        call_cuIpcOpenMemHandle.__name__ = 'call_cuIpcOpenMemHandle'
        safe_call = self._ctypes_wrap_fn('call_cuIpcOpenMemHandle', call_cuIpcOpenMemHandle)
        self.cuIpcOpenMemHandle = safe_call

    is_available = (lambda self: self.ensure_initialized()self.initialization_error is None)()
    
    def __getattr__(self, fname):
        self.ensure_initialized()
    # WARNING: Decompyle incomplete

    
    def _ctypes_wrap_fn(self, fname, libfn = (None,)):
        pass
    # WARNING: Decompyle incomplete

    
    def _cuda_python_wrap_fn(self, fname):
        pass
    # WARNING: Decompyle incomplete

    
    def _find_api(self, fname):
        pass
    # WARNING: Decompyle incomplete

    
    def _detect_fork(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _check_ctypes_error(self, fname, retcode):
        if retcode != enums.CUDA_SUCCESS:
            errname = ERROR_MAP.get(retcode, 'UNKNOWN_CUDA_ERROR')
            msg = f'''Call to {fname!s} results in {errname!s}'''
            _logger.error(msg)
            if retcode == enums.CUDA_ERROR_NOT_INITIALIZED:
                self._detect_fork()
            raise CudaAPIError(retcode, msg)

    
    def _check_cuda_python_error(self, fname, returned):
        retcode = returned[0]
        retval = returned[1:]
        if len(retval) == 1:
            retval = retval[0]
        if retcode != binding.CUresult.CUDA_SUCCESS:
            msg = f'''Call to {fname!s} results in {retcode.name!s}'''
            _logger.error(msg)
            if retcode == binding.CUresult.CUDA_ERROR_NOT_INITIALIZED:
                self._detect_fork()
            raise CudaAPIError(retcode, msg)
        return retval

    
    def get_device(self, devnum = (0,)):
        dev = self.devices.get(devnum)
    # WARNING: Decompyle incomplete

    
    def get_device_count(self):
        if USE_NV_BINDING:
            return self.cuDeviceGetCount()
        count = None()
        self.cuDeviceGetCount(byref(count))
        return count.value

    
    def list_devices(self):
        '''Returns a list of active devices
        '''
        return list(self.devices.values())

    
    def reset(self):
        '''Reset all devices
        '''
        for dev in self.devices.values():
            dev.reset()
            return None

    
    def pop_active_context(self):
        '''Pop the active CUDA context and return the handle.
        If no CUDA context is active, return None.
        '''
        ac = self.get_active_context()
    # WARNING: Decompyle incomplete

    
    def get_active_context(self):
        '''Returns an instance of ``_ActiveContext``.
        '''
        return _ActiveContext()

    
    def get_version(self):
        '''
        Returns the CUDA Runtime version as a tuple (major, minor).
        '''
        if USE_NV_BINDING:
            version = driver.cuDriverGetVersion()
        else:
            dv = ctypes.c_int(0)
            driver.cuDriverGetVersion(ctypes.byref(dv))
            version = dv.value
        major = version // 1000
        minor = (version - major * 1000) // 10
        return (major, minor)



class _ActiveContext(object):
    '''An contextmanager object to cache active context to reduce dependency
    on querying the CUDA driver API.

    Once entering the context, it is assumed that the active CUDA context is
    not changed until the context is exited.
    '''
    _tls_cache = threading.local()
    
    def __enter__(self):
        is_top = False
        if hasattr(self._tls_cache, 'ctx_devnum'):
            (hctx, devnum) = self._tls_cache.ctx_devnum
        elif USE_NV_BINDING:
            hctx = driver.cuCtxGetCurrent()
            if int(hctx) == 0:
                hctx = None
            else:
                hctx = drvapi.cu_context(0)
                driver.cuCtxGetCurrent(byref(hctx))
                hctx = hctx if hctx.value else None
    # WARNING: Decompyle incomplete

    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._is_top:
            delattr(self._tls_cache, 'ctx_devnum')
            return None

    
    def __bool__(self):
        """Returns True is there's a valid and active CUDA context.
        """
        return self.context_handle is not None

    __nonzero__ = __bool__

driver = Driver()

def _build_reverse_device_attrs():
    prefix = 'CU_DEVICE_ATTRIBUTE_'
    map = utils.UniqueDict()
    for name in dir(enums):
        if name.startswith(prefix):
            map[name[len(prefix):]] = getattr(enums, name)
        return map

DEVICE_ATTRIBUTES = _build_reverse_device_attrs()

class Device(object):
    '''
    The device object owns the CUDA contexts.  This is owned by the driver
    object.  User should not construct devices directly.
    '''
    from_identity = (lambda self, identity: for devid in range(driver.get_device_count()):
d = driver.get_device(devid)if d.get_device_identity() == identity:
None, draise RuntimeError(errmsg))()
    
    def __init__(self, devnum):
        if USE_NV_BINDING:
            result = driver.cuDeviceGet(devnum)
            self.id = result
            got_devnum = int(result)
        else:
            result = c_int()
            driver.cuDeviceGet(byref(result), devnum)
            got_devnum = result.value
            self.id = got_devnum
        msg = f'''Driver returned device {got_devnum} instead of {devnum}'''
        if devnum != got_devnum:
            raise RuntimeError(msg)
        self.attributes = { }
        self.compute_capability = (self.COMPUTE_CAPABILITY_MAJOR, self.COMPUTE_CAPABILITY_MINOR)
        bufsz = 128
        if USE_NV_BINDING:
            buf = driver.cuDeviceGetName(bufsz, self.id)
            name = buf.decode('utf-8').rstrip('\x00')
        else:
            buf = c_char * bufsz()
            driver.cuDeviceGetName(buf, bufsz, self.id)
            name = buf.value
        self.name = name
        if USE_NV_BINDING:
            uuid = driver.cuDeviceGetUuid(self.id)
            uuid_vals = tuple(uuid.bytes)
        else:
            uuid = cu_uuid()
            driver.cuDeviceGetUuid(byref(uuid), self.id)
            uuid_vals = tuple(bytes(uuid))
        b = '%02x'
        b2 = b * 2
        b4 = b * 4
        b6 = b * 6
        fmt = f'''GPU-{b4}-{b2}-{b2}-{b2}-{b6}'''
        self.uuid = fmt % uuid_vals
        self.primary_context = None

    
    def get_device_identity(self):
        return {
            'pci_domain_id': self.PCI_DOMAIN_ID,
            'pci_bus_id': self.PCI_BUS_ID,
            'pci_device_id': self.PCI_DEVICE_ID }

    
    def __repr__(self):
        return "<CUDA device %d '%s'>" % (self.id, self.name)

    
    def __getattr__(self, attr):
        '''Read attributes lazily
        '''
        if USE_NV_BINDING:
            code = getattr(binding.CUdevice_attribute, f'''CU_DEVICE_ATTRIBUTE_{attr}''')
            value = driver.cuDeviceGetAttribute(code, self.id)
        else:
            
            try:
                code = DEVICE_ATTRIBUTES[attr]
            except KeyError:
                raise AttributeError(attr)

            result = c_int()
            driver.cuDeviceGetAttribute(byref(result), code, self.id)
            value = result.value
        setattr(self, attr, value)
        return value

    
    def __hash__(self):
        return hash(self.id)

    
    def __eq__(self, other):
        if isinstance(other, Device):
            return self.id == other.id

    
    def __ne__(self, other):
        return not (self == other)

    
    def get_primary_context(self):
        '''
        Returns the primary context for the device.
        Note: it is not pushed to the CPU thread.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def release_primary_context(self):
        '''
        Release reference to primary context if it has been retained.
        '''
        if self.primary_context:
            driver.cuDevicePrimaryCtxRelease(self.id)
            self.primary_context = None
            return None

    
    def reset(self):
        pass
    # WARNING: Decompyle incomplete

    supports_float16 = (lambda self: self.compute_capability >= (5, 3))()


def met_requirement_for_device(device):
    if device.compute_capability < MIN_REQUIRED_CC:
        raise CudaSupportError(f'''{device!s} has compute capability < {MIN_REQUIRED_CC!s}''')


def BaseCUDAMemoryManager():
    '''BaseCUDAMemoryManager'''
    __doc__ = 'Abstract base class for External Memory Management (EMM) Plugins.'
    
    def __init__(self, *args, **kwargs):
        if 'context' not in kwargs:
            raise RuntimeError('Memory manager requires a context')
        self.context = kwargs.pop('context')

    memalloc = (lambda self, size: pass)()
    memhostalloc = (lambda self, size, mapped, portable, wc: pass)()
    mempin = (lambda self, owner, pointer, size, mapped: pass)()
    initialize = (lambda self: pass)()
    get_ipc_handle = (lambda self, memory: pass)()
    get_memory_info = (lambda self: pass)()
    reset = (lambda self: pass)()
    defer_cleanup = (lambda self: pass)()
    interface_version = (lambda self: pass)()()

BaseCUDAMemoryManager = <NODE:27>(BaseCUDAMemoryManager, 'BaseCUDAMemoryManager', object, metaclass = ABCMeta)

class HostOnlyCUDAMemoryManager(BaseCUDAMemoryManager):
    pass
# WARNING: Decompyle incomplete


class GetIpcHandleMixin:
    '''A class that provides a default implementation of ``get_ipc_handle()``.
    '''
    
    def get_ipc_handle(self, memory):
        '''Open an IPC memory handle by using ``cuMemGetAddressRange`` to
        determine the base pointer of the allocation. An IPC handle of type
        ``cu_ipc_mem_handle`` is constructed and initialized with
        ``cuIpcGetMemHandle``. A :class:`numba.cuda.IpcHandle` is returned,
        populated with the underlying ``ipc_mem_handle``.
        '''
        (base, end) = device_extents(memory)
        if USE_NV_BINDING:
            ipchandle = driver.cuIpcGetMemHandle(base)
            offset = int(memory.handle) - int(base)
        else:
            ipchandle = drvapi.cu_ipc_mem_handle()
            driver.cuIpcGetMemHandle(byref(ipchandle), base)
            offset = memory.handle.value - base
        source_info = self.context.device.get_device_identity()
        return IpcHandle(memory, ipchandle, memory.size, source_info, offset = offset)



class NumbaCUDAMemoryManager(HostOnlyCUDAMemoryManager, GetIpcHandleMixin):
    '''Internal on-device memory management for Numba. This is implemented using
    the EMM Plugin interface, but is not part of the public API.'''
    
    def initialize(self):
        if self.deallocations.memory_capacity == _SizeNotSet:
            self.deallocations.memory_capacity = self.get_memory_info().total
            return None

    
    def memalloc(self, size):
        pass
    # WARNING: Decompyle incomplete

    
    def get_memory_info(self):
        if USE_NV_BINDING:
            (free, total) = driver.cuMemGetInfo()
        else:
            free = c_size_t()
            total = c_size_t()
            driver.cuMemGetInfo(byref(free), byref(total))
            free = free.value
            total = total.value
        return MemoryInfo(free = free, total = total)

    interface_version = (lambda self: _SUPPORTED_EMM_INTERFACE_VERSION)()

_SUPPORTED_EMM_INTERFACE_VERSION = 1
_memory_manager = None

def _ensure_memory_manager():
    global _memory_manager
    if _memory_manager:
        return None
    if None.CUDA_MEMORY_MANAGER == 'default':
        _memory_manager = NumbaCUDAMemoryManager
        return None
    
    try:
        mgr_module = importlib.import_module(config.CUDA_MEMORY_MANAGER)
        set_memory_manager(mgr_module._numba_memory_manager)
        return None
    except Exception:
        raise RuntimeError('Failed to use memory manager from %s' % config.CUDA_MEMORY_MANAGER)



def set_memory_manager(mm_plugin):
    '''Configure Numba to use an External Memory Management (EMM) Plugin. If
    the EMM Plugin version does not match one supported by this version of
    Numba, a RuntimeError will be raised.

    :param mm_plugin: The class implementing the EMM Plugin.
    :type mm_plugin: BaseCUDAMemoryManager
    :return: None
    '''
    global _memory_manager
    dummy = mm_plugin(context = None)
    iv = dummy.interface_version
    if iv != _SUPPORTED_EMM_INTERFACE_VERSION:
        err = 'EMM Plugin interface has version %d - version %d required' % (iv, _SUPPORTED_EMM_INTERFACE_VERSION)
        raise RuntimeError(err)
    _memory_manager = mm_plugin


class _SizeNotSet(int):
    pass
# WARNING: Decompyle incomplete

_SizeNotSet = _SizeNotSet()

class _PendingDeallocs(object):
    '''
    Pending deallocations of a context (or device since we are using the primary
    context). The capacity defaults to being unset (_SizeNotSet) but can be
    modified later once the driver is initialized and the total memory capacity
    known.
    '''
    
    def __init__(self, capacity = (_SizeNotSet,)):
        self._cons = deque()
        self._disable_count = 0
        self._size = 0
        self.memory_capacity = capacity

    _max_pending_bytes = (lambda self: int(self.memory_capacity * config.CUDA_DEALLOCS_RATIO))()
    
    def add_item(self, dtor, handle, size = (_SizeNotSet,)):
        '''
        Add a pending deallocation.

        The *dtor* arg is the destructor function that takes an argument,
        *handle*.  It is used as ``dtor(handle)``.  The *size* arg is the
        byte size of the resource added.  It is an optional argument.  Some
        resources (e.g. CUModule) has an unknown memory footprint on the device.
        '''
        _logger.info('add pending dealloc: %s %s bytes', dtor.__name__, size)
        self._cons.append((dtor, handle, size))
        if len(self._cons) > config.CUDA_DEALLOCS_COUNT or self._size > self._max_pending_bytes:
            self.clear()
            return None
        return self, self._size += int(size), ._size

    
    def clear(self):
        '''
        Flush any pending deallocations unless it is disabled.
        Do nothing if disabled.
        '''
        pass
    # WARNING: Decompyle incomplete

    disable = (lambda self: pass# WARNING: Decompyle incomplete
)()
    is_disabled = (lambda self: self._disable_count > 0)()
    
    def __len__(self):
        '''
        Returns number of pending deallocations.
        '''
        return len(self._cons)


MemoryInfo = namedtuple('MemoryInfo', 'free,total')

class Context(object):
    '''
    This object wraps a CUDA Context resource.

    Contexts should not be constructed directly by user code.
    '''
    
    def __init__(self, device, handle):
        self.device = device
        self.handle = handle
        self.allocations = utils.UniqueDict()
        self.deallocations = _PendingDeallocs()
        _ensure_memory_manager()
        self.memory_manager = _memory_manager(context = self)
        self.modules = utils.UniqueDict()
        self.extras = { }

    
    def reset(self):
        '''
        Clean up all owned resources in this context.
        '''
        _logger.info('reset context of device %s', self.device.id)
        self.memory_manager.reset()
        self.modules.clear()
        self.deallocations.clear()

    
    def get_memory_info(self):
        '''Returns (free, total) memory in bytes in the context.
        '''
        return self.memory_manager.get_memory_info()

    
    def get_active_blocks_per_multiprocessor(self, func, blocksize, memsize, flags = (None,)):
        '''Return occupancy of a function.
        :param func: kernel for which occupancy is calculated
        :param blocksize: block size the kernel is intended to be launched with
        :param memsize: per-block dynamic shared memory usage intended, in bytes
        '''
        args = (func, blocksize, memsize, flags)
    # WARNING: Decompyle incomplete

    
    def _cuda_python_active_blocks_per_multiprocessor(self, func, blocksize, memsize, flags):
        ps = [
            func.handle,
            blocksize,
            memsize]
    # WARNING: Decompyle incomplete

    
    def _ctypes_active_blocks_per_multiprocessor(self, func, blocksize, memsize, flags):
        retval = c_int()
        args = (byref(retval), func.handle, blocksize, memsize)
    # WARNING: Decompyle incomplete

    
    def get_max_potential_block_size(self, func, b2d_func, memsize, blocksizelimit, flags = (None,)):
        """Suggest a launch configuration with reasonable occupancy.
        :param func: kernel for which occupancy is calculated
        :param b2d_func: function that calculates how much per-block dynamic
                         shared memory 'func' uses based on the block size.
                         Can also be the address of a C function.
                         Use `0` to pass `NULL` to the underlying CUDA API.
        :param memsize: per-block dynamic shared memory usage intended, in bytes
        :param blocksizelimit: maximum block size the kernel is designed to
                               handle
        """
        args = (func, b2d_func, memsize, blocksizelimit, flags)
    # WARNING: Decompyle incomplete

    
    def _ctypes_max_potential_block_size(self, func, b2d_func, memsize, blocksizelimit, flags):
        gridsize = c_int()
        blocksize = c_int()
        b2d_cb = cu_occupancy_b2d_size(b2d_func)
        args = [
            byref(gridsize),
            byref(blocksize),
            func.handle,
            b2d_cb,
            memsize,
            blocksizelimit]
    # WARNING: Decompyle incomplete

    
    def _cuda_python_max_potential_block_size(self, func, b2d_func, memsize, blocksizelimit, flags):
        b2d_cb = ctypes.CFUNCTYPE(c_size_t, c_int)(b2d_func)
        ptr = int.from_bytes(b2d_cb, byteorder = 'little')
        driver_b2d_cb = binding.CUoccupancyB2DSize(ptr)
        args = [
            func.handle,
            driver_b2d_cb,
            memsize,
            blocksizelimit]
    # WARNING: Decompyle incomplete

    
    def prepare_for_use(self):
        """Initialize the context for use.
        It's safe to be called multiple times.
        """
        self.memory_manager.initialize()

    
    def push(self):
        '''
        Pushes this context on the current CPU Thread.
        '''
        driver.cuCtxPushCurrent(self.handle)
        self.prepare_for_use()

    
    def pop(self):
        '''
        Pops this context off the current CPU thread. Note that this context
        must be at the top of the context stack, otherwise an error will occur.
        '''
        popped = driver.pop_active_context()
    # WARNING: Decompyle incomplete

    
    def memalloc(self, bytesize):
        return self.memory_manager.memalloc(bytesize)

    
    def memallocmanaged(self, bytesize, attach_global = (True,)):
        return self.memory_manager.memallocmanaged(bytesize, attach_global)

    
    def memhostalloc(self, bytesize, mapped, portable, wc = (False, False, False)):
        return self.memory_manager.memhostalloc(bytesize, mapped, portable, wc)

    
    def mempin(self, owner, pointer, size, mapped = (False,)):
        if not mapped and self.device.CAN_MAP_HOST_MEMORY:
            raise CudaDriverError('%s cannot map host memory' % self.device)
        return self.memory_manager.mempin(owner, pointer, size, mapped)

    
    def get_ipc_handle(self, memory):
        '''
        Returns an *IpcHandle* from a GPU allocation.
        '''
        if not SUPPORTS_IPC:
            raise OSError('OS does not support CUDA IPC')
        return self.memory_manager.get_ipc_handle(memory)

    
    def open_ipc_handle(self, handle, size):
        flags = 1
        if USE_NV_BINDING:
            dptr = driver.cuIpcOpenMemHandle(handle, flags)
        else:
            dptr = drvapi.cu_device_ptr()
            driver.cuIpcOpenMemHandle(byref(dptr), handle, flags)
        return MemoryPointer(context = weakref.proxy(self), pointer = dptr, size = size)

    
    def enable_peer_access(self, peer_context, flags = (0,)):
        '''Enable peer access between the current context and the peer context
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def can_access_peer(self, peer_device):
        '''Returns a bool indicating whether the peer access between the
        current and peer device is possible.
        '''
        if USE_NV_BINDING:
            peer_device = binding.CUdevice(peer_device)
            can_access_peer = driver.cuDeviceCanAccessPeer(self.device.id, peer_device)
        else:
            can_access_peer = c_int()
            driver.cuDeviceCanAccessPeer(byref(can_access_peer), self.device.id, peer_device)
        return bool(can_access_peer)

    
    def create_module_ptx(self, ptx):
        if isinstance(ptx, str):
            ptx = ptx.encode('utf8')
        if USE_NV_BINDING:
            image = ptx
        else:
            image = c_char_p(ptx)
        return self.create_module_image(image)

    
    def create_module_image(self, image):
        module = load_module_image(self, image)
        if USE_NV_BINDING:
            key = module.handle
        else:
            key = module.handle.value
        self.modules[key] = module
        return weakref.proxy(module)

    
    def unload_module(self, module):
        if USE_NV_BINDING:
            key = module.handle
        else:
            key = module.handle.value
        del self.modules[key]

    
    def get_default_stream(self):
        if USE_NV_BINDING:
            handle = binding.CUstream(CU_STREAM_DEFAULT)
        else:
            handle = drvapi.cu_stream(drvapi.CU_STREAM_DEFAULT)
        return Stream(weakref.proxy(self), handle, None)

    
    def get_legacy_default_stream(self):
        if USE_NV_BINDING:
            handle = binding.CUstream(binding.CU_STREAM_LEGACY)
        else:
            handle = drvapi.cu_stream(drvapi.CU_STREAM_LEGACY)
        return Stream(weakref.proxy(self), handle, None)

    
    def get_per_thread_default_stream(self):
        if USE_NV_BINDING:
            handle = binding.CUstream(binding.CU_STREAM_PER_THREAD)
        else:
            handle = drvapi.cu_stream(drvapi.CU_STREAM_PER_THREAD)
        return Stream(weakref.proxy(self), handle, None)

    
    def create_stream(self):
        if USE_NV_BINDING:
            flags = binding.CUstream_flags.CU_STREAM_DEFAULT.value
            handle = driver.cuStreamCreate(flags)
        else:
            handle = drvapi.cu_stream()
            driver.cuStreamCreate(byref(handle), 0)
        return Stream(weakref.proxy(self), handle, _stream_finalizer(self.deallocations, handle))

    
    def create_external_stream(self, ptr):
        if not isinstance(ptr, int):
            raise TypeError('ptr for external stream must be an int')
        if USE_NV_BINDING:
            handle = binding.CUstream(ptr)
        else:
            handle = drvapi.cu_stream(ptr)
        return Stream(weakref.proxy(self), handle, None, external = True)

    
    def create_event(self, timing = (True,)):
        flags = 0
        if not timing:
            flags |= enums.CU_EVENT_DISABLE_TIMING
        if USE_NV_BINDING:
            handle = driver.cuEventCreate(flags)
        else:
            handle = drvapi.cu_event()
            driver.cuEventCreate(byref(handle), flags)
        return Event(weakref.proxy(self), handle, finalizer = _event_finalizer(self.deallocations, handle))

    
    def synchronize(self):
        driver.cuCtxSynchronize()

    defer_cleanup = (lambda self: pass# WARNING: Decompyle incomplete
)()
    
    def __repr__(self):
        return '<CUDA context %s of device %d>' % (self.handle, self.device.id)

    
    def __eq__(self, other):
        if isinstance(other, Context):
            return self.handle == other.handle

    
    def __ne__(self, other):
        return not self.__eq__(other)



def load_module_image(context, image):
    '''
    image must be a pointer
    '''
    if USE_NV_BINDING:
        return load_module_image_cuda_python(context, image)
    return None(context, image)


def load_module_image_ctypes(context, image):
    logsz = config.CUDA_LOG_SIZE
    jitinfo = c_char * logsz()
    jiterrors = c_char * logsz()
    options = {
        enums.CU_JIT_LOG_VERBOSE: c_void_p(config.CUDA_VERBOSE_JIT_LOG),
        enums.CU_JIT_ERROR_LOG_BUFFER_SIZE_BYTES: c_void_p(logsz),
        enums.CU_JIT_ERROR_LOG_BUFFER: addressof(jiterrors),
        enums.CU_JIT_INFO_LOG_BUFFER_SIZE_BYTES: c_void_p(logsz),
        enums.CU_JIT_INFO_LOG_BUFFER: addressof(jitinfo) }
# WARNING: Decompyle incomplete


def load_module_image_cuda_python(context, image):
    '''
    image must be a pointer
    '''
    logsz = config.CUDA_LOG_SIZE
    jitinfo = bytearray(logsz)
    jiterrors = bytearray(logsz)
    jit_option = binding.CUjit_option
    options = {
        jit_option.CU_JIT_LOG_VERBOSE: config.CUDA_VERBOSE_JIT_LOG,
        jit_option.CU_JIT_ERROR_LOG_BUFFER_SIZE_BYTES: logsz,
        jit_option.CU_JIT_ERROR_LOG_BUFFER: jiterrors,
        jit_option.CU_JIT_INFO_LOG_BUFFER_SIZE_BYTES: logsz,
        jit_option.CU_JIT_INFO_LOG_BUFFER: jitinfo }
    option_keys = options.keys()()
    option_vals = options.values()()
    
    try:
        handle = driver.cuModuleLoadDataEx(image, len(options), option_keys, option_vals)
    except CudaAPIError:
        
        def e(.0):
            return [ k for k in .0 ]

        err_string = jiterrors.decode('utf-8')
        msg = 'cuModuleLoadDataEx error:\n%s' % err_string
        raise CudaAPIError(e.code, msg)
        e = None
        del e

    info_log = jitinfo.decode('utf-8')
    return CudaPythonModule(weakref.proxy(context), handle, info_log, _module_finalizer(context, handle))


def _alloc_finalizer(memory_manager, ptr, alloc_key, size):
    pass
# WARNING: Decompyle incomplete


def _hostalloc_finalizer(memory_manager, ptr, alloc_key, size, mapped):
    '''
    Finalize page-locked host memory allocated by `context.memhostalloc`.

    This memory is managed by CUDA, and finalization entails deallocation. The
    issues noted in `_pin_finalizer` are not relevant in this case, and the
    finalization is placed in the `context.deallocations` queue along with
    finalization of device objects.

    '''
    pass
# WARNING: Decompyle incomplete


def _pin_finalizer(memory_manager, ptr, alloc_key, mapped):
    '''
    Finalize temporary page-locking of host memory by `context.mempin`.

    This applies to memory not otherwise managed by CUDA. Page-locking can
    be requested multiple times on the same memory, and must therefore be
    lifted as soon as finalization is requested, otherwise subsequent calls to
    `mempin` may fail with `CUDA_ERROR_HOST_MEMORY_ALREADY_REGISTERED`, leading
    to unexpected behavior for the context managers `cuda.{pinned,mapped}`.
    This function therefore carries out finalization immediately, bypassing the
    `context.deallocations` queue.

    '''
    pass
# WARNING: Decompyle incomplete


def _event_finalizer(deallocs, handle):
    pass
# WARNING: Decompyle incomplete


def _stream_finalizer(deallocs, handle):
    pass
# WARNING: Decompyle incomplete


def _module_finalizer(context, handle):
    pass
# WARNING: Decompyle incomplete


class _CudaIpcImpl(object):
    '''Implementation of GPU IPC using CUDA driver API.
    This requires the devices to be peer accessible.
    '''
    
    def __init__(self, parent):
        self.base = parent.base
        self.handle = parent.handle
        self.size = parent.size
        self.offset = parent.offset
        self._opened_mem = None

    
    def open(self, context):
        '''
        Import the IPC memory and returns a raw CUDA memory pointer object
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def close(self):
        pass
    # WARNING: Decompyle incomplete



class _StagedIpcImpl(object):
    '''Implementation of GPU IPC using custom staging logic to workaround
    CUDA IPC limitation on peer accessibility between devices.
    '''
    
    def __init__(self, parent, source_info):
        self.parent = parent
        self.base = parent.base
        self.handle = parent.handle
        self.size = parent.size
        self.source_info = source_info

    
    def open(self, context):

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: nrt.pyc (Python 3.11)

from collections import namedtuple
from weakref import finalize as _finalize
from numba.core.runtime import nrtdynmod
from llvmlite import binding as ll
from numba.core.compiler_lock import global_compiler_lock
from numba.core.typing.typeof import typeof_impl
from numba.core import types, config
from numba.core.runtime import _nrt_python as _nrt
_nrt_mstats = namedtuple('nrt_mstats', [
    'alloc',
    'free',
    'mi_alloc',
    'mi_free'])

class _Runtime(object):
    
    def __init__(self):
        self._init = False

    initialize = (lambda self, ctx: if self._init:
Noneif None.NRT_STATS:
_nrt.memsys_enable_stats()for py_name in _nrt.c_helpers:
if py_name.startswith('_'):
c_name = py_nameelse:
c_name = 'NRT_' + py_namec_address = _nrt.c_helpers[py_name]ll.add_symbol(c_name, c_address)self._library = nrtdynmod.compile_nrt_functions(ctx)self._init = TrueNone)()
    
    def _init_guard(self):
        if not self._init:
            msg = 'Runtime must be initialized before use.'
            raise RuntimeError(msg)

    shutdown = (lambda : _nrt.memsys_shutdown())()
    library = (lambda self: self._init_guard()self._library)()
    
    def meminfo_new(self, data, pyobj):
        '''
        Returns a MemInfo object that tracks memory at `data` owned by `pyobj`.
        MemInfo will acquire a reference on `pyobj`.
        The release of MemInfo will release a reference on `pyobj`.
        '''
        self._init_guard()
        mi = _nrt.meminfo_new(data, pyobj)
        return MemInfo(mi)

    
    def meminfo_alloc(self, size, safe = (False,)):
        '''
        Allocate a new memory of `size` bytes and returns a MemInfo object
        that tracks the allocation.  When there is no more reference to the
        MemInfo object, the underlying memory will be deallocated.

        If `safe` flag is True, the memory is allocated using the `safe` scheme.
        This is used for debugging and testing purposes.
        See `NRT_MemInfo_alloc_safe()` in "nrt.h" for details.
        '''
        self._init_guard()
        if size < 0:
            msg = f'''Cannot allocate a negative number of bytes: {size}.'''
            raise ValueError(msg)
        if safe:
            mi = _nrt.meminfo_alloc_safe(size)
        else:
            mi = _nrt.meminfo_alloc(size)
        if mi == 0:
            msg = f'''Requested allocation of {size} bytes failed.'''
            raise MemoryError(msg)
        return MemInfo(mi)

    
    def get_allocation_stats(self):
        '''
        Returns a namedtuple of (alloc, free, mi_alloc, mi_free) for count of
        each memory operations.
        '''
        return _nrt_mstats(alloc = _nrt.memsys_get_stats_alloc(), free = _nrt.memsys_get_stats_free(), mi_alloc = _nrt.memsys_get_stats_mi_alloc(), mi_free = _nrt.memsys_get_stats_mi_free())


MemInfo = _nrt._MemInfo
typeof_meminfo = (lambda val, c: types.MemInfoPointer(types.voidptr))()
_nrt.memsys_use_cpython_allocator()
rtsys = _Runtime()
_finalize(rtsys, _Runtime.shutdown)
del _Runtime

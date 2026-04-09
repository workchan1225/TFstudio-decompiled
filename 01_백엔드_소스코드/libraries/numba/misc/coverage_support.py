# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: coverage_support.pyc (Python 3.11)

'''
Implement code coverage support.

Currently contains logic to extend ``coverage`` with lines covered by the
compiler.
'''
from typing import Optional, Sequence, Callable, no_type_check
from collections.abc import Mapping
from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from numba.core import ir, config

try:
    import coverage
    coverage_available = True
except ImportError:
    coverage_available = False

get_active_coverage = (lambda : cov = Noneif coverage_available:
cov = coverage.Coverage.current()cov)()
_the_registry: Callable[([], Optional['NotifyLocBase'])] = []

def get_registered_loc_notify():
    '''
    Returns a list of the registered NotifyLocBase instances.
    '''
    if not config.JIT_COVERAGE:
        return []
    
    def <genexpr>(.0):
        pass
    # WARNING: Decompyle incomplete

    return filter((lambda x: x is not None)(<genexpr>, _the_registry()))


class NotifyLocBase(ABC):
    '''Interface for notifying visiting of a ``numba.core.ir.Loc``.'''
    notify = (lambda self = None, loc = None: pass)()
    close = (lambda self = None: pass)()


class NotifyCompilerCoverage(NotifyLocBase):
    '''
    Use to notify ``coverage`` about compiled lines.

    The compiled lines are under the "numba_compiled" context in the coverage
    data.
    '''
    
    def __init__(self, collector):
        self._collector = collector
        tracer_kwargs = collector.core.tracer_kwargs.copy()
        tracer_kwargs.update(dict(data = collector.data, lock_data = collector.lock_data, unlock_data = collector.unlock_data, trace_arcs = collector.branch, should_trace = collector.should_trace, should_trace_cache = collector.should_trace_cache, warn = collector.warn, should_start_context = collector.should_start_context, switch_context = collector.switch_context, packed_arcs = collector.core.packed_arcs))
    # WARNING: Decompyle incomplete

    
    def notify(self = None, loc = None):
        tracer = self._tracer
        if loc.filename.endswith('.py'):
            tracer.switch_context('numba_compiled')
            tracer.trace(loc)
            tracer.switch_context(None)
            return None

    
    def close(self):
        pass


_register_coverage_notifier = (lambda : cov = get_active_coverage()# WARNING: Decompyle incomplete
)()
if coverage_available:
    NumbaTracer = <NODE:12>()
    
    def _pack_arcs(l1 = None, l2 = _the_registry.append):
        '''Pack arcs into a single integer for compatibility with .packed_arcs
        option.

        See
        https://github.com/nedbat/coveragepy/blob/e7c05fe91ee36c0c94e144bb88d25db4fc3d02fd/coverage/ctracer/tracer.c#L171
        '''
        packed = 0
        if l1 < 0:
            packed |= 0x10000000000
            l1 = -l1
        if l2 < 0:
            packed |= 0x20000000000
            l2 = -l2
        packed |= (l2 << 20) + l1
        return packed

    return None
return _the_registry.append

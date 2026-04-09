# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: target_extension.pyc (Python 3.11)

from abc import ABC, abstractmethod
from numba.core.registry import DelayedRegistry, CPUDispatcher
from numba.core.decorators import jit
from numba.core.errors import InternalTargetMismatchError, NonexistentTargetError
from threading import local as tls
_active_context = tls()
_active_context_default = 'cpu'

class _TargetRegistry(DelayedRegistry):
    pass
# WARNING: Decompyle incomplete

target_registry = _TargetRegistry()
jit_registry = DelayedRegistry()

class target_override(object):
    '''Context manager to temporarily override the current target with that
       prescribed.'''
    
    def __init__(self, name):
        self._orig_target = getattr(_active_context, 'target', _active_context_default)
        self.target = name

    
    def __enter__(self):
        _active_context.target = self.target

    
    def __exit__(self, ty, val, tb):
        _active_context.target = self._orig_target



def current_target():
    '''Returns the current target
    '''
    return getattr(_active_context, 'target', _active_context_default)


def get_local_target(context):
    '''
    Gets the local target from the call stack if available and the TLS
    override if not.
    '''
    if len(context.callstack._stack) > 0:
        target = context.callstack[0].target
    else:
        target = target_registry.get(current_target(), None)
# WARNING: Decompyle incomplete


def resolve_target_str(target_str):
    '''Resolves a target specified as a string to its Target class.'''
    return target_registry[target_str]


def resolve_dispatcher_from_str(target_str):
    '''Returns the dispatcher associated with a target string'''
    target_hw = resolve_target_str(target_str)
    return dispatcher_registry[target_hw]


def _get_local_target_checked(tyctx, hwstr, reason):
    '''Returns the local target if it is compatible with the given target
    name during a type resolution; otherwise, raises an exception.

    Parameters
    ----------
    tyctx: typing context
    hwstr: str
        target name to check against
    reason: str
        Reason for the resolution. Expects a noun.
    Returns
    -------
    target_hw : Target

    Raises
    ------
    InternalTargetMismatchError
    '''
    hw_clazz = resolve_target_str(hwstr)
    target_hw = get_local_target(tyctx)
    if not target_hw.inherits_from(hw_clazz):
        raise InternalTargetMismatchError(reason, target_hw, hw_clazz)
    return target_hw


class JitDecorator(ABC):
    __call__ = (lambda self: NotImplemented)()


class Target(ABC):
    ''' Implements a target '''
    inherits_from = (lambda cls, other: issubclass(cls, other))()


class Generic(Target):
    '''Mark the target as generic, i.e. suitable for compilation on
    any target. All must inherit from this.
    '''
    pass


class CPU(Generic):
    '''Mark the target as CPU.
    '''
    pass


class GPU(Generic):
    '''Mark the target as GPU, i.e. suitable for compilation on a GPU
    target.
    '''
    pass


class CUDA(GPU):
    '''Mark the target as CUDA.
    '''
    pass


class NPyUfunc(Target):
    '''Mark the target as a ufunc
    '''
    pass

target_registry['generic'] = Generic
target_registry['CPU'] = CPU
target_registry['cpu'] = CPU
target_registry['GPU'] = GPU
target_registry['gpu'] = GPU
target_registry['CUDA'] = CUDA
target_registry['cuda'] = CUDA
target_registry['npyufunc'] = NPyUfunc
dispatcher_registry = DelayedRegistry(key_type = Target)
cpu_target = target_registry['cpu']
dispatcher_registry[cpu_target] = CPUDispatcher
jit_registry[cpu_target] = jit

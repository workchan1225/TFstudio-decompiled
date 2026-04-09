# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: lowlevel.pyc (Python 3.11)

from __future__ import annotations
__all__ = ('EventLoopToken', 'RunvarToken', 'RunVar', 'checkpoint', 'checkpoint_if_cancelled', 'cancel_shielded_checkpoint', 'current_token')
import enum
from dataclasses import dataclass
from types import TracebackType
from typing import Any, Generic, Literal, TypeVar, final, overload
from weakref import WeakKeyDictionary
from _core._eventloop import get_async_backend
from abc import AsyncBackend
T = TypeVar('T')
D = TypeVar('D')

async def checkpoint():
    '''
    Check for cancellation and allow the scheduler to switch to another task.

    Equivalent to (but more efficient than)::

        await checkpoint_if_cancelled()
        await cancel_shielded_checkpoint()


    .. versionadded:: 3.0

    '''
    pass
# WARNING: Decompyle incomplete


async def checkpoint_if_cancelled():
    '''
    Enter a checkpoint if the enclosing cancel scope has been cancelled.

    This does not allow the scheduler to switch to a different task.

    .. versionadded:: 3.0

    '''
    pass
# WARNING: Decompyle incomplete


async def cancel_shielded_checkpoint():
    '''
    Allow the scheduler to switch to another task but without checking for cancellation.

    Equivalent to (but potentially more efficient than)::

        with CancelScope(shield=True):
            await checkpoint()


    .. versionadded:: 3.0

    '''
    pass
# WARNING: Decompyle incomplete

EventLoopToken = <NODE:12>()()

def current_token():
    '''
    Return a token object that can be used to call code in the current event loop from
    another thread.

    .. versionadded:: 4.11.0

    '''
    backend_class = get_async_backend()
    raw_token = backend_class.current_token()
    return EventLoopToken(backend_class, raw_token)

_run_vars: 'WeakKeyDictionary[object, dict[RunVar[Any], Any]]' = WeakKeyDictionary()

class _NoValueSet(enum.Enum):
    NO_VALUE_SET = enum.auto()


def RunvarToken():
    '''RunvarToken'''
    __slots__ = ('_var', '_value', '_redeemed')
    
    def __init__(self = None, var = None, value = None):
        self._var = var
        self._value = value
        self._redeemed = False

    
    def __enter__(self = None):
        return self

    
    def __exit__(self = None, exc_type = None, exc_val = None, exc_tb = ('exc_type', 'type[BaseException] | None', 'exc_val', 'BaseException | None', 'exc_tb', 'TracebackType | None', 'return', 'None')):
        self._var.reset(self)


RunvarToken = <NODE:27>(RunvarToken, 'RunvarToken', Generic[T])

def RunVar():
    '''RunVar'''
    __doc__ = '\n    Like a :class:`~contextvars.ContextVar`, except scoped to the running event loop.\n\n    Can be used as a context manager, Just like :class:`~contextvars.ContextVar`, that\n    will reset the variable to its previous value when the context block is exited.\n    '
    __slots__ = ('_name', '_default')
    NO_VALUE_SET: 'Literal[_NoValueSet.NO_VALUE_SET]' = _NoValueSet.NO_VALUE_SET
    
    def __init__(self = None, name = None, default = None):
        self._name = name
        self._default = default

    _current_vars = (lambda self = None: native_token = current_token().native_tokentry:
_run_vars[native_token]except KeyError:
run_vars = { }_run_vars[native_token] = { })()
    get = (lambda self = None, default = None: pass)()
    get = (lambda self = None: pass)()
    
    def get(self = None, default = None):
        
        try:
            return self._current_vars[self]
        except KeyError:
            if default is not RunVar.NO_VALUE_SET:
                return 
            if None._default is not RunVar.NO_VALUE_SET:
                return 

        raise LookupError(f'''Run variable "{self._name}" has no value and no default set''')

    
    def set(self = None, value = None):
        current_vars = self._current_vars
        token = RunvarToken(self, current_vars.get(self, RunVar.NO_VALUE_SET))
        current_vars[self] = value
        return token

    
    def reset(self = None, token = None):
        if token._var is not self:
            raise ValueError('This token does not belong to this RunVar')
        if token._redeemed:
            raise ValueError('This token has already been used')
        if token._value is _NoValueSet.NO_VALUE_SET:
            
            try:
                del self._current_vars[self]
            except KeyError:
                pass
            except:
                self._current_vars[self] = token._value

            token._redeemed = True
            return None

    
    def __repr__(self = None):
        return f'''<RunVar name={self._name!r}>'''


RunVar = <NODE:27>(RunVar, 'RunVar', Generic[T])

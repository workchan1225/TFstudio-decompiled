# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _impl.pyc (Python 3.11)

from __future__ import annotations
import abc
from typing import TYPE_CHECKING, AsyncGenerator, Awaitable, Callable, Generator, Generic, NoReturn, TypeVar, Union, overload
import attr
from _util import AlreadyUsedError, remove_tb_frames
if TYPE_CHECKING:
    from typing_extensions import ParamSpec, final
    ArgsT = ParamSpec('ArgsT')
else:
    
    def final(func):
        return func

__all__ = [
    'Error',
    'Outcome',
    'Maybe',
    'Value',
    'acapture',
    'capture']
ValueT = TypeVar('ValueT', covariant = True)
ResultT = TypeVar('ResultT')
capture = (lambda sync_fn = None: pass)()
capture = (lambda sync_fn = None: pass)()

def capture(sync_fn = None, *args, **kwargs):
    '''Run ``sync_fn(*args, **kwargs)`` and capture the result.

    Returns:
      Either a :class:`Value` or :class:`Error` as appropriate.

    '''
    pass
# WARNING: Decompyle incomplete

acapture = (lambda async_fn = None: pass# WARNING: Decompyle incomplete
)()
acapture = (lambda async_fn = None: pass# WARNING: Decompyle incomplete
)()

async def acapture(async_fn = None, *args, **kwargs):
    '''Run ``await async_fn(*args, **kwargs)`` and capture the result.

    Returns:
      Either a :class:`Value` or :class:`Error` as appropriate.

    '''
    pass
# WARNING: Decompyle incomplete


def Outcome():
    '''Outcome'''
    __doc__ = 'An abstract class representing the result of a Python computation.\n\n    This class has two concrete subclasses: :class:`Value` representing a\n    value, and :class:`Error` representing an exception.\n\n    In addition to the methods described below, comparison operators on\n    :class:`Value` and :class:`Error` objects (``==``, ``<``, etc.) check that\n    the other object is also a :class:`Value` or :class:`Error` object\n    respectively, and then compare the contained objects.\n\n    :class:`Outcome` objects are hashable if the contained objects are\n    hashable.\n\n    '
    _unwrapped: 'bool' = attr.ib(default = False, eq = False, init = False)
    
    def _set_unwrapped(self = None):
        if self._unwrapped:
            raise AlreadyUsedError
        object.__setattr__(self, '_unwrapped', True)

    unwrap = (lambda self = None: pass)()
    send = (lambda self = None, gen = None: pass)()
    asend = (lambda self = None, agen = None: pass# WARNING: Decompyle incomplete
)()

Outcome = <NODE:27>(Outcome, 'Outcome', abc.ABC, Generic[ValueT])()

def Value():
    '''Value'''
    __doc__ = 'Concrete :class:`Outcome` subclass representing a regular value.\n\n    '
    value: 'ValueT' = attr.ib()
    
    def __repr__(self = None):
        return f'''Value({self.value!r})'''

    
    def unwrap(self = None):
        self._set_unwrapped()
        return self.value

    
    def send(self = None, gen = None):
        self._set_unwrapped()
        return gen.send(self.value)

    
    async def asend(self = None, agen = None):
        pass
    # WARNING: Decompyle incomplete


Value = <NODE:27>(Value, 'Value', Outcome[ValueT], Generic[ValueT])()()

def Error():
    '''Error'''
    __doc__ = 'Concrete :class:`Outcome` subclass representing a raised exception.\n\n    '
    error: 'BaseException' = attr.ib(validator = attr.validators.instance_of(BaseException))
    
    def __repr__(self = None):
        return f'''Error({self.error!r})'''

    
    def unwrap(self = None):
        self._set_unwrapped()
        captured_error = self.error
        
        try:
            raise captured_error
        except:
            del captured_error
            del self


    
    def send(self = None, gen = None):
        self._set_unwrapped()
        return gen.throw(self.error)

    
    async def asend(self = None, agen = None):
        pass
    # WARNING: Decompyle incomplete


Error = <NODE:27>(Error, 'Error', Outcome[NoReturn])()()
Maybe = Union[(Value[ValueT], Error)]

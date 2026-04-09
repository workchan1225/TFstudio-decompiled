# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: async_timeout.pyc (Python 3.11)

import asyncio
import enum
import sys
import warnings
from types import TracebackType
from typing import Optional, Type
if sys.version_info >= (3, 11):
    from typing import final
else:
    
    def final(f):
        '''This decorator can be used to indicate to type checkers that
        the decorated method cannot be overridden, and decorated class
        cannot be subclassed. For example:

            class Base:
                @final
                def done(self) -> None:
                    ...
            class Sub(Base):
                def done(self) -> None:  # Error reported by type checker
                    ...
            @final
            class Leaf:
                ...
            class Other(Leaf):  # Error reported by type checker
                ...

        There is no runtime checking of these properties. The decorator
        sets the ``__final__`` attribute to ``True`` on the decorated object
        to allow runtime introspection.
        '''
        
        try:
            f.__final__ = True
        except (AttributeError, TypeError):
            pass

        return f

if sys.version_info >= (3, 11):
    
    def _uncancel_task(task = None):
        task.uncancel()

else:
    
    def _uncancel_task(task = None):
        pass

__version__ = '4.0.3'
__all__ = ('timeout', 'timeout_at', 'Timeout')

def timeout(delay = None):
    """timeout context manager.

    Useful in cases when you want to apply timeout logic around block
    of code or in cases when asyncio.wait_for is not suitable. For example:

    >>> async with timeout(0.001):
    ...     async with aiohttp.get('https://github.com') as r:
    ...         await r.text()


    delay - value in seconds or None to disable timeout logic
    """
    loop = asyncio.get_running_loop()
# WARNING: Decompyle incomplete


def timeout_at(deadline = None):
    """Schedule the timeout at absolute time.

    deadline argument points on the time in the same clock system
    as loop.time().

    Please note: it is not POSIX time but a time with
    undefined starting base, e.g. the time of the system power on.

    >>> async with timeout_at(loop.time() + 10):
    ...     async with aiohttp.get('https://github.com') as r:
    ...         await r.text()


    """
    loop = asyncio.get_running_loop()
    return Timeout(deadline, loop)


class _State(enum.Enum):
    INIT = 'INIT'
    ENTER = 'ENTER'
    TIMEOUT = 'TIMEOUT'
    EXIT = 'EXIT'

Timeout = <NODE:12>()

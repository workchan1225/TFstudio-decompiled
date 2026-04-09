# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _check_streams.pyc (Python 3.11)

from __future__ import annotations
import random
import sys
from collections.abc import Awaitable, Callable, Generator
from contextlib import contextmanager, suppress
from typing import TYPE_CHECKING, Generic, TypeAlias, TypeVar
from  import CancelScope, _core
from _abc import AsyncResource, HalfCloseableStream, ReceiveStream, SendStream, Stream
from _highlevel_generic import aclose_forcefully
from _checkpoints import assert_checkpoints
if TYPE_CHECKING:
    from types import TracebackType
    from typing_extensions import ParamSpec
    ArgsT = ParamSpec('ArgsT')
if sys.version_info < (3, 11):
    from exceptiongroup import BaseExceptionGroup
Res1 = TypeVar('Res1', bound = AsyncResource)
Res2 = TypeVar('Res2', bound = AsyncResource)
StreamMaker: 'TypeAlias' = Callable[([], Awaitable[tuple[(Res1, Res2)]])]

def _ForceCloseBoth():
    '''_ForceCloseBoth'''
    
    def __init__(self = None, both = None):
        (self._first, self._second) = both

    
    async def __aenter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def __aexit__(self = None, exc_type = None, exc_value = None, traceback = ('exc_type', 'type[BaseException] | None', 'exc_value', 'BaseException | None', 'traceback', 'TracebackType | None', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete


_ForceCloseBoth = <NODE:27>(_ForceCloseBoth, '_ForceCloseBoth', Generic[(Res1, Res2)])
_assert_raises = (lambda expected_exc = None, wrapped = None: pass# WARNING: Decompyle incomplete
)()

async def check_one_way_stream(stream_maker = None, clogged_stream_maker = None):
    '''Perform a number of generic tests on a custom one-way stream
    implementation.

    Args:
      stream_maker: An async (!) function which returns a connected
          (:class:`~trio.abc.SendStream`, :class:`~trio.abc.ReceiveStream`)
          pair.
      clogged_stream_maker: Either None, or an async function similar to
          stream_maker, but with the extra property that the returned stream
          is in a state where ``send_all`` and
          ``wait_send_all_might_not_block`` will block until ``receive_some``
          has been called. This allows for more thorough testing of some edge
          cases, especially around ``wait_send_all_might_not_block``.

    Raises:
      AssertionError: if a test fails.

    '''
    pass
# WARNING: Decompyle incomplete


async def check_two_way_stream(stream_maker = None, clogged_stream_maker = None):
    """Perform a number of generic tests on a custom two-way stream
    implementation.

    This is similar to :func:`check_one_way_stream`, except that the maker
    functions are expected to return objects implementing the
    :class:`~trio.abc.Stream` interface.

    This function tests a *superset* of what :func:`check_one_way_stream`
    checks – if you call this, then you don't need to also call
    :func:`check_one_way_stream`.

    """
    pass
# WARNING: Decompyle incomplete


async def check_half_closeable_stream(stream_maker = None, clogged_stream_maker = None):
    """Perform a number of generic tests on a custom half-closeable stream
    implementation.

    This is similar to :func:`check_two_way_stream`, except that the maker
    functions are expected to return objects that implement the
    :class:`~trio.abc.HalfCloseableStream` interface.

    This function tests a *superset* of what :func:`check_two_way_stream`
    checks – if you call this, then you don't need to also call
    :func:`check_two_way_stream`.

    """
    pass
# WARNING: Decompyle incomplete

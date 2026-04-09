# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: callable_util.pyc (Python 3.11)

'''Utilities for working with callables.'''
from abc import ABC
import collections
import enum
import functools
import logging
_LOGGER = logging.getLogger(__name__)

class Outcome(ABC):
    '''A sum type describing the outcome of some call.

    Attributes:
      kind: One of Kind.RETURNED or Kind.RAISED respectively indicating that the
        call returned a value or raised an exception.
      return_value: The value returned by the call. Must be present if kind is
        Kind.RETURNED.
      exception: The exception raised by the call. Must be present if kind is
        Kind.RAISED.
    '''
    Kind = <NODE:12>()


def _EasyOutcome():
    '''_EasyOutcome'''
    __doc__ = 'A trivial implementation of Outcome.'

_EasyOutcome = <NODE:27>(_EasyOutcome, '_EasyOutcome', collections.namedtuple('_EasyOutcome', [
    'kind',
    'return_value',
    'exception']), Outcome)

def _call_logging_exceptions(behavior, message, *args, **kwargs):
    pass
# WARNING: Decompyle incomplete


def with_exceptions_logged(behavior, message):
    '''Wraps a callable in a try-except that logs any exceptions it raises.

    Args:
      behavior: Any callable.
      message: A string to log if the behavior raises an exception.

    Returns:
      A callable that when executed invokes the given behavior. The returned
        callable takes the same arguments as the given behavior but returns a
        future.Outcome describing whether the given behavior returned a value or
        raised an exception.
    '''
    pass
# WARNING: Decompyle incomplete


def call_logging_exceptions(behavior, message, *args, **kwargs):
    '''Calls a behavior in a try-except that logs any exceptions it raises.

    Args:
      behavior: Any callable.
      message: A string to log if the behavior raises an exception.
      *args: Positional arguments to pass to the given behavior.
      **kwargs: Keyword arguments to pass to the given behavior.

    Returns:
      An Outcome describing whether the given behavior returned a value or raised
        an exception.
    '''
    pass
# WARNING: Decompyle incomplete

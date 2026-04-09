# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: sandbox.pyc (Python 3.11)

'''A sandbox layer that ensures unsafe operations cannot be performed.
Useful when the template itself comes from an untrusted source.
'''
import operator
import types
import typing as t
from _string import formatter_field_name_split
from collections import abc
from collections import deque
from functools import update_wrapper
from string import Formatter
from markupsafe import EscapeFormatter
from markupsafe import Markup
from environment import Environment
from exceptions import SecurityError
from runtime import Context
from runtime import Undefined
F = t.TypeVar('F', bound = t.Callable[(..., t.Any)])
MAX_RANGE = 100000
UNSAFE_FUNCTION_ATTRIBUTES: t.Set[str] = set()
UNSAFE_METHOD_ATTRIBUTES: t.Set[str] = set()
UNSAFE_GENERATOR_ATTRIBUTES = {
    'gi_frame',
    'gi_code'}
UNSAFE_COROUTINE_ATTRIBUTES = {
    'cr_frame',
    'cr_code'}
UNSAFE_ASYNC_GENERATOR_ATTRIBUTES = {
    'ag_code',
    'ag_frame'}
_mutable_spec: t.Tuple[(t.Tuple[(t.Type[t.Any], t.FrozenSet[str])], ...)] = ((abc.MutableSet, frozenset([
    'add',
    'clear',
    'difference_update',
    'discard',
    'pop',
    'remove',
    'symmetric_difference_update',
    'update'])), (abc.MutableMapping, frozenset([
    'clear',
    'pop',
    'popitem',
    'setdefault',
    'update'])), (abc.MutableSequence, frozenset([
    'append',
    'clear',
    'pop',
    'reverse',
    'insert',
    'sort',
    'extend',
    'remove'])), (deque, frozenset([
    'append',
    'appendleft',
    'clear',
    'extend',
    'extendleft',
    'pop',
    'popleft',
    'remove',
    'rotate'])))

def safe_range(*args):
    """A range that can't generate ranges with a length of more than
    MAX_RANGE items.
    """
    pass
# WARNING: Decompyle incomplete


def unsafe(f = None):
    '''Marks a function or method as unsafe.

    .. code-block: python

        @unsafe
        def delete(self):
            pass
    '''
    f.unsafe_callable = True
    return f


def is_internal_attribute(obj = None, attr = None):
    '''Test if the attribute given is an internal python attribute.  For
    example this function returns `True` for the `func_code` attribute of
    python objects.  This is useful if the environment method
    :meth:`~SandboxedEnvironment.is_safe_attribute` is overridden.

    >>> from jinja2.sandbox import is_internal_attribute
    >>> is_internal_attribute(str, "mro")
    True
    >>> is_internal_attribute(str, "upper")
    False
    '''
    if isinstance(obj, types.FunctionType):
        if attr in UNSAFE_FUNCTION_ATTRIBUTES:
            return True
    if isinstance(obj, types.MethodType):
        if attr in UNSAFE_FUNCTION_ATTRIBUTES or attr in UNSAFE_METHOD_ATTRIBUTES:
            return True
    if isinstance(obj, type):
        if attr == 'mro':
            return True
    if isinstance(obj, (types.CodeType, types.TracebackType, types.FrameType)):
        return True
    if None(obj, types.GeneratorType):
        if attr in UNSAFE_GENERATOR_ATTRIBUTES:
            return True
    if hasattr(types, 'CoroutineType') and isinstance(obj, types.CoroutineType):
        if attr in UNSAFE_COROUTINE_ATTRIBUTES:
            return True
    if hasattr(types, 'AsyncGeneratorType') and isinstance(obj, types.AsyncGeneratorType) and attr in UNSAFE_ASYNC_GENERATOR_ATTRIBUTES:
        return True
    return None.startswith('__')


def modifies_known_mutable(obj = None, attr = None):
    '''This function checks if an attribute on a builtin mutable object
    (list, dict, set or deque) or the corresponding ABCs would modify it
    if called.

    >>> modifies_known_mutable({}, "clear")
    True
    >>> modifies_known_mutable({}, "keys")
    False
    >>> modifies_known_mutable([], "append")
    True
    >>> modifies_known_mutable([], "index")
    False

    If called with an unsupported object, ``False`` is returned.

    >>> modifies_known_mutable("foo", "upper")
    False
    '''
    for typespec, unsafe in _mutable_spec:
        if isinstance(obj, typespec):
            
            return None, attr in unsafe
        return False


class SandboxedEnvironment(Environment):
    pass
# WARNING: Decompyle incomplete


class ImmutableSandboxedEnvironment(SandboxedEnvironment):
    pass
# WARNING: Decompyle incomplete


class SandboxedFormatter(Formatter):
    pass
# WARNING: Decompyle incomplete


class SandboxedEscapeFormatter(EscapeFormatter, SandboxedFormatter):
    pass

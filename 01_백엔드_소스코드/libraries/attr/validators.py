# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: validators.pyc (Python 3.11)

'''
Commonly useful validators.
'''
import operator
import re
from contextlib import contextmanager
from re import Pattern
from _config import get_run_validators, set_run_validators
from _make import _AndValidator, and_, attrib, attrs
from converters import default_if_none
from exceptions import NotCallableError
__all__ = [
    'and_',
    'deep_iterable',
    'deep_mapping',
    'disabled',
    'ge',
    'get_disabled',
    'gt',
    'in_',
    'instance_of',
    'is_callable',
    'le',
    'lt',
    'matches_re',
    'max_len',
    'min_len',
    'not_',
    'optional',
    'or_',
    'set_disabled']

def set_disabled(disabled):
    '''
    Globally disable or enable running validators.

    By default, they are run.

    Args:
        disabled (bool): If `True`, disable running all validators.

    .. warning::

        This function is not thread-safe!

    .. versionadded:: 21.3.0
    '''
    set_run_validators(not disabled)


def get_disabled():
    '''
    Return a bool indicating whether validators are currently disabled or not.

    Returns:
        bool:`True` if validators are currently disabled.

    .. versionadded:: 21.3.0
    '''
    return not get_run_validators()

disabled = (lambda : pass# WARNING: Decompyle incomplete
)()
_InstanceOfValidator = <NODE:12>()

def instance_of(type):
    """
    A validator that raises a `TypeError` if the initializer is called with a
    wrong type for this particular attribute (checks are performed using
    `isinstance` therefore it's also valid to pass a tuple of types).

    Args:
        type (type | tuple[type]): The type to check for.

    Raises:
        TypeError:
            With a human readable error message, the attribute (of type
            `attrs.Attribute`), the expected type, and the value it got.
    """
    return _InstanceOfValidator(type)

_MatchesReValidator = <NODE:12>()

def matches_re(regex, flags, func = (0, None)):
    """
    A validator that raises `ValueError` if the initializer is called with a
    string that doesn't match *regex*.

    Args:
        regex (str, re.Pattern):
            A regex string or precompiled pattern to match against

        flags (int):
            Flags that will be passed to the underlying re function (default 0)

        func (typing.Callable):
            Which underlying `re` function to call. Valid options are
            `re.fullmatch`, `re.search`, and `re.match`; the default `None`
            means `re.fullmatch`. For performance reasons, the pattern is
            always precompiled using `re.compile`.

    .. versionadded:: 19.2.0
    .. versionchanged:: 21.3.0 *regex* can be a pre-compiled pattern.
    """
    valid_funcs = (re.fullmatch, None, re.search, re.match)
    if func not in valid_funcs:
        msg = ', '.join(sorted((lambda .0: pass# WARNING: Decompyle incomplete
)(set(valid_funcs)())))
        raise ValueError(msg)
    if isinstance(regex, Pattern):
        if flags:
            msg = "'flags' can only be used with a string pattern; pass flags to re.compile() instead"
            raise TypeError(msg)
        pattern = regex
    else:
        pattern = re.compile(regex, flags)
    if func is re.match:
        match_func = pattern.match
    elif func is re.search:
        match_func = pattern.search
    else:
        match_func = pattern.fullmatch
    return _MatchesReValidator(pattern, match_func)

_OptionalValidator = <NODE:12>()

def optional(validator):
    '''
    A validator that makes an attribute optional.  An optional attribute is one
    which can be set to `None` in addition to satisfying the requirements of
    the sub-validator.

    Args:
        validator
            (typing.Callable | tuple[typing.Callable] | list[typing.Callable]):
            A validator (or validators) that is used for non-`None` values.

    .. versionadded:: 15.1.0
    .. versionchanged:: 17.1.0 *validator* can be a list of validators.
    .. versionchanged:: 23.1.0 *validator* can also be a tuple of validators.
    '''
    if isinstance(validator, (list, tuple)):
        return _OptionalValidator(_AndValidator(validator))
    return None(validator)

_InValidator = <NODE:12>()

def in_(options):
    '''
    A validator that raises a `ValueError` if the initializer is called with a
    value that does not belong in the *options* provided.

    The check is performed using ``value in options``, so *options* has to
    support that operation.

    To keep the validator hashable, dicts, lists, and sets are transparently
    transformed into a `tuple`.

    Args:
        options: Allowed options.

    Raises:
        ValueError:
            With a human readable error message, the attribute (of type
            `attrs.Attribute`), the expected options, and the value it got.

    .. versionadded:: 17.1.0
    .. versionchanged:: 22.1.0
       The ValueError was incomplete until now and only contained the human
       readable error message. Now it contains all the information that has
       been promised since 17.1.0.
    .. versionchanged:: 24.1.0
       *options* that are a list, dict, or a set are now transformed into a
       tuple to keep the validator hashable.
    '''
    repr_options = options
    if isinstance(options, (list, dict, set)):
        options = tuple(options)
    return _InValidator(options, repr_options)

_IsCallableValidator = <NODE:12>()

def is_callable():
    '''
    A validator that raises a `attrs.exceptions.NotCallableError` if the
    initializer is called with a value for this particular attribute that is
    not callable.

    .. versionadded:: 19.1.0

    Raises:
        attrs.exceptions.NotCallableError:
            With a human readable error message containing the attribute
            (`attrs.Attribute`) name, and the value it got.
    '''
    return _IsCallableValidator()

_DeepIterable = <NODE:12>()

def deep_iterable(member_validator, iterable_validator = (None,)):
    '''
    A validator that performs deep validation of an iterable.

    Args:
        member_validator: Validator(s) to apply to iterable members.

        iterable_validator:
            Validator(s) to apply to iterable itself (optional).

    Raises
        TypeError: if any sub-validators fail

    .. versionadded:: 19.1.0

    .. versionchanged:: 25.4.0
       *member_validator* and *iterable_validator* can now be a list or tuple
       of validators.
    '''
    pass
# WARNING: Decompyle incomplete

_DeepMapping = <NODE:12>()

def deep_mapping(key_validator, value_validator, mapping_validator = (None, None, None)):
    '''
    A validator that performs deep validation of a dictionary.

    All validators are optional, but at least one of *key_validator* or
    *value_validator* must be provided.

    Args:
        key_validator: Validator(s) to apply to dictionary keys.

        value_validator: Validator(s) to apply to dictionary values.

        mapping_validator:
            Validator(s) to apply to top-level mapping attribute.

    .. versionadded:: 19.1.0

    .. versionchanged:: 25.4.0
       *key_validator* and *value_validator* are now optional, but at least one
       of them must be provided.

    .. versionchanged:: 25.4.0
       *key_validator*, *value_validator*, and *mapping_validator* can now be a
       list or tuple of validators.

    Raises:
        TypeError: If any sub-validator fails on validation.

        ValueError:
            If neither *key_validator* nor *value_validator* is provided on
            instantiation.
    '''
    pass
# WARNING: Decompyle incomplete

_NumberValidator = <NODE:12>()

def lt(val):
    '''
    A validator that raises `ValueError` if the initializer is called with a
    number larger or equal to *val*.

    The validator uses `operator.lt` to compare the values.

    Args:
        val: Exclusive upper bound for values.

    .. versionadded:: 21.3.0
    '''
    return _NumberValidator(val, '<', operator.lt)


def le(val):
    '''
    A validator that raises `ValueError` if the initializer is called with a
    number greater than *val*.

    The validator uses `operator.le` to compare the values.

    Args:
        val: Inclusive upper bound for values.

    .. versionadded:: 21.3.0
    '''
    return _NumberValidator(val, '<=', operator.le)


def ge(val):
    '''
    A validator that raises `ValueError` if the initializer is called with a
    number smaller than *val*.

    The validator uses `operator.ge` to compare the values.

    Args:
        val: Inclusive lower bound for values

    .. versionadded:: 21.3.0
    '''
    return _NumberValidator(val, '>=', operator.ge)


def gt(val):
    '''
    A validator that raises `ValueError` if the initializer is called with a
    number smaller or equal to *val*.

    The validator uses `operator.gt` to compare the values.

    Args:
       val: Exclusive lower bound for values

    .. versionadded:: 21.3.0
    '''
    return _NumberValidator(val, '>', operator.gt)

_MaxLengthValidator = <NODE:12>()

def max_len(length):
    '''
    A validator that raises `ValueError` if the initializer is called
    with a string or iterable that is longer than *length*.

    Args:
        length (int): Maximum length of the string or iterable

    .. versionadded:: 21.3.0
    '''
    return _MaxLengthValidator(length)

_MinLengthValidator = <NODE:12>()

def min_len(length):
    '''
    A validator that raises `ValueError` if the initializer is called
    with a string or iterable that is shorter than *length*.

    Args:
        length (int): Minimum length of the string or iterable

    .. versionadded:: 22.1.0
    '''
    return _MinLengthValidator(length)

_SubclassOfValidator = <NODE:12>()

def _subclass_of(type):
    """
    A validator that raises a `TypeError` if the initializer is called with a
    wrong type for this particular attribute (checks are performed using
    `issubclass` therefore it's also valid to pass a tuple of types).

    Args:
        type (type | tuple[type, ...]): The type(s) to check for.

    Raises:
        TypeError:
            With a human readable error message, the attribute (of type
            `attrs.Attribute`), the expected type, and the value it got.
    """
    return _SubclassOfValidator(type)

_NotValidator = <NODE:12>()

def not_(validator = attrs(repr = False, slots = True, unsafe_hash = True), *, msg, exc_types):
    """
    A validator that wraps and logically 'inverts' the validator passed to it.
    It will raise a `ValueError` if the provided validator *doesn't* raise a
    `ValueError` or `TypeError` (by default), and will suppress the exception
    if the provided validator *does*.

    Intended to be used with existing validators to compose logic without
    needing to create inverted variants, for example, ``not_(in_(...))``.

    Args:
        validator: A validator to be logically inverted.

        msg (str):
            Message to raise if validator fails. Formatted with keys
            ``exc_types`` and ``validator``.

        exc_types (tuple[type, ...]):
            Exception type(s) to capture. Other types raised by child
            validators will not be intercepted and pass through.

    Raises:
        ValueError:
            With a human readable error message, the attribute (of type
            `attrs.Attribute`), the validator that failed to raise an
            exception, the value it got, and the expected exception types.

    .. versionadded:: 22.2.0
    """
    
    try:
        exc_types = tuple(exc_types)
    except TypeError:
        exc_types = (exc_types,)

    return _NotValidator(validator, msg, exc_types)

_OrValidator = <NODE:12>()

def or_(*validators):
    '''
    A validator that composes multiple validators into one.

    When called on a value, it runs all wrapped validators until one of them is
    satisfied.

    Args:
        validators (~collections.abc.Iterable[typing.Callable]):
            Arbitrary number of validators.

    Raises:
        ValueError:
            If no validator is satisfied. Raised with a human-readable error
            message listing all the wrapped validators and the value that
            failed all of them.

    .. versionadded:: 24.1.0
    '''
    vals = []
    for v in validators:
        vals.extend(v.validators if isinstance(v, _OrValidator) else [
            v])
        return _OrValidator(tuple(vals))

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: converters.pyc (Python 3.11)

'''
Commonly useful converters.
'''
import typing
from _compat import _AnnotationExtractor
from _make import NOTHING, Converter, Factory, pipe
__all__ = [
    'default_if_none',
    'optional',
    'pipe',
    'to_bool']

def optional(converter):
    """
    A converter that allows an attribute to be optional. An optional attribute
    is one which can be set to `None`.

    Type annotations will be inferred from the wrapped converter's, if it has
    any.

    Args:
        converter (typing.Callable):
            the converter that is used for non-`None` values.

    .. versionadded:: 17.1.0
    """
    pass
# WARNING: Decompyle incomplete


def default_if_none(default, factory = (NOTHING, None)):
    '''
    A converter that allows to replace `None` values by *default* or the result
    of *factory*.

    Args:
        default:
            Value to be used if `None` is passed. Passing an instance of
            `attrs.Factory` is supported, however the ``takes_self`` option is
            *not*.

        factory (typing.Callable):
            A callable that takes no parameters whose result is used if `None`
            is passed.

    Raises:
        TypeError: If **neither** *default* or *factory* is passed.

        TypeError: If **both** *default* and *factory* are passed.

        ValueError:
            If an instance of `attrs.Factory` is passed with
            ``takes_self=True``.

    .. versionadded:: 18.2.0
    '''
    pass
# WARNING: Decompyle incomplete


def to_bool(val):
    '''
    Convert "boolean" strings (for example, from environment variables) to real
    booleans.

    Values mapping to `True`:

    - ``True``
    - ``"true"`` / ``"t"``
    - ``"yes"`` / ``"y"``
    - ``"on"``
    - ``"1"``
    - ``1``

    Values mapping to `False`:

    - ``False``
    - ``"false"`` / ``"f"``
    - ``"no"`` / ``"n"``
    - ``"off"``
    - ``"0"``
    - ``0``

    Raises:
        ValueError: For any other value.

    .. versionadded:: 21.3.0
    '''
    if isinstance(val, str):
        val = val.lower()
    if val in (True, 'true', 't', 'yes', 'y', 'on', '1', 1):
        return True
    if None in (False, 'false', 'f', 'no', 'n', 'off', '0', 0):
        return False
    msg = f'''{val!r}'''
    raise ValueError(msg)

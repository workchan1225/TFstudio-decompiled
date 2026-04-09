# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: converters.pyc (Python 3.11)

from __future__ import annotations
import re
import typing as t
import uuid
from urllib.parse import quote
if t.TYPE_CHECKING:
    from map import Map

class ValidationError(ValueError):
    '''Validation error.  If a rule converter raises this exception the rule
    does not match the current URL and the next URL is tried.
    '''
    pass


class BaseConverter:
    pass
# WARNING: Decompyle incomplete


class UnicodeConverter(BaseConverter):
    pass
# WARNING: Decompyle incomplete


class AnyConverter(BaseConverter):
    pass
# WARNING: Decompyle incomplete


class PathConverter(BaseConverter):
    """Like the default :class:`UnicodeConverter`, but it also matches
    slashes.  This is useful for wikis and similar applications::

        Rule('/<path:wikipage>')
        Rule('/<path:wikipage>/edit')

    :param map: the :class:`Map`.
    """
    part_isolating = False
    regex = '[^/].*?'
    weight = 200


class NumberConverter(BaseConverter):
    pass
# WARNING: Decompyle incomplete


class IntegerConverter(NumberConverter):
    '''This converter only accepts integer values::

        Rule("/page/<int:page>")

    By default it only accepts unsigned, positive values. The ``signed``
    parameter will enable signed, negative values. ::

        Rule("/page/<int(signed=True):page>")

    :param map: The :class:`Map`.
    :param fixed_digits: The number of fixed digits in the URL. If you
        set this to ``4`` for example, the rule will only match if the
        URL looks like ``/0001/``. The default is variable length.
    :param min: The minimal value.
    :param max: The maximal value.
    :param signed: Allow signed (negative) values.

    .. versionadded:: 0.15
        The ``signed`` parameter.
    '''
    regex = '\\d+'


class FloatConverter(NumberConverter):
    pass
# WARNING: Decompyle incomplete


class UUIDConverter(BaseConverter):
    """This converter only accepts UUID strings::

        Rule('/object/<uuid:identifier>')

    .. versionadded:: 0.10

    :param map: the :class:`Map`.
    """
    regex = '[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}'
    
    def to_python(self = None, value = None):
        return uuid.UUID(value)

    
    def to_url(self = None, value = None):
        return str(value)


DEFAULT_CONVERTERS: 't.Mapping[str, type[BaseConverter]]' = {
    'default': UnicodeConverter,
    'string': UnicodeConverter,
    'any': AnyConverter,
    'path': PathConverter,
    'int': IntegerConverter,
    'float': FloatConverter,
    'uuid': UUIDConverter }

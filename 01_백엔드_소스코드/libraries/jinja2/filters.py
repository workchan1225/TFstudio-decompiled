# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: filters.pyc (Python 3.11)

__doc__ = 'Built-in template filters used with the ``|`` operator.'
import math
import random
import re
import typing
import typing as t
from collections import abc
from inspect import getattr_static
from itertools import chain
from itertools import groupby
from markupsafe import escape
from markupsafe import Markup
from markupsafe import soft_str
from async_utils import async_variant
from async_utils import auto_aiter
from async_utils import auto_await
from async_utils import auto_to_list
from exceptions import FilterArgumentError
from runtime import Undefined
from utils import htmlsafe_json_dumps
from utils import pass_context
from utils import pass_environment
from utils import pass_eval_context
from utils import pformat
from utils import url_quote
from utils import urlize
if t.TYPE_CHECKING:
    import typing_extensions as te
    from environment import Environment
    from nodes import EvalContext
    from runtime import Context
    from sandbox import SandboxedEnvironment
    
    class HasHTML(te.Protocol):
        
        def __html__(self = None):
            pass


F = t.TypeVar('F', bound = t.Callable[(..., t.Any)])
K = t.TypeVar('K')
V = t.TypeVar('V')

def ignore_case(value = None):
    '''For use as a postprocessor for :func:`make_attrgetter`. Converts strings
    to lowercase and returns other types as-is.'''
    if isinstance(value, str):
        return t.cast(V, value.lower())


def make_attrgetter(environment = None, attribute = None, postprocess = None, default = (None, None)):
    '''Returns a callable that looks up the given attribute from a
    passed object with the rules of the environment.  Dots are allowed
    to access attributes of attributes.  Integer parts in paths are
    looked up as integers.
    '''
    pass
# WARNING: Decompyle incomplete


def make_multi_attrgetter(environment = None, attribute = None, postprocess = None):
    '''Returns a callable that looks up the given comma separated
    attributes from a passed object with the rules of the environment.
    Dots are allowed to access attributes of each attribute.  Integer
    parts in paths are looked up as integers.

    The value returned by the returned callable is a list of extracted
    attribute values.

    Examples of attribute: "attr1,attr2", "attr1.inner1.0,attr2.inner2.0", etc.
    '''
    pass
# WARNING: Decompyle incomplete


def _prepare_attribute_parts(attr = None):
    pass
# WARNING: Decompyle incomplete


def do_forceescape(value = None):
    '''Enforce HTML escaping.  This will probably double escape variables.'''
    if hasattr(value, '__html__'):
        value = t.cast('HasHTML', value).__html__()
    return escape(str(value))


def do_urlencode(value = None):
    '''Quote data for use in a URL path or query using UTF-8.

    Basic wrapper around :func:`urllib.parse.quote` when given a
    string, or :func:`urllib.parse.urlencode` for a dict or iterable.

    :param value: Data to quote. A string will be quoted directly. A
        dict or iterable of ``(key, value)`` pairs will be joined as a
        query string.

    When given a string, "/" is not quoted. HTTP servers treat "/" and
    "%2F" equivalently in paths. If you need quoted slashes, use the
    ``|replace("/", "%2F")`` filter.

    .. versionadded:: 2.7
    '''
    if not isinstance(value, str) or isinstance(value, abc.Iterable):
        return url_quote(value)
    if None(value, dict):
        items = value.items()
    else:
        items = value
    return (lambda .0: pass# WARNING: Decompyle incomplete
)(items())

do_replace = (lambda eval_ctx = None, s = None, old = pass_eval_context, new = (None,), count = ('eval_ctx', 'EvalContext', 's', str, 'old', str, 'new', str, 'count', t.Optional[int], 'return', str): pass# WARNING: Decompyle incomplete
)()

def do_upper(s = None):
    '''Convert a value to uppercase.'''
    return soft_str(s).upper()


def do_lower(s = None):
    '''Convert a value to lowercase.'''
    return soft_str(s).lower()


def do_items(value = None):
    '''Return an iterator over the ``(key, value)`` items of a mapping.

    ``x|items`` is the same as ``x.items()``, except if ``x`` is
    undefined an empty iterator is returned.

    This filter is useful if you expect the template to be rendered with
    an implementation of Jinja in another programming language that does
    not have a ``.items()`` method on its mapping type.

    .. code-block:: html+jinja

        <dl>
        {% for key, value in my_dict|items %}
            <dt>{{ key }}
            <dd>{{ value }}
        {% endfor %}
        </dl>

    .. versionadded:: 3.1
    '''
    pass
# WARNING: Decompyle incomplete

_attr_key_re = re.compile('[\\s/>=]', flags = re.ASCII)
do_xmlattr = (lambda eval_ctx = None, d = None, autospace = pass_eval_context: items = []# WARNING: Decompyle incomplete
)()

def do_capitalize(s = None):
    '''Capitalize a value. The first character will be uppercase, all others
    lowercase.
    '''
    return soft_str(s).capitalize()

_word_beginning_split_re = re.compile('([-\\s({\\[<]+)')

def do_title(s = None):
    '''Return a titlecased version of the value. I.e. words will start with
    uppercase letters, all remaining characters are lowercase.
    '''
    return (lambda .0: pass# WARNING: Decompyle incomplete
)(_word_beginning_split_re.split(soft_str(s))())


def do_dictsort(value = None, case_sensitive = None, by = None, reverse = (False, 'key', False)):
    """Sort a dict and yield (key, value) pairs. Python dicts may not
    be in the order you want to display them in, so sort them first.

    .. sourcecode:: jinja

        {% for key, value in mydict|dictsort %}
            sort the dict by key, case insensitive

        {% for key, value in mydict|dictsort(reverse=true) %}
            sort the dict by key, case insensitive, reverse order

        {% for key, value in mydict|dictsort(true) %}
            sort the dict by key, case sensitive

        {% for key, value in mydict|dictsort(false, 'value') %}
            sort the dict by value, case insensitive
    """
    pass
# WARNING: Decompyle incomplete

do_sort = (lambda environment = None, value = None, reverse = pass_environment, case_sensitive = (False, False, None), attribute = ('environment', 'Environment', 'value', 't.Iterable[V]', 'reverse', bool, 'case_sensitive', bool, 'attribute', t.Optional[t.Union[(str, int)]], 'return', 't.List[V]'): key_func = make_multi_attrgetter(environment, attribute, postprocess = ignore_case if not case_sensitive else None)sorted(value, key = key_func, reverse = reverse))()
sync_do_unique = (lambda environment = None, value = None, case_sensitive = pass_environment, attribute = (False, None): pass# WARNING: Decompyle incomplete
)()
do_unique = (lambda environment = None, value = None, case_sensitive = async_variant(sync_do_unique), attribute = (False, None): pass# WARNING: Decompyle incomplete
)()

def _min_or_max(environment, value = None, func = None, case_sensitive = None, attribute = ('environment', 'Environment', 'value', 't.Iterable[V]', 'func', 't.Callable[..., V]', 'case_sensitive', bool, 'attribute', t.Optional[t.Union[(str, int)]], 'return', 't.Union[V, Undefined]')):
    it = iter(value)
    
    try:
        first = next(it)
    except StopIteration:
        return 

    return func(chain([
        first], it), key = key_func)

do_min = (lambda environment = None, value = None, case_sensitive = pass_environment, attribute = (False, None): _min_or_max(environment, value, min, case_sensitive, attribute))()
do_max = (lambda environment = None, value = None, case_sensitive = pass_environment, attribute = (False, None): _min_or_max(environment, value, max, case_sensitive, attribute))()

def do_default(value = None, default_value = None, boolean = None):
    """If the value is undefined it will return the passed default value,
    otherwise the value of the variable:

    .. sourcecode:: jinja

        {{ my_variable|default('my_variable is not defined') }}

    This will output the value of ``my_variable`` if the variable was
    defined, otherwise ``'my_variable is not defined'``. If you want
    to use default with variables that evaluate to false you have to
    set the second parameter to `true`:

    .. sourcecode:: jinja

        {{ ''|default('the string was empty', true) }}

    .. versionchanged:: 2.11
       It's now possible to configure the :class:`~jinja2.Environment` with
       :class:`~jinja2.ChainableUndefined` to make the `default` filter work
       on nested elements and attributes that may contain undefined values
       in the chain without getting an :exc:`~jinja2.UndefinedError`.
    """
    if not (isinstance(value, Undefined) or boolean) and value:
        return default_value

sync_do_join = (lambda eval_ctx = None, value = None, d = pass_eval_context, attribute = ('', None): pass# WARNING: Decompyle incomplete
)()
do_join = (lambda eval_ctx = None, value = None, d = async_variant(sync_do_join), attribute = ('', None): pass# WARNING: Decompyle incomplete
)()

def do_center(value = None, width = None):
    '''Centers the value in a field of a given width.'''
    return soft_str(value).center(width)

sync_do_first = (lambda environment = None, seq = None: try:
next(iter(seq))except StopIteration:
)()
do_first = (lambda environment = None, seq = None: pass# WARNING: Decompyle incomplete
)()
do_last = (lambda environment = None, seq = None: try:
next(iter(reversed(seq)))except StopIteration:
)()
do_random = (lambda context = None, seq = None: try:
random.choice(seq)except IndexError:
)()

def do_filesizeformat(value = None, binary = None):
    """Format the value like a 'human-readable' file size (i.e. 13 kB,
    4.1 MB, 102 Bytes, etc).  Per default decimal prefixes are used (Mega,
    Giga, etc.), if the second parameter is set to `True` the binary
    prefixes are used (Mebi, Gibi).
    """
    bytes = float(value)
    base = 1024 if binary else 1000
    prefixes = [
        'KiB' if binary else 'kB',
        'MiB' if binary else 'MB',
        'GiB' if binary else 'GB',
        'TiB' if binary else 'TB',
        'PiB' if binary else 'PB',
        'EiB' if binary else 'EB',
        'ZiB' if binary else 'ZB',
        'YiB' if binary else 'YB']
    if bytes == 1:
        return '1 Byte'
    if None < base:
        return f'''{int(bytes)} Bytes'''
    for i, prefix in None(prefixes):
        unit = base ** (i + 2)
        if bytes < unit:
            
            return None, f'''{base * bytes / unit:.1f} {prefix}'''
        return f'''{base * bytes / unit:.1f} {prefix}'''


def do_pprint(value = None):
    '''Pretty print a variable. Useful for debugging.'''
    return pformat(value)

_uri_scheme_re = re.compile('^([\\w.+-]{2,}:(/){0,2})$')
do_urlize = (lambda eval_ctx, value, trim_url_limit = None, nofollow = None, target = pass_eval_context, rel = (None, False, None, None, None), extra_schemes = ('eval_ctx', 'EvalContext', 'value', str, 'trim_url_limit', t.Optional[int], 'nofollow', bool, 'target', t.Optional[str], 'rel', t.Optional[str], 'extra_schemes', t.Optional[t.Iterable[str]], 'return', str): policies = eval_ctx.environment.policiesif not rel:
rel_parts = set(''.split())if nofollow:
rel_parts.add('nofollow')# WARNING: Decompyle incomplete
)()

def do_indent(s = None, width = None, first = None, blank = (4, False, False)):
    """Return a copy of the string with each line indented by 4 spaces. The
    first line and blank lines are not indented by default.

    :param width: Number of spaces, or a string, to indent by.
    :param first: Don't skip indenting the first line.
    :param blank: Don't skip indenting empty lines.

    .. versionchanged:: 3.0
        ``width`` can be a string.

    .. versionchanged:: 2.10
        Blank lines are not indented by default.

        Rename the ``indentfirst`` argument to ``first``.
    """
    pass
# WARNING: Decompyle incomplete

do_truncate = (lambda env, s = None, length = None, killwords = pass_environment, end = (255, False, '...', None), leeway = ('env', 'Environment', 's', str, 'length', int, 'killwords', bool, 'end', str, 'leeway', t.Optional[int], 'return', str): pass# WARNING: Decompyle incomplete
)()
do_wordwrap = (lambda environment, s = None, width = None, break_long_words = pass_environment, wrapstring = (79, True, None, True), break_on_hyphens = ('environment', 'Environment', 's', str, 'width', int, 'break_long_words', bool, 'wrapstring', t.Optional[str], 'break_on_hyphens', bool, 'return', str): pass# WARNING: Decompyle incomplete
)()
_word_re = re.compile('\\w+')

def do_wordcount(s = None):
    '''Count the words in that string.'''
    return len(_word_re.findall(soft_str(s)))


def do_int(value = None, default = None, base = None):
    """Convert the value into an integer. If the
    conversion doesn't work it will return ``0``. You can
    override this default using the first parameter. You
    can also override the default base (10) in the second
    parameter, which handles input with prefixes such as
    0b, 0o and 0x for bases 2, 8 and 16 respectively.
    The base is ignored for decimal numbers and non-string values.
    """
    
    try:
        if isinstance(value, str):
            return int(value, base)
        return None(value)
    except (TypeError, ValueError):
        return 
        except (TypeError, ValueError, OverflowError):
            return 



def do_float(value = None, default = None):
    """Convert the value into a floating point number. If the
    conversion doesn't work it will return ``0.0``. You can
    override this default using the first parameter.
    """
    
    try:
        return float(value)
    except (TypeError, ValueError):
        return 



def do_format(value = None, *args, **kwargs):

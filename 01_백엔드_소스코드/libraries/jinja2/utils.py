# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: utils.pyc (Python 3.11)

import enum
import json
import os
import re
import typing as t
from collections import abc
from collections import deque
from random import choice
from random import randrange
from threading import Lock
from types import CodeType
from urllib.parse import quote_from_bytes
import markupsafe
if t.TYPE_CHECKING:
    import typing_extensions as te
F = t.TypeVar('F', bound = t.Callable[(..., t.Any)])

class _MissingType:
    
    def __repr__(self = None):
        return 'missing'

    
    def __reduce__(self = None):
        return 'missing'


missing: t.Any = _MissingType()
internal_code: t.MutableSet[CodeType] = set()
concat = ''.join

def pass_context(f = None):
    '''Pass the :class:`~jinja2.runtime.Context` as the first argument
    to the decorated function when called while rendering a template.

    Can be used on functions, filters, and tests.

    If only ``Context.eval_context`` is needed, use
    :func:`pass_eval_context`. If only ``Context.environment`` is
    needed, use :func:`pass_environment`.

    .. versionadded:: 3.0.0
        Replaces ``contextfunction`` and ``contextfilter``.
    '''
    f.jinja_pass_arg = _PassArg.context
    return f


def pass_eval_context(f = None):
    '''Pass the :class:`~jinja2.nodes.EvalContext` as the first argument
    to the decorated function when called while rendering a template.
    See :ref:`eval-context`.

    Can be used on functions, filters, and tests.

    If only ``EvalContext.environment`` is needed, use
    :func:`pass_environment`.

    .. versionadded:: 3.0.0
        Replaces ``evalcontextfunction`` and ``evalcontextfilter``.
    '''
    f.jinja_pass_arg = _PassArg.eval_context
    return f


def pass_environment(f = None):
    '''Pass the :class:`~jinja2.Environment` as the first argument to
    the decorated function when called while rendering a template.

    Can be used on functions, filters, and tests.

    .. versionadded:: 3.0.0
        Replaces ``environmentfunction`` and ``environmentfilter``.
    '''
    f.jinja_pass_arg = _PassArg.environment
    return f


class _PassArg(enum.Enum):
    context = enum.auto()
    eval_context = enum.auto()
    environment = enum.auto()
    from_obj = (lambda cls = None, obj = None: if hasattr(obj, 'jinja_pass_arg'):
obj.jinja_pass_arg)()


def internalcode(f = None):
    '''Marks the function as internally used'''
    internal_code.add(f.__code__)
    return f


def is_undefined(obj = None):
    """Check if the object passed is undefined.  This does nothing more than
    performing an instance check against :class:`Undefined` but looks nicer.
    This can be used for custom filters or tests that want to react to
    undefined variables.  For example a custom default filter can look like
    this::

        def default(var, default=''):
            if is_undefined(var):
                return default
            return var
    """
    Undefined = Undefined
    import runtime
    return isinstance(obj, Undefined)


def consume(iterable = None):
    '''Consumes an iterable without doing anything with it.'''
    for _ in iterable:
        pass


def clear_caches():
    """Jinja keeps internal caches for environments and lexers.  These are
    used so that Jinja doesn't have to recreate environments and lexers all
    the time.  Normally you don't have to care about that but if you are
    measuring memory consumption you may want to clean the caches.
    """
    get_spontaneous_environment = get_spontaneous_environment
    import environment
    _lexer_cache = _lexer_cache
    import lexer
    get_spontaneous_environment.cache_clear()
    _lexer_cache.clear()


def import_string(import_name = None, silent = None):
    '''Imports an object based on a string.  This is useful if you want to
    use import paths as endpoints or something similar.  An import path can
    be specified either in dotted notation (``xml.sax.saxutils.escape``)
    or with a colon as object delimiter (``xml.sax.saxutils:escape``).

    If the `silent` is True the return value will be `None` if the import
    fails.

    :return: imported object
    '''
    
    try:
        if ':' in import_name:
            (module, obj) = import_name.split(':', 1)
        elif '.' in import_name:
            (module, _, obj) = import_name.rpartition('.')
        else:
            return __import__(import_name)
        return None(__import__(module, None, None, [
            obj]), obj)
    except (ImportError, AttributeError):
        if not silent:
            raise 
        return None



def open_if_exists(filename = None, mode = None):
    '''Returns a file descriptor for the filename if that file exists,
    otherwise ``None``.
    '''
    if not os.path.isfile(filename):
        return None
    return None(filename, mode)


def object_type_repr(obj = None):
    """Returns the name of the object's type.  For some recognized
    singletons the name of the object is returned instead. (For
    example for `None` and `Ellipsis`).
    """
    pass
# WARNING: Decompyle incomplete


def pformat(obj = None):
    '''Format an object using :func:`pprint.pformat`.'''
    pformat = pformat
    import pprint
    return pformat(obj)

_http_re = re.compile('\n    ^\n    (\n        (https?://|www\\.)  # scheme or www\n        (([\\w%-]+\\.)+)?  # subdomain\n        (\n            [a-z]{2,63}  # basic tld\n        |\n            xn--[\\w%]{2,59}  # idna tld\n        )\n    |\n        ([\\w%-]{2,63}\\.)+  # basic domain\n        (com|net|int|edu|gov|org|info|mil)  # basic tld\n    |\n        (https?://)  # scheme\n        (\n            (([\\d]{1,3})(\\.[\\d]{1,3}){3})  # IPv4\n        |\n            (\\[([\\da-f]{0,4}:){2}([\\da-f]{0,4}:?){1,6}])  # IPv6\n        )\n    )\n    (?::[\\d]{1,5})?  # port\n    (?:[/?#]\\S*)?  # path, query, and fragment\n    $\n    ', re.IGNORECASE | re.VERBOSE)
_email_re = re.compile('^\\S+@\\w[\\w.-]*\\.\\w+$')

def urlize(text = None, trim_url_limit = None, rel = None, target = (None, None, None, None), extra_schemes = ('text', str, 'trim_url_limit', t.Optional[int], 'rel', t.Optional[str], 'target', t.Optional[str], 'extra_schemes', t.Optional[t.Iterable[str]], 'return', str)):
    '''Convert URLs in text into clickable links.

    This may not recognize links in some situations. Usually, a more
    comprehensive formatter, such as a Markdown library, is a better
    choice.

    Works on ``http://``, ``https://``, ``www.``, ``mailto:``, and email
    addresses. Links with trailing punctuation (periods, commas, closing
    parentheses) and leading punctuation (opening parentheses) are
    recognized excluding the punctuation. Email addresses that include
    header fields are not recognized (for example,
    ``mailto:address@example.com?cc=copy@example.com``).

    :param text: Original text containing URLs to link.
    :param trim_url_limit: Shorten displayed URL values to this length.
    :param target: Add the ``target`` attribute to links.
    :param rel: Add the ``rel`` attribute to links.
    :param extra_schemes: Recognize URLs that start with these schemes
        in addition to the default behavior.

    .. versionchanged:: 3.0
        The ``extra_schemes`` parameter was added.

    .. versionchanged:: 3.0
        Generate ``https://`` links for URLs without a scheme.

    .. versionchanged:: 3.0
        The parsing rules were updated. Recognize email addresses with
        or without the ``mailto:`` scheme. Validate IP addresses. Ignore
        parentheses and brackets in more cases.
    '''
    pass
# WARNING: Decompyle incomplete


def generate_lorem_ipsum(n = None, html = None, min = None, max = (5, True, 20, 100)):
    '''Generate some lorem ipsum for the template.'''
    LOREM_IPSUM_WORDS = LOREM_IPSUM_WORDS
    import constants
    words = LOREM_IPSUM_WORDS.split()
    result = []
    for _ in range(n):
        next_capitalized = True
        last_comma = 0
        last_fullstop = 0
        word = None
        last = None
        p = []
        for idx, _ in enumerate(range(randrange(min, max))):
            word = choice(words)
            if word != last:
                last = word
            
            if next_capitalized:
                word = word.capitalize()
                next_capitalized = False
            if idx - randrange(3, 8) > last_comma:
                last_comma = idx
                last_fullstop += 2
                word += ','
            if idx - randrange(10, 20) > last_fullstop:
                last_comma = idx
                last_fullstop = idx
                word += '.'
                next_capitalized = True
            p.append(word)
            p_str = ' '.join(p)
            if p_str.endswith(','):
                p_str = p_str[:-1] + '.'
            elif not p_str.endswith('.'):
                p_str += '.'
        result.append(p_str)
        if not html:
            return '\n\n'.join(result)
        return '\n'.join((lambda .0: pass# WARNING: Decompyle incomplete
)(result()))


def url_quote(obj = None, charset = None, for_qs = None):
    '''Quote a string for use in a URL using the given charset.

    :param obj: String or bytes to quote. Other types are converted to
        string then encoded to bytes using the given charset.
    :param charset: Encode text to bytes using this charset.
    :param for_qs: Quote "/" and use "+" for spaces.
    '''
    if not isinstance(obj, bytes):
        if not isinstance(obj, str):
            obj = str(obj)
        obj = obj.encode(charset)
    safe = b'' if for_qs else b'/'
    rv = quote_from_bytes(obj, safe)
    if for_qs:
        rv = rv.replace('%20', '+')
    return rv

LRUCache = <NODE:12>()

def select_autoescape(enabled_extensions = None, disabled_extensions = None, default_for_string = abc.MutableMapping.register, default = (('html', 'htm', 'xml'), (), True, False)):
    """Intelligently sets the initial value of autoescaping based on the
    filename of the template.  This is the recommended way to configure
    autoescaping if you do not want to write a custom function yourself.

    If you want to enable it for all templates created from strings or
    for all templates with `.html` and `.xml` extensions::

        from jinja2 import Environment, select_autoescape
        env = Environment(autoescape=select_autoescape(
            enabled_extensions=('html', 'xml'),
            default_for_string=True,
        ))

    Example configuration to turn it on at all times except if the template
    ends with `.txt`::

        from jinja2 import Environment, select_autoescape
        env = Environment(autoescape=select_autoescape(
            disabled_extensions=('txt',),
            default_for_string=True,
            default=True,
        ))

    The `enabled_extensions` is an iterable of all the extensions that
    autoescaping should be enabled for.  Likewise `disabled_extensions` is
    a list of all templates it should be disabled for.  If a template is
    loaded from a string then the default from `default_for_string` is used.
    If nothing matches then the initial value of autoescaping is set to the
    value of `default`.

    For security reasons this function operates case insensitive.

    .. versionadded:: 2.9
    """
    pass
# WARNING: Decompyle incomplete


def htmlsafe_json_dumps(obj = None, dumps = None, **kwargs):
    '''Serialize an object to a string of JSON with :func:`json.dumps`,
    then replace HTML-unsafe characters with Unicode escapes and mark
    the result safe with :class:`~markupsafe.Markup`.

    This is available in templates as the ``|tojson`` filter.

    The following characters are escaped: ``<``, ``>``, ``&``, ``\'``.

    The returned string is safe to render in HTML documents and
    ``<script>`` tags. The exception is in HTML attributes that are
    double quoted; either use single quotes or the ``|forceescape``
    filter.

    :param obj: The object to serialize to JSON.
    :param dumps: The ``dumps`` function to use. Defaults to
        ``env.policies["json.dumps_function"]``, which defaults to
        :func:`json.dumps`.
    :param kwargs: Extra arguments to pass to ``dumps``. Merged onto
        ``env.policies["json.dumps_kwargs"]``.

    .. versionchanged:: 3.0
        The ``dumper`` parameter is renamed to ``dumps``.

    .. versionadded:: 2.9
    '''
    pass
# WARNING: Decompyle incomplete


class Cycler:
    '''Cycle through values by yield them one at a time, then restarting
    once the end is reached. Available as ``cycler`` in templates.

    Similar to ``loop.cycle``, but can be used outside loops or across
    multiple loops. For example, render a list of folders and files in a
    list, alternating giving them "odd" and "even" classes.

    .. code-block:: html+jinja

        {% set row_class = cycler("odd", "even") %}
        <ul class="browser">
        {% for folder in folders %}
          <li class="folder {{ row_class.next() }}">{{ folder }}
        {% endfor %}
        {% for file in files %}
          <li class="file {{ row_class.next() }}">{{ file }}
        {% endfor %}
        </ul>

    :param items: Each positional argument will be yielded in the order
        given for each cycle.

    .. versionadded:: 2.1
    '''
    
    def __init__(self = None, *items):
        if not items:
            raise RuntimeError('at least one item has to be provided')
        self.items = items
        self.pos = 0

    
    def reset(self = None):
        '''Resets the current item to the first item.'''
        self.pos = 0

    current = (lambda self = None: self.items[self.pos])()
    
    def next(self = None):
        '''Return the current item, then advance :attr:`current` to the
        next item.
        '''
        rv = self.current
        self.pos = (self.pos + 1) % len(self.items)
        return rv

    __next__ = next


class Joiner:
    '''A joining helper for templates.'''
    
    def __init__(self = None, sep = None):
        self.sep = sep
        self.used = False

    
    def __call__(self = None):
        if not self.used:
            self.used = True
            return ''
        return None.sep



class Namespace:
    '''A namespace object that can hold arbitrary attributes.  It may be
    initialized from a dictionary or with keyword arguments.'''
    
    def __init__(*args, **kwargs):
        args = args[1:]
        self = args[0]
    # WARNING: Decompyle incomplete

    
    def __getattribute__(self = None, name = None):
        if name in frozenset({'__class__', '_Namespace__attrs'}):
            return object.__getattribute__(self, name)
        
        try:
            return self._Namespace__attrs[name]
        except KeyError:
            raise AttributeError(name), None


    
    def __setitem__(self = None, name = None, value = None):
        self._Namespace__attrs[name] = value

    
    def __repr__(self = None):
        return f'''<Namespace {self._Namespace__attrs!r}>'''

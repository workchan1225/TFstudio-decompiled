# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: rules.pyc (Python 3.11)

from __future__ import annotations
import ast
import re
import typing as t
from dataclasses import dataclass
from string import Template
from types import CodeType
from urllib.parse import quote
from datastructures import iter_multi_items
from urls import _urlencode
from converters import ValidationError
if t.TYPE_CHECKING:
    from converters import BaseConverter
    from map import Map

class Weighting(t.NamedTuple):
    argument_weights: 'list[int]' = 'Weighting'

RulePart = <NODE:12>()
_part_re = re.compile('\n    (?:\n        (?P<slash>/)                                 # a slash\n      |\n        (?P<static>[^</]+)                           # static rule data\n      |\n        (?:\n          <\n            (?:\n              (?P<converter>[a-zA-Z_][a-zA-Z0-9_]*)   # converter name\n              (?:\\((?P<arguments>.*?)\\))?             # converter arguments\n              :                                       # variable delimiter\n            )?\n            (?P<variable>[a-zA-Z_][a-zA-Z0-9_]*)      # variable name\n           >\n        )\n    )\n    ', re.VERBOSE)
_simple_rule_re = re.compile('<([^>]+)>')
_converter_args_re = re.compile('\n    \\s*\n    ((?P<name>\\w+)\\s*=\\s*)?\n    (?P<value>\n        True|False|\n        \\d+.\\d+|\n        \\d+.|\n        \\d+|\n        [\\w\\d_.]+|\n        [urUR]?(?P<stringval>"[^"]*?"|\'[^\']*\')\n    )\\s*,\n    ', re.VERBOSE)
_PYTHON_CONSTANTS = {
    'None': None,
    'True': True,
    'False': False }

def _find(value = None, target = None, pos = dataclass):
    """Find the *target* in *value* after *pos*.

    Returns the *value* length if *target* isn't found.
    """
    
    try:
        return value.index(target, pos)
    except ValueError:
        return 



def _pythonize(value = None):
    if value in _PYTHON_CONSTANTS:
        return _PYTHON_CONSTANTS[value]
    for convert in (None, float):
        
        return None, convert(value)
        except ValueError:
            continue
        if value[:1] == value[-1:] and value[0] in '"\'':
            pass
    return str(value)


def parse_converter_args(argstr = None):
    argstr += ','
    args = []
    kwargs = { }
    position = 0
# WARNING: Decompyle incomplete


class RuleFactory:
    """As soon as you have more complex URL setups it's a good idea to use rule
    factories to avoid repetitive tasks.  Some of them are builtin, others can
    be added by subclassing `RuleFactory` and overriding `get_rules`.
    """
    
    def get_rules(self = None, map = None):
        '''Subclasses of `RuleFactory` have to override this method and return
        an iterable of rules.'''
        raise NotImplementedError()



class Subdomain(RuleFactory):
    """All URLs provided by this factory have the subdomain set to a
    specific domain. For example if you want to use the subdomain for
    the current language this can be a good setup::

        url_map = Map([
            Rule('/', endpoint='#select_language'),
            Subdomain('<string(length=2):lang_code>', [
                Rule('/', endpoint='index'),
                Rule('/about', endpoint='about'),
                Rule('/help', endpoint='help')
            ])
        ])

    All the rules except for the ``'#select_language'`` endpoint will now
    listen on a two letter long subdomain that holds the language code
    for the current request.
    """
    
    def __init__(self = None, subdomain = None, rules = None):
        self.subdomain = subdomain
        self.rules = rules

    
    def get_rules(self = None, map = None):
        pass
    # WARNING: Decompyle incomplete



class Submount(RuleFactory):
    """Like `Subdomain` but prefixes the URL rule with a given string::

        url_map = Map([
            Rule('/', endpoint='index'),
            Submount('/blog', [
                Rule('/', endpoint='blog/index'),
                Rule('/entry/<entry_slug>', endpoint='blog/show')
            ])
        ])

    Now the rule ``'blog/show'`` matches ``/blog/entry/<entry_slug>``.
    """
    
    def __init__(self = None, path = None, rules = None):
        self.path = path.rstrip('/')
        self.rules = rules

    
    def get_rules(self = None, map = None):
        pass
    # WARNING: Decompyle incomplete



class EndpointPrefix(RuleFactory):
    """Prefixes all endpoints (which must be strings for this factory) with
    another string. This can be useful for sub applications::

        url_map = Map([
            Rule('/', endpoint='index'),
            EndpointPrefix('blog/', [Submount('/blog', [
                Rule('/', endpoint='index'),
                Rule('/entry/<entry_slug>', endpoint='show')
            ])])
        ])
    """
    
    def __init__(self = None, prefix = None, rules = None):
        self.prefix = prefix
        self.rules = rules

    
    def get_rules(self = None, map = None):
        pass
    # WARNING: Decompyle incomplete



class RuleTemplate:
    """Returns copies of the rules wrapped and expands string templates in
    the endpoint, rule, defaults or subdomain sections.

    Here a small example for such a rule template::

        from werkzeug.routing import Map, Rule, RuleTemplate

        resource = RuleTemplate([
            Rule('/$name/', endpoint='$name.list'),
            Rule('/$name/<int:id>', endpoint='$name.show')
        ])

        url_map = Map([resource(name='user'), resource(name='page')])

    When a rule template is called the keyword arguments are used to
    replace the placeholders in all the string parameters.
    """
    
    def __init__(self = None, rules = None):
        self.rules = list(rules)

    
    def __call__(self = None, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete



class RuleTemplateFactory(RuleFactory):
    '''A factory that fills in template variables into rules.  Used by
    `RuleTemplate` internally.

    :internal:
    '''
    
    def __init__(self = None, rules = None, context = None):
        self.rules = rules
        self.context = context

    
    def get_rules(self = None, map = None):
        pass
    # WARNING: Decompyle incomplete


_ASTT = t.TypeVar('_ASTT', bound = ast.AST)

def _prefix_names(src = None, expected_type = None):
    '''ast parse and prefix names with `.` to avoid collision with user vars'''
    tree = ast.parse(src).body[0]
    if isinstance(tree, ast.Expr):
        tree = tree.value
    if not isinstance(tree, expected_type):
        raise TypeError(f'''AST node is of type {type(tree).__name__}, not {expected_type.__name__}''')
    for node in ast.walk(tree):
        if isinstance(node, ast.Name):
            node.id = f'''.{node.id}'''
        return tree

_CALL_CONVERTER_CODE_FMT = 'self._converters[{elem!r}].to_url()'
_IF_KWARGS_URL_ENCODE_CODE = 'if kwargs:\n    params = self._encode_query_vars(kwargs)\n    q = "?" if params else ""\nelse:\n    q = params = ""\n'
_IF_KWARGS_URL_ENCODE_AST = _prefix_names(_IF_KWARGS_URL_ENCODE_CODE, ast.If)
_URL_ENCODE_AST_NAMES = (_prefix_names('q', ast.Name), _prefix_names('params', ast.Name))

class Rule(RuleFactory):
    """A Rule represents one URL pattern.  There are some options for `Rule`
    that change the way it behaves and are passed to the `Rule` constructor.
    Note that besides the rule-string all arguments *must* be keyword arguments
    in order to not break the application on Werkzeug upgrades.

    `string`
        Rule strings basically are just normal URL paths with placeholders in
        the format ``<converter(arguments):name>`` where the converter and the
        arguments are optional.  If no converter is defined the `default`
        converter is used which means `string` in the normal configuration.

        URL rules that end with a slash are branch URLs, others are leaves.
        If you have `strict_slashes` enabled (which is the default), all
        branch URLs that are matched without a trailing slash will trigger a
        redirect to the same URL with the missing slash appended.

        The converters are defined on the `Map`.

    `endpoint`
        The endpoint for this rule. This can be anything. A reference to a
        function, a string, a number etc.  The preferred way is using a string
        because the endpoint is used for URL generation.

    `defaults`
        An optional dict with defaults for other rules with the same endpoint.
        This is a bit tricky but useful if you want to have unique URLs::

            url_map = Map([
                Rule('/all/', defaults={'page': 1}, endpoint='all_entries'),
                Rule('/all/page/<int:page>', endpoint='all_entries')
            ])

        If a user now visits ``http://example.com/all/page/1`` they will be
        redirected to ``http://example.com/all/``.  If `redirect_defaults` is
        disabled on the `Map` instance this will only affect the URL
        generation.

    `subdomain`
        The subdomain rule string for this rule. If not specified the rule
        only matches for the `default_subdomain` of the map.  If the map is
        not bound to a subdomain this feature is disabled.

        Can be useful if you want to have user profiles on different subdomains
        and all subdomains are forwarded to your application::

            url_map = Map([
                Rule('/', subdomain='<username>', endpoint='user/homepage'),
                Rule('/stats', subdomain='<username>', endpoint='user/stats')
            ])

    `methods`
        A sequence of http methods this rule applies to.  If not specified, all
        methods are allowed. For example this can be useful if you want different
        endpoints for `POST` and `GET`.  If methods are defined and the path
        matches but the method matched against is not in this list or in the
        list of another rule for that path the error raised is of the type
        `MethodNotAllowed` rather than `NotFound`.  If `GET` is present in the
        list of methods and `HEAD` is not, `HEAD` is added automatically.

    `strict_slashes`
        Override the `Map` setting for `strict_slashes` only for this rule. If
        not specified the `Map` setting is used.

    `merge_slashes`
        Override :attr:`Map.merge_slashes` for this rule.

    `build_only`
        Set this to True and the rule will never match but will create a URL
        that can be build. This is useful if you have resources on a subdomain
        or folder that are not handled by the WSGI application (like static data)

    `redirect_to`
        If given this must be either a string or callable.  In case of a
        callable it's called with the url adapter that triggered the match and
        the values of the URL as keyword arguments and has to return the target
        for the redirect, otherwise it has to be a string with placeholders in
        rule syntax::

            def foo_with_slug(adapter, id):
                # ask the database for the slug for the old id.  this of
                # course has nothing to do with werkzeug.
                return f'foo/{Foo.get_slug_for_id(id)}'

            url_map = Map([
                Rule('/foo/<slug>', endpoint='foo'),
                Rule('/some/old/url/<slug>', redirect_to='foo/<slug>'),
                Rule('/other/old/url/<int:id>', redirect_to=foo_with_slug)
            ])

        When the rule is matched the routing system will raise a
        `RequestRedirect` exception with the target for the redirect.

        Keep in mind that the URL will be joined against the URL root of the
        script so don't use a leading slash on the target URL unless you
        really mean root of that domain.

    `alias`
        If enabled this rule serves as an alias for another rule with the same
        endpoint and arguments.

    `host`
        If provided and the URL map has host matching enabled this can be
        used to provide a match rule for the whole host.  This also means
        that the subdomain feature is disabled.

    `websocket`
        If ``True``, this rule is only matches for WebSocket (``ws://``,
        ``wss://``) requests. By default, rules will only match for HTTP
        requests.

    .. versionchanged:: 2.1
        Percent-encoded newlines (``%0a``), which are decoded by WSGI
        servers, are considered when routing instead of terminating the
        match early.

    .. versionadded:: 1.0
        Added ``websocket``.

    .. versionadded:: 1.0
        Added ``merge_slashes``.

    .. versionadded:: 0.7
        Added ``alias`` and ``host``.

    .. versionchanged:: 0.6.1
       ``HEAD`` is added to ``methods`` if ``GET`` is present.
    """
    
    def __init__(self, string, defaults, subdomain, methods, build_only, endpoint, strict_slashes, merge_slashes = None, redirect_to = None, alias = None, host = (None, None, None, False, None, None, None, None, False, None, False), websocket = ('string', 'str', 'defaults', 't.Mapping[str, t.Any] | None', 'subdomain', 'str | None', 'methods', 't.Iterable[str] | None', 'build_only', 'bool', 'endpoint', 't.Any | None', 'strict_slashes', 'bool | None', 'merge_slashes', 'bool | None', 'redirect_to', 'str | t.Callable[..., str] | None', 'alias', 'bool', 'host', 'str | None', 'websocket', 'bool', 'return', 'None')):
        if not string.startswith('/'):
            raise ValueError(f'''URL rule \'{string}\' must start with a slash.''')
        self.rule = string
        self.is_leaf = not string.endswith('/')
        self.is_branch = string.endswith('/')
        self.map = None
        self.strict_slashes = strict_slashes
        self.merge_slashes = merge_slashes
        self.subdomain = subdomain
        self.host = host
        self.defaults = defaults
        self.build_only = build_only
        self.alias = alias
        self.websocket = websocket
    # WARNING: Decompyle incomplete

    
    def empty(self = None):
        '''
        Return an unbound copy of this rule.

        This can be useful if want to reuse an already bound URL for another
        map.  See ``get_empty_kwargs`` to override what keyword arguments are
        provided to the new copy.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def get_empty_kwargs(self = None):
        '''
        Provides kwargs for instantiating empty copy with empty()

        Use this method to provide custom keyword arguments to the subclass of
        ``Rule`` when calling ``some_rule.empty()``.  Helpful when the subclass
        has custom keyword arguments that are needed at instantiation.

        Must return a ``dict`` that will be provided as kwargs to the new
        instance of ``Rule``, following the initial ``self.rule`` value which
        is always provided as the first, required positional argument.
        '''
        defaults = None
        if self.defaults:
            defaults = dict(self.defaults)
        return dict(defaults = defaults, subdomain = self.subdomain, methods = self.methods, build_only = self.build_only, endpoint = self.endpoint, strict_slashes = self.strict_slashes, redirect_to = self.redirect_to, alias = self.alias, host = self.host)

    
    def get_rules(self = None, map = None):
        pass
    # WARNING: Decompyle incomplete

    
    def refresh(self = None):
        '''Rebinds and refreshes the URL.  Call this if you modified the
        rule in place.

        :internal:
        '''
        self.bind(self.map, rebind = True)

    
    def bind(self = None, map = None, rebind = None):
        '''Bind the url to a map and create a regular expression based on
        the information from the rule itself and the defaults from the map.

        :internal:
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def get_converter(self, variable_name = None, converter_name = None, args = None, kwargs = ('variable_name', 'str', 'converter_name', 'str', 'args', 'tuple[t.Any, ...]', 'kwargs', 't.Mapping[str, t.Any]', 'return', 'BaseConverter')):
        '''Looks up the converter for the given parameter.

        .. versionadded:: 0.9
        '''
        if converter_name not in self.map.converters:
            raise LookupError(f'''the converter {converter_name!r} does not exist''')
    # WARNING: Decompyle incomplete

    
    def _encode_query_vars(self = None, query_vars = None):
        items = iter_multi_items(query_vars)
        if self.map.sort_parameters:
            items = sorted(items, key = self.map.sort_key)
        return _urlencode(items)

    
    def _parse_rule(self = None, rule = None):
        pass
    # WARNING: Decompyle incomplete

    
    def compile(self = None):
        '''Compiles the regular expression and stores it.'''
        pass
    # WARNING: Decompyle incomplete

    _get_func_code = (lambda code = None, name = None: globs = { }locs = { }exec(code, globs, locs)locs[name])()
    
    def _compile_builder(self = None, append_unknown = None):
        pass
    # WARNING: Decompyle incomplete

    
    def build(self = None, values = None, append_unknown = None):
        """Assembles the relative url for that rule and the subdomain.
        If building doesn't work for some reasons `None` is returned.

        :internal:
        """
        pass
    # WARNING: Decompyle incomplete

    
    def provides_defaults_for(self = None, rule = None):

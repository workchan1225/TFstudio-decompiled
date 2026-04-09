# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: map.pyc (Python 3.11)

from __future__ import annotations
import typing as t
import warnings
from pprint import pformat
from threading import Lock
from urllib.parse import quote
from urllib.parse import urljoin
from urllib.parse import urlunsplit
from _internal import _get_environ
from _internal import _wsgi_decoding_dance
from datastructures import ImmutableDict
from datastructures import MultiDict
from exceptions import BadHost
from exceptions import HTTPException
from exceptions import MethodNotAllowed
from exceptions import NotFound
from urls import _urlencode
from wsgi import get_host
from converters import DEFAULT_CONVERTERS
from exceptions import BuildError
from exceptions import NoMatch
from exceptions import RequestAliasRedirect
from exceptions import RequestPath
from exceptions import RequestRedirect
from exceptions import WebsocketMismatch
from matcher import StateMachineMatcher
from rules import _simple_rule_re
from rules import Rule
if t.TYPE_CHECKING:
    from _typeshed.wsgi import WSGIApplication
    from _typeshed.wsgi import WSGIEnvironment
    from wrappers.request import Request
    from converters import BaseConverter
    from rules import RuleFactory

class Map:
    """The map class stores all the URL rules and some configuration
    parameters.  Some of the configuration values are only stored on the
    `Map` instance since those affect all rules, others are just defaults
    and can be overridden for each rule.  Note that you have to specify all
    arguments besides the `rules` as keyword arguments!

    :param rules: sequence of url rules for this map.
    :param default_subdomain: The default subdomain for rules without a
                              subdomain defined.
    :param strict_slashes: If a rule ends with a slash but the matched
        URL does not, redirect to the URL with a trailing slash.
    :param merge_slashes: Merge consecutive slashes when matching or
        building URLs. Matches will redirect to the normalized URL.
        Slashes in variable parts are not merged.
    :param redirect_defaults: This will redirect to the default rule if it
                              wasn't visited that way. This helps creating
                              unique URLs.
    :param converters: A dict of converters that adds additional converters
                       to the list of converters. If you redefine one
                       converter this will override the original one.
    :param sort_parameters: If set to `True` the url parameters are sorted.
                            See `url_encode` for more details.
    :param sort_key: The sort key function for `url_encode`.
    :param host_matching: if set to `True` it enables the host matching
                          feature and disables the subdomain one.  If
                          enabled the `host` parameter to rules is used
                          instead of the `subdomain` one.

    .. versionchanged:: 3.0
        The ``charset`` and ``encoding_errors`` parameters were removed.

    .. versionchanged:: 1.0
        If ``url_scheme`` is ``ws`` or ``wss``, only WebSocket rules will match.

    .. versionchanged:: 1.0
        The ``merge_slashes`` parameter was added.

    .. versionchanged:: 0.7
        The ``encoding_errors`` and ``host_matching`` parameters were added.

    .. versionchanged:: 0.5
        The ``sort_parameters`` and ``sort_key``  paramters were added.
    """
    default_converters = ImmutableDict(DEFAULT_CONVERTERS)
    lock_class = Lock
    
    def __init__(self, rules, default_subdomain, strict_slashes, merge_slashes, redirect_defaults = None, converters = None, sort_parameters = None, sort_key = (None, '', True, True, True, None, False, None, False), host_matching = ('rules', 't.Iterable[RuleFactory] | None', 'default_subdomain', 'str', 'strict_slashes', 'bool', 'merge_slashes', 'bool', 'redirect_defaults', 'bool', 'converters', 't.Mapping[str, type[BaseConverter]] | None', 'sort_parameters', 'bool', 'sort_key', 't.Callable[[t.Any], t.Any] | None', 'host_matching', 'bool', 'return', 'None')):
        self._matcher = StateMachineMatcher(merge_slashes)
        self._rules_by_endpoint = { }
        self._remap = True
        self._remap_lock = self.lock_class()
        self.default_subdomain = default_subdomain
        self.strict_slashes = strict_slashes
        self.redirect_defaults = redirect_defaults
        self.host_matching = host_matching
        self.converters = self.default_converters.copy()
        if converters:
            self.converters.update(converters)
        self.sort_parameters = sort_parameters
        self.sort_key = sort_key
        if not rules:
            for rulefactory in ():
                self.add(rulefactory)
                return None

    merge_slashes = (lambda self = None: self._matcher.merge_slashes)()
    merge_slashes = (lambda self = None, value = None: self._matcher.merge_slashes = value)()
    
    def is_endpoint_expecting(self = None, endpoint = None, *arguments):
        '''Iterate over all rules and check if the endpoint expects
        the arguments provided.  This is for example useful if you have
        some URLs that expect a language code and others that do not and
        you want to wrap the builder a bit so that the current language
        code is automatically added if not provided but endpoints expect
        it.

        :param endpoint: the endpoint to check.
        :param arguments: this function accepts one or more arguments
                          as positional arguments.  Each one of them is
                          checked.
        '''
        self.update()
        arguments_set = set(arguments)
        for rule in self._rules_by_endpoint[endpoint]:
            if arguments_set.issubset(rule.arguments):
                return True
            return False

    _rules = (lambda self = None: self._rules_by_endpoint.values()())()
    
    def iter_rules(self = None, endpoint = None):
        '''Iterate over all rules or the rules of an endpoint.

        :param endpoint: if provided only the rules for that endpoint
                         are returned.
        :return: an iterator
        '''
        self.update()
    # WARNING: Decompyle incomplete

    
    def add(self = None, rulefactory = None):
        '''Add a new rule or factory to the map and bind it.  Requires that the
        rule is not bound to another map.

        :param rulefactory: a :class:`Rule` or :class:`RuleFactory`
        '''
        for rule in rulefactory.get_rules(self):
            rule.bind(self)
            if not rule.build_only:
                self._matcher.add(rule)
            self._rules_by_endpoint.setdefault(rule.endpoint, []).append(rule)
            self._remap = True
            return None

    
    def bind(self, server_name, script_name, subdomain = None, url_scheme = None, default_method = None, path_info = (None, None, 'http', 'GET', None, None), query_args = ('server_name', 'str', 'script_name', 'str | None', 'subdomain', 'str | None', 'url_scheme', 'str', 'default_method', 'str', 'path_info', 'str | None', 'query_args', 't.Mapping[str, t.Any] | str | None', 'return', 'MapAdapter')):
        """Return a new :class:`MapAdapter` with the details specified to the
        call.  Note that `script_name` will default to ``'/'`` if not further
        specified or `None`.  The `server_name` at least is a requirement
        because the HTTP RFC requires absolute URLs for redirects and so all
        redirect exceptions raised by Werkzeug will contain the full canonical
        URL.

        If no path_info is passed to :meth:`match` it will use the default path
        info passed to bind.  While this doesn't really make sense for
        manual bind calls, it's useful if you bind a map to a WSGI
        environment which already contains the path info.

        `subdomain` will default to the `default_subdomain` for this map if
        no defined. If there is no `default_subdomain` you cannot use the
        subdomain feature.

        .. versionchanged:: 1.0
            If ``url_scheme`` is ``ws`` or ``wss``, only WebSocket rules
            will match.

        .. versionchanged:: 0.15
            ``path_info`` defaults to ``'/'`` if ``None``.

        .. versionchanged:: 0.8
            ``query_args`` can be a string.

        .. versionchanged:: 0.7
            Added ``query_args``.
        """
        server_name = server_name.lower()
    # WARNING: Decompyle incomplete

    
    def bind_to_environ(self = None, environ = None, server_name = None, subdomain = (None, None)):
        """Like :meth:`bind` but you can pass it an WSGI environment and it
        will fetch the information from that dictionary.  Note that because of
        limitations in the protocol there is no way to get the current
        subdomain and real `server_name` from the environment.  If you don't
        provide it, Werkzeug will use `SERVER_NAME` and `SERVER_PORT` (or
        `HTTP_HOST` if provided) as used `server_name` with disabled subdomain
        feature.

        If `subdomain` is `None` but an environment and a server name is
        provided it will calculate the current subdomain automatically.
        Example: `server_name` is ``'example.com'`` and the `SERVER_NAME`
        in the wsgi `environ` is ``'staging.dev.example.com'`` the calculated
        subdomain will be ``'staging.dev'``.

        If the object passed as environ has an environ attribute, the value of
        this attribute is used instead.  This allows you to pass request
        objects.  Additionally `PATH_INFO` added as a default of the
        :class:`MapAdapter` so that you don't have to pass the path info to
        the match method.

        .. versionchanged:: 1.0.0
            If the passed server name specifies port 443, it will match
            if the incoming scheme is ``https`` without a port.

        .. versionchanged:: 1.0.0
            A warning is shown when the passed server name does not
            match the incoming WSGI server name.

        .. versionchanged:: 0.8
           This will no longer raise a ValueError when an unexpected server
           name was passed.

        .. versionchanged:: 0.5
            previously this method accepted a bogus `calculate_subdomain`
            parameter that did not have any effect.  It was removed because
            of that.

        :param environ: a WSGI environment.
        :param server_name: an optional server name hint (see above).
        :param subdomain: optionally the current subdomain (see above).
        """
        pass
    # WARNING: Decompyle incomplete

    
    def update(self = None):
        '''Called before matching and building to keep the compiled rules
        in the correct order after things changed.
        '''
        if not self._remap:
            return None
        None._remap_lock
        if not self._remap:
            None(None, None)
            return None
        None._matcher.update()
        for rules in self._rules_by_endpoint.values():
            rules.sort(key = (lambda x: x.build_compare_key()))
            self._remap = False
            None(None, None)
            return None
            with None:
                if not None:
                    pass

    
    def __repr__(self = None):
        rules = self.iter_rules()
        return f'''{type(self).__name__}({pformat(list(rules))})'''



class MapAdapter:
    '''Returned by :meth:`Map.bind` or :meth:`Map.bind_to_environ` and does
    the URL matching and building based on runtime information.
    '''
    
    def __init__(self, map, server_name, script_name, subdomain = None, url_scheme = None, path_info = None, default_method = (None,), query_args = ('map', 'Map', 'server_name', 'str', 'script_name', 'str', 'subdomain', 'str | None', 'url_scheme', 'str', 'path_info', 'str', 'default_method', 'str', 'query_args', 't.Mapping[str, t.Any] | str | None')):
        self.map = map
        self.server_name = server_name
        if not script_name.endswith('/'):
            script_name += '/'
        self.script_name = script_name
        self.subdomain = subdomain
        self.url_scheme = url_scheme
        self.path_info = path_info
        self.default_method = default_method
        self.query_args = query_args
        self.websocket = self.url_scheme in frozenset({'ws', 'wss'})

    
    def dispatch(self = None, view_func = None, path_info = None, method = (None, None, False), catch_http_exceptions = ('view_func', 't.Callable[[str, t.Mapping[str, t.Any]], WSGIApplication]', 'path_info', 'str | None', 'method', 'str | None', 'catch_http_exceptions', 'bool', 'return', 'WSGIApplication')):
        """Does the complete dispatching process.  `view_func` is called with
        the endpoint and a dict with the values for the view.  It should
        look up the view function, call it, and return a response object
        or WSGI application.  http exceptions are not caught by default
        so that applications can display nicer error messages by just
        catching them by hand.  If you want to stick with the default
        error messages you can pass it ``catch_http_exceptions=True`` and
        it will catch the http exceptions.

        Here a small example for the dispatch usage::

            from werkzeug.wrappers import Request, Response
            from werkzeug.wsgi import responder
            from werkzeug.routing import Map, Rule

            def on_index(request):
                return Response('Hello from the index')

            url_map = Map([Rule('/', endpoint='index')])
            views = {'index': on_index}

            @responder
            def application(environ, start_response):
                request = Request(environ)
                urls = url_map.bind_to_environ(environ)
                return urls.dispatch(lambda e, v: views[e](request, **v),
                                     catch_http_exceptions=True)

        Keep in mind that this method might return exception objects, too, so
        use :class:`Response.force_type` to get a response object.

        :param view_func: a function that is called with the endpoint as
                          first argument and the value dict as second.  Has
                          to dispatch to the actual view function with this
                          information.  (see above)
        :param path_info: the path info to use for matching.  Overrides the
                          path info specified on binding.
        :param method: the HTTP method used for matching.  Overrides the
                       method specified on binding.
        :param catch_http_exceptions: set to `True` to catch any of the
                                      werkzeug :class:`HTTPException`\\s.
        """
        
        try:
            (endpoint, args) = self.match(path_info, method)
            
            try:
                pass
            except RequestRedirect:
                e = None
                
                try:
                    del e
                    return None
                    None = 
                    del e
                    
                    try:
                        return view_func(endpoint, args)
                    except HTTPException:
                        e = None
                        if catch_http_exceptions:
                            del e
                            return None
                        None = None
                        del e





    match = (lambda self, path_info = None, method = None, return_rule = t.overload, query_args = (None, None, False, None, None), websocket = ('path_info', 'str | None', 'method', 'str | None', 'return_rule', 't.Literal[False]', 'query_args', 't.Mapping[str, t.Any] | str | None', 'websocket', 'bool | None', 'return', 'tuple[t.Any, t.Mapping[str, t.Any]]'): pass)()
    match = (lambda self, path_info = None, method = None, return_rule = t.overload, query_args = (None, None, True, None, None), websocket = ('path_info', 'str | None', 'method', 'str | None', 'return_rule', 't.Literal[True]', 'query_args', 't.Mapping[str, t.Any] | str | None', 'websocket', 'bool | None', 'return', 'tuple[Rule, t.Mapping[str, t.Any]]'): pass)()
    
    def match(self, path_info = None, method = None, return_rule = None, query_args = (None, None, False, None, None), websocket = ('path_info', 'str | None', 'method', 'str | None', 'return_rule', 'bool', 'query_args', 't.Mapping[str, t.Any] | str | None', 'websocket', 'bool | None', 'return', 'tuple[t.Any | Rule, t.Mapping[str, t.Any]]')):
        '''The usage is simple: you just pass the match method the current
        path info as well as the method (which defaults to `GET`).  The
        following things can then happen:

        - you receive a `NotFound` exception that indicates that no URL is
          matching.  A `NotFound` exception is also a WSGI application you
          can call to get a default page not found page (happens to be the
          same object as `werkzeug.exceptions.NotFound`)

        - you receive a `MethodNotAllowed` exception that indicates that there
          is a match for this URL but not for the current request method.
          This is useful for RESTful applications.

        - you receive a `RequestRedirect` exception with a `new_url`
          attribute.  This exception is used to notify you about a request
          Werkzeug requests from your WSGI application.  This is for example the
          case if you request ``/foo`` although the correct URL is ``/foo/``
          You can use the `RequestRedirect` instance as response-like object
          similar to all other subclasses of `HTTPException`.

        - you receive a ``WebsocketMismatch`` exception if the only
          match is a WebSocket rule but the bind is an HTTP request, or
          if the match is an HTTP rule but the bind is a WebSocket
          request.

        - you get a tuple in the form ``(endpoint, arguments)`` if there is
          a match (unless `return_rule` is True, in which case you get a tuple
          in the form ``(rule, arguments)``)

        If the path info is not passed to the match method the default path
        info of the map is used (defaults to the root URL if not defined
        explicitly).

        All of the exceptions raised are subclasses of `HTTPException` so they
        can be used as WSGI responses. They will all render generic error or
        redirect pages.

        Here is a small example for matching:

        >>> m = Map([
        ...     Rule(\'/\', endpoint=\'index\'),
        ...     Rule(\'/downloads/\', endpoint=\'downloads/index\'),
        ...     Rule(\'/downloads/<int:id>\', endpoint=\'downloads/show\')
        ... ])
        >>> urls = m.bind("example.com", "/")
        >>> urls.match("/", "GET")
        (\'index\', {})
        >>> urls.match("/downloads/42")
        (\'downloads/show\', {\'id\': 42})

        And here is what happens on redirect and missing URLs:

        >>> urls.match("/downloads")
        Traceback (most recent call last):
          ...
        RequestRedirect: http://example.com/downloads/
        >>> urls.match("/missing")
        Traceback (most recent call last):
          ...
        NotFound: 404 Not Found

        :param path_info: the path info to use for matching.  Overrides the
                          path info specified on binding.
        :param method: the HTTP method used for matching.  Overrides the
                       method specified on binding.
        :param return_rule: return the rule that matched instead of just the
                            endpoint (defaults to `False`).
        :param query_args: optional query arguments that are used for
                           automatic redirects as string or dictionary.  It\'s
                           currently not possible to use the query arguments
                           for URL matching.
        :param websocket: Match WebSocket instead of HTTP requests. A
            websocket request has a ``ws`` or ``wss``
            :attr:`url_scheme`. This overrides that detection.

        .. versionadded:: 1.0
            Added ``websocket``.

        .. versionchanged:: 0.8
            ``query_args`` can be a string.

        .. versionadded:: 0.7
            Added ``query_args``.

        .. versionadded:: 0.6
            Added ``return_rule``.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def test(self = None, path_info = None, method = None):
        '''Test if a rule would match.  Works like `match` but returns `True`
        if the URL matches, or `False` if it does not exist.

        :param path_info: the path info to use for matching.  Overrides the
                          path info specified on binding.
        :param method: the HTTP method used for matching.  Overrides the
                       method specified on binding.
        '''
        
        try:
            self.match(path_info, method)
        except RequestRedirect:
            pass
        except HTTPException:
            return False

        return True

    
    def allowed_methods(self = None, path_info = None):
        '''Returns the valid methods that match for a given path.

        .. versionadded:: 0.7
        '''
        
        try:
            self.match(path_info, method = '--')
        except MethodNotAllowed:
            e = None
            del e
            return None
            None = 
            del e
            except HTTPException:
                pass
            return []


    
    def get_host(self = None, domain_part = None):
        '''Figures out the full host name for the given domain part.  The
        domain part is a subdomain in case host matching is disabled or
        a full host name.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def get_default_redirect(self, rule = None, method = None, values = None, query_args = ('rule', 'Rule', 'method', 'str', 'values', 't.MutableMapping[str, t.Any]', 'query_args', 't.Mapping[str, t.Any] | str', 'return', 'str | None')):
        '''A helper that returns the URL to redirect to if it finds one.
        This is used for default redirecting only.

        :internal:
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def encode_query_args(self = None, query_args = None):
        if not isinstance(query_args, str):
            return _urlencode(query_args)

    
    def make_redirect_url(self = None, path_info = None, query_args = None, domain_part = (None, None)):
        '''Creates a redirect URL.

        :internal:
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def make_alias_redirect_url(self, path, endpoint = None, values = None, method = None, query_args = ('path', 'str', 'endpoint', 't.Any', 'values', 't.Mapping[str, t.Any]', 'method', 'str', 'query_args', 't.Mapping[str, t.Any] | str', 'return', 'str')):
        '''Internally called to make an alias redirect URL.'''
        url = self.build(endpoint, values, method, append_unknown = False, force_external = True)
        if query_args:
            url += f'''?{self.encode_query_args(query_args)}'''
    # WARNING: Decompyle incomplete

    
    def _partial_build(self, endpoint = None, values = None, method = None, append_unknown = ('endpoint', 't.Any', 'values', 't.Mapping[str, t.Any]', 'method', 'str | None', 'append_unknown', 'bool', 'return', 'tuple[str, str, bool] | None')):
        '''Helper for :meth:`build`.  Returns subdomain and path for the
        rule that accepts this endpoint, values and method.

        :internal:
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def build(self, endpoint, values = None, method = None, force_external = None, append_unknown = (None, None, False, True, None), url_scheme = ('endpoint', 't.Any', 'values', 't.Mapping[str, t.Any] | None', 'method', 'str | None', 'force_external', 'bool', 'append_unknown', 'bool', 'url_scheme', 'str | None', 'return', 'str')):
        '''Building URLs works pretty much the other way round.  Instead of
        `match` you call `build` and pass it the endpoint and a dict of
        arguments for the placeholders.

        The `build` function also accepts an argument called `force_external`
        which, if you set it to `True` will force external URLs. Per default
        external URLs (include the server name) will only be used if the
        target URL is on a different subdomain.

        >>> m = Map([
        ...     Rule(\'/\', endpoint=\'index\'),
        ...     Rule(\'/downloads/\', endpoint=\'downloads/index\'),
        ...     Rule(\'/downloads/<int:id>\', endpoint=\'downloads/show\')
        ... ])
        >>> urls = m.bind("example.com", "/")
        >>> urls.build("index", {})
        \'/\'
        >>> urls.build("downloads/show", {\'id\': 42})
        \'/downloads/42\'
        >>> urls.build("downloads/show", {\'id\': 42}, force_external=True)
        \'http://example.com/downloads/42\'

        Because URLs cannot contain non ASCII data you will always get
        bytes back.  Non ASCII characters are urlencoded with the
        charset defined on the map instance.

        Additional values are converted to strings and appended to the URL as
        URL querystring parameters:

        >>> urls.build("index", {\'q\': \'My Searchstring\'})
        \'/?q=My+Searchstring\'

        When processing those additional values, lists are furthermore
        interpreted as multiple values (as per
        :py:class:`werkzeug.datastructures.MultiDict`):

        >>> urls.build("index", {\'q\': [\'a\', \'b\', \'c\']})
        \'/?q=a&q=b&q=c\'

        Passing a ``MultiDict`` will also add multiple values:

        >>> urls.build("index", MultiDict(((\'p\', \'z\'), (\'q\', \'a\'), (\'q\', \'b\'))))
        \'/?p=z&q=a&q=b\'

        If a rule does not exist when building a `BuildError` exception is
        raised.

        The build method accepts an argument called `method` which allows you
        to specify the method you want to have an URL built for if you have
        different methods for the same endpoint specified.

        :param endpoint: the endpoint of the URL to build.
        :param values: the values for the URL to build.  Unhandled values are
                       appended to the URL as query parameters.
        :param method: the HTTP method for the rule if there are different
                       URLs for different methods on the same endpoint.
        :param force_external: enforce full canonical external URLs. If the URL
                               scheme is not provided, this will generate
                               a protocol-relative URL.
        :param append_unknown: unknown parameters are appended to the generated
                               URL as query string argument.  Disable this
                               if you want the builder to ignore those.
        :param url_scheme: Scheme to use in place of the bound
            :attr:`url_scheme`.

        .. versionchanged:: 2.0
            Added the ``url_scheme`` parameter.

        .. versionadded:: 0.6
           Added the ``append_unknown`` parameter.
        '''
        self.map.update()
        rv = self._partial_build(endpoint, values, method, append_unknown)
    # WARNING: Decompyle incomplete

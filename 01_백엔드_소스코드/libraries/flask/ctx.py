# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ctx.pyc (Python 3.11)

from __future__ import annotations
import contextvars
import sys
import typing as t
from functools import update_wrapper
from types import TracebackType
from werkzeug.exceptions import HTTPException
from  import typing as ft
from globals import _cv_app
from globals import _cv_request
from signals import appcontext_popped
from signals import appcontext_pushed
if t.TYPE_CHECKING:
    from app import Flask
    from sessions import SessionMixin
    from wrappers import Request
_sentinel = object()

class _AppCtxGlobals:
    """A plain object. Used as a namespace for storing data during an
    application context.

    Creating an app context automatically creates this object, which is
    made available as the :data:`g` proxy.

    .. describe:: 'key' in g

        Check whether an attribute is present.

        .. versionadded:: 0.10

    .. describe:: iter(g)

        Return an iterator over the attribute names.

        .. versionadded:: 0.10
    """
    
    def __getattr__(self = None, name = None):
        
        try:
            return self.__dict__[name]
        except KeyError:
            raise AttributeError(name), None


    
    def __setattr__(self = None, name = None, value = None):
        self.__dict__[name] = value

    
    def __delattr__(self = None, name = None):
        
        try:
            del self.__dict__[name]
            return None
        except KeyError:
            raise AttributeError(name), None


    
    def get(self = None, name = None, default = None):
        '''Get an attribute by name, or a default value. Like
        :meth:`dict.get`.

        :param name: Name of attribute to get.
        :param default: Value to return if the attribute is not present.

        .. versionadded:: 0.10
        '''
        return self.__dict__.get(name, default)

    
    def pop(self = None, name = None, default = None):
        '''Get and remove an attribute by name. Like :meth:`dict.pop`.

        :param name: Name of attribute to pop.
        :param default: Value to return if the attribute is not present,
            instead of raising a ``KeyError``.

        .. versionadded:: 0.11
        '''
        if default is _sentinel:
            return self.__dict__.pop(name)
        return None.__dict__.pop(name, default)

    
    def setdefault(self = None, name = None, default = None):
        '''Get the value of an attribute if it is present, otherwise
        set and return a default value. Like :meth:`dict.setdefault`.

        :param name: Name of attribute to get.
        :param default: Value to set and return if the attribute is not
            present.

        .. versionadded:: 0.11
        '''
        return self.__dict__.setdefault(name, default)

    
    def __contains__(self = None, item = None):
        return item in self.__dict__

    
    def __iter__(self = None):
        return iter(self.__dict__)

    
    def __repr__(self = None):
        ctx = _cv_app.get(None)
    # WARNING: Decompyle incomplete



def after_this_request(f = None):
    """Executes a function after this request.  This is useful to modify
    response objects.  The function is passed the response object and has
    to return the same or a new one.

    Example::

        @app.route('/')
        def index():
            @after_this_request
            def add_header(response):
                response.headers['X-Foo'] = 'Parachute'
                return response
            return 'Hello World!'

    This is more useful if a function other than the view function wants to
    modify a response.  For instance think of a decorator that wants to add
    some headers without converting the return value into a response object.

    .. versionadded:: 0.9
    """
    ctx = _cv_request.get(None)
# WARNING: Decompyle incomplete


def copy_current_request_context(f = None):
    """A helper function that decorates a function to retain the current
    request context.  This is useful when working with greenlets.  The moment
    the function is decorated a copy of the request context is created and
    then pushed when the function is called.  The current session is also
    included in the copied request context.

    Example::

        import gevent
        from flask import copy_current_request_context

        @app.route('/')
        def index():
            @copy_current_request_context
            def do_some_work():
                # do some work here, it can access flask.request or
                # flask.session like you would otherwise in the view function.
                ...
            gevent.spawn(do_some_work)
            return 'Regular response'

    .. versionadded:: 0.10
    """
    pass
# WARNING: Decompyle incomplete


def has_request_context():
    '''If you have code that wants to test if a request context is there or
    not this function can be used.  For instance, you may want to take advantage
    of request information if the request object is available, but fail
    silently if it is unavailable.

    ::

        class User(db.Model):

            def __init__(self, username, remote_addr=None):
                self.username = username
                if remote_addr is None and has_request_context():
                    remote_addr = request.remote_addr
                self.remote_addr = remote_addr

    Alternatively you can also just test any of the context bound objects
    (such as :class:`request` or :class:`g`) for truthness::

        class User(db.Model):

            def __init__(self, username, remote_addr=None):
                self.username = username
                if remote_addr is None and request:
                    remote_addr = request.remote_addr
                self.remote_addr = remote_addr

    .. versionadded:: 0.7
    '''
    return _cv_request.get(None) is not None


def has_app_context():
    '''Works like :func:`has_request_context` but for the application
    context.  You can also just do a boolean check on the
    :data:`current_app` object instead.

    .. versionadded:: 0.9
    '''
    return _cv_app.get(None) is not None


class AppContext:
    '''The app context contains application-specific information. An app
    context is created and pushed at the beginning of each request if
    one is not already active. An app context is also pushed when
    running CLI commands.
    '''
    
    def __init__(self = None, app = None):
        self.app = app
        self.url_adapter = app.create_url_adapter(None)
        self.g = app.app_ctx_globals_class()
        self._cv_tokens = []

    
    def push(self = None):
        '''Binds the app context to the current context.'''
        self._cv_tokens.append(_cv_app.set(self))
        appcontext_pushed.send(self.app, _async_wrapper = self.app.ensure_sync)

    
    def pop(self = None, exc = None):
        '''Pops the app context.'''
        
        try:
            if len(self._cv_tokens) == 1:
                if exc is _sentinel:
                    exc = sys.exc_info()[1]
                self.app.do_teardown_appcontext(exc)
            ctx = _cv_app.get()
            _cv_app.reset(self._cv_tokens.pop())
        except:
            ctx = _cv_app.get()
            _cv_app.reset(self._cv_tokens.pop())

        if ctx is not self:
            raise AssertionError(f'''Popped wrong app context. ({ctx!r} instead of {self!r})''')
        appcontext_popped.send(self.app, _async_wrapper = self.app.ensure_sync)

    
    def __enter__(self = None):
        self.push()
        return self

    
    def __exit__(self = None, exc_type = None, exc_value = None, tb = ('exc_type', 'type | None', 'exc_value', 'BaseException | None', 'tb', 'TracebackType | None', 'return', 'None')):
        self.pop(exc_value)



class RequestContext:
    '''The request context contains per-request information. The Flask
    app creates and pushes it at the beginning of the request, then pops
    it at the end of the request. It will create the URL adapter and
    request object for the WSGI environment provided.

    Do not attempt to use this class directly, instead use
    :meth:`~flask.Flask.test_request_context` and
    :meth:`~flask.Flask.request_context` to create this object.

    When the request context is popped, it will evaluate all the
    functions registered on the application for teardown execution
    (:meth:`~flask.Flask.teardown_request`).

    The request context is automatically popped at the end of the
    request. When using the interactive debugger, the context will be
    restored so ``request`` is still accessible. Similarly, the test
    client can preserve the context after the request ends. However,
    teardown functions may already have closed some resources such as
    database connections.
    '''
    
    def __init__(self = None, app = None, environ = None, request = (None, None), session = ('app', 'Flask', 'environ', 'dict', 'request', 'Request | None', 'session', 'SessionMixin | None', 'return', 'None')):
        self.app = app
    # WARNING: Decompyle incomplete

    
    def copy(self = None):
        '''Creates a copy of this request context with the same request object.
        This can be used to move a request context to a different greenlet.
        Because the actual request object is the same this cannot be used to
        move a request context to a different thread unless access to the
        request object is locked.

        .. versionadded:: 0.10

        .. versionchanged:: 1.1
           The current session object is used instead of reloading the original
           data. This prevents `flask.session` pointing to an out-of-date object.
        '''
        return self.__class__(self.app, environ = self.request.environ, request = self.request, session = self.session)

    
    def match_request(self = None):
        '''Can be overridden by a subclass to hook into the matching
        of the request.
        '''
        
        try:
            result = self.url_adapter.match(return_rule = True)
            (self.request.url_rule, self.request.view_args) = result
            return None
        except HTTPException:
            e = None
            self.request.routing_exception = e
            e = None
            del e
            return None
            e = None
            del e


    
    def push(self = None):
        app_ctx = _cv_app.get(None)
    # WARNING: Decompyle incomplete

    
    def pop(self = None, exc = None):
        '''Pops the request context and unbinds it by doing that.  This will
        also trigger the execution of functions registered by the
        :meth:`~flask.Flask.teardown_request` decorator.

        .. versionchanged:: 0.9
           Added the `exc` argument.
        '''
        clear_request = len(self._cv_tokens) == 1
    # WARNING: Decompyle incomplete

    
    def __enter__(self = None):
        self.push()
        return self

    
    def __exit__(self = None, exc_type = None, exc_value = None, tb = ('exc_type', 'type | None', 'exc_value', 'BaseException | None', 'tb', 'TracebackType | None', 'return', 'None')):
        self.pop(exc_value)

    
    def __repr__(self = None):
        return f'''<{type(self).__name__} {self.request.url!r} [{self.request.method}] of {self.app.name}>'''

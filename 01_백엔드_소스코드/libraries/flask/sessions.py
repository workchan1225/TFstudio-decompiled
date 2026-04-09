# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: sessions.pyc (Python 3.11)

from __future__ import annotations
import hashlib
import typing as t
from collections.abc import MutableMapping
from datetime import datetime
from datetime import timezone
from itsdangerous import BadSignature
from itsdangerous import URLSafeTimedSerializer
from werkzeug.datastructures import CallbackDict
from json.tag import TaggedJSONSerializer
if t.TYPE_CHECKING:
    from app import Flask
    from wrappers import Request, Response

class SessionMixin(MutableMapping):
    '''Expands a basic dictionary with session attributes.'''
    permanent = (lambda self = None: self.get('_permanent', False))()
    permanent = (lambda self = None, value = None: self['_permanent'] = bool(value))()
    new = False
    modified = True
    accessed = True


class SecureCookieSession(SessionMixin, CallbackDict):
    pass
# WARNING: Decompyle incomplete


class NullSession(SecureCookieSession):
    '''Class used to generate nicer error messages if sessions are not
    available.  Will still allow read-only access to the empty session
    but fail on setting.
    '''
    
    def _fail(self = None, *args, **kwargs):
        raise RuntimeError('The session is unavailable because no secret key was set.  Set the secret_key on the application to something unique and secret.')

    __setitem__ = _fail
    __delitem__ = _fail
    clear = _fail
    pop = _fail
    popitem = _fail
    update = _fail
    setdefault = _fail
    del _fail


class SessionInterface:
    """The basic interface you have to implement in order to replace the
    default session interface which uses werkzeug's securecookie
    implementation.  The only methods you have to implement are
    :meth:`open_session` and :meth:`save_session`, the others have
    useful defaults which you don't need to change.

    The session object returned by the :meth:`open_session` method has to
    provide a dictionary like interface plus the properties and methods
    from the :class:`SessionMixin`.  We recommend just subclassing a dict
    and adding that mixin::

        class Session(dict, SessionMixin):
            pass

    If :meth:`open_session` returns ``None`` Flask will call into
    :meth:`make_null_session` to create a session that acts as replacement
    if the session support cannot work because some requirement is not
    fulfilled.  The default :class:`NullSession` class that is created
    will complain that the secret key was not set.

    To replace the session interface on an application all you have to do
    is to assign :attr:`flask.Flask.session_interface`::

        app = Flask(__name__)
        app.session_interface = MySessionInterface()

    Multiple requests with the same session may be sent and handled
    concurrently. When implementing a new session interface, consider
    whether reads or writes to the backing store must be synchronized.
    There is no guarantee on the order in which the session for each
    request is opened or saved, it will occur in the order that requests
    begin and end processing.

    .. versionadded:: 0.8
    """
    null_session_class = NullSession
    pickle_based = False
    
    def make_null_session(self = None, app = None):
        '''Creates a null session which acts as a replacement object if the
        real session support could not be loaded due to a configuration
        error.  This mainly aids the user experience because the job of the
        null session is to still support lookup without complaining but
        modifications are answered with a helpful error message of what
        failed.

        This creates an instance of :attr:`null_session_class` by default.
        '''
        return self.null_session_class()

    
    def is_null_session(self = None, obj = None):
        '''Checks if a given object is a null session.  Null sessions are
        not asked to be saved.

        This checks if the object is an instance of :attr:`null_session_class`
        by default.
        '''
        return isinstance(obj, self.null_session_class)

    
    def get_cookie_name(self = None, app = None):
        '''The name of the session cookie. Uses``app.config["SESSION_COOKIE_NAME"]``.'''
        return app.config['SESSION_COOKIE_NAME']

    
    def get_cookie_domain(self = None, app = None):
        '''The value of the ``Domain`` parameter on the session cookie. If not set,
        browsers will only send the cookie to the exact domain it was set from.
        Otherwise, they will send it to any subdomain of the given value as well.

        Uses the :data:`SESSION_COOKIE_DOMAIN` config.

        .. versionchanged:: 2.3
            Not set by default, does not fall back to ``SERVER_NAME``.
        '''
        rv = app.config['SESSION_COOKIE_DOMAIN']
        return rv if rv else None

    
    def get_cookie_path(self = None, app = None):

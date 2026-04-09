# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from __future__ import annotations
import getpass
import hashlib
import json
import os
import pkgutil
import re
import sys
import time
import typing as t
import uuid
from contextlib import ExitStack
from io import BytesIO
from itertools import chain
from multiprocessing import Value
from os.path import basename
from os.path import join
from zlib import adler32
from _internal import _log
from exceptions import NotFound
from exceptions import SecurityError
from http import parse_cookie
from sansio.utils import host_is_trusted
from security import gen_salt
from utils import send_file
from wrappers.request import Request
from wrappers.response import Response
from console import Console
from tbtools import DebugFrameSummary
from tbtools import DebugTraceback
from tbtools import render_console_html
if t.TYPE_CHECKING:
    from _typeshed.wsgi import StartResponse
    from _typeshed.wsgi import WSGIApplication
    from _typeshed.wsgi import WSGIEnvironment
PIN_TIME = 604800

def hash_pin(pin = None):
    return hashlib.sha1(f'''{pin} added salt'''.encode('utf-8', 'replace')).hexdigest()[:12]

_machine_id: 'str | bytes | None' = None

def get_machine_id():
    pass
# WARNING: Decompyle incomplete


class _ConsoleFrame:
    '''Helper class so that we can reuse the frame console code for the
    standalone console.
    '''
    
    def __init__(self = None, namespace = None):
        self.console = Console(namespace)
        self.id = 0

    
    def eval(self = None, code = None):
        return self.console.eval(code)



def get_pin_and_cookie_name(app = None):
    '''Given an application object this returns a semi-stable 9 digit pin
    code and a random key.  The hope is that this is stable between
    restarts to not make debugging particularly frustrating.  If the pin
    was forcefully disabled this returns `None`.

    Second item in the resulting tuple is the cookie name for remembering.
    '''
    pass
# WARNING: Decompyle incomplete


class DebuggedApplication:
    _pin_cookie: 'str' = 'Enables debugging support for a given application::\n\n        from werkzeug.debug import DebuggedApplication\n        from myapp import app\n        app = DebuggedApplication(app, evalex=True)\n\n    The ``evalex`` argument allows evaluating expressions in any frame\n    of a traceback. This works by preserving each frame with its local\n    state. Some state, such as context globals, cannot be restored with\n    the frame by default. When ``evalex`` is enabled,\n    ``environ["werkzeug.debug.preserve_context"]`` will be a callable\n    that takes a context manager, and can be called multiple times.\n    Each context manager will be entered before evaluating code in the\n    frame, then exited again, so they can perform setup and cleanup for\n    each call.\n\n    :param app: the WSGI application to run debugged.\n    :param evalex: enable exception evaluation feature (interactive\n                   debugging).  This requires a non-forking server.\n    :param request_key: The key that points to the request object in this\n                        environment.  This parameter is ignored in current\n                        versions.\n    :param console_path: the URL for a general purpose console.\n    :param console_init_func: the function that is executed before starting\n                              the general purpose console.  The return value\n                              is used as initial namespace.\n    :param show_hidden_frames: by default hidden traceback frames are skipped.\n                               You can show them by setting this parameter\n                               to `True`.\n    :param pin_security: can be used to disable the pin based security system.\n    :param pin_logging: enables the logging of the pin system.\n\n    .. versionchanged:: 2.2\n        Added the ``werkzeug.debug.preserve_context`` environ key.\n    '
    
    def __init__(self, app, evalex, request_key, console_path = None, console_init_func = None, show_hidden_frames = None, pin_security = (False, 'werkzeug.request', '/console', None, False, True, True), pin_logging = ('app', 'WSGIApplication', 'evalex', 'bool', 'request_key', 'str', 'console_path', 'str', 'console_init_func', 't.Callable[[], dict[str, t.Any]] | None', 'show_hidden_frames', 'bool', 'pin_security', 'bool', 'pin_logging', 'bool', 'return', 'None')):
        if not console_init_func:
            console_init_func = None
        self.app = app
        self.evalex = evalex
        self.frames = { }
        self.frame_contexts = { }
        self.request_key = request_key
        self.console_path = console_path
        self.console_init_func = console_init_func
        self.show_hidden_frames = show_hidden_frames
        self.secret = gen_salt(20)
        self._failed_pin_auth = Value('B')
        self.pin_logging = pin_logging
    # WARNING: Decompyle incomplete

    pin = (lambda self = None: if not hasattr(self, '_pin'):
pin_cookie = get_pin_and_cookie_name(self.app)(self._pin, self._pin_cookie) = pin_cookieself._pin)()
    pin = (lambda self = None, value = None: pass# WARNING: Decompyle incomplete
)()
    pin_cookie_name = (lambda self = None: if not hasattr(self, '_pin_cookie'):
pin_cookie = get_pin_and_cookie_name(self.app)(self._pin, self._pin_cookie) = pin_cookieself._pin_cookie)()
    
    def debug_application(self = None, environ = None, start_response = None):
        '''Run the application and conserve the traceback frames.'''
        pass
    # WARNING: Decompyle incomplete

    
    def execute_command(self = None, request = None, command = None, frame = ('request', 'Request', 'command', 'str', 'frame', 'DebugFrameSummary | _ConsoleFrame', 'return', 'Response')):
        '''Execute a command in a console.'''
        if not self.check_host_trust(request.environ):
            return SecurityError()
        contexts = None.frame_contexts.get(id(frame), [])
        exit_stack = ExitStack()
        for cm in contexts:
            exit_stack.enter_context(cm)
            None(None, None)
            return 
            with None:
                if not None, Response(frame.eval(command), mimetype = 'text/html'):
                    pass

    
    def display_console(self = None, request = None):
        '''Display a standalone shell.'''
        if not self.check_host_trust(request.environ):
            return SecurityError()
    # WARNING: Decompyle incomplete

    
    def get_resource(self = None, request = None, filename = None):
        '''Return a static resource from the shared folder.'''
        path = join('shared', basename(filename))
    # WARNING: Decompyle incomplete

    
    def check_pin_trust(self = None, environ = None):
        """Checks if the request passed the pin test.  This returns `True` if the
        request is trusted on a pin/cookie basis and returns `False` if not.
        Additionally if the cookie's stored pin hash is wrong it will return
        `None` so that appropriate action can be taken.
        """
        pass
    # WARNING: Decompyle incomplete

    
    def check_host_trust(self = None, environ = None):
        return host_is_trusted(environ.get('HTTP_HOST'), self.trusted_hosts)

    
    def _fail_pin_auth(self = None):
        self._failed_pin_auth.get_lock()
        count = self._failed_pin_auth.value
        self._failed_pin_auth.value = count + 1
        None(None, None)

    
    def pin_auth(self = None, request = None):
        '''Authenticates with the pin.'''
        if not self.check_host_trust(request.environ):
            return SecurityError()
        exhausted = None
        auth = False
        trust = self.check_pin_trust(request.environ)
        pin = t.cast(str, self.pin)
        bad_cookie = False
    # WARNING: Decompyle incomplete

    
    def log_pin_request(self = None, request = None):
        '''Log the pin if needed.'''
        if not self.check_host_trust(request.environ):
            return SecurityError()
    # WARNING: Decompyle incomplete

    
    def __call__(self = None, environ = None, start_response = None):
        '''Dispatch the requests.'''
        request = Request(environ)
        response = self.debug_application
    # WARNING: Decompyle incomplete

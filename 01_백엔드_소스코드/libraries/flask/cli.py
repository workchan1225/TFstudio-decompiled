# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: cli.pyc (Python 3.11)

from __future__ import annotations
import ast
import importlib.metadata as importlib
import inspect
import os
import platform
import re
import sys
import traceback
import typing as t
from functools import update_wrapper
from operator import itemgetter
import click
from click.core import ParameterSource
from werkzeug import run_simple
from werkzeug.serving import is_running_from_reloader
from werkzeug.utils import import_string
from globals import current_app
from helpers import get_debug_flag
from helpers import get_load_dotenv
if t.TYPE_CHECKING:
    from app import Flask

class NoAppException(click.UsageError):
    '''Raised if an application cannot be found or loaded.'''
    pass


def find_best_app(module):
    '''Given a module instance this tries to find the best possible
    application in the module or raises an exception.
    '''
    pass
# WARNING: Decompyle incomplete


def _called_with_wrong_args(f):
    '''Check whether calling a function raised a ``TypeError`` because
    the call failed or because something in the factory raised the
    error.

    :param f: The function that was called.
    :return: ``True`` if the call failed.
    '''
    tb = sys.exc_info()[2]
# WARNING: Decompyle incomplete


def find_app_by_string(module, app_name):
    '''Check if the given string is a variable name or a function. Call
    a function to get the app instance, or return the variable directly.
    '''
    Flask = Flask
    import 
    
    try:
        expr = ast.parse(app_name.strip(), mode = 'eval').body
    except SyntaxError:
        raise NoAppException(f'''Failed to parse {app_name!r} as an attribute name or function call.'''), None

    if isinstance(expr, ast.Name):
        name = expr.id
        args = []
        kwargs = { }
# WARNING: Decompyle incomplete


def prepare_import(path):
    '''Given a filename this will try to calculate the python path, add it
    to the search path and return the actual module name that is expected.
    '''
    path = os.path.realpath(path)
    (fname, ext) = os.path.splitext(path)
    if ext == '.py':
        path = fname
    if os.path.basename(path) == '__init__':
        path = os.path.dirname(path)
    module_name = []
    (path, name) = os.path.split(path)
    module_name.append(name)
    if not os.path.exists(os.path.join(path, '__init__.py')):
        pass
    
    if sys.path[0] != path:
        sys.path.insert(0, path)
    return '.'.join(module_name[::-1])


def locate_app(module_name, app_name, raise_if_not_found = (True,)):
    
    try:
        __import__(module_name)
    except ImportError:
        if sys.exc_info()[2].tb_next:
            raise NoAppException(f'''While importing {module_name!r}, an ImportError was raised:\n\n{traceback.format_exc()}'''), None
        if raise_if_not_found:
            raise NoAppException(f'''Could not import {module_name!r}.'''), None
        return None

    module = sys.modules[module_name]
# WARNING: Decompyle incomplete


def get_version(ctx, param, value):
    if value or ctx.resilient_parsing:
        return None
    flask_version = None.metadata.version('flask')
    werkzeug_version = importlib.metadata.version('werkzeug')
    click.echo(f'''Python {platform.python_version()}\nFlask {flask_version}\nWerkzeug {werkzeug_version}''', color = ctx.color)
    ctx.exit()

version_option = click.Option([
    '--version'], help = 'Show the Flask version.', expose_value = False, callback = get_version, is_flag = True, is_eager = True)

class ScriptInfo:
    """Helper object to deal with Flask applications.  This is usually not
    necessary to interface with as it's used internally in the dispatching
    to click.  In future versions of Flask this object will most likely play
    a bigger role.  Typically it's created automatically by the
    :class:`FlaskGroup` but you can also manually create it and pass it
    onwards as click object.
    """
    
    def __init__(self = None, app_import_path = None, create_app = None, set_debug_flag = (None, None, True)):
        self.app_import_path = app_import_path
        self.create_app = create_app
        self.data = { }
        self.set_debug_flag = set_debug_flag
        self._loaded_app = None

    
    def load_app(self = None):
        '''Loads the Flask app (if not yet loaded) and returns it.  Calling
        this multiple times will just result in the already loaded app to
        be returned.
        '''
        pass
    # WARNING: Decompyle incomplete


pass_script_info = click.make_pass_decorator(ScriptInfo, ensure = True)

def with_appcontext(f):
    """Wraps a callback so that it's guaranteed to be executed with the
    script's application context.

    Custom commands (and their options) registered under ``app.cli`` or
    ``blueprint.cli`` will always have an app context available, this
    decorator is not required in that case.

    .. versionchanged:: 2.2
        The app context is active for subcommands as well as the
        decorated callback. The app context is always available to
        ``app.cli`` command and parameter callbacks.
    """
    pass
# WARNING: Decompyle incomplete


class AppGroup(click.Group):
    '''This works similar to a regular click :class:`~click.Group` but it
    changes the behavior of the :meth:`command` decorator so that it
    automatically wraps the functions in :func:`with_appcontext`.

    Not to be confused with :class:`FlaskGroup`.
    '''
    
    def command(self, *args, **kwargs):
        """This works exactly like the method of the same name on a regular
        :class:`click.Group` but it wraps callbacks in :func:`with_appcontext`
        unless it's disabled by passing ``with_appcontext=False``.
        """
        pass
    # WARNING: Decompyle incomplete

    
    def group(self, *args, **kwargs):
        '''This works exactly like the method of the same name on a regular
        :class:`click.Group` but it defaults the group class to
        :class:`AppGroup`.
        '''
        kwargs.setdefault('cls', AppGroup)
    # WARNING: Decompyle incomplete



def _set_app(ctx = None, param = None, value = None):
    pass
# WARNING: Decompyle incomplete

_app_option = click.Option([
    '-A',
    '--app'], metavar = 'IMPORT', help = "The Flask application or factory function to load, in the form 'module:name'. Module can be a dotted import or file path. Name is not required if it is 'app', 'application', 'create_app', or 'make_app', and can be 'name(args)' to pass arguments.", is_eager = True, expose_value = False, callback = _set_app)

def _set_debug(ctx = None, param = None, value = None):
    source = ctx.get_parameter_source(param.name)
# WARNING: Decompyle incomplete

_debug_option = click.Option([
    '--debug/--no-debug'], help = 'Set debug mode.', expose_value = False, callback = _set_debug)

def _env_file_callback(ctx = None, param = None, value = None):
    pass
# WARNING: Decompyle incomplete

_env_file_option = click.Option([
    '-e',
    '--env-file'], type = click.Path(exists = True, dir_okay = False), help = 'Load environment variables from this file. python-dotenv must be installed.', is_eager = True, expose_value = False, callback = _env_file_callback)

class FlaskGroup(AppGroup):
    pass
# WARNING: Decompyle incomplete


def _path_is_ancestor(path, other):
    '''Take ``other`` and remove the length of ``path`` from it. Then join it
    to ``path``. If it is the original value, ``path`` is an ancestor of
    ``other``.'''
    return os.path.join(path, other[len(path):].lstrip(os.sep)) == other


def load_dotenv(path = None):
    '''Load "dotenv" files in order of precedence to set environment variables.

    If an env var is already set it is not overwritten, so earlier files in the
    list are preferred over later files.

    This is a no-op if `python-dotenv`_ is not installed.

    .. _python-dotenv: https://github.com/theskumar/python-dotenv#readme

    :param path: Load the file at this location instead of searching.
    :return: ``True`` if a file was loaded.

    .. versionchanged:: 2.0
        The current directory is not changed to the location of the
        loaded file.

    .. versionchanged:: 2.0
        When loading the env files, set the default encoding to UTF-8.

    .. versionchanged:: 1.1.0
        Returns ``False`` when python-dotenv is not installed, or when
        the given path isn\'t a file.

    .. versionadded:: 1.0
    '''
    
    try:
        import dotenv
    except ImportError:
        if path and os.path.isfile('.env') or os.path.isfile('.flaskenv'):
            click.secho(' * Tip: There are .env or .flaskenv files present. Do "pip install python-dotenv" to use them.', fg = 'yellow', err = True)
        return False

# WARNING: Decompyle incomplete


def show_server_banner(debug, app_import_path):
    '''Show extra startup messages the first time the server is run,
    ignoring the reloader.
    '''
    if is_running_from_reloader():
        return None
# WARNING: Decompyle incomplete


class CertParamType(click.ParamType):
    """Click option type for the ``--cert`` option. Allows either an
    existing file, the string ``'adhoc'``, or an import for a
    :class:`~ssl.SSLContext` object.
    """
    name = 'path'
    
    def __init__(self):
        self.path_type = click.Path(exists = True, dir_okay = False, resolve_path = True)

    
    def convert(self, value, param, ctx):
        
        try:
            import ssl
        except ImportError:
            raise click.BadParameter('Using "--cert" requires Python to be compiled with SSL support.', ctx, param), None

        
        try:
            return self.path_type(value, param, ctx)
        except click.BadParameter:
            value = click.STRING(value, param, ctx).lower()
            return 
            if isinstance(obj, ssl.SSLContext):
                return 




def _validate_key(ctx, param, value):
    '''The ``--key`` option must be specified when ``--cert`` is a file.
    Modifies the ``cert`` param to be a ``(cert, key)`` pair if needed.
    '''
    cert = ctx.params.get('cert')
    is_adhoc = cert == 'adhoc'
    
    try:
        import ssl
        is_context = isinstance(cert, ssl.SSLContext)
    except ImportError:
        is_context = False

# WARNING: Decompyle incomplete


class SeparatedPathType(click.Path):
    pass
# WARNING: Decompyle incomplete

run_command = (lambda info, host, port, reload, debugger, with_threads, cert, extra_files, exclude_patterns: pass# WARNING: Decompyle incomplete
)()()()()()()()()()()()
run_command.params.insert(0, _debug_option)
shell_command = (lambda : import codebanner = f'''Python {sys.version} on {sys.platform}\nApp: {current_app.import_name}\nInstance: {current_app.instance_path}'''ctx = { }startup = os.environ.get('PYTHONSTARTUP')if startup and os.path.isfile(startup):
f = open(startup)eval(compile(f.read(), startup, 'exec'), ctx)None(None, None)else:
with None:
if not None:
passctx.update(current_app.make_shell_context())interactive_hook = getattr(sys, '__interactivehook__', None)# WARNING: Decompyle incomplete
)()()
routes_command = (lambda sort = click.option('--sort', '-s', type = click.Choice(('endpoint', 'methods', 'domain', 'rule', 'match')), default = 'endpoint', help = "Method to sort routes by. 'match' is the order that Flask will match routes when dispatching a request."), all_methods = click.option('--all-methods', is_flag = True, help = 'Show HEAD and OPTIONS methods.'): pass# WARNING: Decompyle incomplete
)()()()()
cli = FlaskGroup(name = 'flask', help = "A general utility script for Flask applications.\n\nAn application to load must be given with the '--app' option,\n'FLASK_APP' environment variable, or with a 'wsgi.py' or 'app.py' file\nin the current directory.\n")

def main():
    cli.main()

if __name__ == '__main__':
    main()
    return None
return click.option('--with-threads/--without-threads', default = True, help = 'Enable or disable multithreading.')

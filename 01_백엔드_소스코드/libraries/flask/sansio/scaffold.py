# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: scaffold.pyc (Python 3.11)

from __future__ import annotations
import importlib.util as importlib
import os
import pathlib
import sys
import typing as t
from collections import defaultdict
from functools import update_wrapper
from jinja2 import FileSystemLoader
from werkzeug.exceptions import default_exceptions
from werkzeug.exceptions import HTTPException
from werkzeug.utils import cached_property
from  import typing as ft
from cli import AppGroup
from helpers import get_root_path
from templating import _default_template_ctx_processor
_sentinel = object()
F = t.TypeVar('F', bound = t.Callable[(..., t.Any)])
T_after_request = t.TypeVar('T_after_request', bound = ft.AfterRequestCallable)
T_before_request = t.TypeVar('T_before_request', bound = ft.BeforeRequestCallable)
T_error_handler = t.TypeVar('T_error_handler', bound = ft.ErrorHandlerCallable)
T_teardown = t.TypeVar('T_teardown', bound = ft.TeardownCallable)
T_template_context_processor = t.TypeVar('T_template_context_processor', bound = ft.TemplateContextProcessorCallable)
T_url_defaults = t.TypeVar('T_url_defaults', bound = ft.URLDefaultCallable)
T_url_value_preprocessor = t.TypeVar('T_url_value_preprocessor', bound = ft.URLValuePreprocessorCallable)
T_route = t.TypeVar('T_route', bound = ft.RouteCallable)

def setupmethod(f = None):
    pass
# WARNING: Decompyle incomplete


class Scaffold:
    name: 'str' = 'Common behavior shared between :class:`~flask.Flask` and\n    :class:`~flask.blueprints.Blueprint`.\n\n    :param import_name: The import name of the module where this object\n        is defined. Usually :attr:`__name__` should be used.\n    :param static_folder: Path to a folder of static files to serve.\n        If this is set, a static route will be added.\n    :param static_url_path: URL prefix for the static route.\n    :param template_folder: Path to a folder containing template files.\n        for rendering. If this is set, a Jinja loader will be added.\n    :param root_path: The path that static, template, and resource files\n        are relative to. Typically not set, it is discovered based on\n        the ``import_name``.\n\n    .. versionadded:: 2.0\n    '
    _static_folder: 'str | None' = None
    _static_url_path: 'str | None' = None
    
    def __init__(self, import_name = None, static_folder = None, static_url_path = None, template_folder = (None, None, None, None), root_path = ('import_name', 'str', 'static_folder', 'str | os.PathLike | None', 'static_url_path', 'str | None', 'template_folder', 'str | os.PathLike | None', 'root_path', 'str | None')):
        self.import_name = import_name
        self.static_folder = static_folder
        self.static_url_path = static_url_path
        self.template_folder = template_folder
    # WARNING: Decompyle incomplete

    
    def __repr__(self = None):
        return f'''<{type(self).__name__} {self.name!r}>'''

    
    def _check_setup_finished(self = None, f_name = None):
        raise NotImplementedError

    static_folder = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    static_folder = (lambda self = None, value = None: pass# WARNING: Decompyle incomplete
)()
    has_static_folder = (lambda self = None: self.static_folder is not None)()
    static_url_path = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    static_url_path = (lambda self = None, value = None: pass# WARNING: Decompyle incomplete
)()
    jinja_loader = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    def _method_route(self = None, method = None, rule = None, options = ('method', 'str', 'rule', 'str', 'options', 'dict', 'return', 't.Callable[[T_route], T_route]')):
        if 'methods' in options:
            raise TypeError("Use the 'route' decorator to use the 'methods' argument.")
    # WARNING: Decompyle incomplete

    get = (lambda self = None, rule = None: self._method_route('GET', rule, options))()
    post = (lambda self = None, rule = None: self._method_route('POST', rule, options))()
    put = (lambda self = None, rule = None: self._method_route('PUT', rule, options))()
    delete = (lambda self = None, rule = None: self._method_route('DELETE', rule, options))()
    patch = (lambda self = None, rule = None: self._method_route('PATCH', rule, options))()
    route = (lambda self = None, rule = None: pass# WARNING: Decompyle incomplete
)()
    add_url_rule = (lambda self = None, rule = None, endpoint = setupmethod, view_func = (None, None, None), provide_automatic_options = ('rule', 'str', 'endpoint', 'str | None', 'view_func', 'ft.RouteCallable | None', 'provide_automatic_options', 'bool | None', 'options', 't.Any', 'return', 'None'): raise NotImplementedError)()
    endpoint = (lambda self = None, endpoint = None: pass# WARNING: Decompyle incomplete
)()
    before_request = (lambda self = None, f = None: self.before_request_funcs.setdefault(None, []).append(f)f)()
    after_request = (lambda self = None, f = None: self.after_request_funcs.setdefault(None, []).append(f)f)()
    teardown_request = (lambda self = None, f = None: self.teardown_request_funcs.setdefault(None, []).append(f)f)()
    context_processor = (lambda self = None, f = None: self.template_context_processors[None].append(f)f)()
    url_value_preprocessor = (lambda self = None, f = None: self.url_value_preprocessors[None].append(f)f)()
    url_defaults = (lambda self = None, f = None: self.url_default_functions[None].append(f)f)()
    errorhandler = (lambda self = None, code_or_exception = None: pass# WARNING: Decompyle incomplete
)()
    register_error_handler = (lambda self = None, code_or_exception = None, f = setupmethod: (exc_class, code) = self._get_exc_class_and_code(code_or_exception)self.error_handler_spec[None][code][exc_class] = f)()
    _get_exc_class_and_code = (lambda exc_class_or_code = None: if isinstance(exc_class_or_code, int):
try:
exc_class = default_exceptions[exc_class_or_code]except KeyError:
raise ValueError(f'''\'{exc_class_or_code}\' is not a recognized HTTP error code. Use a subclass of HTTPException with that code instead.'''), Noneexc_class = exc_class_or_codeif isinstance(exc_class, Exception):
raise TypeError(f'''{exc_class!r} is an instance, not a class. Handlers can only be registered for Exception classes or HTTP error codes.''')if not issubclass(exc_class, Exception):
raise ValueError(f'''\'{exc_class.__name__}\' is not a subclass of Exception. Handlers can only be registered for Exception classes or HTTP error codes.''')if issubclass(exc_class, HTTPException):
(exc_class, exc_class.code)(None, None))()


def _endpoint_from_view_func(view_func = None):
    '''Internal helper that returns the default endpoint for a given
    function.  This always is the function name.
    '''
    pass
# WARNING: Decompyle incomplete


def _path_is_relative_to(path = None, base = None):
    
    try:
        path.relative_to(base)
        return True
    except ValueError:
        return False



def _find_package_path(import_name):
    '''Find the path that contains the package or module.'''
    pass
# WARNING: Decompyle incomplete


def find_package(import_name = None):
    """Find the prefix that a package is installed under, and the path
    that it would be imported from.

    The prefix is the directory containing the standard directory
    hierarchy (lib, bin, etc.). If the package is not installed to the
    system (:attr:`sys.prefix`) or a virtualenv (``site-packages``),
    ``None`` is returned.

    The path is the entry in :attr:`sys.path` that contains the package
    for import. If the package is not installed, it's assumed that the
    package was imported from the current working directory.
    """
    package_path = _find_package_path(import_name)
    py_prefix = os.path.abspath(sys.prefix)
    if _path_is_relative_to(pathlib.PurePath(package_path), py_prefix):
        return (py_prefix, package_path)
    (site_parent, site_folder) = None.path.split(package_path)
    if site_folder.lower() == 'site-packages':
        (parent, folder) = os.path.split(site_parent)
        if folder.lower() == 'lib':
            return (parent, package_path)
        if None.path.basename(parent).lower() == 'lib':
            return (os.path.dirname(parent), package_path)
        return (None, package_path)
    return (None, package_path)

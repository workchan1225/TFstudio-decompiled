# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: blueprints.pyc (Python 3.11)

from __future__ import annotations
import os
import typing as t
from collections import defaultdict
from functools import update_wrapper
from  import typing as ft
from scaffold import _endpoint_from_view_func
from scaffold import _sentinel
from scaffold import Scaffold
from scaffold import setupmethod
if t.TYPE_CHECKING:
    from app import App
DeferredSetupFunction = t.Callable[([
    'BlueprintSetupState'], t.Callable)]
T_after_request = t.TypeVar('T_after_request', bound = ft.AfterRequestCallable)
T_before_request = t.TypeVar('T_before_request', bound = ft.BeforeRequestCallable)
T_error_handler = t.TypeVar('T_error_handler', bound = ft.ErrorHandlerCallable)
T_teardown = t.TypeVar('T_teardown', bound = ft.TeardownCallable)
T_template_context_processor = t.TypeVar('T_template_context_processor', bound = ft.TemplateContextProcessorCallable)
T_template_filter = t.TypeVar('T_template_filter', bound = ft.TemplateFilterCallable)
T_template_global = t.TypeVar('T_template_global', bound = ft.TemplateGlobalCallable)
T_template_test = t.TypeVar('T_template_test', bound = ft.TemplateTestCallable)
T_url_defaults = t.TypeVar('T_url_defaults', bound = ft.URLDefaultCallable)
T_url_value_preprocessor = t.TypeVar('T_url_value_preprocessor', bound = ft.URLValuePreprocessorCallable)

class BlueprintSetupState:
    '''Temporary holder object for registering a blueprint with the
    application.  An instance of this class is created by the
    :meth:`~flask.Blueprint.make_setup_state` method and later passed
    to all register callback functions.
    '''
    
    def __init__(self, blueprint = None, app = None, options = None, first_registration = ('blueprint', 'Blueprint', 'app', 'App', 'options', 't.Any', 'first_registration', 'bool', 'return', 'None')):
        self.app = app
        self.blueprint = blueprint
        self.options = options
        self.first_registration = first_registration
        subdomain = self.options.get('subdomain')
    # WARNING: Decompyle incomplete

    
    def add_url_rule(self = None, rule = None, endpoint = None, view_func = (None, None), **options):
        """A helper method to register a rule (and optionally a view function)
        to the application.  The endpoint is automatically prefixed with the
        blueprint's name.
        """
        pass
    # WARNING: Decompyle incomplete



class Blueprint(Scaffold):
    pass
# WARNING: Decompyle incomplete

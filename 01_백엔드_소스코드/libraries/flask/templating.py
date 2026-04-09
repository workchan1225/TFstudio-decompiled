# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: templating.pyc (Python 3.11)

from __future__ import annotations
import typing as t
from jinja2 import BaseLoader
from jinja2 import Environment as BaseEnvironment
from jinja2 import Template
from jinja2 import TemplateNotFound
from globals import _cv_app
from globals import _cv_request
from globals import current_app
from globals import request
from helpers import stream_with_context
from signals import before_render_template
from signals import template_rendered
if t.TYPE_CHECKING:
    from app import Flask
    from sansio.app import App
    from sansio.scaffold import Scaffold

def _default_template_ctx_processor():
    '''Default template context processor.  Injects `request`,
    `session` and `g`.
    '''
    appctx = _cv_app.get(None)
    reqctx = _cv_request.get(None)
    rv = { }
# WARNING: Decompyle incomplete


class Environment(BaseEnvironment):
    """Works like a regular Jinja2 environment but has some additional
    knowledge of how Flask's blueprint works so that it can prepend the
    name of the blueprint to referenced templates if necessary.
    """
    
    def __init__(self = None, app = None, **options):
        if 'loader' not in options:
            options['loader'] = app.create_global_jinja_loader()
    # WARNING: Decompyle incomplete



class DispatchingJinjaLoader(BaseLoader):
    '''A loader that looks for templates in the application and all
    the blueprint folders.
    '''
    
    def __init__(self = None, app = None):
        self.app = app

    
    def get_source(self = None, environment = None, template = None):
        if self.app.config['EXPLAIN_TEMPLATE_LOADING']:
            return self._get_source_explained(environment, template)
        return None._get_source_fast(environment, template)

    
    def _get_source_explained(self = None, environment = None, template = None):
        attempts = []
        trv = None
    # WARNING: Decompyle incomplete

    
    def _get_source_fast(self = None, environment = None, template = None):
        for _srcobj, loader in self._iter_loaders(template):
            
            return None, loader.get_source(environment, template)
            except TemplateNotFound:
                continue
            raise TemplateNotFound(template)

    
    def _iter_loaders(self = None, template = None):
        pass
    # WARNING: Decompyle incomplete

    
    def list_templates(self = None):
        result = set()
        loader = self.app.jinja_loader
    # WARNING: Decompyle incomplete



def _render(app = None, template = None, context = None):
    app.update_template_context(context)
    before_render_template.send(app, _async_wrapper = app.ensure_sync, template = template, context = context)
    rv = template.render(context)
    template_rendered.send(app, _async_wrapper = app.ensure_sync, template = template, context = context)
    return rv


def render_template(template_name_or_list = None, **context):
    '''Render a template by name with the given context.

    :param template_name_or_list: The name of the template to render. If
        a list is given, the first name to exist will be rendered.
    :param context: The variables to make available in the template.
    '''
    app = current_app._get_current_object()
    template = app.jinja_env.get_or_select_template(template_name_or_list)
    return _render(app, template, context)


def render_template_string(source = None, **context):
    '''Render a template from the given source string with the given
    context.

    :param source: The source code of the template to render.
    :param context: The variables to make available in the template.
    '''
    app = current_app._get_current_object()
    template = app.jinja_env.from_string(source)
    return _render(app, template, context)


def _stream(app = None, template = None, context = None):
    pass
# WARNING: Decompyle incomplete


def stream_template(template_name_or_list = None, **context):
    '''Render a template by name with the given context as a stream.
    This returns an iterator of strings, which can be used as a
    streaming response from a view.

    :param template_name_or_list: The name of the template to render. If
        a list is given, the first name to exist will be rendered.
    :param context: The variables to make available in the template.

    .. versionadded:: 2.2
    '''
    app = current_app._get_current_object()
    template = app.jinja_env.get_or_select_template(template_name_or_list)
    return _stream(app, template, context)


def stream_template_string(source = None, **context):
    '''Render a template from the given source string with the given
    context as a stream. This returns an iterator of strings, which can
    be used as a streaming response from a view.

    :param source: The source code of the template to render.
    :param context: The variables to make available in the template.

    .. versionadded:: 2.2
    '''
    app = current_app._get_current_object()
    template = app.jinja_env.from_string(source)
    return _stream(app, template, context)

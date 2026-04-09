# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: window.pyc (Python 3.11)

from __future__ import annotations
import inspect
import logging
import os
from collections.abc import Mapping, Sequence
from enum import Flag, auto
from functools import wraps
from threading import Lock
from typing import Any, Callable, TypeVar
from urllib.parse import urljoin
from uuid import uuid1
from typing_extensions import Any, Concatenate, ParamSpec, TypeAlias
from webview.http import http
from webview.dom.dom import DOM
from webview.errors import JavascriptException, WebViewException
from webview.event import Event, EventContainer
from webview.localization import original_localization
from webview.menu import Menu
from webview.screen import Screen
from webview.state import State
from webview.util import base_uri, escape_string, is_app, is_local_url, parse_file_type
P = ParamSpec('P')
T = TypeVar('T')
logger = logging.getLogger('pywebview')

def _api_call(function = None, event_type = None):
    '''
    Decorator to call a pywebview API, checking for _webview_ready and raisings
    appropriate Exceptions on failure.
    '''
    pass
# WARNING: Decompyle incomplete


def _shown_call(function = None):
    return _api_call(function, 'shown')


def _loaded_call(function = None):
    return _api_call(function, 'loaded')


def _before_load_call(function = None):
    return _api_call(function, 'before_load')


def _pywebview_ready_call(function = None):
    return _api_call(function, '_pywebviewready')


class FixPoint(Flag):
    NORTH = auto()
    WEST = auto()
    EAST = auto()
    SOUTH = auto()


class Window:
    
    def __init__(self, uid, title, url, html, width, height, x, y, resizable, fullscreen, min_size, hidden, frameless, easy_drag, shadow, focus, minimized, maximized, on_top, confirm_close, background_color, js_api, text_select, transparent, zoomable, draggable, vibrancy, menu, localization = None, http_port = None, server = None, server_args = ('', 800, 600, None, None, True, False, (200, 100), False, False, True, True, True, False, False, False, False, '#FFFFFF', None, False, False, False, False, False, [], None, None, None, { }, None), screen = ('uid', 'str', 'title', 'str', 'url', 'str | None', 'html', 'str', 'width', 'int', 'height', 'int', 'x', 'int | None', 'y', 'int | None', 'resizable', 'bool', 'fullscreen', 'bool', 'min_size', 'tuple[int, int]', 'hidden', 'bool', 'frameless', 'bool', 'easy_drag', 'bool', 'shadow', 'bool', 'focus', 'bool', 'minimized', 'bool', 'maximized', 'bool', 'on_top', 'bool', 'confirm_close', 'bool', 'background_color', 'str', 'js_api', 'Any', 'text_select', 'bool', 'transparent', 'bool', 'zoomable', 'bool', 'draggable', 'bool', 'vibrancy', 'bool', 'menu', 'list[Menu]', 'localization', 'Mapping[str, str] | None', 'http_port', 'int | None', 'server', 'type[http.ServerType] | None', 'server_args', 'http.ServerArgs', 'screen', 'Screen', 'return', 'None')):
        self.uid = uid
        self._title = title
        self.original_url = None if html else url
        self.real_url = None
        self.html = html
        self.initial_width = width
        self.initial_height = height
        self.initial_x = x
        self.initial_y = y
        self.resizable = resizable
        self.fullscreen = fullscreen
        self.min_size = min_size
        self.confirm_close = confirm_close
        self.background_color = background_color
        self.text_select = text_select
        self.frameless = frameless
        self.easy_drag = easy_drag
        self.shadow = shadow
        self.focus = focus
        self.hidden = hidden
        self.on_top = on_top
        self.minimized = minimized
        self.maximized = maximized
        self.transparent = transparent
        self.zoomable = zoomable
        self.draggable = draggable
        self.localization_override = localization
        self.vibrancy = vibrancy
        self.screen = screen
        self.menu = menu
        self._http_port = http_port
        self._server = server
        self._server_args = server_args
        self._url_prefix = None
        self._common_path = None
        self._server = None
        self._js_api = js_api
        self._functions = { }
        self._callbacks = { }
        self.events = EventContainer()
        self.events.closed = Event(self)
        self.events.closing = Event(self, True)
        self.events.loaded = Event(self)
        self.events.before_load = Event(self, True)
        self.events.before_show = Event(self, True)
        self.events.initialized = Event(self, True)
        self.events.shown = Event(self)
        self.events.minimized = Event(self)
        self.events.maximized = Event(self)
        self.events.restored = Event(self)
        self.events.resized = Event(self)
        self.events.moved = Event(self)
        self.events.request_sent = Event(self)
        self.events.response_received = Event(self)
        self.events._pywebviewready = Event(self)
        self._expose_lock = Lock()
        self.dom = DOM(self)
        self.gui = None
        self.native = None
        self._state = State(self)

    
    def _initialize(self = None, gui = None, server = None, server_args = (None, dict)):
        self.gui = gui
        self.localization = original_localization.copy()
        if self.localization_override:
            self.localization.update(self.localization_override)
    # WARNING: Decompyle incomplete

    width = (lambda self = None: self.events.shown.wait(15)(width, _) = self.gui.get_size(self.uid)width)()
    height = (lambda self = None: self.events.shown.wait(15)(_, height) = self.gui.get_size(self.uid)height)()
    state = (lambda self = None: self._state)()
    state = (lambda self = None, state = None: if not isinstance(state, State):
raise TypeError('State must be an instance of State class')self._state = state)()
    title = (lambda self = None: self._title)()
    title = (lambda self = None, title = None: self.events.loaded.wait(15)self._title = titleself.gui.set_title(title, self.uid))()
    x = (lambda self = None: self.events.shown.wait(15)(x, _) = self.gui.get_position(self.uid)x)()
    y = (lambda self = None: self.events.shown.wait(15)(_, y) = self.gui.get_position(self.uid)y)()
    on_top = (lambda self = None: self._Window__on_top)()
    on_top = (lambda self = None, on_top = None: self._Window__on_top = on_topif hasattr(self, 'gui') or self.gui != None:
self.gui.set_on_top(self.uid, on_top)NoneNone)()
    load_url = (lambda self = None, url = None: pass# WARNING: Decompyle incomplete
)()
    load_html = (lambda self = None, html = None, base_uri = _shown_call: self.events.loaded.clear()self.events.before_load.clear()self.events._pywebviewready.clear()logger.debug(f'''Loading HTML: {html[:30]}''')self.gui.load_html(html, base_uri, self.uid))()
    load_css = (lambda self = None, stylesheet = None: sanitized_css = stylesheet.replace('\n', '').replace('\r', '').replace('"', "'")js_code = f'''pywebview._loadCss("{sanitized_css}")'''self.run_js(js_code))()
    set_title = (lambda self = None, title = None: self._title = titleself.gui.set_title(title, self.uid))()
    clear_cookies = (lambda self: self.gui.clear_cookies(self.uid))()
    get_cookies = (lambda self: self.gui.get_cookies(self.uid))()
    get_current_url = (lambda self = _loaded_call: self.gui.get_current_url(self.uid))()
    destroy = (lambda self = None: self.gui.destroy_window(self.uid))()
    show = (lambda self = None: self.gui.show(self.uid))()
    hide = (lambda self = None: self.gui.hide(self.uid))()
    set_window_size = (lambda self = None, width = None, height = _shown_call: logger.warning('This function is deprecated and will be removed in future releases. Use resize() instead')self.resize(width, height))()
    resize = (lambda self = None, width = None, height = _shown_call, fix_point = (FixPoint.NORTH | FixPoint.WEST,): self.gui.resize(width, height, self.uid, fix_point))()
    maximize = (lambda self = None: self.gui.maximize(self.uid))()
    minimize = (lambda self = None: self.gui.minimize(self.uid))()
    restore = (lambda self = None: self.gui.restore(self.uid))()
    toggle_fullscreen = (lambda self = None: self.gui.toggle_fullscreen(self.uid))()
    move = (lambda self = None, x = None, y = _shown_call: self.gui.move(x, y, self.uid))()
    run_js = (lambda self = None, script = None: self.gui.evaluate_js(script, self.uid, False))()
    evaluate_js = (lambda self = None, script = None, callback = _pywebview_ready_call: unique_id = uuid1().hexself._callbacks[unique_id] = callbackif self.gui.renderer == 'cef':
return_result = f'''window.external.return_result(pywebview.stringify(value), "{unique_id}");'''elif self.gui.renderer == 'android-webkit':
return_result = 'return pywebview.stringify(value);'else:
return_result = 'pywebview.stringify(value);'if callback:
escaped_script = f'''\n                var value = eval("{escape_string(script)}");\n                if (pywebview._isPromise(value)) {{\n                    value.then(function evaluate_async(result) {{\n                        pywebview._asyncCallback(pywebview.stringify(result), "{unique_id}")\n                    }}).catch(function evaluate_async(error) {{\n                        pywebview._asyncCallback(pywebview.stringify(error), "{unique_id}")\n                    }});\n                    "true";\n                }} else {{ {return_result} }}\n            '''else:
escaped_script = f'''\n                var value;\n                try {{\n                    value = eval("{escape_string(script)}");\n                }} catch (e) {{\n                    value = {{\n                        name: e.name,\n                        pywebviewJavascriptError420: true,\n                    }}\n                    var keys = Object.getOwnPropertyNames(e);\n                    keys.forEach(function(key) {{ value[key] = e[key] }})\n                }}\n                {return_result};\n            '''if self.gui.renderer == 'cef':
result = self.gui.evaluate_js(escaped_script, self.uid, True, unique_id)elif self.gui.renderer == 'android-webkit':
escaped_script = f'''\n                (function() {{\n                    {escaped_script}\n                }})()\n            '''result = self.gui.evaluate_js(escaped_script, self.uid, True)else:
result = self.gui.evaluate_js(escaped_script, self.uid, True)if isinstance(result, dict) and result.get('pywebviewJavascriptError420'):
del result['pywebviewJavascriptError420']raise JavascriptException(result)result)()
    create_confirmation_dialog = (lambda self = None, title = None, message = _shown_call: self.gui.create_confirmation_dialog(title, message, self.uid))()
    create_file_dialog = (lambda self, dialog_type = None, directory = None, allow_multiple = _shown_call, save_filename = (10, '', False, '', tuple()), file_types = ('dialog_type', 'int', 'directory', 'str', 'allow_multiple', 'bool', 'save_filename', 'str', 'file_types', 'Sequence[str]', 'return', 'Sequence[str] | None'): for f in file_types:
parse_file_type(f)if not os.path.exists(directory):
directory = ''self.gui.create_file_dialog(dialog_type, directory, allow_multiple, save_filename, file_types, self.uid))()
    
    def expose(self = None, *functions):
        if not all(map(callable, functions)):
            raise TypeError('Parameter must be a function')
        func_list = []
        self._expose_lock
        for func in functions:
            name = func.__name__
            self._functions[name] = func
            params = list(inspect.getfullargspec(func).args)
            func_list.append({
                'func': name,
                'params': params })
            None(None, None)
        with None:
            if not None:
                pass
        if self.events.loaded.is_set():
            self.run_js(f'''window.pywebview._createApi({func_list})''')
            return None

    
    def _resolve_url(self = None, url = None):
        if is_app(url):
            return self._url_prefix
    # WARNING: Decompyle incomplete


WindowFunc: 'TypeAlias' = Callable[(Concatenate[(Window, P)], T)]

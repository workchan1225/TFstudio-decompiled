# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''
pywebview is a lightweight cross-platform wrapper around a webview component that allows to display HTML content in its
own dedicated window. Works on Windows, OS X and Linux and compatible with Python 2 and 3.

(C) 2014-2019 Roman Sirokov and contributors
Licensed under BSD license

http://github.com/r0x0r/pywebview/
'''
from __future__ import annotations
import datetime
import enum
import logging
import os
import re
import tempfile
import threading
from collections.abc import Iterable, Mapping
from typing import Any, Callable
from uuid import uuid4
from proxy_tools import module_property
from webview.http import http
from webview.errors import JavascriptException, WebViewException
from webview.event import Event
from webview.guilib import GUIType, initialize
from webview.localization import original_localization
from webview.menu import Menu
from webview.screen import Screen
from webview.util import _TOKEN, ImmutableDict, abspath, is_app, is_local_url
from webview.window import Window
__all__ = ('active_window', 'start', 'create_window', 'token', 'renderer', 'screens', 'settings', 'Event', 'JavascriptException', 'WebViewException', 'Screen', 'Window')

def _setup_logger():
    '''Setup logger with console handler and appropriate log level.'''
    logger = logging.getLogger('pywebview')
    if logger.handlers:
        return logger
    handler = None.StreamHandler()
    formatter = logging.Formatter('[pywebview] %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    log_level_name = os.environ.get('PYWEBVIEW_LOG', 'INFO').upper()
    
    try:
        log_level = getattr(logging, log_level_name)
        logger.setLevel(log_level)
    except AttributeError:
        logger.setLevel(logging.INFO)
        logger.warning(f'''Invalid log level \'{log_level_name}\', using INFO instead''')

    return logger

logger = _setup_logger()
OPEN_DIALOG = (lambda : logger.warning("OPEN_DIALOG is deprecated and will be removed in a future version. Use 'FileDialog.OPEN' instead.")10)()
FOLDER_DIALOG = (lambda : logger.warning("FOLDER_DIALOG is deprecated and will be removed in a future version. Use 'FileDialog.FOLDER' instead.")20)()
SAVE_DIALOG = (lambda : logger.warning("SAVE_DIALOG is deprecated and will be removed in a future version. Use 'FileDialog.SAVE' instead.")30)()

class FileDialog(enum.IntEnum):
    OPEN = 10
    FOLDER = 20
    SAVE = 30

settings = ImmutableDict({
    'ALLOW_DOWNLOADS': False,
    'ALLOW_FILE_URLS': True,
    'DRAG_REGION_SELECTOR': '.pywebview-drag-region',
    'DRAG_REGION_DIRECT_TARGET_ONLY': False,
    'DEFAULT_HTTP_PORT': 42001,
    'OPEN_EXTERNAL_LINKS_IN_BROWSER': True,
    'OPEN_DEVTOOLS_IN_DEBUG': True,
    'REMOTE_DEBUGGING_PORT': None,
    'IGNORE_SSL_ERRORS': False,
    'SHOW_DEFAULT_MENUS': True,
    'WEBVIEW2_RUNTIME_PATH': None })
_state = ImmutableDict({
    'debug': False,
    'storage_path': None,
    'private_mode': True,
    'user_agent': None,
    'http_server': False,
    'ssl': False,
    'icon': None,
    'menu': None })
DRAG_REGION_SELECTOR = (lambda : logger.warning('DRAG_REGION_SELECTOR is deprecated and will be removed in a future version. Use \'settings["DRAG_REGION_SELECTOR"]\' instead.')settings['DRAG_REGION_SELECTOR'])()
guilib = None
token = _TOKEN
windows: 'list[Window]' = []
renderer: 'str | None' = None

def start(func, args, localization, gui, debug, http_server, http_port, user_agent, private_mode, storage_path, menu = module_property, server = None, server_args = module_property, ssl = (None, None, { }, None, False, False, None, None, True, None, [], http.BottleServer, { }, False, None), icon = ('func', 'Callable[..., None] | None', 'args', 'Iterable[Any] | None', 'localization', 'dict[str, str]', 'gui', 'GUIType | None', 'debug', 'bool', 'http_server', 'bool', 'http_port', 'int | None', 'user_agent', 'str | None', 'private_mode', 'bool', 'storage_path', 'str | None', 'menu', 'list[Menu]', 'server', 'type[http.ServerType]', 'server_args', 'dict[Any, Any]', 'ssl', 'bool', 'icon', 'str | None')):
    '''
    Start a GUI loop and display previously created windows. This function must
    be called from a main thread.

    :param func: Function to invoke upon starting the GUI loop.
    :param args: Function arguments. Can be either a single value or a tuple of
        values.
    :param localization: A dictionary with localized strings. Default strings
        and their keys are defined in localization.py.
    :param gui: Force a specific GUI. Allowed values are ``cef``, ``qt``,
        ``gtk``, ``mshtml`` or ``edgechromium`` depending on a platform.
    :param debug: Enable debug mode. Default is False.
    :param http_server: Enable built-in HTTP server. If enabled, local files
        will be served using a local HTTP server on a random port. For each
        window, a separate HTTP server is spawned. This option is ignored for
        non-local URLs.
    :param user_agent: Change user agent string.
    :param private_mode: Enable private mode. In private mode, cookies and local storage are not preserved.
           Default is True.
    :param storage_path: Custom location for cookies and other website data
    :param menu: List of menus to be included in the app menu
    :param server: Server class. Defaults to BottleServer
    :param server_args: Dictionary of arguments to pass through to the server instantiation
    :param ssl: Enable SSL for local HTTP server. Default is False.
    :param icon: Path to the icon file. Supported only on GTK/QT.
    '''
    global guilib, renderer
    
    def _create_children(other_windows):
        if not windows[0].events.shown.wait(10):
            raise WebViewException('Main window failed to load')
        for window in other_windows:
            guilib.create_window(window)
            return None

    _state['debug'] = debug
    _state['user_agent'] = user_agent
    _state['http_server'] = http_server
    _state['private_mode'] = private_mode
    if icon:
        _state['icon'] = abspath(icon)
    if storage_path:
        __set_storage_path(storage_path)
    if not debug and os.environ.get('PYWEBVIEW_LOG'):
        logger.setLevel(logging.DEBUG)
    if not _state['storage_path'] and _state['private_mode'] and os.path.exists(_state['storage_path']):
        os.makedirs(_state['storage_path'])
    original_localization.update(localization)
    if threading.current_thread().name != 'MainThread':
        raise WebViewException('pywebview must be run on a main thread.')
    if len(windows) == 0:
        raise WebViewException('You must create a window first before calling this function.')
    guilib = initialize(gui)
    renderer = guilib.renderer
    if ssl:
        if server_args and 'keyfile' not in server_args or 'certfile' not in server_args:
            (keyfile, certfile) = __generate_ssl_cert()
            server_args['keyfile'] = keyfile
            server_args['certfile'] = certfile
        else:
            keyfile = server_args['keyfile']
            certfile = server_args['certfile']
            if not os.path.exists(keyfile):
                raise WebViewException(f'''The {keyfile} does not exist.''')
            if not os.path.exists(certfile):
                raise WebViewException(f'''The {certfile} does not exist.''')
        _state['ssl'] = True
    else:
        (keyfile, certfile) = (None, None)
        server_args.pop('keyfile', None)
        server_args.pop('certfile', None)
    urls = windows()
    has_local_urls = not (not windows())
# WARNING: Decompyle incomplete


def create_window(title, url, html, js_api, width, height, x, y, screen, resizable, fullscreen, min_size, hidden, frameless, easy_drag, shadow, focus, minimized, maximized, on_top, confirm_close, background_color, transparent, text_select, zoomable, draggable, vibrancy, menu = None, localization = module_property, server = module_property, http_port = (None, None, None, 800, 600, None, None, None, True, False, (200, 100), False, False, True, True, True, False, False, False, False, '#FFFFFF', False, False, False, False, False, [], None, http.BottleServer, None, { }), server_args = ('title', 'str', 'url', 'str | callable | None', 'html', 'str | None', 'js_api', 'Any', 'width', 'int', 'height', 'int', 'x', 'int | None', 'y', 'int | None', 'screen', 'Screen', 'resizable', 'bool', 'fullscreen', 'bool', 'min_size', 'tuple[int, int]', 'hidden', 'bool', 'frameless', 'bool', 'easy_drag', 'bool', 'shadow', 'bool', 'focus', 'bool', 'minimized', 'bool', 'maximized', 'bool', 'on_top', 'bool', 'confirm_close', 'bool', 'background_color', 'str', 'transparent', 'bool', 'text_select', 'bool', 'zoomable', 'bool', 'draggable', 'bool', 'vibrancy', 'bool', 'menu', 'list[Menu]', 'localization', 'Mapping[str, str] | None', 'server', 'type[http.ServerType]', 'http_port', 'int | None', 'server_args', 'http.ServerArgs', 'return', 'Window | None')):
    """
    Create a web view window using a native GUI. The execution blocks after this function is invoked, so other
    program logic must be executed in a separate thread.
    :param title: Window title
    :param url: URL or WSGI/ASGI app to load
    :param html: HTML content to load
    :param width: window width. Default is 800px
    :param height: window height. Default is 600px
    :param screen: Screen to display the window on.
    :param resizable: True if window can be resized, False otherwise. Default is True
    :param fullscreen: True if start in fullscreen mode. Default is False
    :param min_size: a (width, height) tuple that specifies a minimum window size. Default is 200x100
    :param hidden: Whether the window should be hidden.
    :param frameless: Whether the window should have a frame.
    :param easy_drag: Easy window drag mode when window is frameless.
    :param shadow: Whether the window should have a frame border (shadows and Windows rounded edges).
    :param focus: Whether to activate the window when user opens it. Window can be controlled with mouse but keyboard input will go to another (active) window and not this one.
    :param minimized: Display window minimized
    :param maximized: Display window maximized
    :param on_top: Keep window above other windows (required OS: Windows)
    :param confirm_close: Display a window close confirmation dialog. Default is False
    :param background_color: Background color as a hex string that is displayed before the content of webview is loaded. Default is white.
    :param text_select: Allow text selection on page. Default is False.
    :param transparent: Don't draw window background.
    :param menu: List of menus to be included in the window menu
    :param server: Server class. Defaults to BottleServer
    :param server_args: Dictionary of arguments to pass through to the server instantiation
    :return: window object or None if window initialization is cancelled in the window.events.initialized event
    """
    valid_color = '^#(?:[0-9a-fA-F]{3}){1,2}$'
    if not re.match(valid_color, background_color):
        raise ValueError(f'''{background_color} is not a valid hex triplet color''')
    uid = 'master' if len(windows) == 0 else 'child_' + uuid4().hex[:8]
# WARNING: Decompyle incomplete


def __generate_ssl_cert():

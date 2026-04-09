# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: gtk.pyc (Python 3.11)

import json
import logging
import os
import pathlib
import sys
import webbrowser
from threading import Semaphore, Thread, main_thread
from typing import Any
from uuid import uuid1
from webview import FileDialog, _state, settings, windows
from webview.dom import _dnd_state
from webview.menu import Menu, MenuAction, MenuSeparator
from webview.models import Request, Response
from webview.screen import Screen
from webview.util import DEFAULT_HTML, create_cookie, inject_pywebview, js_bridge_call, parse_file_type
from webview.window import FixPoint, Window
logger = logging.getLogger('pywebview')
os.environ['EGL_LOG_LEVEL'] = 'fatal'
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')

try:
    gi.require_version('WebKit2', '4.1')
    gi.require_version('Soup', '3.0')
except ValueError:
    logger.debug('WebKit2 4.1 not found. Using 4.0.')
    gi.require_version('WebKit2', '4.0')
    gi.require_version('Soup', '2.4')

from gi.repository import Gdk, Gio
from gi.repository import GLib as glib
from gi.repository import Gtk as gtk
from gi.repository import WebKit2 as webkit
renderer = 'gtkwebkit2'
webkit_ver = (webkit.get_major_version(), webkit.get_minor_version(), webkit.get_micro_version())
_app = None
_app_actions = { }
cert = None

class BrowserView:
    instances = { }
    
    class JSBridge:
        
        def __init__(self = None, window = None):
            self.window = window
            self.uid = uuid1().hex[:8]

        
        def call(self = None, func_name = None, param = None, value_id = ('func_name', str, 'param', Any, 'value_id', str)):
            if param == 'undefined':
                param = None
            return js_bridge_call(self.window, func_name, param, value_id)


    
    def __init__(self = None, window = None):
        BrowserView.instances[window.uid] = self
        self.uid = window.uid
        self.pywebview_window = window
        self.is_fullscreen = False
        self.js_results = { }
        self.window = gtk.ApplicationWindow(title = window.title, application = _app)
        self.pywebview_window.native = self.window
        self.shown = window.events.shown
        self.loaded = window.events.loaded
        self.localization = window.localization
        self._last_width = window.initial_width
        self._last_height = window.initial_height
        if window.screen:
            self.screen = window.screen.frame
        else:
            display = Gdk.Display.get_default()
            monitor = Gdk.Display.get_monitor(display, 0)
            self.screen = Gdk.Monitor.get_geometry(monitor)
        if window.resizable:
            self.window.set_size_request(window.min_size[0], window.min_size[1])
            self.window.resize(window.initial_width, window.initial_height)
        else:
            self.window.set_size_request(window.initial_width, window.initial_height)
        if window.maximized:
            self.window.maximize()
        elif window.minimized:
            self.window.iconify()
    # WARNING: Decompyle incomplete

    
    def close_window(self, *data):
        should_cancel = self.pywebview_window.events.closing.set()
        if should_cancel:
            return True
        if None.pywebview_window.confirm_close:
            dialog = gtk.MessageDialog(parent = self.window, flags = gtk.DialogFlags.MODAL & gtk.DialogFlags.DESTROY_WITH_PARENT, type = gtk.MessageType.QUESTION, buttons = gtk.ButtonsType.OK_CANCEL, message_format = self.localization['global.quitConfirmation'])
            result = dialog.run()
            dialog.destroy()
            if result == gtk.ResponseType.CANCEL:
                return True
            for res in None.js_results.values():
                res['semaphore'].release()
                self.window.destroy()
                del BrowserView.instances[self.uid]
                if self.pywebview_window in windows:
                    windows.remove(self.pywebview_window)
        self.pywebview_window.events.closed.set()
        return False

    
    def on_drag_data(self, widget, drag_context, x, y, data, info, time):
        text = data.get_text()
        if _dnd_state['num_listeners'] > 0 and text:
            files = []
            for value in text.split('\n'):
                value = value.strip()
                if value.startswith('file://'):
                    path = value.replace('file://', '')
                    files.append((os.path.basename(path), path))
                    continue
                if value.startswith('/') and os.path.exists(value):
                    files.append((os.path.basename(value), value))
                return False

    
    def on_window_state_change(self, window, window_state):
        if window_state.changed_mask == Gdk.WindowState.ICONIFIED:
            if Gdk.WindowState.ICONIFIED & window_state.new_window_state == Gdk.WindowState.ICONIFIED:
                self.pywebview_window.events.minimized.set()
                return None
            None.pywebview_window.events.restored.set()
            return None
        if None.changed_mask == Gdk.WindowState.MAXIMIZED:
            if Gdk.WindowState.MAXIMIZED & window_state.new_window_state == Gdk.WindowState.MAXIMIZED:
                self.pywebview_window.events.maximized.set()
                return None
            None.pywebview_window.events.restored.set()
            return None

    
    def on_js_bridge_call(self, manager, message):
        body = json.loads(message.get_js_value().to_string())
        if body['funcName'] == '_pywebviewAlert':
            self.message_box(body['params'])
            return None
        None(self.pywebview_window, body['funcName'], body['params'], body['id'])

    
    def on_window_resize(self, window, allocation):
        if allocation.width != self._last_width or allocation.height != self._last_height:
            self._last_width = allocation.width
            self._last_height = allocation.height
            self.pywebview_window.events.resized.set(allocation.width, allocation.height)
            return None

    
    def on_window_configure(self, window, event):
        self.pywebview_window.events.moved.set(event.x, event.y)

    
    def on_webview_ready(self, arg1, arg2):
        if 'shown' in dir(self):
            self.shown.set()
            return None

    
    def on_response(self, resource, _):
        response = resource.get_response()
        headers = response.get_http_headers()
        original_headers = self._headers_to_dict(headers)
        url = resource.get_uri()
        response_ = Response(url, response.get_status_code(), original_headers)
        self.pywebview_window.events.response_received.set(response_)

    
    def on_request(self, webview, resource, request):
        pass
    # WARNING: Decompyle incomplete

    
    def on_load_finish(self, webview, status):
        if not webview.props.opacity:
            glib.idle_add(webview.set_opacity, 1)
        if not status == webkit.LoadEvent.FINISHED and self.request_headers_mutated:
            inject_pywebview(renderer, self.js_bridge.window)
        if self.request_headers_mutated:
            self.request_headers_mutated = False
            return None

    
    def on_download_started(self, session, download):
        download.connect('decide-destination', self.on_download_decide_destination)

    
    def on_download_decide_destination(self, download, suggested_filename):
        destination = self.create_file_dialog(FileDialog.SAVE, glib.get_user_special_dir(glib.UserDirectory.DIRECTORY_DOWNLOAD), False, suggested_filename, ())
        if destination:
            destination_uri = glib.filename_to_uri(destination[0])
            download.set_destination(destination_uri)
            return None
        None.cancel()

    
    def on_navigation(self, webview, decision, decision_type):
        if type(decision) == webkit.NavigationPolicyDecision:
            uri = decision.get_navigation_action().get_request().get_uri()
            if decision.get_navigation_action().get_frame_name() == '_blank':
                if settings['OPEN_EXTERNAL_LINKS_IN_BROWSER']:
                    webbrowser.open(uri, 2, True)
                    decision.ignore()
                    return None
                None.load_url(uri)
                return None
            return None
        if None(decision) == webkit.ResponsePolicyDecision:
            if not decision.is_mime_type_supported():
                self._download_filename = decision.get_response().get_suggested_filename()
                decision.download()
                return None
            None.use()
            return None

    
    def on_mouse_release(self, sender, event):
        self.move_progress = False

    
    def on_mouse_press(self, _, event):
        self.point_diff = zip(self.window.get_position(), [
            event.x_root,
            event.y_root])()
        self.move_progress = True

    
    def on_mouse_move(self, _, event):
        if self.move_progress:
            point = zip((event.x_root, event.y_root), self.point_diff)()
            self.window.move(point[0], point[1])
            return None

    
    def show(self):
        self.window.show_all()
        if gtk.main_level() == 0:
            if self.pywebview_window.hidden:
                self.window.hide()
                return None
            return None
        None.idle_add(self.window.show_all)

    
    def hide(self):
        glib.idle_add(self.window.hide)

    
    def destroy(self):
        self.window.emit('delete-event', Gdk.Event())

    
    def set_title(self, title):
        self.window.set_title(title)

    
    def toggle_fullscreen(self):
        if self.is_fullscreen:
            self.window.unfullscreen()
        else:
            self.window.fullscreen()
        self.is_fullscreen = not (self.is_fullscreen)

    
    def resize(self, width, height, fix_point):
        if fix_point & FixPoint.NORTH and fix_point & FixPoint.WEST:
            self.window.set_gravity(Gdk.Gravity.NORTH_WEST)
        elif fix_point & FixPoint.NORTH and fix_point & FixPoint.EAST:
            self.window.set_gravity(Gdk.Gravity.NORTH_EAST)
        elif fix_point & FixPoint.SOUTH and fix_point & FixPoint.EAST:
            self.window.set_gravity(Gdk.Gravity.SOUTH_EAST)
        elif fix_point & FixPoint.SOUTH and fix_point & FixPoint.WEST:
            self.window.set_gravity(Gdk.Gravity.SOUTH_WEST)
        elif fix_point & FixPoint.SOUTH:
            self.window.set_gravity(Gdk.Gravity.SOUTH)
        elif fix_point & FixPoint.NORTH:
            self.window.set_gravity(Gdk.Gravity.NORTH)
        elif fix_point & FixPoint.WEST:
            self.window.set_gravity(Gdk.Gravity.WEST)
        elif fix_point & FixPoint.EAST:
            self.window.set_gravity(Gdk.Gravity.EAST)
        self.window.resize(width, height)

    
    def move(self, x, y):
        self.window.move(self.screen.x + x, self.screen.y + y)

    
    def maximize(self):
        glib.idle_add(self.window.maximize)

    
    def minimize(self):
        glib.idle_add(self.window.iconify)

    
    def restore(self):
        pass
    # WARNING: Decompyle incomplete

    
    def create_confirmation_dialog(self, title, message):
        dialog = gtk.MessageDialog(parent = self.window, flags = gtk.DialogFlags.MODAL & gtk.DialogFlags.DESTROY_WITH_PARENT, type = gtk.MessageType.QUESTION, text = title, message_format = message, buttons = gtk.ButtonsType.OK_CANCEL)
        response = dialog.run()
        dialog.destroy()
        if response == gtk.ResponseType.OK:
            return True

    
    def create_file_dialog(self, dialog_type, directory, allow_multiple, save_filename, file_types):
        if dialog_type == FileDialog.FOLDER:
            gtk_dialog_type = gtk.FileChooserAction.SELECT_FOLDER
            title = self.localization['linux.openFolder']
            button = gtk.STOCK_OPEN
        elif dialog_type == FileDialog.OPEN:
            gtk_dialog_type = gtk.FileChooserAction.OPEN
            if allow_multiple:
                title = self.localization['linux.openFiles']
            else:
                title = self.localization['linux.openFile']
            button = gtk.STOCK_OPEN
        elif dialog_type == FileDialog.SAVE:
            gtk_dialog_type = gtk.FileChooserAction.SAVE
            title = self.localization['global.saveFile']
            button = gtk.STOCK_SAVE
        dialog = gtk.FileChooserDialog(title, self.window, gtk_dialog_type, (gtk.STOCK_CANCEL, gtk.ResponseType.CANCEL, button, gtk.ResponseType.OK))
        dialog.set_select_multiple(allow_multiple)
        dialog.set_current_folder(directory)
        self._add_file_filters(dialog, file_types)
        if dialog_type == FileDialog.SAVE:
            dialog.set_current_name(save_filename)
        response = dialog.run()
        if response == gtk.ResponseType.OK:
            if dialog_type == FileDialog.SAVE:
                file_name = (dialog.get_filename(),)
            else:
                file_name = dialog.get_filenames()
        else:
            file_name = None
        dialog.destroy()
        return file_name

    
    def _add_file_filters(self, dialog, file_types):
        for s in file_types:
            (description, extensions) = parse_file_type(s)
            f = gtk.FileFilter()
            f.set_name(description)
            for e in extensions.split(';'):
                f.add_pattern(e)
                dialog.add_filter(f)
                return None

    
    def clear_cookies(self):
        pass
    # WARNING: Decompyle incomplete

    
    def get_cookies(self):
        pass
    # WARNING: Decompyle incomplete

    
    def get_current_url(self):
        uri = self.webview.get_uri()
        return uri if uri != 'about:blank' else None

    
    def load_url(self, url):
        self.webview.load_uri(url)

    
    def load_html(self, content, base_uri):
        self.webview.load_html(content, base_uri)

    
    def evaluate_js(self, script, parse_json):
        pass
    # WARNING: Decompyle incomplete

    
    def message_box(self, message):
        dialog = gtk.MessageDialog(parent = self.window, flags = gtk.DialogFlags.MODAL & gtk.DialogFlags.DESTROY_WITH_PARENT, type = gtk.MessageType.INFO, buttons = gtk.ButtonsType.OK, message_format = message)
        dialog.run()
        dialog.destroy()

    
    def _convert_js_value(self, js_value):
        if js_value and js_value.is_null() or js_value.is_undefined():
            return None
        if None.is_boolean():
            return js_value.to_boolean()
        if None.is_number():
            return js_value.to_double()
        if None.is_string():
            return js_value.to_string()
        if None.is_object():
            return json.loads(js_value.to_json(2))
        None.error(f'''Unsupported JavaScriptCore.Value type: {js_value}''')
        return js_value.to_string()

    
    def _headers_to_dict(self, headers):
        pass
    # WARNING: Decompyle incomplete



def setup_app():
    pass
# WARNING: Decompyle incomplete


def create_window(window):
    pass
# WARNING: Decompyle incomplete


def set_title(title, uid):
    pass
# WARNING: Decompyle incomplete


def destroy_window(uid):
    pass
# WARNING: Decompyle incomplete


def toggle_fullscreen(uid):
    pass
# WARNING: Decompyle incomplete


def add_tls_cert(certfile):
    global cert
    cert = Gio.TlsCertificate.new_from_file(certfile)


def set_on_top(uid, top):
    pass
# WARNING: Decompyle incomplete


def resize(width, height, uid, fix_point):
    pass
# WARNING: Decompyle incomplete


def move(x, y, uid):
    pass
# WARNING: Decompyle incomplete


def hide(uid):
    i = BrowserView.instances.get(uid)
    if i:
        glib.idle_add(i.hide)
        return None


def show(uid):
    i = BrowserView.instances.get(uid)
    if i:
        glib.idle_add(i.show)
        return None


def maximize(uid):
    i = BrowserView.instances.get(uid)
    if i:
        glib.idle_add(i.maximize)
        return None


def minimize(uid):
    i = BrowserView.instances.get(uid)
    if i:
        glib.idle_add(i.minimize)
        return None


def restore(uid):
    i = BrowserView.instances.get(uid)
    if i:
        glib.idle_add(i.restore)
        return None


def clear_cookies(uid):
    i = BrowserView.instances.get(uid)
    if i:
        i.clear_cookies()
        return None


def get_cookies(uid):
    i = BrowserView.instances.get(uid)
    if i:
        cookies = i.get_cookies()
        return cookies


def get_current_url(uid):
    pass
# WARNING: Decompyle incomplete


def load_url(url, uid):
    pass
# WARNING: Decompyle incomplete


def load_html(content, base_uri, uid):
    pass
# WARNING: Decompyle incomplete


def create_confirmation_dialog(title, message, uid):
    pass
# WARNING: Decompyle incomplete


def create_menu(app_menu_list):
    pass
# WARNING: Decompyle incomplete


def get_active_window():
    active_window = None
    
    try:
        active_window = _app.get_active_window()
    except Exception:
        return None

    active_window_number = active_window.get_id()
    for uid, browser_view_instance in BrowserView.instances.items():
        if browser_view_instance.window.get_id() == active_window_number:
            
            return None, browser_view_instance.pywebview_window
        return None


def create_file_dialog(dialog_type, directory, allow_multiple, save_filename, file_types, uid):
    pass
# WARNING: Decompyle incomplete


def evaluate_js(script, uid, parse_json = (True,)):
    i = BrowserView.instances.get(uid)
    if i:
        return i.evaluate_js(script, parse_json)


def get_position(uid):
    pass
# WARNING: Decompyle incomplete


def get_size(uid):
    pass
# WARNING: Decompyle incomplete


def get_screens():
    pass
# WARNING: Decompyle incomplete


def configure_transparency(c):
    c.set_visual(c.get_screen().get_rgba_visual())
    c.override_background_color(gtk.StateFlags.ACTIVE, Gdk.RGBA(0, 0, 0, 0))
    c.override_background_color(gtk.StateFlags.BACKDROP, Gdk.RGBA(0, 0, 0, 0))
    c.override_background_color(gtk.StateFlags.DIR_LTR, Gdk.RGBA(0, 0, 0, 0))
    c.override_background_color(gtk.StateFlags.DIR_RTL, Gdk.RGBA(0, 0, 0, 0))
    c.override_background_color(gtk.StateFlags.FOCUSED, Gdk.RGBA(0, 0, 0, 0))
    c.override_background_color(gtk.StateFlags.INCONSISTENT, Gdk.RGBA(0, 0, 0, 0))
    c.override_background_color(gtk.StateFlags.INSENSITIVE, Gdk.RGBA(0, 0, 0, 0))
    c.override_background_color(gtk.StateFlags.NORMAL, Gdk.RGBA(0, 0, 0, 0))
    c.override_background_color(gtk.StateFlags.PRELIGHT, Gdk.RGBA(0, 0, 0, 0))
    c.override_background_color(gtk.StateFlags.SELECTED, Gdk.RGBA(0, 0, 0, 0))
    transparentWindowStyleProvider = gtk.CssProvider()
    transparentWindowStyleProvider.load_from_data(b'\n        GtkWindow {\n            background-color:rgba(0,0,0,0);\n            background-image:none;\n        }')
    c.get_style_context().add_provider(transparentWindowStyleProvider, gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

import json
import logging
from http.cookies import SimpleCookie
from threading import Semaphore
from urllib.parse import urlparse
from android.activity import _activity as activity
from android.runnable import run_on_ui_thread
from jnius import autoclass, cast
from webview import _state, settings
from webview.models import Request, Response
from webview.platforms.android.app import App
from webview.platforms.android.jclass import AlertDialogBuilder, Context, CookieManager, DownloadManagerRequest, Environment, KeyEvent, PyJavascriptInterface, PyWebChromeClient, PyWebViewClient, Uri, View, WebView
from webview.platforms.android.jinterface import DownloadListener, EventCallbackWrapper, JsApiCallbackWrapper, KeyListener, RequestInterceptor, ValueCallback
from webview.util import create_cookie, inject_pywebview, js_bridge_call
logger = logging.getLogger('pywebview')
renderer = 'android-webkit'
app = None

class BrowserView:
    
    def __init__(self, window):
        self.pywebview_window = window
        self.webview = None
        self.dialog = None
        self.pywebview_window.native = self
        self.is_fullscreen = False
        self.create_webview()

    create_webview = (lambda self: pass# WARNING: Decompyle incomplete
)()
    
    def _on_request(self = None, url = None, method = run_on_ui_thread, headers_json = ('url', str, 'method', str, 'headers_json', str)):
        headers = json.loads(headers_json) if headers_json else { }
        original_headers = headers.copy()
        request = Request(url, method, headers)
        self.pywebview_window.events.request_sent.set(request)
        if request.headers != original_headers:
            logger.debug('Request headers mutated. Original: %s, Mutated: %s', original_headers, request.headers)
            return json.dumps(request.headers)

    
    def _on_response(self = None, url = None, status_code = None, headers_json = ('url', str, 'status_code', int, 'headers_json', str)):
        headers = json.loads(headers_json) if headers_json else { }
        response = Response(url, status_code, headers)
        self.pywebview_window.events.response_received.set(response)

    
    def dismiss(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _quit_confirmation(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _back_pressed(self, v, key_code, event):
        if not event.getAction() == KeyEvent.ACTION_DOWN or key_code == KeyEvent.KEYCODE_BACK:
            return False
        if None.webview.canGoBack():
            self.webview.goBack()
        elif self.pywebview_window.events.closing.set():
            pass
        elif self.pywebview_window.confirm_close:
            self._quit_confirmation()
        else:
            app.pause()
            self.pywebview_window.events.closed.set()
        return True

    
    def get_size(self):
        pass
    # WARNING: Decompyle incomplete

    
    def get_url(self):
        pass
    # WARNING: Decompyle incomplete

    load_url = (lambda self, url: self.webview.loadUrl(url))()
    load_data_with_base_url = (lambda self, base_uri, html_content: self.webview.loadDataWithBaseURL(base_uri, html_content, 'text/html', 'UTF-8', None))()


class AndroidApp(App):
    pass
# WARNING: Decompyle incomplete


def create_file_dialog(*_):
    logger.warning('Creating file dialogs is not supported on Android')


def create_window(window):
    global app
    if app:
        logger.error('Multiple windows are not supported on Android')
        return None
    app = None(window)
    app.run()


def setup_app():
    pass


def load_url(url, _):
    app.view._cookies = []
    app.view.load_url(url)


def load_html(html_content, base_uri, _):
    app.view._cookies = []
    app.view.load_data_with_base_url(base_uri, html_content)


def evaluate_js(js_code, _, parse_json = (True,)):
    pass
# WARNING: Decompyle incomplete


def clear_cookies(_):
    pass
# WARNING: Decompyle incomplete


def get_cookies(_):
    pass
# WARNING: Decompyle incomplete


def get_current_url(_):
    pass
# WARNING: Decompyle incomplete


def get_screens():
    logger.warning('Screen information is not supported on Android')
    return []


def get_size(_):
    return app.view.get_size()


def get_position(_):
    return (0, 0)


def show(_):
    logger.warning('Showing window is not supported on Android')


def hide(_):
    app.pause()


def minimize(_):
    app.pause()


def move(_):
    logger.warning('Moving window is not supported on Android')


def restore(_):
    logger.warning('Restoring window is not supported on Android')


def resize(width, height, _, fix_point):
    logger.warning('Resizing window is not supported on Android')


def destroy_window():
    app.stop()


def set_title(title, _):
    logger.warning('Changing app title is not supported on Android')


def set_on_top(_, on_top):
    logger.warning('Always on top mode is not supported on Android')

toggle_fullscreen = (lambda _: is_fullscreen = app.view.is_fullscreentry:
if not is_fullscreen:
option = View.SYSTEM_UI_FLAG_FULLSCREEN | View.SYSTEM_UI_FLAG_HIDE_NAVIGATION | View.SYSTEM_UI_FLAG_IMMERSIVE_STICKY | View.SYSTEM_UI_FLAG_LAYOUT_STABLE | View.SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION | View.SYSTEM_UI_FLAG_LAYOUT_FULLSCREENapp.view.webview.setSystemUiVisibility(option)app.view.is_fullscreen = TrueNoneoption = None.SYSTEM_UI_FLAG_VISIBLEapp.view.webview.setSystemUiVisibility(option)app.view.is_fullscreen = FalseNoneexcept Exception:
e = Nonelogger.error(f'''Error toggling fullscreen: {e}''')e = Nonedel eNonee = Nonedel e)()

def add_tls_cert(certfile):
    pass

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: cef.pyc (Python 3.11)

import json
import logging
import os
import shutil
import sys
import webbrowser
from copy import copy
from ctypes import windll
from functools import wraps
from threading import Event
from time import sleep
from cefpython3 import cefpython as cef
from webview import _state, settings
from webview.util import DEFAULT_HTML, create_cookie, inject_pywebview, js_bridge_call
sys.excepthook = cef.ExceptHook
instances = { }
logger = logging.getLogger(__name__)
browser_settings = { }
command_line_switches = { }
renderer = 'cef'

def _set_dpi_mode(enabled):
    ''' '''
    import winreg
    
    try:
        dpi_support = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\Microsoft\\Windows NT\\CurrentVersion\\AppCompatFlags\\Layers', 0, winreg.KEY_ALL_ACCESS)
    except OSError:
        dpi_support = winreg.CreateKeyEx(winreg.HKEY_CURRENT_USER, 'Software\\Microsoft\\Windows NT\\CurrentVersion\\AppCompatFlags\\Layers', 0, winreg.KEY_ALL_ACCESS)

    
    try:
        subprocess_path = os.path.join(sys._MEIPASS, 'subprocess.exe')
    except:
        subprocess_path = os.path.join(os.path.dirname(cef.__file__), 'subprocess.exe')

    if enabled:
        winreg.SetValueEx(dpi_support, subprocess_path, 0, winreg.REG_SZ, '~HIGHDPIAWARE')
    else:
        winreg.DeleteValue(dpi_support, subprocess_path)
    winreg.CloseKey(dpi_support)


class JSBridge:
    
    def __init__(self, window, eval_events):
        self.results = { }
        self.window = window
        self.eval_events = eval_events

    
    def return_result(self, result, uid):
        self.results[uid] = json.loads(result) if result else None
        self.eval_events[uid].set()

    
    def call(self, func_name, param, value_id):
        js_bridge_call(self.window, func_name, json.loads(param), value_id)



class CookieVisitor:
    
    def Visit(self, cookie, count, total, delete_cookie_out):
        data = {
            'name': cookie.GetName(),
            'value': cookie.GetValue(),
            'path': cookie.GetPath(),
            'domain': cookie.GetDomain(),
            'expires': cookie.GetExpires().strftime('%a, %d %b %Y %H:%M:%S GMT'),
            'secure': cookie.GetSecure(),
            'httponly': cookie.GetHttpOnly() }
        cookie = create_cookie(data)
        self.cookies.append(cookie)
        if count + 1 == total:
            self.lock.set()
        return True



class Browser:
    
    def __init__(self, window, handle, browser, parent):
        self.window = window
        self.handle = handle
        self.browser = browser
        self.parent = parent
        self.uid = window.uid
        self.loaded = window.events.loaded
        self.shown = window.events.shown
        self.inner_hwnd = self.browser.GetWindowHandle()
        self.eval_events = { }
        self.js_bridge = JSBridge(window, self.eval_events)
        self.initialized = False

    
    def initialize(self):
        if self.initialized:
            return None
        self.cookie_manager = None.CookieManager.GetGlobalManager()
        self.cookie_visitor = CookieVisitor()
        self.browser.GetJavascriptBindings().Rebind()
        inject_pywebview('cef', self.window)
        sleep(0.1)
        self.initialized = True

    
    def close(self):
        self.browser.CloseBrowser(True)

    
    def resize(self, width, height):
        screen = self.parent.RectangleToScreen(self.parent.ClientRectangle)
        height_diff = (screen.Top - self.parent.Top) + 12
        width_diff = (self.parent.Right - screen.Right) + 12
        windll.user32.SetWindowPos(self.inner_hwnd, 0, 0, 0, width - width_diff, height - height_diff, 22)
        self.browser.NotifyMoveOrResizeStarted()

    
    def evaluate_js(self, code, unique_id, parse_json):
        self.eval_events[unique_id] = Event()
        if unique_id:
            eval_script = f'''\n                try {{\n                    {code}\n                }} catch(e) {{\n                    window.external.return_result(null, \'{unique_id}\');\n                }}\n            '''
            self.browser.ExecuteJavascript(eval_script)
            self.eval_events[unique_id].wait()
            result = copy(self.js_bridge.results[unique_id])
            del self.eval_events[unique_id]
            del self.js_bridge.results[unique_id]
            return result
        None.browser.ExecuteJavascript(code)

    
    def clear_cookies(self):
        self.cookie_manager.DeleteCookies('', '')
        self.cookie_manager.FlushStore()

    
    def get_cookies(self):
        self.cookie_visitor.cookies = []
        self.cookie_visitor.lock = Event()
        self.cookie_manager.VisitUrlCookies(self.browser.GetUrl(), True, self.cookie_visitor)
        self.cookie_visitor.lock.wait()
        return self.cookie_visitor.cookies

    
    def get_current_url(self):
        return self.browser.GetUrl()

    
    def load_url(self, url):
        self.initialized = False
        self.browser.LoadUrl(url)

    
    def load_html(self, html):
        self.initialized = False
        self.browser.LoadUrl(f'''data:text/html,{html}''')

    
    def focus(self):
        self.browser.SendFocusEvent(True)



def find_instance(browser):
    for instance in instances.values():
        if instance.browser is browser:
            
            return None, instance
        return None


class LoadHandler:
    
    def OnBeforePopup(self, **args):
        url = args['target_url']
        user_gesture = args['user_gesture']
        if user_gesture:
            webbrowser.open(url)
        return True

    
    def OnLoadingStateChange(self, browser, is_loading, **_):
        instance = find_instance(browser)
    # WARNING: Decompyle incomplete



def _cef_call(func):
    pass
# WARNING: Decompyle incomplete


def init(_, cache_dir):
    pass
# WARNING: Decompyle incomplete


def create_browser(window, handle, alert_func, parent):
    pass
# WARNING: Decompyle incomplete

focus = (lambda uid: instance = instances[uid]instance.focus())()
load_html = (lambda html, uid: instance = instances[uid]instance.load_html(html))()
load_url = (lambda url, uid: instance = instances[uid]instance.load_url(url))()
evaluate_js = (lambda code, unique_id, parse_json, uid: instance = instances[uid]instance.evaluate_js(code, unique_id, parse_json))()
clear_cookies = (lambda uid: instance = instances[uid]instance.clear_cookies())()
get_cookies = (lambda uid: instance = instances[uid]instance.get_cookies())()
get_current_url = (lambda uid: instance = instances[uid]url = instance.get_current_url()if url.startswith('data:text/html,'):
None)()
resize = (lambda width, height, uid: instance = instances[uid]instance.resize(width, height))()
close_window = (lambda uid: instance = instances[uid]instance.close()del instances[uid])()

def shutdown():

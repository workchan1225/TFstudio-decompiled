# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: edgechromium.pyc (Python 3.11)

import json
import logging
import os
import shutil
import webbrowser
import winreg
from threading import Semaphore
import clr
from webview import Window, _state
from webview import settings as webview_settings
from webview.dom import _dnd_state
from webview.models import Request, Response
from webview.util import DEFAULT_HTML, create_cookie, get_app_root, inject_pywebview, interop_dll_path, js_bridge_call
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Collections')
clr.AddReference('System.Threading')

Forms
from System import Action, Convert, Func, Object, String, Type, Uri
Convert = Convert
Func = Func
Object = Object
String = String
Type = Type
Uri = Uri
import System.Windows.Forms, Windows
from System.Collections.Generic import List
from System.Diagnostics import Process
from System.Drawing import Color
from System.Globalization import CultureInfo
from System.Threading.Tasks import Task, TaskScheduler
clr.AddReference(interop_dll_path('Microsoft.Web.WebView2.Core.dll'))
clr.AddReference(interop_dll_path('Microsoft.Web.WebView2.WinForms.dll'))
from Microsoft.Web.WebView2.Core import CoreWebView2Cookie, CoreWebView2ServerCertificateErrorAction, CoreWebView2WebResourceContext
from Microsoft.Web.WebView2.WinForms import CoreWebView2CreationProperties, WebView2
for platform in ('win-arm64', 'win-x64', 'win-x86'):
    logging.getLogger('pywebview') = None
    renderer = 'edgechromium'
    
    class EdgeChrome:
        
        def __init__(self = None, form = None, window = None, cache_dir = ('form', WinForms.Form, 'window', Window, 'cache_dir', str)):
            self.pywebview_window = window
            self.webview = WebView2()
            props = CoreWebView2CreationProperties()
            runtime_path = webview_settings['WEBVIEW2_RUNTIME_PATH']
            if runtime_path:
                if not os.path.isabs(runtime_path):
                    runtime_path = os.path.join(get_app_root(), runtime_path)
                if os.path.exists(runtime_path):
                    props.BrowserExecutableFolder = runtime_path
                    logger.debug(f'''Using custom WebView2 runtime: {runtime_path}''')
                else:
                    logger.warning(f'''Custom WebView2 runtime path does not exist: {runtime_path}. Using system WebView2.''')
            props.UserDataFolder = cache_dir
            self.user_data_folder = props.UserDataFolder
            props.set_IsInPrivateModeEnabled(_state['private_mode'])
            props.AdditionalBrowserArguments = '--disable-features=ElasticOverscroll'
            if webview_settings['ALLOW_FILE_URLS']:
                pass
        # WARNING: Decompyle incomplete

        
        def clear_user_data(self):
            if not _state['private_mode']:
                return None
            process_id = None.ToInt32(self.webview.CoreWebView2.BrowserProcessId)
            process = Process.GetProcessById(process_id)
            self.webview.Dispose()
            process.WaitForExit(3000)
            
            try:
                shutil.rmtree(self.user_data_folder)
                return None
            except Exception:
                e = None
                logger.warning(f'''Failed to delete user data folder: {e}''')
                e = None
                del e
                return None
                e = None
                del e


        
        def evaluate_js(self = None, script = None, parse_json = None):
            pass
        # WARNING: Decompyle incomplete

        
        def clear_cookies(self):
            self.webview.CoreWebView2.CookieManager.DeleteAllCookies()

        
        def get_cookies(self, cookies, semaphore):
            pass
        # WARNING: Decompyle incomplete

        
        def get_current_url(self):
            return self.url

        
        def load_html(self, content, _):
            self.html = content
            self.ishtml = True
            if self.webview.CoreWebView2:
                self.webview.CoreWebView2.NavigateToString(self.html)
                return None
            None.webview.EnsureCoreWebView2Async(None)

        
        def load_url(self = None, url = None):
            self.ishtml = False
            self.webview.Source = Uri(url)

        
        def on_certificate_error(self, _, args):
            args.set_Action(CoreWebView2ServerCertificateErrorAction.AlwaysAllow)

        
        def on_script_notify(self, _, args):
            pass
        # WARNING: Decompyle incomplete

        
        def on_new_window_request(self, sender, args):
            args.set_Handled(True)
            if webview_settings['OPEN_EXTERNAL_LINKS_IN_BROWSER']:
                webbrowser.open(str(args.get_Uri()))
                return None
            None.load_url(str(args.get_Uri()))

        
        def on_source_changed(self, sender, args):
            self.url = sender.Source
            self.ishtml = False

        
        def on_webview_ready(self, sender, args):
            if not args.IsSuccess:
                logger.error('WebView2 initialization failed with exception:\n ' + str(args.InitializationException))
                return None
            sender.CoreWebView2.AddWebResourceRequestedFilter('*', CoreWebView2WebResourceContext.All)
            if _state['ssl'] or webview_settings['IGNORE_SSL_ERRORS']:
                pass
            sender.CoreWebView2.Settings = sender.CoreWebView2, sender.CoreWebView2.DownloadStarting += self.on_download_starting, .DownloadStarting
            settings.AreBrowserAcceleratorKeysEnabled = _state['debug']
            settings.AreDefaultContextMenusEnabled = _state['debug']
            settings.AreDefaultScriptDialogsEnabled = True
            settings.AreDevToolsEnabled = _state['debug']
            settings.IsBuiltInErrorPageEnabled = True
            settings.IsScriptEnabled = True
            settings.IsWebMessageEnabled = True
            settings.IsStatusBarEnabled = _state['debug']
            settings.IsSwipeNavigationEnabled = False
            settings.IsZoomControlEnabled = True
            if _state['user_agent']:
                settings.UserAgent = _state['user_agent']
            if _state['private_mode']:
                sender.CoreWebView2.CookieManager.DeleteAllCookies()
            if self.pywebview_window.real_url:
                self.load_url(self.pywebview_window.real_url)
            elif self.pywebview_window.html:
                self.html = self.pywebview_window.html
                self.load_html(self.pywebview_window.html, '')
            else:
                self.load_html(DEFAULT_HTML, '')
            if _state['debug'] or webview_settings['OPEN_DEVTOOLS_IN_DEBUG']:
                sender.CoreWebView2.OpenDevToolsWindow()
                return None
            return sender.CoreWebView2, sender.CoreWebView2.ServerCertificateErrorDetected += self.on_certificate_error, .ServerCertificateErrorDetected

        
        def on_download_starting(self, sender, args):
            if not webview_settings['ALLOW_DOWNLOADS']:
                args.Cancel = True
                return None
            dialog = None.SaveFileDialog()
            
            try:
                windows_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Shell Folders')
                dialog.InitialDirectory = winreg.QueryValueEx(windows_key, '{374DE290-123F-4565-9164-39C4925E467B}')[0]
                
                try:
                    None(None, None)
                with None:
                    if not None:
                        
                        try:
                            
                            try:
                                pass
                            except Exception:
                                e = None
                                logger.exception(e)
                                e = None
                                del e
                            except:
                                e = None
                                del e

                            dialog.Filter = self.pywebview_window.localization['windows.fileFilter.allFiles'] + ' (*.*)|*.*'
                            dialog.RestoreDirectory = True
                            dialog.FileName = os.path.basename(args.ResultFilePath)
                            result = dialog.ShowDialog(self.form)
                            if result == WinForms.DialogResult.OK:
                                args.ResultFilePath = dialog.FileName
                                return None
                            args.Cancel = None
                            return None




        
        def on_navigation_start(self, sender, args):
            if self.pywebview_window.transparent:
                self.form.Show()
                self.form.Activate()
                return None

        
        def on_web_resource_response(self, sender, args):
            headers = { }
            for header in args.Response.Headers.GetEnumerator():
                headers[header.Key] = header.Value
                response = Response(str(args.Request.Uri), args.Response.StatusCode, headers)
                self.pywebview_window.events.response_received.set(response)
                return None

        
        def on_web_resource_request(self, sender, args):
            pass
        # WARNING: Decompyle incomplete

        
        def on_navigation_completed(self, sender, _):
            url = str(sender.Source)
            self.url = None if self.ishtml else url
            inject_pywebview(renderer, self.pywebview_window)


    return None

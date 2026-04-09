# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: cocoa.pyc (Python 3.11)

from __future__ import annotations
import json
import logging
import os
import urllib
import uuid
import webbrowser
from threading import Semaphore, Thread, main_thread
import AppKit
import Foundation
import WebKit
from objc import nil, super
from PyObjCTools import AppHelper
from webview import FileDialog, _state, windows
from webview import settings as webview_settings
from webview.dom import _dnd_state
from webview.menu import Menu, MenuAction, MenuSeparator
from webview.models import Request, Response
from webview.screen import Screen
from webview.util import DEFAULT_HTML, create_cookie, inject_pywebview, js_bridge_call, parse_file_type, stringify_headers
from webview.window import FixPoint
bundle = AppKit.NSBundle.mainBundle()
if not bundle.localizedInfoDictionary():
    info = bundle.infoDictionary()
    info['NSAppTransportSecurity'] = {
        'NSAllowsArbitraryLoads': Foundation.YES }
    info['NSRequiresAquaSystemAppearance'] = Foundation.NO
    
    try:
        NSFullSizeContentViewWindowMask = AppKit.NSFullSizeContentViewWindowMask
    except AttributeError:
        NSFullSizeContentViewWindowMask = 32768

    
    try:
        NSWindowTitleHidden = AppKit.NSWindowTitleHidden
    except AttributeError:
        NSWindowTitleHidden = 1

    logger = logging.getLogger('pywebview')
    logger.debug('Using Cocoa')
    renderer = 'wkwebview'
    
    class BrowserView:
        instances = { }
        app = AppKit.NSApplication.sharedApplication()
        app.setActivationPolicy_(0)
        current_menu = None
        cascade_loc = Foundation.NSMakePoint(100, 0)
        
        class AppDelegate(AppKit.NSObject):
            
            def applicationShouldTerminate_(self, app):
                should_close = True
                for i in BrowserView.instances.values():
                    if should_close:
                        should_close = BrowserView.should_close(i.pywebview_window)
                        continue
                return Foundation.YES if should_close else Foundation.NO

            
            def applicationSupportsSecureRestorableState_(self, app):
                return Foundation.YES


        
        class WindowHost(AppKit.NSWindow):
            
            def canBecomeKeyWindow(self):
                return self.focus


        
        class WindowDelegate(AppKit.NSObject):
            
            def windowDidBecomeKey_(self, notification):
                i = BrowserView.get_instance('window', notification.object())
                if i.menu or BrowserView.current_menu != i.menu:
                    BrowserView.current_menu = i.menu
                    new_menu = i._recreate_menus(BrowserView.current_menu)
                    BrowserView.app.setMainMenu_(new_menu)
                    return None
                return None

            
            def windowShouldClose_(self, window):
                i = BrowserView.get_instance('window', window)
                return BrowserView.should_close(i.pywebview_window)

            
            def windowWillClose_(self, notification):
                i = BrowserView.get_instance('window', notification.object())
                del BrowserView.instances[i.uid]
                if i.pywebview_window in windows:
                    windows.remove(i.pywebview_window)
                i.webview.setNavigationDelegate_(None)
                i.webview.setUIDelegate_(None)
                i.webview.loadHTMLString_baseURL_('', None)
                i.webview.removeFromSuperview()
                i.webview = None
                i.closed.set()
                if BrowserView.instances == { }:
                    BrowserView.app.stop_(self)
                    BrowserView.app.abortModal()
                    return None

            
            def windowDidResize_(self, notification):
                i = BrowserView.get_instance('window', notification.object())
                if i:
                    size = i.window.frame().size
                    i.pywebview_window.events.resized.set(size.width, size.height)
                    return None

            
            def windowDidMiniaturize_(self, notification):
                i = BrowserView.get_instance('window', notification.object())
                if i:
                    i.pywebview_window.events.minimized.set()
                    return None

            
            def windowDidDeminiaturize_(self, notification):
                i = BrowserView.get_instance('window', notification.object())
                if i:
                    i.pywebview_window.events.restored.set()
                    return None

            
            def windowDidEnterFullScreen_(self, notification):
                i = BrowserView.get_instance('window', notification.object())
                if i:
                    i.pywebview_window.events.maximized.set()
                    return None

            
            def windowDidExitFullScreen_(self, notification):
                i = BrowserView.get_instance('window', notification.object())
                if i:
                    i.pywebview_window.events.restored.set()
                    return None

            
            def windowDidMove_(self, notification):
                i = BrowserView.get_instance('window', notification.object())
                if i:
                    frame = i.window.frame()
                    screen = i.window.screen().frame()
                    flipped_y = screen.size.height - frame.size.height - frame.origin.y
                    i.pywebview_window.events.moved.set(frame.origin.x, flipped_y)
                    return None


        
        class JSBridge(AppKit.NSObject):
            pass
        # WARNING: Decompyle incomplete

        
        class DownloadDelegate(AppKit.NSObject):
            
            def download_decideDestinationUsingResponse_suggestedFilename_completionHandler_(self, download, decideDestinationUsingResponse, suggestedFilename, completionHandler):
                save_dlg = AppKit.NSSavePanel.savePanel()
                directory = Foundation.NSSearchPathForDirectoriesInDomains(Foundation.NSDownloadsDirectory, Foundation.NSUserDomainMask, True)[0]
                save_dlg.setDirectoryURL_(Foundation.NSURL.fileURLWithPath_(directory))
                save_dlg.setNameFieldStringValue_(suggestedFilename)
                if save_dlg.runModal() == AppKit.NSFileHandlingPanelOKButton:
                    filename = save_dlg.filename()
                    url = Foundation.NSURL.fileURLWithPath_(filename)
                    completionHandler(url)
                    return None
                completionHandler(None)


        
        class BrowserDelegate(AppKit.NSObject):
            
            def webView_runJavaScriptAlertPanelWithMessage_initiatedByFrame_completionHandler_(self, webview, message, frame, handler):
                AppKit.NSRunningApplication.currentApplication().activateWithOptions_(AppKit.NSApplicationActivateIgnoringOtherApps)
                alert = AppKit.NSAlert.alloc().init()
                alert.setInformativeText_(str(message))
                alert.runModal()
                handler()

            
            def webView_didReceiveAuthenticationChallenge_completionHandler_(self, webview, challenge, handler):
                if webview_settings['IGNORE_SSL_ERRORS'] or _state['ssl']:
                    credential = AppKit.NSURLCredential.credentialForTrust_(challenge.protectionSpace().serverTrust())
                    handler(AppKit.NSURLSessionAuthChallengeUseCredential, credential)
                    return None
                handler(AppKit.NSURLSessionAuthChallengePerformDefaultHandling, nil)

            
            def webView_runJavaScriptConfirmPanelWithMessage_initiatedByFrame_completionHandler_(self, webview, message, frame, handler):
                i = BrowserView.get_instance('webview', webview)
                ok = i.localization['global.ok']
                cancel = i.localization['global.cancel']
                result = BrowserView.display_confirmation_dialog(ok, cancel, message)
                handler(result)

            
            def webView_runJavaScriptTextInputPanelWithPrompt_defaultText_initiatedByFrame_completionHandler_(self, webview, prompt, default_text, frame, handler):
                i = BrowserView.get_instance('webview', webview)
                ok = i.localization['global.ok']
                cancel = i.localization['global.cancel']
                result = BrowserView.display_input_dialog(ok, cancel, prompt, default_text)
                handler(result)

            
            def webView_runOpenPanelWithParameters_initiatedByFrame_completionHandler_(self, webview, param, frame, handler):
                i = list(BrowserView.instances.values())[0]
                file_filter = param._acceptedMIMETypes()
                files = i.create_file_dialog(FileDialog.OPEN, '', param.allowsMultipleSelection(), '', file_filter, main_thread = True)
                if files:
                    urls = files()
                    handler(urls)
                    return None
                handler(nil)

            
            def webView_createWebViewWithConfiguration_forNavigationAction_windowFeatures_(self, webview, config, action, features):
                if action.navigationType() == getattr(WebKit, 'WKNavigationTypeLinkActivated', 0):
                    if webview_settings['OPEN_EXTERNAL_LINKS_IN_BROWSER']:
                        webbrowser.open(action.request().URL().absoluteString(), 2, True)
                    else:
                        webview.loadRequest_(action.request())
                return nil

            
            def webView_decidePolicyForNavigationAction_decisionHandler_(self, webview, action, handler):
                event = AppKit.NSApp.currentEvent()
                if action.shouldPerformDownload() and webview_settings['ALLOW_DOWNLOADS']:
                    handler(getattr(WebKit, 'WKNavigationActionPolicyDownload', 2))
                    return None
                if action.navigationType() == getattr(WebKit, 'WKNavigationTypeBackForward', 2) and event and event.type() == AppKit.NSKeyDown and event.keyCode() == 51:
                    handler(getattr(WebKit, 'WKNavigationActionPolicyCancel', 0))
                    return None
                request = None.request()
                url = request.URL()
                original_headers = dict(request.allHTTPHeaderFields())
                i = BrowserView.get_instance('webview', webview)
                if len(i.pywebview_window.events.request_sent) > 0 and 'X-Handled' not in original_headers and str(url) != 'about:blank':
                    request_ = Request(str(url), request.HTTPMethod(), original_headers)
                    i.pywebview_window.events.request_sent.set(request_)
                    request_.headers['X-Handled'] = 'true'
                    new_request = Foundation.NSMutableURLRequest.requestWithURL_(url)
                    new_request.setHTTPMethod_(request.HTTPMethod())
                    new_request.setAllHTTPHeaderFields_(AppKit.NSDictionary(stringify_headers(request_.headers)))
                    new_request.setHTTPBody_(request.HTTPBody())
                    new_request.setHTTPBodyStream_(request.HTTPBodyStream())
                    new_request.setHTTPShouldHandleCookies_(request.HTTPShouldHandleCookies())
                    new_request.setHTTPShouldUsePipelining_(request.HTTPShouldUsePipelining())
                    new_request.setMainDocumentURL_(request.mainDocumentURL())
                    new_request.setNetworkServiceType_(request.networkServiceType())
                    webview.loadRequest_(new_request)
                    handler(getattr(WebKit, 'WKNavigationActionPolicyCancel', 1))
                    return None
                handler(getattr(WebKit, 'WKNavigationActionPolicyAllow', 1))

            
            def webView_navigationAction_didBecomeDownload_(self, webview, navigationAction, download):
                download.setDelegate_(BrowserView.DownloadDelegate.alloc().init().retain())

            
            def webView_decidePolicyForNavigationResponse_decisionHandler_(self, webview, navigationResponse, decisionHandler):
                if navigationResponse.canShowMIMEType():
                    response_ = navigationResponse.response()
                    headers = dict(response_.allHeaderFields())
                    response = Response(response_.URL().absoluteString(), response_.statusCode(), headers)
                    webview.pywebview_window.events.response_received.set(response)
                    decisionHandler(WebKit.WKNavigationResponsePolicyAllow)
                    return None
                if None['ALLOW_DOWNLOADS']:
                    decisionHandler(WebKit.WKNavigationResponsePolicyCancel)
                    save_filename = navigationResponse.response().suggestedFilename()
                    save_dlg = AppKit.NSSavePanel.savePanel()
                    save_dlg.setTitle_(webview.pywebview_window.localization['global.saveFile'])
                    directory = Foundation.NSSearchPathForDirectoriesInDomains(Foundation.NSDownloadsDirectory, Foundation.NSUserDomainMask, True)[0]
                    save_dlg.setDirectoryURL_(Foundation.NSURL.fileURLWithPath_(directory))
                    if save_filename:
                        save_dlg.setNameFieldStringValue_(save_filename)
                    if save_dlg.runModal() == AppKit.NSFileHandlingPanelOKButton:
                        self._file_name = save_dlg.filename()
                        dataTask = Foundation.NSURLSession.sharedSession().downloadTaskWithURL_completionHandler_(navigationResponse.response().URL(), self.download_completionHandler_error_)
                        dataTask.resume()
                        return None
                    self._file_name = None
                    return None
                decisionHandler(WebKit.WKNavigationResponsePolicyCancel)

            
            def download_completionHandler_error_(self, temporaryLocation, response, error):
                pass
            # WARNING: Decompyle incomplete

            
            def webView_didFinishNavigation_(self, webview, nav):
                i = BrowserView.get_instance('webview', webview)
                if i:
                    if not webview.window():
                        i.window.setContentView_(webview)
                        i.window.makeFirstResponder_(webview)
                    inject_pywebview('cocoa', i.js_bridge.window)
                    if _state['debug'] or webview_settings['OPEN_DEVTOOLS_IN_DEBUG']:
                        BrowserView._open_web_inspector(webview)
                        return None
                    return None
                return None

            
            def userContentController_didReceiveScriptMessage_(self, controller, message):
                if message.body() == 'print':
                    i = BrowserView.get_instance('_browserDelegate', self)
                    BrowserView.print_webview(i.webview)
                    return None


        
        class FileFilterChooser(AppKit.NSPopUpButton):
            pass
        # WARNING: Decompyle incomplete

        
        class WebKitHost(WebKit.WKWebView):
            pass
        # WARNING: Decompyle incomplete

        
        def __init__(self, window):
            BrowserView.instances[window.uid] = self
            self.uid = window.uid
            self.pywebview_window = window
            self.js_bridge = None
            self._file_name = None
            self._file_name_semaphore = Semaphore(0)
            self._current_url_semaphore = Semaphore(0)
            self.closed = window.events.closed
            self.closing = window.events.closing
            self.shown = window.events.shown
            self.loaded = window.events.loaded
            self.confirm_close = window.confirm_close
            self.title = window.title
            self.is_fullscreen = False
            self.hidden = window.hidden
            self.minimized = window.minimized
            self.maximized = window.maximized
            self.localization = window.localization
            if window.screen:
                self.screen = window.screen.frame
            else:
                self.screen = AppKit.NSScreen.mainScreen().frame()
            rect = AppKit.NSMakeRect(0, 0, window.initial_width, window.initial_height)
            window_mask = AppKit.NSTitledWindowMask | AppKit.NSClosableWindowMask | AppKit.NSMiniaturizableWindowMask
            if window.resizable:
                window_mask = window_mask | AppKit.NSResizableWindowMask
            if window.frameless:
                window_mask = window_mask | NSFullSizeContentViewWindowMask | AppKit.NSTexturedBackgroundWindowMask
            if not window.menu:
                self.menu = _state['menu']
                self.window = BrowserView.WindowHost.alloc().initWithContentRect_styleMask_backing_defer_(rect, window_mask, AppKit.NSBackingStoreBuffered, False).retain()
                self.pywebview_window.native = self.window
                self.window.focus = window.focus
                self.window.setTitle_(window.title)
                self.window.setMinSize_(AppKit.NSSize(window.min_size[0], window.min_size[1]))
                self.window.setAnimationBehavior_(AppKit.NSWindowAnimationBehaviorDocumentWindow)
                BrowserView.cascade_loc = self.window.cascadeTopLeftFromPoint_(BrowserView.cascade_loc)
                frame = self.window.frame()
                frame.size.width = window.initial_width
                frame.size.height = window.initial_height
                self.window.setFrame_display_(frame, True)
                config = WebKit.WKWebViewConfiguration.alloc().init()
                self.webview = BrowserView.WebKitHost.alloc().initWithFrame_configuration_(rect, config).retain()
                self.webview.pywebview_window = window
                self._browserDelegate = BrowserView.BrowserDelegate.alloc().init().retain()
                self._windowDelegate = BrowserView.WindowDelegate.alloc().init().retain()
                self._appDelegate = BrowserView.AppDelegate.alloc().init().retain()
                BrowserView.app.setDelegate_(self._appDelegate)
                self.webview.setUIDelegate_(self._browserDelegate)
                self.webview.setNavigationDelegate_(self._browserDelegate)
                self.window.setDelegate_(self._windowDelegate)
                config.userContentController().addScriptMessageHandler_name_(self._browserDelegate, 'browserDelegate')
                self.datastore = WebKit.WKWebsiteDataStore.defaultDataStore()
                if _state['private_mode']:
                    
                    def dummy_completion_handler():
                        pass

                    data_types = WebKit.WKWebsiteDataStore.allWebsiteDataTypes()
                    from_start = WebKit.NSDate.dateWithTimeIntervalSince1970_(0)
                    config.setWebsiteDataStore_(self.datastore)
                    self.datastore.removeDataOfTypes_modifiedSince_completionHandler_(data_types, from_start, dummy_completion_handler)
                else:
                    config.setWebsiteDataStore_(self.datastore)
            
            try:
                config.preferences().setValue_forKey_(False, 'backspaceKeyNavigationEnabled')
            except KeyError:
                pass

            config.preferences().setValue_forKey_(webview_settings['ALLOW_FILE_URLS'], 'allowFileAccessFromFileURLs')
            if _state['debug']:
                config.preferences().setValue_forKey_(True, 'developerExtrasEnabled')
            self.js_bridge = BrowserView.JSBridge.alloc().initWithObject_(window)
            config.userContentController().addScriptMessageHandler_name_(self.js_bridge, 'jsBridge')
            if not webview_settings.get('user_agent'):
                user_agent = _state['user_agent']
                if user_agent:
                    self.webview.setCustomUserAgent_(user_agent)
            self.window.setFrameOrigin_(self.screen.origin)
        # WARNING: Decompyle incomplete

        
        def first_show(self):
            if not self.hidden:
                self.window.makeKeyAndOrderFront_(self.window)
            if self.maximized:
                self.maximize()
            elif self.minimized:
                self.minimize()
            self.shown.set()
            if not BrowserView.app.isRunning():
                new_menu = self._recreate_menus(self.menu)
                BrowserView.app.setMainMenu_(new_menu)
                BrowserView.app.activateIgnoringOtherApps_(Foundation.YES)
                AppHelper.installMachInterrupt()
                BrowserView.app.run()
                return None

        
        def show(self):
            pass
        # WARNING: Decompyle incomplete

        
        def hide(self):
            AppHelper.callAfter(self.window.orderOut_, self.window)

        
        def destroy(self):
            AppHelper.callAfter(self.window.close)

        
        def set_title(self, title):
            AppHelper.callAfter(self.window.setTitle_, title)

        
        def toggle_fullscreen(self):
            pass
        # WARNING: Decompyle incomplete

        
        def resize(self, width, height, fix_point):
            pass
        # WARNING: Decompyle incomplete

        
        def maximize(self):
            width = self.screen.size.width
            height = self.screen.size.height
            self.resize(width, height, None)

        
        def minimize(self):
            AppHelper.callAfter(self.window.miniaturize_, self)

        
        def restore(self):
            AppHelper.callAfter(self.window.deminiaturize_, self)

        
        def move(self, x, y):
            flipped_y = self.screen.size.height - y
            self.window.setFrameTopLeftPoint_(AppKit.NSPoint(self.screen.origin.x + x, self.screen.origin.y + flipped_y))

        
        def center(self):
            window_frame = self.window.frame()
            window_frame.origin.x = self.screen.origin.x + (self.screen.size.width - window_frame.size.width) / 2
            window_frame.origin.y = self.screen.origin.y + (self.screen.size.height - window_frame.size.height) / 2
            self.window.setFrameOrigin_(window_frame.origin)

        
        def clear_cookies(self):
            pass
        # WARNING: Decompyle incomplete

        
        def get_cookies(self):
            pass
        # WARNING: Decompyle incomplete

        
        def get_current_url(self):
            pass
        # WARNING: Decompyle incomplete

        
        def load_url(self, url):
            pass
        # WARNING: Decompyle incomplete

        
        def load_html(self, content, base_uri):
            pass
        # WARNING: Decompyle incomplete

        
        def evaluate_js(self, script, parse_json):
            pass
        # WARNING: Decompyle incomplete

        
        def create_file_dialog(self, dialog_type, directory, allow_multiple, save_filename, file_filter, main_thread = (False,)):
            pass
        # WARNING: Decompyle incomplete

        
        def _recreate_menus(self, user_menu):
            main_menu = self._clear_main_menu()
            app_menu_items = None
            regular_menus = None
            if user_menu:
                app_menu_items = []
                regular_menus = []
                for menu in user_menu:
                    if isinstance(menu, Menu) and menu.title == '__app__':
                        app_menu_items.extend(menu.items)
                        continue
                    regular_menus.append(menu)
                    if not app_menu_items:
                        app_menu_items = None
                if not regular_menus:
                    regular_menus = None
            self._add_app_menu(main_menu, app_menu_items)
            if webview_settings['SHOW_DEFAULT_MENUS']:
                self._add_view_menu(main_menu)
                self._add_edit_menu(main_menu)
            self._add_custom_menu(main_menu, regular_menus)
            return main_menu

        
        def _clear_main_menu(self):
            """
        Remove all items from the main menu or create a new one if it doesn't exist.
        """
            mainMenu = BrowserView.app.mainMenu()
            if mainMenu:
                mainMenu.removeAllItems()
            mainMenu = AppKit.NSMenu.alloc().init()
            return mainMenu

        
        def _add_app_menu(self, mainMenu, custom_items = (None,)):
            """
        Create a default Cocoa menu that shows 'Services', 'Hide',
        'Hide Others', 'Show All', and 'Quit'. Will append the application name
        to some menu items if it's available.
        """
            mainAppMenuItem = AppKit.NSMenuItem.alloc().init()
            mainMenu.insertItem_atIndex_(mainAppMenuItem, 0)
            appMenu = AppKit.NSMenu.alloc().init()
            mainAppMenuItem.setSubmenu_(appMenu)
            appMenu.addItemWithTitle_action_keyEquivalent_(self._append_app_name(self.localization['cocoa.menu.about']), 'orderFrontStandardAboutPanel:', '')
            if custom_items:
                appMenu.addItem_(AppKit.NSMenuItem.separatorItem())
                self._process_menu_items(custom_items, appMenu)
            appMenu.addItem_(AppKit.NSMenuItem.separatorItem())
            appServicesMenu = AppKit.NSMenu.alloc().init()
            BrowserView.app.setServicesMenu_(appServicesMenu)
            servicesMenuItem = appMenu.addItemWithTitle_action_keyEquivalent_(self.localization['cocoa.menu.services'], nil, '')
            servicesMenuItem.setSubmenu_(appServicesMenu)
            appMenu.addItem_(AppKit.NSMenuItem.separatorItem())
            appMenu.addItemWithTitle_action_keyEquivalent_(self._append_app_name(self.localization['cocoa.menu.hide']), 'hide:', 'h')
            hideOthersMenuItem = appMenu.addItemWithTitle_action_keyEquivalent_(self.localization['cocoa.menu.hideOthers'], 'hideOtherApplications:', 'h')
            hideOthersMenuItem.setKeyEquivalentModifierMask_(AppKit.NSAlternateKeyMask | AppKit.NSCommandKeyMask)
            appMenu.addItemWithTitle_action_keyEquivalent_(self.localization['cocoa.menu.showAll'], 'unhideAllApplications:', '')
            appMenu.addItem_(AppKit.NSMenuItem.separatorItem())
            appMenu.addItemWithTitle_action_keyEquivalent_(self._append_app_name(self.localization['cocoa.menu.quit']), 'terminate:', 'q')

        
        def _add_view_menu(self, mainMenu):
            """
        Create a default View menu that shows 'Enter Full Screen'.
        """
            viewMenu = AppKit.NSMenu.alloc().init()
            viewMenu.setTitle_(self.localization['cocoa.menu.view'])
            viewMenuItem = AppKit.NSMenuItem.alloc().init()
            viewMenuItem.setSubmenu_(viewMenu)
            mainMenu.insertItem_atIndex_(viewMenuItem, 1)
            fullScreenMenuItem = viewMenu.addItemWithTitle_action_keyEquivalent_(self.localization['cocoa.menu.fullscreen'], 'toggleFullScreen:', 'f')
            fullScreenMenuItem.setKeyEquivalentModifierMask_(AppKit.NSControlKeyMask | AppKit.NSCommandKeyMask)

        
        def _add_edit_menu(self, mainMenu):
            '''
        Create a default Edit menu that shows Copy/Paste/etc.
        '''
            editMenu = AppKit.NSMenu.alloc().init()
            editMenu.setTitle_(self.localization['cocoa.menu.edit'])
            editMenuItem = AppKit.NSMenuItem.alloc().init()
            editMenuItem.setSubmenu_(editMenu)
            mainMenu.insertItem_atIndex_(editMenuItem, 1)
            for title, action, keyEquivalent in ((self.localization['cocoa.menu.cut'], 'cut:', 'x'), (self.localization['cocoa.menu.copy'], 'copy:', 'c'), (self.localization['cocoa.menu.paste'], 'paste:', 'v'), (self.localization['cocoa.menu.selectAll'], 'selectAll:', 'a')):
                menuItem = editMenu.addItemWithTitle_action_keyEquivalent_(title, action, keyEquivalent)
                return None

        
        def _process_menu_items(self, menu_items, parent_menu):
            '''
        Process menu items and add them to the parent menu.
        Used for both custom menus and app menu items.
        '''
            for item in menu_items:
                if isinstance(item, MenuSeparator):
                    parent_menu.addItem_(AppKit.NSMenuItem.separatorItem())
                    continue
                if isinstance(item, MenuAction):
                    random_id = str(uuid.uuid4())[:6]
                    if hasattr(item.function, '__name__'):
                        func_name = item.function.__name__
                    elif hasattr(item.function, 'func') and hasattr(item.function.func, '__name__'):
                        func_name = item.function.func.__name__
                    else:
                        func_name = 'anonymous_function'
                    action_id = func_name + '.' + random_id
                    menu_handler.register_action(action_id, item.function)
                    menu_item = AppKit.NSMenuItem.alloc().initWithTitle_action_keyEquivalent_(item.title, 'handleMenuAction:', '')
                    menu_item.setTarget_(menu_handler)
                    menu_item.setRepresentedObject_(action_id)
                    parent_menu.addItem_(menu_item)
                    continue
                if isinstance(item, Menu):
                    submenu = AppKit.NSMenu.alloc().init()
                    submenu.setTitle_(item.title)
                    menu_item = AppKit.NSMenuItem.alloc().init()
                    menu_item.setTitle_(item.title)
                    menu_item.setSubmenu_(submenu)
                    parent_menu.addItem_(menu_item)
                    self._process_menu_items(item.items, submenu)
                return None

        
        def _add_custom_menu(self, mainMenu, app_menu_list):
            '''
        Create a custom menu for the app menu (MacOS bar menu)
        '''
            pass
        # WARNING: Decompyle incomplete

        
        def _append_app_name(self, val):
            """
        Append the application name to a string if it's available. If not, the
        string is returned unchanged.

        :param str val: The string to append to
        :return: String with app name appended, or unchanged string
        :rtype: str
        """
            if 'CFBundleName' in info:
                val += ' {}'.format(info['CFBundleName'])
            return val

        nscolor_from_hex = (lambda hex_string, alpha = (1,): hex_string = hex_string[1:]if len(hex_string) == 3:
hex_string = (lambda .0: [ c * 2 for c in .0 ])(hex_string())
            hex_int = int(hex_string, 16)
            rgb = (hex_int >> 16 & 255, hex_int >> 8 & 255, hex_int & 255)
            rgb = rgb()
            return AppKit.NSColor.colorWithSRGBRed_green_blue_alpha_(rgb[0], rgb[1], rgb[2], alpha)
)()
        get_instance = (lambda attr, value: for i in list(BrowserView.instances.values()):
if getattr(i, attr) == value:
None, iexcept AttributeError:
passNone)()
        display_confirmation_dialog = (lambda first_button, second_button, message: AppKit.NSApplication.sharedApplication()AppKit.NSRunningApplication.currentApplication().activateWithOptions_(AppKit.NSApplicationActivateIgnoringOtherApps)alert = AppKit.NSAlert.alloc().init()alert.addButtonWithTitle_(first_button)alert.addButtonWithTitle_(second_button)alert.setMessageText_(message)alert.setAlertStyle_(AppKit.NSWarningAlertStyle)alert.runModal() == AppKit.NSAlertFirstButtonReturn)()
        display_input_dialog = (lambda first_button, second_button, prompt, default_text: AppKit.NSApplication.sharedApplication()AppKit.NSRunningApplication.currentApplication().activateWithOptions_(AppKit.NSApplicationActivateIgnoringOtherApps)alert = AppKit.NSAlert.alloc().init()text_field = AppKit.NSTextField.alloc().initWithFrame_(AppKit.NSMakeRect(0, 0, 240, 24))text_field.cell().setScrollable_(True)text_field.setStringValue_(default_text)alert.setAccessoryView_(text_field)alert.addButtonWithTitle_(first_button)alert.addButtonWithTitle_(second_button)alert.setMessageText_(prompt)alert.setAlertStyle_(AppKit.NSWarningAlertStyle)if alert.runModal() == AppKit.NSAlertFirstButtonReturn:
text_field.stringValue())()
        should_close = (lambda window: quit = window.localization['global.quit']cancel = window.localization['global.cancel']msg = window.localization['global.quitConfirmation']should_cancel = window.events.closing.set()if should_cancel:
Foundation.NOif None.confirm_close or BrowserView.display_confirmation_dialog(quit, cancel, msg):
Foundation.YESNone.NO)()
        print_webview = (lambda webview: info = AppKit.NSPrintInfo.sharedPrintInfo().copy()info.setHorizontalPagination_(AppKit.NSFitPagination)info.setHorizontallyCentered_(Foundation.NO)info.setVerticallyCentered_(Foundation.NO)imageableBounds = info.imageablePageBounds()paperSize = info.paperSize()if Foundation.NSWidth(imageableBounds) > paperSize.width:
imageableBounds.origin.x = 0imageableBounds.size.width = paperSize.widthif Foundation.NSHeight(imageableBounds) > paperSize.height:
imageableBounds.origin.y = 0imageableBounds.size.height = paperSize.heightinfo.setBottomMargin_(Foundation.NSMinY(imageableBounds))info.setTopMargin_(paperSize.height - Foundation.NSMinY(imageableBounds) - Foundation.NSHeight(imageableBounds))info.setLeftMargin_(Foundation.NSMinX(imageableBounds))info.setRightMargin_(paperSize.width - Foundation.NSMinX(imageableBounds) - Foundation.NSWidth(imageableBounds))print_op = webview._printOperationWithPrintInfo_(info)print_op.runOperationModalForWindow_delegate_didRunSelector_contextInfo_(webview.window(), nil, nil, nil))()
        _open_web_inspector = (lambda webview: try:
if hasattr(webview, '_inspector'):
inspector = webview._inspector()if inspector and hasattr(inspector, 'show'):
inspector.show()TrueNoneexcept Exception:
False)()
        quote = (lambda string: string.replace(' ', '%20'))()

    
    class MenuHandler:
        
        def __init__(self):
            self.actions = { }

        
        def handleMenuAction_(self, sender):
            action_id = sender.representedObject()
            if action_id in self.actions:
                Thread(target = self.actions[action_id]).start()
                return None
            None.warning(f'''Menu cction {action_id} not found''')

        
        def register_action(self, action_id, action_callable):
            self.actions[action_id] = action_callable


    menu_handler = MenuHandler()
    
    def setup_app():
        pass

    
    def get_active_window():
        active_window = BrowserView.app.keyWindow()
    # WARNING: Decompyle incomplete

    
    def create_window(window):
        pass
    # WARNING: Decompyle incomplete

    
    def set_title(title, uid):
        i = BrowserView.instances.get(uid)
        if i:
            i.set_title(title)
            return None

    
    def create_confirmation_dialog(title, message, uid):
        pass
    # WARNING: Decompyle incomplete

    
    def create_file_dialog(dialog_type, directory, allow_multiple, save_filename, file_types, uid):

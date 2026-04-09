# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: webdriver.pyc (Python 3.11)

'''The WebDriver implementation.'''
import base64
import contextlib
import copy
import os
import pkgutil
import tempfile
import types
import warnings
import zipfile
from abc import ABCMeta
from base64 import b64decode, urlsafe_b64encode
from contextlib import asynccontextmanager, contextmanager
from importlib import import_module
from typing import Any, cast
from selenium.common.exceptions import InvalidArgumentException, JavascriptException, NoSuchCookieException, NoSuchElementException, WebDriverException
from selenium.webdriver.common.bidi.browser import Browser
from selenium.webdriver.common.bidi.browsing_context import BrowsingContext
from selenium.webdriver.common.bidi.emulation import Emulation
from selenium.webdriver.common.bidi.input import Input
from selenium.webdriver.common.bidi.network import Network
from selenium.webdriver.common.bidi.permissions import Permissions
from selenium.webdriver.common.bidi.script import Script
from selenium.webdriver.common.bidi.session import Session
from selenium.webdriver.common.bidi.storage import Storage
from selenium.webdriver.common.bidi.webextension import WebExtension
from selenium.webdriver.common.by import By
from selenium.webdriver.common.fedcm.dialog import Dialog
from selenium.webdriver.common.options import ArgOptions, BaseOptions
from selenium.webdriver.common.print_page_options import PrintOptions
from selenium.webdriver.common.timeouts import Timeouts
from selenium.webdriver.common.virtual_authenticator import Credential, VirtualAuthenticatorOptions, required_virtual_authenticator
from selenium.webdriver.remote.bidi_connection import BidiConnection
from selenium.webdriver.remote.client_config import ClientConfig
from selenium.webdriver.remote.command import Command
from selenium.webdriver.remote.errorhandler import ErrorHandler
from selenium.webdriver.remote.fedcm import FedCM
from selenium.webdriver.remote.file_detector import FileDetector, LocalFileDetector
from selenium.webdriver.remote.locator_converter import LocatorConverter
from selenium.webdriver.remote.mobile import Mobile
from selenium.webdriver.remote.remote_connection import RemoteConnection
from selenium.webdriver.remote.script_key import ScriptKey
from selenium.webdriver.remote.shadowroot import ShadowRoot
from selenium.webdriver.remote.switch_to import SwitchTo
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.websocket_connection import WebSocketConnection
from selenium.webdriver.support.relative_locator import RelativeBy
cdp = None

def import_cdp():
    global cdp
    if not cdp:
        cdp = import_module('selenium.webdriver.common.bidi.cdp')
        return None


def _create_caps(caps = None):
    '''Makes a W3C alwaysMatch capabilities object.

    Filters out capability names that are not in the W3C spec. Spec-compliant
    drivers will reject requests containing unknown capability names.

    Moves the Firefox profile, if present, from the old location to the new Firefox
    options object.

    Args:
        caps: A dictionary of capabilities requested by the caller.
    '''
    caps = copy.deepcopy(caps)
    always_match = { }
    for k, v in caps.items():
        always_match[k] = v
        return {
            'capabilities': {
                'firstMatch': [
                    { }],
                'alwaysMatch': always_match } }


def get_remote_connection(capabilities = None, command_executor = None, keep_alive = None, ignore_local_proxy = (None,), client_config = ('capabilities', dict, 'command_executor', str | RemoteConnection, 'keep_alive', bool, 'ignore_local_proxy', bool, 'client_config', ClientConfig | None, 'return', RemoteConnection)):
    pass
# WARNING: Decompyle incomplete


def create_matches(options = None):
    capabilities = {
        'capabilities': { } }
    opts = []
    for opt in options:
        opts.append(opt.to_capabilities())
        opts_size = len(opts)
        samesies = { }
        for i in range(opts_size):
            min_index = i
            if i + 1 < opts_size:
                first_keys = opts[min_index].keys()
                for kys in first_keys:
                    if kys in opts[i + 1].keys() and opts[min_index][kys] == opts[i + 1][kys]:
                        samesies.update({
                            kys: opts[min_index][kys] })
                    always = { }
                    for k, v in samesies.items():
                        always[k] = v
                        for opt_dict in opts:
                            for k in always:
                                del opt_dict[k]
                                capabilities['capabilities']['alwaysMatch'] = always
                                capabilities['capabilities']['firstMatch'] = opts
                                return capabilities


def BaseWebDriver():
    '''BaseWebDriver'''
    __doc__ = "Abstract Base Class for all Webdriver subtypes.\n\n    ABC's allow custom implementations of Webdriver to be registered so\n    that isinstance type checks will succeed.\n    "

BaseWebDriver = <NODE:27>(BaseWebDriver, 'BaseWebDriver', metaclass = ABCMeta)

class WebDriver(BaseWebDriver):
    '''Control a browser by sending commands to a remote WebDriver server.

    This class expects the remote server to be running the WebDriver wire protocol
    as defined at https://www.selenium.dev/documentation/legacy/json_wire_protocol/.

    Attributes:
    -----------
    session_id - String ID of the browser session started and controlled by this WebDriver.
    capabilities - Dictionary of effective capabilities of this browser session as returned
        by the remote server. See https://www.selenium.dev/documentation/legacy/desired_capabilities/
    command_executor : str or remote_connection.RemoteConnection object used to execute commands.
    error_handler - errorhandler.ErrorHandler object used to handle errors.
    '''
    _web_element_cls = WebElement
    _shadowroot_cls = ShadowRoot
    
    def __init__(self, command_executor, keep_alive, file_detector = None, options = None, locator_converter = None, web_element_cls = ('http://127.0.0.1:4444', True, None, None, None, None, None), client_config = ('command_executor', str | RemoteConnection, 'keep_alive', bool, 'file_detector', FileDetector | None, 'options', BaseOptions | list[BaseOptions] | None, 'locator_converter', LocatorConverter | None, 'web_element_cls', type[WebElement] | None, 'client_config', ClientConfig | None, 'return', None)):
        """Create a new driver instance that issues commands using the WebDriver protocol.

        Args:
            command_executor: Either a string representing the URL of the remote
                server or a custom remote_connection.RemoteConnection object.
                Defaults to 'http://127.0.0.1:4444/wd/hub'.
            keep_alive: (Deprecated) Whether to configure
                remote_connection.RemoteConnection to use HTTP keep-alive.
                Defaults to True.
            file_detector: Pass a custom file detector object during
                instantiation. If None, the default LocalFileDetector() will be
                used.
            options: Instance of a driver options.Options class.
            locator_converter: Custom locator converter to use. Defaults to None.
            web_element_cls: Custom class to use for web elements. Defaults to
                WebElement.
            client_config: Custom client configuration to use. Defaults to None.
        """
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self = None):
        return f'''<{type(self).__module__}.{type(self).__name__} (session="{self.session_id}")>'''

    
    def __enter__(self = None):
        return self

    
    def __exit__(self = None, exc_type = None, exc = None, traceback = ('exc_type', type[BaseException] | None, 'exc', BaseException | None, 'traceback', types.TracebackType | None)):
        self.quit()

    file_detector_context = (lambda self, file_detector_class: pass# WARNING: Decompyle incomplete
)()
    mobile = (lambda self = None: self._mobile)()
    name = (lambda self = None: if 'browserName' in self.caps:
self.caps['browserName']raise None('browserName not specified in session capabilities'))()
    
    def start_client(self = None):
        '''Called before starting a new session.

        This method may be overridden to define custom startup behavior.
        '''
        pass

    
    def stop_client(self = None):
        '''Called after executing a quit command.

        This method may be overridden to define custom shutdown
        behavior.
        '''
        pass

    
    def start_session(self = None, capabilities = None):
        '''Creates a new session with the desired capabilities.

        Args:
            capabilities: A capabilities dict to start the session with.
        '''
        caps = _create_caps(capabilities)
    # WARNING: Decompyle incomplete

    
    def _wrap_value(self, value):
        pass
    # WARNING: Decompyle incomplete

    
    def create_web_element(self = None, element_id = None):
        '''Creates a web element with the specified `element_id`.'''
        return self._web_element_cls(self, element_id)

    
    def _unwrap_value(self, value):
        pass
    # WARNING: Decompyle incomplete

    
    def execute_cdp_cmd(self = None, cmd = None, cmd_args = None):
        '''Execute Chrome Devtools Protocol command and get returned result.

        The command and command args should follow chrome devtools protocol domains/commands:
          - https://chromedevtools.github.io/devtools-protocol/

        Args:
            cmd: Command name.
            cmd_args: Command args. Empty dict {} if there is no command args.

        Returns:
            A dict, empty dict {} if there is no result to return. To
            getResponseBody: {\'base64Encoded\': False, \'body\': \'response body
            string\'}

        Example:
            `driver.execute_cdp_cmd("Network.getResponseBody", {"requestId": requestId})`
        '''
        return self.execute('executeCdpCommand', {
            'cmd': cmd,
            'params': cmd_args })['value']

    
    def execute(self = None, driver_command = None, params = None):
        """Sends a command to be executed by a command.CommandExecutor.

        Args:
            driver_command: The name of the command to execute as a string.
            params: A dictionary of named parameters to send with the command.

        Returns:
            The command's JSON response loaded into a dictionary object.
        """
        params = self._wrap_value(params)
        if self.session_id:
            if not params:
                params = {
                    'sessionId': self.session_id }
            elif 'sessionId' not in params:
                params['sessionId'] = self.session_id
        response = cast(RemoteConnection, self.command_executor).execute(driver_command, params)
        if response:
            self.error_handler.check_response(response)
            response['value'] = self._unwrap_value(response.get('value', None))
            return response
        return {
            'success': None,
            'value': None,
            'sessionId': self.session_id }

    
    def get(self = None, url = None):
        '''Navigate the browser to the specified URL.

        The method does not return until the page is fully loaded (i.e. the
        onload event has fired) in the current window or tab.

        Args:
            url: The URL to be opened by the browser. Must include the protocol
                (e.g., http://, https://).

        Example:
            `driver.get("https://example.com")`
        '''
        self.execute(Command.GET, {
            'url': url })

    title = (lambda self = None: self.execute(Command.GET_TITLE).get('value', ''))()
    
    def pin_script(self = None, script = None, script_key = None):
        '''Store a JavaScript script by a unique hashable ID for later execution.

        Example:
            `script = "return document.getElementById(\'foo\').value"`
        '''
        script_key_instance = ScriptKey(script_key)
        self.pinned_scripts[script_key_instance.id] = script
        return script_key_instance

    
    def unpin(self = None, script_key = None):
        '''Remove a pinned script from storage.

        Example:
            `driver.unpin(script_key)`
        '''
        
        try:
            self.pinned_scripts.pop(script_key.id)
            return None
        except KeyError:
            raise KeyError(f'''No script with key: {script_key} existed in {self.pinned_scripts}'''), None


    
    def get_pinned_scripts(self = None):
        '''Return a list of all pinned scripts.

        Example:
            `pinned_scripts = driver.get_pinned_scripts()`
        '''
        return list(self.pinned_scripts)

    
    def execute_script(self = None, script = None, *args):
        '''Synchronously Executes JavaScript in the current window/frame.

        Args:
            script: The javascript to execute.
            *args: Any applicable arguments for your JavaScript.

        Example:
            ```
            id = "username"
            value = "test_user"
            driver.execute_script("document.getElementById(arguments[0]).value = arguments[1];", id, value)
            ```
        '''
        if isinstance(script, ScriptKey):
            
            try:
                script = self.pinned_scripts[script.id]
            except KeyError:
                raise JavascriptException('Pinned script could not be found')

            converted_args = list(args)
            command = Command.W3C_EXECUTE_SCRIPT
            return self.execute(command, {
                'script': script,
                'args': converted_args })['value']

    
    def execute_async_script(self = None, script = None, *args):
        '''Asynchronously Executes JavaScript in the current window/frame.

        Args:
            script: The javascript to execute.
            *args: Any applicable arguments for your JavaScript.

        Example:
            ```
            script = "var callback = arguments[arguments.length - 1]; "
                "window.setTimeout(function(){ callback(\'timeout\') }, 3000);"
            driver.execute_async_script(script)
            ```
        '''
        converted_args = list(args)
        command = Command.W3C_EXECUTE_SCRIPT_ASYNC
        return self.execute(command, {
            'script': script,
            'args': converted_args })['value']

    current_url = (lambda self = None: self.execute(Command.GET_CURRENT_URL)['value'])()
    page_source = (lambda self = None: self.execute(Command.GET_PAGE_SOURCE)['value'])()
    
    def close(self = None):
        '''Closes the current window.'''
        self.execute(Command.CLOSE)

    
    def quit(self = None):
        '''Quits the driver and closes every associated window.'''
        
        try:
            self.execute(Command.QUIT)
            self.stop_client()
            executor = cast(RemoteConnection, self.command_executor)
            executor.close()
            return None
        except:
            self.stop_client()
            executor = cast(RemoteConnection, self.command_executor)
            executor.close()


    current_window_handle = (lambda self = None: self.execute(Command.W3C_GET_CURRENT_WINDOW_HANDLE)['value'])()
    window_handles = (lambda self = None: self.execute(Command.W3C_GET_WINDOW_HANDLES)['value'])()
    
    def maximize_window(self = None):
        '''Maximizes the current window that webdriver is using.'''
        command = Command.W3C_MAXIMIZE_WINDOW
        self.execute(command, None)

    
    def fullscreen_window(self = None):
        """Invokes the window manager-specific 'full screen' operation."""
        self.execute(Command.FULLSCREEN_WINDOW)

    
    def minimize_window(self = None):
        """Invokes the window manager-specific 'minimize' operation."""
        self.execute(Command.MINIMIZE_WINDOW)

    
    def print_page(self = None, print_options = None):
        '''Takes PDF of the current page.

        The driver makes a best effort to return a PDF based on the
        provided parameters.
        '''
        options = { }
        if print_options:
            options = print_options.to_dict()
        return self.execute(Command.PRINT_PAGE, options)['value']

    switch_to = (lambda self = None: self._switch_to)()
    
    def back(self = None):
        '''Goes one step backward in the browser history.'''
        self.execute(Command.GO_BACK)

    
    def forward(self = None):
        '''Goes one step forward in the browser history.'''
        self.execute(Command.GO_FORWARD)

    
    def refresh(self = None):
        '''Refreshes the current page.'''
        self.execute(Command.REFRESH)

    
    def get_cookies(self = None):
        '''Get all cookies visible to the current WebDriver instance.

        Returns:
            A list of dictionaries, corresponding to cookies visible in the
            current session.
        '''
        return self.execute(Command.GET_ALL_COOKIES)['value']

    
    def get_cookie(self = None, name = None):
        '''Get a single cookie by name (case-sensitive,).

        Returns:
             A cookie dictionary or None if not found.

        Raises:
            ValueError if the name is empty or whitespace.

        Example:
            `cookie = driver.get_cookie("my_cookie")`
        '''
        if name or name.isspace():
            raise ValueError('Cookie name cannot be empty')
        contextlib.suppress(NoSuchCookieException)
        None(None, None)
        return 
        with None:
            if not None, self.execute(Command.GET_COOKIE, {
                'name': name })['value']:
                pass

    
    def delete_cookie(self = None, name = None):
        '''Delete a single cookie with the given name (case-sensitive).

        Raises:
            ValueError if the name is empty or whitespace.

        Example:
            `driver.delete_cookie("my_cookie")`
        '''
        if name or name.isspace():
            raise ValueError('Cookie name cannot be empty')
        self.execute(Command.DELETE_COOKIE, {
            'name': name })

    
    def delete_all_cookies(self = None):
        '''Delete all cookies in the scope of the session.'''
        self.execute(Command.DELETE_ALL_COOKIES)

    
    def add_cookie(self = None, cookie_dict = None):
        '''Adds a cookie to your current session.

        Args:
            cookie_dict: A dictionary object, with required keys - "name" and
                "value"; Optional keys - "path", "domain", "secure", "httpOnly",
                "expiry", "sameSite".

        Examples:
            `driver.add_cookie({"name": "foo", "value": "bar"})`
            `driver.add_cookie({"name": "foo", "value": "bar", "path": "/"})`
            `driver.add_cookie({"name": "foo", "value": "bar", "path": "/", "secure": True})`
            `driver.add_cookie({"name": "foo", "value": "bar", "sameSite": "Strict"})`
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def implicitly_wait(self = None, time_to_wait = None):
        '''Set a sticky implicit timeout for element location and command completion.

        This method sets a timeout that applies to all element location strategies
        for the duration of the session. It only needs to be called once per session.
        To set the timeout for asynchronous script execution, see set_script_timeout.

        Args:
            time_to_wait: Amount of time to wait (in seconds).

        Example:
            `driver.implicitly_wait(30)`
        '''
        self.execute(Command.SET_TIMEOUTS, {
            'implicit': int(float(time_to_wait) * 1000) })

    
    def set_script_timeout(self = None, time_to_wait = None):
        '''Set the timeout for asynchronous script execution.

        This timeout specifies how long a script can run during an
        execute_async_script call before throwing an error.

        Args:
            time_to_wait: The amount of time to wait (in seconds).

        Example:
            `driver.set_script_timeout(30)`
        '''
        self.execute(Command.SET_TIMEOUTS, {
            'script': int(float(time_to_wait) * 1000) })

    
    def set_page_load_timeout(self = None, time_to_wait = None):
        '''Set the timeout for page load completion.

        This specifies how long to wait for a page load to complete before
        throwing an error.

        Args:
            time_to_wait: The amount of time to wait (in seconds).

        Example:
            `driver.set_page_load_timeout(30)`
        '''
        
        try:
            self.execute(Command.SET_TIMEOUTS, {
                'pageLoad': int(float(time_to_wait) * 1000) })
            return None
        except WebDriverException:
            self.execute(Command.SET_TIMEOUTS, {
                'ms': float(time_to_wait) * 1000,
                'type': 'page load' })
            return None


    timeouts = (lambda self = None: timeouts = self.execute(Command.GET_TIMEOUTS)['value']timeouts['implicit_wait'] = timeouts.pop('implicit') / 1000timeouts['page_load'] = timeouts.pop('pageLoad') / 1000timeouts['script'] = timeouts.pop('script') / 1000# WARNING: Decompyle incomplete
)()
    timeouts = (lambda self = None, timeouts = None: _ = self.execute(Command.SET_TIMEOUTS, timeouts._to_json())['value'])()
    
    def find_element(self = None, by = None, value = None):
        """Find an element given a By strategy and locator.

        Args:
            by: The locating strategy to use. Default is `By.ID`. Supported
                values include: By.ID, By.NAME, By.XPATH, By.CSS_SELECTOR,
                By.CLASS_NAME, By.TAG_NAME, By.LINK_TEXT, By.PARTIAL_LINK_TEXT,
                or RelativeBy.
            value: The locator value to use with the specified `by` strategy.

        Returns:
            The first matching WebElement found on the page.

        Example:
            `element = driver.find_element(By.ID, 'foo')`
        """
        (by, value) = self.locator_converter.convert(by, value)
        if isinstance(by, RelativeBy):
            elements = self.find_elements(by = by, value = value)
            if not elements:
                raise NoSuchElementException(f'''Cannot locate relative element with: {by.root}''')
            return elements[0]
        return None.execute(Command.FIND_ELEMENT, {
            'using': by,
            'value': value })['value']

    
    def find_elements(self = None, by = None, value = None):
        """Find elements given a By strategy and locator.

        Args:
            by: The locating strategy to use. Default is `By.ID`. Supported
                values include: By.ID, By.NAME, By.XPATH, By.CSS_SELECTOR,
                By.CLASS_NAME, By.TAG_NAME, By.LINK_TEXT, By.PARTIAL_LINK_TEXT,
                or RelativeBy.
            value: The locator value to use with the specified `by` strategy.

        Returns:
            List of WebElements matching locator strategy found on the page.

        Example:
            `element = driver.find_elements(By.ID, 'foo')`
        """
        (by, value) = self.locator_converter.convert(by, value)
    # WARNING: Decompyle incomplete

    capabilities = (lambda self = None: self.caps)()
    
    def get_screenshot_as_file(self = None, filename = None):
        '''Save a screenshot of the current window to a PNG image file.

        Returns:
            False if there is any IOError, else returns True. Use full paths in your filename.

        Args:
            filename: The full path you wish to save your screenshot to. This
                should end with a `.png` extension.

        Example:
            `driver.get_screenshot_as_file("./screenshots/foo.png")`
        '''
        if not str(filename).lower().endswith('.png'):
            warnings.warn('name used for saved screenshot does not match file type. It should end with a `.png` extension', UserWarning, stacklevel = 2)
        png = self.get_screenshot_as_png()
        
        try:
            f = open(filename, 'wb')
            f.write(png)
            
            try:
                None(None, None)
            with None:
                if not None:
                    
                    try:
                        
                        try:
                            
                            try:
                                pass
                            except OSError:
                                
                                try:
                                    del png
                                    return False
                                    
                                    try:
                                        del png
                                    except:
                                        del png

                                    return True







    
    def save_screenshot(self = None, filename = None):
        '''Save a screenshot of the current window to a PNG image file.

        Returns:
            False if there is any IOError, else returns True. Use full paths in your filename.

        Args:
            filename: The full path you wish to save your screenshot to. This
                should end with a `.png` extension.

        Example:
            `driver.save_screenshot("./screenshots/foo.png")`
        '''
        return self.get_screenshot_as_file(filename)

    
    def get_screenshot_as_png(self = None):
        '''Gets the screenshot of the current window as a binary data.

        Example:
            `driver.get_screenshot_as_png()`
        '''
        return b64decode(self.get_screenshot_as_base64().encode('ascii'))

    
    def get_screenshot_as_base64(self = None):
        '''Get a base64-encoded screenshot of the current window.

        This encoding is useful for embedding screenshots in HTML.

        Example:
            `driver.get_screenshot_as_base64()`
        '''
        return self.execute(Command.SCREENSHOT)['value']

    
    def set_window_size(self = None, width = None, height = None, windowHandle = ('current',)):
        '''Sets the width and height of the current window.

        Args:
            width: The width in pixels to set the window to.
            height: The height in pixels to set the window to.
            windowHandle: The handle of the window to resize. Default is "current".

        Example:
            `driver.set_window_size(800, 600)`
        '''
        self._check_if_window_handle_is_current(windowHandle)
        self.set_window_rect(width = int(width), height = int(height))

    
    def get_window_size(self = None, windowHandle = None):
        '''Gets the width and height of the current window.

        Example:
            `driver.get_window_size()`
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def set_window_position(self = None, x = None, y = None, windowHandle = ('current',)):
        '''Sets the x,y position of the current window.

        Args:
            x: The x-coordinate in pixels to set the window position.
            y: The y-coordinate in pixels to set the window position.
            windowHandle: The handle of the window to reposition. Default is "current".

        Example:
            `driver.set_window_position(0, 0)`
        '''
        self._check_if_window_handle_is_current(windowHandle)
        return self.set_window_rect(x = int(x), y = int(y))

    
    def get_window_position(self = None, windowHandle = None):
        '''Gets the x,y position of the current window.

        Example:
            `driver.get_window_position()`
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _check_if_window_handle_is_current(self = None, windowHandle = None):
        '''Warns if the window handle is not equal to `current`.'''
        if windowHandle != 'current':
            warnings.warn("Only 'current' window is supported for W3C compatible browsers.", stacklevel = 2)
            return None

    
    def get_window_rect(self = None):
        """Get the window's position and size.

        Returns:
            x, y coordinates and height and width of the current window.

        Example:
            `driver.get_window_rect()`
        """
        return self.execute(Command.GET_WINDOW_RECT)['value']

    
    def set_window_rect(self = None, x = None, y = None, width = (None, None, None, None), height = ('return', dict)):
        """Set the window's position and size.

        Sets the x, y coordinates and height and width of the current window.
        This method is only supported for W3C compatible browsers; other browsers
        should use `set_window_position` and `set_window_size`.

        Example:
            `driver.set_window_rect(x=10, y=10)`
            `driver.set_window_rect(width=100, height=200)`
            `driver.set_window_rect(x=10, y=10, width=100, height=200)`
        """
        pass
    # WARNING: Decompyle incomplete

    file_detector = (lambda self = None: self._file_detector)()
    file_detector = (lambda self = None, detector = None: if not detector:
raise WebDriverException('You may not set a file detector that is null')if not isinstance(detector, FileDetector):
raise WebDriverException('Detector has to be instance of FileDetector')self._file_detector = detector)()
    orientation = (lambda self = None: self.execute(Command.GET_SCREEN_ORIENTATION)['value'])()
    orientation = (lambda self = None, value = None: allowed_values = [
'LANDSCAPE',
'PORTRAIT']if value.upper() in allowed_values:
self.execute(Command.SET_SCREEN_ORIENTATION, {
'orientation': value })Noneraise None("You can only set the orientation to 'LANDSCAPE' and 'PORTRAIT'"))()
    
    def start_devtools(self = None):
        import_cdp()
    # WARNING: Decompyle incomplete

    bidi_connection = (lambda self: pass# WARNING: Decompyle incomplete
)()
    script = (lambda self = None: if not self._websocket_connection:
self._start_bidi()if not self._script:
self._script = Script(self._websocket_connection, self)self._script)()
    
    def _start_bidi(self = None):
        if self.caps.get('webSocketUrl'):
            ws_url = self.caps.get('webSocketUrl')
        else:
            raise WebDriverException('Unable to find url to connect to from capabilities')
        if not isinstance(self.command_executor, RemoteConnection):
            raise WebDriverException('command_executor must be a RemoteConnection instance for BiDi support')
        self._websocket_connection = WebSocketConnection(ws_url, self.command_executor.client_config.websocket_timeout, self.command_executor.client_config.websocket_interval)

    network = (lambda self = None: if not self._websocket_connection:
self._start_bidi()# WARNING: Decompyle incomplete
)()
    browser = (lambda self = None: if not self._websocket_connection:
self._start_bidi()# WARNING: Decompyle incomplete
)()
    _session = (lambda self = None: if not self._websocket_connection:
self._start_bidi()# WARNING: Decompyle incomplete
)()
    browsing_context = (lambda self = None: if not self._websocket_connection:
self._start_bidi()# WARNING: Decompyle incomplete
)()
    storage = (lambda self = None: if not self._websocket_connection:
self._start_bidi()# WARNING: Decompyle incomplete
)()
    permissions = (lambda self = None: if not self._websocket_connection:
self._start_bidi()# WARNING: Decompyle incomplete
)()
    webextension = (lambda self = None: if not self._websocket_connection:
self._start_bidi()# WARNING: Decompyle incomplete
)()
    emulation = (lambda self = None: if not self._websocket_connection:
self._start_bidi()# WARNING: Decompyle incomplete
)()
    input = (lambda self = None: if not self._websocket_connection:
self._start_bidi()# WARNING: Decompyle incomplete
)()
    
    def _get_cdp_details(self):
        import json
        import urllib3
        http = urllib3.PoolManager()
        
        try:
            if self.caps.get('browserName') == 'chrome':
                debugger_address = self.caps.get('goog:chromeOptions').get('debuggerAddress')
            elif self.caps.get('browserName') in ('MicrosoftEdge', 'webview2'):
                debugger_address = self.caps.get('ms:edgeOptions').get('debuggerAddress')
            else:
                except AttributeError:
                    raise WebDriverException("Can't get debugger address.")

        res = http.request('GET', f'''http://{debugger_address}/json/version''')
        data = json.loads(res.data)
        browser_version = data.get('Browser')
        websocket_url = data.get('webSocketDebuggerUrl')
        import re
        version = re.search('.*/(\\d+)\\.', browser_version).group(1)
        return (version, websocket_url)

    
    def add_virtual_authenticator(self = None, options = None):
        '''Adds a virtual authenticator with the given options.

        Example:
            ```
            from selenium.webdriver.common.virtual_authenticator import VirtualAuthenticatorOptions

            options = VirtualAuthenticatorOptions(protocol="u2f", transport="usb", device_id="myDevice123")
            driver.add_virtual_authenticator(options)
            ```
        '''
        self._authenticator_id = self.execute(Command.ADD_VIRTUAL_AUTHENTICATOR, options.to_dict())['value']

    virtual_authenticator_id = (lambda self = None: self._authenticator_id)()
    remove_virtual_authenticator = (lambda self = None: self.execute(Command.REMOVE_VIRTUAL_AUTHENTICATOR, {
'authenticatorId': self._authenticator_id })self._authenticator_id = None)()
    add_credential = (lambda self = None, credential = None: pass# WARNING: Decompyle incomplete
)()
    get_credentials = (lambda self = None: credential_data = self.execute(Command.GET_CREDENTIALS, {
'authenticatorId': self._authenticator_id })credential_data['value']())()
    remove_credential = (lambda self = None, credential_id = None: if isinstance(credential_id, bytearray):
credential_id = urlsafe_b64encode(credential_id).decode()self.execute(Command.REMOVE_CREDENTIAL, {
'credentialId': credential_id,
'authenticatorId': self._authenticator_id }))()
    remove_all_credentials = (lambda self = None: self.execute(Command.REMOVE_ALL_CREDENTIALS, {
'authenticatorId': self._authenticator_id }))()
    set_user_verified = (lambda self = None, verified = None: self.execute(Command.SET_USER_VERIFIED, {
'authenticatorId': self._authenticator_id,
'isUserVerified': verified }))()
    
    def get_downloadable_files(self = None):
        '''Retrieves the downloadable files as a list of file names.'''
        if 'se:downloadsEnabled' not in self.capabilities:
            raise WebDriverException('You must enable downloads in order to work with downloadable files.')
        return self.execute(Command.GET_DOWNLOADABLE_FILES)['value']['names']

    
    def download_file(self = None, file_name = None, target_directory = None):

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: switch_to.pyc (Python 3.11)

from selenium.common.exceptions import NoSuchElementException, NoSuchFrameException, NoSuchWindowException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.command import Command
from selenium.webdriver.remote.webelement import WebElement

class SwitchTo:
    
    def __init__(self = None, driver = None):
        import weakref
        self._driver = weakref.proxy(driver)

    active_element = (lambda self = None: self._driver.execute(Command.W3C_GET_ACTIVE_ELEMENT)['value'])()
    alert = (lambda self = None: alert = Alert(self._driver)_ = alert.textalert)()
    
    def default_content(self = None):
        '''Switch focus to the default frame.

        Example:
            driver.switch_to.default_content()
        '''
        self._driver.execute(Command.SWITCH_TO_FRAME, {
            'id': None })

    
    def frame(self = None, frame_reference = None):
        '''Switch focus to the specified frame by index, name, or element.

        Args:
            frame_reference: The name of the frame to switch to, an integer representing the index,
                or a WebElement that is an (i)frame to switch to.

        Example:
                driver.switch_to.frame("frame_name")
                driver.switch_to.frame(1)
                driver.switch_to.frame(driver.find_elements(By.TAG_NAME, "iframe")[0])
        '''
        self._driver.execute(Command.SWITCH_TO_FRAME, {
            'id': frame_reference })

    
    def new_window(self = None, type_hint = None):
        '''Switches to a new top-level browsing context.

        The type hint can be one of "tab" or "window". If not specified the
        browser will automatically select it.

        Example:
                driver.switch_to.new_window("tab")
        '''
        value = self._driver.execute(Command.NEW_WINDOW, {
            'type': type_hint })['value']
        self._w3c_window(value['handle'])

    
    def parent_frame(self = None):
        '''Switch focus to the parent browsing context.

        If the current context is already the top level browsing context, it remains unchanged.

        Example:
                driver.switch_to.parent_frame()
        '''
        self._driver.execute(Command.SWITCH_TO_PARENT_FRAME)

    
    def window(self = None, window_name = None):
        '''Switches focus to the specified window.

        Args:
            window_name: The name or window handle of the window to switch to.

        Example:
            driver.switch_to.window("main")
        '''
        self._w3c_window(window_name)

    
    def _w3c_window(self = None, window_name = None):
        pass
    # WARNING: Decompyle incomplete

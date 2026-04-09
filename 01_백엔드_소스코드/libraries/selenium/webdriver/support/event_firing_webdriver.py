# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: event_firing_webdriver.pyc (Python 3.11)

from typing import Any
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.abstract_event_listener import AbstractEventListener

def _wrap_elements(result, ef_driver):
    pass
# WARNING: Decompyle incomplete


class EventFiringWebDriver:
    '''Wrap an arbitrary WebDriver instance and support firing events.

    This wrapper allows you to hook into various WebDriver events through an
    AbstractEventListener implementation.
    '''
    
    def __init__(self = None, driver = None, event_listener = None):
        '''Creates a new instance of the EventFiringWebDriver.

        Args:
            driver: A WebDriver instance
            event_listener: Instance of a class that subclasses AbstractEventListener and implements it fully
                           or partially

        Example:
            from selenium.webdriver import Firefox
            from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener


            class MyListener(AbstractEventListener):
                def before_navigate_to(self, url, driver):
                    print("Before navigate to %s" % url)

                def after_navigate_to(self, url, driver):
                    print("After navigate to %s" % url)


            driver = Firefox()
            ef_driver = EventFiringWebDriver(driver, MyListener())
            ef_driver.get("http://www.google.co.in/")
        '''
        if not isinstance(driver, WebDriver):
            raise WebDriverException('A WebDriver instance must be supplied')
        if not isinstance(event_listener, AbstractEventListener):
            raise WebDriverException('Event listener must be a subclass of AbstractEventListener')
        self._driver = driver
        self._driver._wrap_value = self._wrap_value
        self._listener = event_listener

    wrapped_driver = (lambda self = None: self._driver)()
    
    def get(self = None, url = None):
        self._dispatch('navigate_to', (url, self._driver), 'get', (url,))

    
    def back(self = None):
        self._dispatch('navigate_back', (self._driver,), 'back', ())

    
    def forward(self = None):
        self._dispatch('navigate_forward', (self._driver,), 'forward', ())

    
    def execute_script(self = None, script = None, *args):
        unwrapped_args = (script,) + self._unwrap_element_args(args)
        return self._dispatch('execute_script', (script, self._driver), 'execute_script', unwrapped_args)

    
    def execute_async_script(self, script, *args):
        unwrapped_args = (script,) + self._unwrap_element_args(args)
        return self._dispatch('execute_script', (script, self._driver), 'execute_async_script', unwrapped_args)

    
    def close(self = None):
        self._dispatch('close', (self._driver,), 'close', ())

    
    def quit(self = None):
        self._dispatch('quit', (self._driver,), 'quit', ())

    
    def find_element(self = None, by = None, value = None):
        return self._dispatch('find', (by, value, self._driver), 'find_element', (by, value))

    
    def find_elements(self = None, by = None, value = None):
        return self._dispatch('find', (by, value, self._driver), 'find_elements', (by, value))

    
    def _dispatch(self, l_call = None, l_args = None, d_call = None, d_args = ('l_call', str, 'l_args', tuple[(Any, ...)], 'd_call', str, 'd_args', tuple[(Any, ...)])):
        pass
    # WARNING: Decompyle incomplete

    
    def _unwrap_element_args(self, args):
        pass
    # WARNING: Decompyle incomplete

    
    def _wrap_value(self, value):
        if isinstance(value, EventFiringWebElement):
            return WebDriver._wrap_value(self._driver, value.wrapped_element)
        return None._wrap_value(self._driver, value)

    
    def __setattr__(self, item, value):
        if not item.startswith('_') or hasattr(self._driver, item):
            object.__setattr__(self, item, value)
            return None
        
        try:
            object.__setattr__(self._driver, item, value)
            return None
        except Exception:
            exc = None
            self._listener.on_exception(exc, self._driver)
            raise 
            exc = None
            del exc


    
    def __getattr__(self, name):
        pass
    # WARNING: Decompyle incomplete



class EventFiringWebElement:
    '''A wrapper around WebElement instance which supports firing events.'''
    
    def __init__(self = None, webelement = None, ef_driver = None):
        '''Creates a new instance of the EventFiringWebElement.'''
        self._webelement = webelement
        self._ef_driver = ef_driver
        self._driver = ef_driver.wrapped_driver
        self._listener = ef_driver._listener

    wrapped_element = (lambda self = None: self._webelement)()
    
    def click(self = None):
        self._dispatch('click', (self._webelement, self._driver), 'click', ())

    
    def clear(self = None):
        self._dispatch('change_value_of', (self._webelement, self._driver), 'clear', ())

    
    def send_keys(self = None, *value):
        self._dispatch('change_value_of', (self._webelement, self._driver), 'send_keys', value)

    
    def find_element(self = None, by = None, value = None):
        return self._dispatch('find', (by, value, self._driver), 'find_element', (by, value))

    
    def find_elements(self = None, by = None, value = None):
        return self._dispatch('find', (by, value, self._driver), 'find_elements', (by, value))

    
    def _dispatch(self, l_call, l_args, d_call, d_args):
        pass
    # WARNING: Decompyle incomplete

    
    def __setattr__(self, item, value):
        if not item.startswith('_') or hasattr(self._webelement, item):
            object.__setattr__(self, item, value)
            return None
        
        try:
            object.__setattr__(self._webelement, item, value)
            return None
        except Exception:
            exc = None
            self._listener.on_exception(exc, self._driver)
            raise 
            exc = None
            del exc


    
    def __getattr__(self, name):
        pass
    # WARNING: Decompyle incomplete


WebElement.register(EventFiringWebElement)

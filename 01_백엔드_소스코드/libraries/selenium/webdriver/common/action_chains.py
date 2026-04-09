# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: action_chains.pyc (Python 3.11)

'''The ActionChains implementation.'''
from __future__ import annotations
from typing import TYPE_CHECKING
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.key_input import KeyInput
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin, WheelInput
from selenium.webdriver.common.utils import keys_to_typing
from selenium.webdriver.remote.webelement import WebElement
if TYPE_CHECKING:
    from selenium.webdriver.remote.webdriver import WebDriver

class ActionChains:
    '''Automate low-level interactions like mouse movements, button actions, key presses, and context menus.

    ActionChains are a way to automate low level interactions such as mouse
    movements, mouse button actions, key press, and context menu interactions.
    This is useful for doing more complex actions like hover over and drag and
    drop.

    Generate user actions.
       When you call methods for actions on the ActionChains object,
       the actions are stored in a queue in the ActionChains object.
       When you call perform(), the events are fired in the order they
       are queued up.

    ActionChains can be used in a chain pattern::

        menu = driver.find_element(By.CSS_SELECTOR, ".nav")
        hidden_submenu = driver.find_element(By.CSS_SELECTOR, ".nav #submenu1")

        ActionChains(driver).move_to_element(menu).click(hidden_submenu).perform()

    Or actions can be queued up one by one, then performed.::

        menu = driver.find_element(By.CSS_SELECTOR, ".nav")
        hidden_submenu = driver.find_element(By.CSS_SELECTOR, ".nav #submenu1")

        actions = ActionChains(driver)
        actions.move_to_element(menu)
        actions.click(hidden_submenu)
        actions.perform()

    Either way, the actions are performed in the order they are called, one after
    another.
    '''
    
    def __init__(self = None, driver = None, duration = None, devices = (250, None)):
        '''Creates a new ActionChains.

        Args:
            driver: The WebDriver instance which performs user actions.
            duration: override the default 250 msecs of DEFAULT_MOVE_DURATION in PointerInput
            devices: Optional list of input devices (PointerInput, KeyInput, WheelInput) to use.
                If not provided, default devices will be created.
        '''
        self._driver = driver
        mouse = None
        keyboard = None
        wheel = None
    # WARNING: Decompyle incomplete

    
    def perform(self = None):
        '''Performs all stored actions.'''
        self.w3c_actions.perform()

    
    def reset_actions(self = None):
        '''Clear actions stored locally and on the remote end.'''
        self.w3c_actions.clear_actions()
        for device in self.w3c_actions.devices:
            device.clear_actions()
            return None

    
    def click(self = None, on_element = None):
        '''Clicks an element.

        Args:
            on_element: The element to click.
                If None, clicks on current mouse position.
        '''
        if on_element:
            self.move_to_element(on_element)
        self.w3c_actions.pointer_action.click()
        self.w3c_actions.key_action.pause()
        self.w3c_actions.key_action.pause()
        return self

    
    def click_and_hold(self = None, on_element = None):
        '''Holds down the left mouse button on an element.

        Args:
            on_element: The element to mouse down.
                If None, clicks on current mouse position.
        '''
        if on_element:
            self.move_to_element(on_element)
        self.w3c_actions.pointer_action.click_and_hold()
        self.w3c_actions.key_action.pause()
        return self

    
    def context_click(self = None, on_element = None):
        '''Performs a context-click (right click) on an element.

        Args:
            on_element: The element to context-click.
                If None, clicks on current mouse position.
        '''
        if on_element:
            self.move_to_element(on_element)
        self.w3c_actions.pointer_action.context_click()
        self.w3c_actions.key_action.pause()
        self.w3c_actions.key_action.pause()
        return self

    
    def double_click(self = None, on_element = None):
        '''Double-clicks an element.

        Args:
            on_element: The element to double-click.
                If None, clicks on current mouse position.
        '''
        if on_element:
            self.move_to_element(on_element)
        self.w3c_actions.pointer_action.double_click()
        for _ in range(4):
            self.w3c_actions.key_action.pause()
            return self

    
    def drag_and_drop(self = None, source = None, target = None):
        '''Hold down the left mouse button on an element, then move to target and release.

        Args:
            source: The element to mouse down.
            target: The element to mouse up.
        '''
        self.click_and_hold(source)
        self.release(target)
        return self

    
    def drag_and_drop_by_offset(self = None, source = None, xoffset = None, yoffset = ('source', 'WebElement', 'xoffset', 'int', 'yoffset', 'int', 'return', 'ActionChains')):
        '''Hold down the left mouse button on an element, then move by offset and release.

        Args:
            source: The element to mouse down.
            xoffset: X offset to move to.
            yoffset: Y offset to move to.
        '''
        self.click_and_hold(source)
        self.move_by_offset(xoffset, yoffset)
        self.release()
        return self

    
    def key_down(self = None, value = None, element = None):
        '''Send a key press only without releasing it (modifier keys only).

        Args:
            value: The modifier key to send. Values are defined in `Keys` class.
            element: The element to send keys.
                If None, sends a key to current focused element.

        Example, pressing ctrl+c::

            ActionChains(driver).key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
        '''
        if element:
            self.click(element)
        self.w3c_actions.key_action.key_down(value)
        self.w3c_actions.pointer_action.pause()
        return self

    
    def key_up(self = None, value = None, element = None):
        '''Releases a modifier key.

        Args:
            value: The modifier key to send. Values are defined in Keys class.
            element: The element to send keys.
                If None, sends a key to current focused element.

        Example, pressing ctrl+c::

            ActionChains(driver).key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
        '''
        if element:
            self.click(element)
        self.w3c_actions.key_action.key_up(value)
        self.w3c_actions.pointer_action.pause()
        return self

    
    def move_by_offset(self = None, xoffset = None, yoffset = None):
        '''Moving the mouse to an offset from current mouse position.

        Args:
            xoffset: X offset to move to, as a positive or negative integer.
            yoffset: Y offset to move to, as a positive or negative integer.
        '''
        self.w3c_actions.pointer_action.move_by(xoffset, yoffset)
        self.w3c_actions.key_action.pause()
        return self

    
    def move_to_element(self = None, to_element = None):
        '''Moving the mouse to the middle of an element.

        Args:
            to_element: The WebElement to move to.
        '''
        self.w3c_actions.pointer_action.move_to(to_element)
        self.w3c_actions.key_action.pause()
        return self

    
    def move_to_element_with_offset(self = None, to_element = None, xoffset = None, yoffset = ('to_element', 'WebElement', 'xoffset', 'int', 'yoffset', 'int', 'return', 'ActionChains')):
        '''Move the mouse to an element with the specified offsets.

        Offsets are relative to the in-view center point of the element.

        Args:
            to_element: The WebElement to move to.
            xoffset: X offset to move to, as a positive or negative integer.
            yoffset: Y offset to move to, as a positive or negative integer.
        '''
        self.w3c_actions.pointer_action.move_to(to_element, int(xoffset), int(yoffset))
        self.w3c_actions.key_action.pause()
        return self

    
    def pause(self = None, seconds = None):
        '''Pause all inputs for the specified duration in seconds.'''
        self.w3c_actions.pointer_action.pause(seconds)
        self.w3c_actions.key_action.pause(int(seconds))
        return self

    
    def release(self = None, on_element = None):
        '''Releasing a held mouse button on an element.

        Args:
            on_element: The element to mouse up.
                If None, releases on current mouse position.
        '''
        if on_element:
            self.move_to_element(on_element)
        self.w3c_actions.pointer_action.release()
        self.w3c_actions.key_action.pause()
        return self

    
    def send_keys(self = None, *keys_to_send):
        """Sends keys to current focused element.

        Args:
            keys_to_send: The keys to send. Modifier keys constants can be found in the
                'Keys' class.
        """
        typing = keys_to_typing(keys_to_send)
        for key in typing:
            self.key_down(key)
            self.key_up(key)
            return self

    
    def send_keys_to_element(self = None, element = None, *keys_to_send):
        """Sends keys to an element.

        Args:
            element: The element to send keys.
            keys_to_send: The keys to send. Modifier keys constants can be found in the
                'Keys' class.
        """
        self.click(element)
    # WARNING: Decompyle incomplete

    
    def scroll_to_element(self = None, element = None):
        """Scroll the element into the viewport if it's outside it.

        Scrolls the bottom of the element to the bottom of the viewport.

        Args:
            element: Which element to scroll into the viewport.
        """
        self.w3c_actions.wheel_action.scroll(origin = element)
        return self

    
    def scroll_by_amount(self = None, delta_x = None, delta_y = None):
        '''Scroll by a provided amount with the origin in the top left corner.

        Scrolls by provided amounts with the origin in the top left corner
        of the viewport.

        Args:
            delta_x: Distance along X axis to scroll using the wheel. A negative value scrolls left.
            delta_y: Distance along Y axis to scroll using the wheel. A negative value scrolls up.
        '''
        self.w3c_actions.wheel_action.scroll(delta_x = delta_x, delta_y = delta_y)
        return self

    
    def scroll_from_origin(self = None, scroll_origin = None, delta_x = None, delta_y = ('scroll_origin', 'ScrollOrigin', 'delta_x', 'int', 'delta_y', 'int', 'return', 'ActionChains')):
        '''Scroll by a provided amount based on a scroll origin (element or viewport).

        The scroll origin is either the center of an element or the upper left of the
        viewport plus any offsets. If the origin is an element, and the element
        is not in the viewport, the bottom of the element will first be
        scrolled to the bottom of the viewport.

        Args:
            scroll_origin: Where scroll originates (viewport or element center) plus provided offsets.
            delta_x: Distance along X axis to scroll using the wheel. A negative value scrolls left.
            delta_y: Distance along Y axis to scroll using the wheel. A negative value scrolls up.

        Raises:
            MoveTargetOutOfBoundsException: If the origin with offset is outside the viewport.
        '''
        if not isinstance(scroll_origin, ScrollOrigin):
            raise TypeError(f'''Expected object of type ScrollOrigin, got: {type(scroll_origin)}''')
        self.w3c_actions.wheel_action.scroll(origin = scroll_origin.origin, x = scroll_origin.x_offset, y = scroll_origin.y_offset, delta_x = delta_x, delta_y = delta_y)
        return self

    
    def __enter__(self = None):
        return self

    
    def __exit__(self = None, _type = None, _value = None, _traceback = ('return', 'None')):
        pass

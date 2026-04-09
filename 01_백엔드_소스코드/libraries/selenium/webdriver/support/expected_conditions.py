# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: expected_conditions.pyc (Python 3.11)

import re
from collections.abc import Callable, Iterable
from typing import Any, Literal, TypeVar
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException, NoSuchFrameException, StaleElementReferenceException, WebDriverException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.remote.webdriver import WebDriver, WebElement
D = TypeVar('D')
T = TypeVar('T')
WebDriverOrWebElement = WebDriver | WebElement

def title_is(title = None):
    '''An expectation for checking the title of a page.

    Args:
        title: The expected title, which must be an exact match.

    Returns:
        True if the title matches, False otherwise.
    '''
    pass
# WARNING: Decompyle incomplete


def title_contains(title = None):
    '''Check that the title contains a case-sensitive substring.

    Args:
        title: The fragment of title expected.

    Returns:
        True when the title matches, False otherwise.
    '''
    pass
# WARNING: Decompyle incomplete


def presence_of_element_located(locator = None):
    '''Check that an element is present on the DOM (not necessarily visible).

    Args:
        locator: Used to find the element.

    Returns:
        The WebElement once it is located.

    Example:
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "q")))
    '''
    pass
# WARNING: Decompyle incomplete


def url_contains(url = None):
    '''Check that the current url contains a case-sensitive substring.

    Args:
        url: The fragment of url expected.

    Returns:
        True when the url matches, False otherwise.
    '''
    pass
# WARNING: Decompyle incomplete


def url_matches(pattern = None):
    '''An expectation for checking the current url.

    Args:
        pattern: The pattern to match with the current url.

    Returns:
        True when the pattern matches, False otherwise.

    Note:
        More powerful than url_contains, as it allows for regular expressions.
    '''
    pass
# WARNING: Decompyle incomplete


def url_to_be(url = None):
    '''An expectation for checking the current url.

    Args:
        url: The expected url, which must be an exact match.

    Returns:
        True when the url matches, False otherwise.
    '''
    pass
# WARNING: Decompyle incomplete


def url_changes(url = None):
    '''Check that the current url differs from a given string.

    Args:
        url: The expected url, which must not be an exact match.

    Returns:
        True when the url does not match, False otherwise.
    '''
    pass
# WARNING: Decompyle incomplete


def visibility_of_element_located(locator = None):
    '''Check that an element is visible (present in DOM and width/height greater than zero).

    Args:
        locator: Used to find the element.

    Returns:
        The WebElement once it is located and visible.

    Example:
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "q")))
    '''
    pass
# WARNING: Decompyle incomplete


def visibility_of(element = None):
    '''Check that an element is visible (present in DOM and width/height greater than zero).

    Args:
        element: The WebElement to check.

    Returns:
        The WebElement once it is visible.

    Example:
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        element = WebDriverWait(driver, 10).until(EC.visibility_of(driver.find_element(By.NAME, "q")))
    '''
    pass
# WARNING: Decompyle incomplete


def _element_if_visible(element = None, visibility = None):
    '''Check if an element has the expected visibility state.

    Args:
        element: The WebElement to check.
        visibility: The expected visibility of the element.

    Returns:
        The WebElement once it is visible or not visible.
    '''
    return element if element.is_displayed() == visibility else False


def presence_of_all_elements_located(locator = None):
    '''Check that all elements matching the locator are present on the DOM.

    Args:
        locator: Used to find the element.

    Returns:
        The list of WebElements once they are located.

    Example:
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "foo")))
    '''
    pass
# WARNING: Decompyle incomplete


def visibility_of_any_elements_located(locator = None):
    '''Check that at least one element is visible on the web page (present in DOM and width/height greater than zero).

    Args:
        locator: Used to find the element.

    Returns:
        The list of WebElements once they are located and visible.

    Example:
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        elements = WebDriverWait(driver, 10).until(EC.visibility_of_any_elements_located((By.CLASS_NAME, "foo")))
    '''
    pass
# WARNING: Decompyle incomplete


def visibility_of_all_elements_located(locator = None):
    '''Check that all elements are visible (present in DOM and width/height greater than zero).

    Args:
        locator: Used to find the elements.

    Returns:
        The list of WebElements once they are located and visible.

    Example:
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        elements = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "foo")))
    '''
    pass
# WARNING: Decompyle incomplete


def text_to_be_present_in_element(locator = None, text_ = None):
    '''Check that the given text is present in the specified element.

    Args:
        locator: Used to find the element.
        text_: The text to be present in the element.

    Returns:
        True when the text is present, False otherwise.

    Example:
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        is_text_in_element = WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "foo"), "bar")
        )
    '''
    pass
# WARNING: Decompyle incomplete


def text_to_be_present_in_element_value(locator = None, text_ = None):
    '''Check that the given text is present in the element\'s value.

    Args:
        locator: Used to find the element.
        text_: The text to be present in the element\'s value.

    Returns:
        True when the text is present, False otherwise.

    Example:
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        is_text_in_element_value = WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element_value((By.CLASS_NAME, "foo"), "bar")
        )
    '''
    pass
# WARNING: Decompyle incomplete


def text_to_be_present_in_element_attribute(locator = None, attribute_ = None, text_ = None):
    '''Check that the given text is present in the element\'s attribute.

    Args:
        locator: Used to find the element.
        attribute_: The attribute to check the text in.
        text_: The text to be present in the element\'s attribute.

    Returns:
        True when the text is present, False otherwise.

    Example:
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        is_text_in_element_attribute = WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element_attribute((By.CLASS_NAME, "foo"), "bar", "baz")
        )
    '''
    pass
# WARNING: Decompyle incomplete


def frame_to_be_available_and_switch_to_it(locator = None):
    '''Check that the given frame is available and switch to it.

    Args:
        locator: Used to find the frame.

    Returns:
        True when the frame is available, False otherwise.

    Example:
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it("frame_name"))
    '''
    pass
# WARNING: Decompyle incomplete


def invisibility_of_element_located(locator = None):
    '''Check that an element is either invisible or not present on the DOM.

    Args:
        locator: Used to find the element.

    Returns:
        True when the element is invisible or not present, False otherwise.

    Example:
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        is_invisible = WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.CLASS_NAME, "foo")))

    Note:
        In the case of NoSuchElement, returns true because the element is not
        present in DOM. The try block checks if the element is present but is
        invisible.
        In the case of StaleElementReference, returns true because stale element
        reference implies that element is no longer visible.
    '''
    pass
# WARNING: Decompyle incomplete


def invisibility_of_element(element = None):
    '''Check that an element is either invisible or not present on the DOM.

    Args:
        element: Used to find the element.

    Returns:
        True when the element is invisible or not present, False otherwise.

    Example:
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        is_invisible_or_not_present = WebDriverWait(driver, 10).until(
            EC.invisibility_of_element(driver.find_element(By.CLASS_NAME, "foo"))
        )
    '''
    return invisibility_of_element_located(element)


def element_to_be_clickable(mark = None):
    '''Check that an element is visible and enabled so it can be clicked.

    Args:
        mark: Used to find the element.

    Returns:
        The WebElement once it is located and clickable.

    Example:
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "foo")))
    '''
    pass
# WARNING: Decompyle incomplete


def staleness_of(element = None):
    '''Wait until an element is no longer attached to the DOM.

    Args:
        element: The element to wait for.

    Returns:
        False if the element is still attached to the DOM, true otherwise.

    Example:
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        is_stale = WebDriverWait(driver, 10).until(EC.staleness_of(driver.find_element(By.CLASS_NAME, "foo")))
    '''
    pass
# WARNING: Decompyle incomplete


def element_to_be_selected(element = None):
    '''An expectation for checking the selection is selected.

    Args:
        element: The WebElement to check.

    Returns:
        True if the element is selected, False otherwise.

    Example:
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        is_selected = WebDriverWait(driver, 10).until(EC.element_to_be_selected(driver.find_element(
            By.CLASS_NAME, "foo"))
        )
    '''
    pass
# WARNING: Decompyle incomplete


def element_located_to_be_selected(locator = None):
    '''An expectation for the element to be located is selected.

    Args:
        locator: Used to find the element.

    Returns:
        True if the element is selected, False otherwise.

    Example:
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        is_selected = WebDriverWait(driver, 10).until(EC.element_located_to_be_selected((By.CLASS_NAME, "foo")))
    '''
    pass
# WARNING: Decompyle incomplete


def element_selection_state_to_be(element = None, is_selected = None):
    '''An expectation for checking if the given element is selected.

    Args:
        element: The WebElement to check.
        is_selected: The expected selection state.

    Returns:
        True if the element\'s selection state is the same as is_selected.

    Example:
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        is_selected = WebDriverWait(driver, 10).until(
            EC.element_selection_state_to_be(driver.find_element(By.CLASS_NAME, "foo"), True)
        )
    '''
    pass
# WARNING: Decompyle incomplete


def element_located_selection_state_to_be(locator = None, is_selected = None):
    '''Check that an element\'s selection state matches the expected state.

    Args:
        locator: Used to find the element.
        is_selected: The expected selection state.

    Returns:
        True if the element\'s selection state is the same as is_selected.

    Example:
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        is_selected = WebDriverWait(driver, 10).until(EC.element_located_selection_state_to_be(
            (By.CLASS_NAME, "foo"), True)
        )
    '''
    pass
# WARNING: Decompyle incomplete


def number_of_windows_to_be(num_windows = None):
    '''An expectation for the number of windows to be a certain value.

    Args:
        num_windows: The expected number of windows.

    Returns:
        True when the number of windows matches, False otherwise.

    Example:
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        is_number_of_windows = WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    '''
    pass
# WARNING: Decompyle incomplete


def new_window_is_opened(current_handles = None):
    '''Check that a new window has been opened (window handles count increased).

    Args:
        current_handles: The current window handles.

    Returns:
        True when a new window is opened, False otherwise.

    Example:
        from selenium.webdriver.support.ui import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        is_new_window_opened = WebDriverWait(driver, 10).until(EC.new_window_is_opened(driver.window_handles))
    '''
    pass
# WARNING: Decompyle incomplete


def alert_is_present():
    '''Check that an alert is present and switch to it.

    Returns:
        The Alert once it is located.

    Example:
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        alert = WebDriverWait(driver, 10).until(EC.alert_is_present())

    Note:
        If the alert is present it switches the given driver to it.
    '''
    
    def _predicate(driver = None):
        
        try:
            return driver.switch_to.alert
        except NoAlertPresentException:
            return False


    return _predicate


def element_attribute_to_include(locator = None, attribute_ = None):
    '''Check if the given attribute is included in the specified element.

    Args:
        locator: Used to find the element.
        attribute_: The attribute to check.

    Returns:
        True when the attribute is included, False otherwise.

    Example:
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        is_attribute_in_element = WebDriverWait(driver, 10).until(
            EC.element_attribute_to_include((By.CLASS_NAME, "foo"), "bar")
        )
    '''
    pass
# WARNING: Decompyle incomplete


def any_of(*expected_conditions):
    '''An expectation that any of multiple expected conditions is true.

    Equivalent to a logical \'OR\'. Returns results of the first matching
    condition, or False if none do.

    Args:
        expected_conditions: The list of expected conditions to check.

    Returns:
        The result of the first matching condition, or False if none do.

    Example:
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        element = WebDriverWait(driver, 10).until(
            EC.any_of(EC.presence_of_element_located((By.NAME, "q"),
            EC.visibility_of_element_located((By.NAME, "q")))
        )
    '''
    pass
# WARNING: Decompyle incomplete


def all_of(*expected_conditions):
    '''An expectation that all of multiple expected conditions is true.

    Equivalent to a logical \'AND\'. When any ExpectedCondition is not met,
    returns False. When all ExpectedConditions are met, returns a List with
    each ExpectedCondition\'s return value.

    Args:
        expected_conditions: The list of expected conditions to check.

    Returns:
        The results of all the matching conditions, or False if any do not.

    Example:
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        elements = WebDriverWait(driver, 10).until(
            EC.all_of(EC.presence_of_element_located((By.NAME, "q"),
            EC.visibility_of_element_located((By.NAME, "q")))
        )
    '''
    pass
# WARNING: Decompyle incomplete


def none_of(*expected_conditions):
    '''An expectation that none of 1 or multiple expected conditions is true.

    Equivalent to a logical \'NOT-OR\'.

    Args:
        expected_conditions: The list of expected conditions to check.

    Returns:
        True if none of the conditions are true, False otherwise.

    Example:
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        element = WebDriverWait(driver, 10).until(
            EC.none_of(EC.presence_of_element_located((By.NAME, "q"),
            EC.visibility_of_element_located((By.NAME, "q")))
        )
    '''
    pass
# WARNING: Decompyle incomplete

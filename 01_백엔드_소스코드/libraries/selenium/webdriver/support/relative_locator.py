# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: relative_locator.pyc (Python 3.11)

import warnings
from typing import NoReturn, overload
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By, ByType
from selenium.webdriver.remote.webelement import WebElement

def with_tag_name(tag_name = None):
    '''Start searching for relative objects using a tag name.

    Args:
        tag_name: The DOM tag of element to start searching.

    Returns:
        RelativeBy: Use this object to create filters within a `find_elements` call.

    Raises:
        WebDriverException: If `tag_name` is None.

    Note:
        This method is deprecated and may be removed in future versions.
        Please use `locate_with` instead.
    '''
    warnings.warn('This method is deprecated and may be removed in future versions. Please use `locate_with` instead.')
    if not tag_name:
        raise WebDriverException('tag_name can not be null')
    return RelativeBy({
        By.CSS_SELECTOR: tag_name })


def locate_with(by = None, using = None):
    '''Start searching for relative objects your search criteria with By.

    Args:
        by: The method to find the element.
        using: The value from `By` passed in.

    Returns:
        RelativeBy: Use this object to create filters within a `find_elements` call.

    Example:
        >>> lowest = driver.find_element(By.ID, "below")
        >>> elements = driver.find_elements(locate_with(By.CSS_SELECTOR, "p").above(lowest))
    '''
    pass
# WARNING: Decompyle incomplete


class RelativeBy:
    '''Find elements based on their relative location from a root element.

    It is recommended that you use the helper function to create instances.

    Example:
    --------
    >>> lowest = driver.find_element(By.ID, "below")
    >>> elements = driver.find_elements(locate_with(By.CSS_SELECTOR, "p").above(lowest))
    >>> ids = [el.get_attribute("id") for el in elements]
    >>> assert "above" in ids
    >>> assert "mid" in ids
    '''
    LocatorType = dict[(ByType, str)]
    
    def __init__(self = None, root = None, filters = None):

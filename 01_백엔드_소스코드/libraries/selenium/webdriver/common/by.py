# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: by.pyc (Python 3.11)

'''The By implementation.'''
from typing import Literal
ByType = Literal[('id', 'xpath', 'link text', 'partial link text', 'name', 'tag name', 'class name', 'css selector')]

class By:
    '''Set of supported locator strategies.

    ID:
    --
    Select the element by its ID.

    >>> element = driver.find_element(By.ID, "myElement")

    XPATH:
    ------
    Select the element via XPATH.
        - absolute path
        - relative path

    >>> element = driver.find_element(By.XPATH, "//html/body/div")

    LINK_TEXT:
    ----------
    Select the link element having the exact text.

    >>> element = driver.find_element(By.LINK_TEXT, "myLink")

    PARTIAL_LINK_TEXT:
    ------------------
    Select the link element having the partial text.

    >>> element = driver.find_element(By.PARTIAL_LINK_TEXT, "my")

    NAME:
    ----
    Select the element by its name attribute.

    >>> element = driver.find_element(By.NAME, "myElement")

    TAG_NAME:
    --------
    Select the element by its tag name.

    >>> element = driver.find_element(By.TAG_NAME, "div")

    CLASS_NAME:
    -----------
    Select the element by its class name.

    >>> element = driver.find_element(By.CLASS_NAME, "myElement")

    CSS_SELECTOR:
    -------------
    Select the element by its CSS selector.

    >>> element = driver.find_element(By.CSS_SELECTOR, "div.myElement")
    '''
    ID: ByType = 'id'
    XPATH: ByType = 'xpath'
    LINK_TEXT: ByType = 'link text'
    PARTIAL_LINK_TEXT: ByType = 'partial link text'
    NAME: ByType = 'name'
    TAG_NAME: ByType = 'tag name'
    CLASS_NAME: ByType = 'class name'
    CSS_SELECTOR: ByType = 'css selector'
    _custom_finders: dict[(str, str)] = { }
    register_custom_finder = (lambda cls = None, name = None, strategy = classmethod: cls._custom_finders[name] = strategy)()
    get_finder = (lambda cls = None, name = None: if not cls._custom_finders.get(name):
passgetattr(cls, name.upper(), None))()
    clear_custom_finders = (lambda cls = None: cls._custom_finders.clear())()

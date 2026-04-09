# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: webelement.pyc (Python 3.11)

from typing import List
from selenium.webdriver.common.by import By
import selenium.webdriver.remote.webelement as selenium

class WebElement(selenium.webdriver.remote.webelement.WebElement):
    pass
# WARNING: Decompyle incomplete


class UCWebElement(WebElement):
    pass
# WARNING: Decompyle incomplete


def _recursive_children(element = None, tag = None, _results = None):
    """
    returns all children of <element> recursively

    :param element: `WebElement` object.
            find children below this <element>

    :param tag: str = None.
            if provided, return only <tag> elements. example: 'a', or 'img'
    :param _results: do not use!
    """
    if not _results:
        pass
    results = set()
    for element in element.children():
        if tag:
            if element.tag_name == tag:
                results.add(element)
            else:
                results.add(element)
        results |= _recursive_children(element, tag, results)
        return results

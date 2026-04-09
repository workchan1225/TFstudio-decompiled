# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: options.pyc (Python 3.11)

import warnings
from abc import ABCMeta, abstractmethod
from enum import Enum
from selenium.common.exceptions import InvalidArgumentException
from selenium.webdriver.common.proxy import Proxy

class PageLoadStrategy(Enum, str):
    '''Enum of possible page load strategies.

    Selenium support following strategies:
        * normal (default) - waits for all resources to download
        * eager - DOM access is ready, but other resources like images may still be loading
        * none - does not block `WebDriver` at all

    Docs: https://www.selenium.dev/documentation/webdriver/drivers/options/#pageloadstrategy.
    '''
    normal = 'normal'
    eager = 'eager'
    none = 'none'


class _BaseOptionsDescriptor:
    
    def __init__(self, name):
        self.name = name

    
    def __get__(self, obj, cls):

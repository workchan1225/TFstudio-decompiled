# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''

         888                                                  888         d8b
         888                                                  888         Y8P
         888                                                  888
 .d8888b 88888b.  888d888 .d88b.  88888b.d88b.   .d88b.   .d88888 888d888 888 888  888  .d88b.  888d888
d88P"    888 "88b 888P"  d88""88b 888 "888 "88b d8P  Y8b d88" 888 888P"   888 888  888 d8P  Y8b 888P"
888      888  888 888    888  888 888  888  888 88888888 888  888 888     888 Y88  88P 88888888 888
Y88b.    888  888 888    Y88..88P 888  888  888 Y8b.     Y88b 888 888     888  Y8bd8P  Y8b.     888
 "Y8888P 888  888 888     "Y88P"  888  888  888  "Y8888   "Y88888 888     888   Y88P    "Y8888  888   88888888

by UltrafunkAmsterdam (https://github.com/ultrafunkamsterdam)

'''
from __future__ import annotations
__version__ = '3.5.5'
import json
import logging
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import time
from weakref import finalize
import selenium.webdriver.chrome.service as selenium
import selenium.webdriver.chrome.webdriver as selenium
from selenium.webdriver.common.by import By
import selenium.webdriver.chromium.service as selenium
import selenium.webdriver.remote.command as selenium
import selenium.webdriver.remote.webdriver as selenium
from cdp import CDP
from dprocess import start_detached
from options import ChromeOptions
from patcher import IS_POSIX
from patcher import Patcher
from reactor import Reactor
from webelement import UCWebElement
from webelement import WebElement
__all__ = ('Chrome', 'ChromeOptions', 'Patcher', 'Reactor', 'CDP', 'find_chrome_executable')
logger = logging.getLogger('uc')
logger.setLevel(logging.getLogger().getEffectiveLevel())

class Chrome(selenium.webdriver.chrome.webdriver.WebDriver):
    pass
# WARNING: Decompyle incomplete


def find_chrome_executable():
    '''
    Finds the chrome, chrome beta, chrome canary, chromium executable

    Returns
    -------
    executable_path :  str
        the full file path to found executable

    '''
    candidates = set()
# WARNING: Decompyle incomplete

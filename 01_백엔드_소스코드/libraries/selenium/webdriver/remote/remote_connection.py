# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: remote_connection.pyc (Python 3.11)

import logging
import string
import sys
import warnings
from base64 import b64encode
from urllib import parse
from urllib.parse import unquote, urlparse
import urllib3
from selenium import __version__
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.remote import utils
from selenium.webdriver.remote.client_config import ClientConfig
from selenium.webdriver.remote.command import Command
from selenium.webdriver.remote.errorhandler import ErrorCode
LOGGER = logging.getLogger(__name__)
# WARNING: Decompyle incomplete

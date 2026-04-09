# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: util.pyc (Python 3.11)

'''
(C) 2014-2019 Roman Sirokov and contributors
Licensed under BSD license

http://github.com/r0x0r/pywebview/
'''
from __future__ import annotations
import inspect
import json
import logging
import os
import re
import sys
import traceback
import urllib.parse as urllib
from collections import UserDict
from glob import glob
from http.cookies import SimpleCookie
from platform import architecture
from threading import Thread
from typing import TYPE_CHECKING, Any
from uuid import uuid4
import webview
from webview.dom import _dnd_state
from webview.errors import WebViewException
if TYPE_CHECKING:
    from webview.window import Window
_TOKEN = uuid4().hex
DEFAULT_HTML = '\n    <!doctype html>\n    <html>\n        <head>\n            <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=0">\n        </head>\n        <body></body>\n    </html>\n'
logger = logging.getLogger('pywebview')

class ImmutableDict(UserDict):
    pass
# WARNING: Decompyle incomplete


def is_app(url = None):
    """Returns true if 'url' is a WSGI or ASGI app."""
    return callable(url)


def is_local_url(url = None):

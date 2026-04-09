# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: log.pyc (Python 3.11)

import json
import pkgutil
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from importlib import import_module
from typing import Any
from selenium.webdriver.common.by import By
cdp = None

def import_cdp():
    global cdp
    if not cdp:
        cdp = import_module('selenium.webdriver.common.bidi.cdp')
        return None


class Log:
    '''Class for accessing logging APIs using the WebDriver Bidi protocol.

    This class is not to be used directly and should be used from the
    webdriver base classes.
    '''
    
    def __init__(self = None, driver = None, bidi_session = None):
        self.driver = driver
        self.session = bidi_session.session
        self.cdp = bidi_session.cdp
        self.devtools = bidi_session.devtools
        _pkg = '.'.join(__name__.split('.')[:-1])
        _mutation_listener_js_bytes = pkgutil.get_data(_pkg, 'mutation-listener.js')
    # WARNING: Decompyle incomplete

    mutation_events = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    add_js_error_listener = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    add_listener = (lambda self = None, event_type = None: pass# WARNING: Decompyle incomplete
)()

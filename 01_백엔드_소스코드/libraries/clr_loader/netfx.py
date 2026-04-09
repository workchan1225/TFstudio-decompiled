# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: netfx.pyc (Python 3.11)

import atexit
from pathlib import Path
from typing import Any, Optional
from ffi import ffi, load_netfx
from types import Runtime, RuntimeInfo, StrOrPath
_FW: Any = None

class NetFx(Runtime):
    
    def __init__(self = None, domain = None, config_file = None):
        self._domain = None
        initialize()
    # WARNING: Decompyle incomplete

    
    def info(self = None):

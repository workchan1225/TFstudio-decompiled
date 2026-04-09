# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: state.pyc (Python 3.11)

import json
from threading import Thread
from typing import Any, Callable
from typing_extensions import Self
from webview.util import escape_string

try:
    from enum import StrEnum
except ImportError:
    from enum import Enum
    
    class StrEnum(Enum, str):
        pass



class StateEventType(StrEnum):
    CHANGE = 'change'
    DELETE = 'delete'


class State(dict):
    pass
# WARNING: Decompyle incomplete

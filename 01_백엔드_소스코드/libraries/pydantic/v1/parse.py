# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: parse.pyc (Python 3.11)

import json
import pickle
from enum import Enum
from pathlib import Path
from typing import Any, Callable, Union
from pydantic.v1.types import StrBytes

class Protocol(Enum, str):
    json = 'json'
    pickle = 'pickle'


def load_str_bytes(b = None, *, content_type, encoding, proto, allow_pickle, json_loads):
    pass
# WARNING: Decompyle incomplete


def load_file(path = None, *, content_type, encoding, proto, allow_pickle, json_loads):
    path = Path(path)
    b = path.read_bytes()
# WARNING: Decompyle incomplete

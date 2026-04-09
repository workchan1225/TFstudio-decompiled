# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: control.pyc (Python 3.11)

import time
from typing import TYPE_CHECKING, Callable, Dict, Iterable, List, Union, Final
from segment import ControlCode, ControlType, Segment
if TYPE_CHECKING:
    from console import Console, ConsoleOptions, RenderResult
STRIP_CONTROL_CODES: Final = [
    7,
    8,
    11,
    12,
    13]
_CONTROL_STRIP_TRANSLATE: Final = STRIP_CONTROL_CODES()
CONTROL_ESCAPE: Final = {
    7: '\\a',
    8: '\\b',
    11: '\\v',
    12: '\\f',
    13: '\\r' }
# WARNING: Decompyle incomplete

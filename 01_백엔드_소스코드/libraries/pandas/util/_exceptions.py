# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _exceptions.pyc (Python 3.11)

from __future__ import annotations
import contextlib
import inspect
import os
import re
from typing import TYPE_CHECKING, Any
import warnings
if TYPE_CHECKING:
    from collections.abc import Generator
    from types import FrameType
rewrite_exception = (lambda old_name = None, new_name = None: pass# WARNING: Decompyle incomplete
)()

def find_stack_level():
    '''
    Find the first place in the stack that is not inside pandas
    (tests notwithstanding).
    '''
    import pandas as pd
    pkg_dir = os.path.dirname(pd.__file__)
    test_dir = os.path.join(pkg_dir, 'tests')
    frame = inspect.currentframe()
# WARNING: Decompyle incomplete

rewrite_warning = (lambda target_message = None, target_category = None, new_message = contextlib.contextmanager, new_category = (None,): pass# WARNING: Decompyle incomplete
)()

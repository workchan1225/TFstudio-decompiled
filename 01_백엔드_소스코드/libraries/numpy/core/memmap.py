# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: memmap.pyc (Python 3.11)

from contextlib import nullcontext
import numpy as np
from _utils import set_module
from numeric import uint8, ndarray, dtype
from numpy.compat import os_fspath, is_pathlib_path
__all__ = [
    'memmap']
dtypedescr = dtype
valid_filemodes = [
    'r',
    'c',
    'r+',
    'w+']
writeable_filemodes = [
    'r+',
    'w+']
mode_equivalents = {
    'readonly': 'r',
    'copyonwrite': 'c',
    'readwrite': 'r+',
    'write': 'w+' }
memmap = <NODE:12>()

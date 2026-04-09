# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tags.pyc (Python 3.11)

from __future__ import annotations
import logging
import platform
import re
import struct
import subprocess
import sys
import sysconfig
from importlib.machinery import EXTENSION_SUFFIXES
from typing import Iterable, Iterator, Sequence, Tuple, cast
from  import _manylinux, _musllinux
logger = logging.getLogger(__name__)
PythonVersion = Sequence[int]
AppleVersion = Tuple[(int, int)]
INTERPRETER_SHORT_NAMES: 'dict[str, str]' = {
    'python': 'py',
    'cpython': 'cp',
    'pypy': 'pp',
    'ironpython': 'ip',
    'jython': 'jy' }
_32_BIT_INTERPRETER = struct.calcsize('P') == 4

class Tag:
    '''
    A representation of the tag triple for a wheel.

    Instances are considered immutable and thus are hashable. Equality checking
    is also supported.
    '''
    __slots__ = [
        '_abi',
        '_hash',
        '_interpreter',
        '_platform']
    
    def __init__(self = None, interpreter = None, abi = None, platform = ('interpreter', 'str', 'abi', 'str', 'platform', 'str', 'return', 'None')):
        self._interpreter = interpreter.lower()
        self._abi = abi.lower()
        self._platform = platform.lower()
        self._hash = hash((self._interpreter, self._abi, self._platform))

    interpreter = (lambda self = None: self._interpreter)()
    abi = (lambda self = None: self._abi)()
    platform = (lambda self = None: self._platform)()
    
    def __eq__(self = None, other = None):

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tags.pyc (Python 3.11)

import logging
import platform
import sys
import sysconfig
from importlib.machinery import EXTENSION_SUFFIXES
from typing import Dict, FrozenSet, Iterable, Iterator, List, Optional, Sequence, Tuple, Union, cast
from  import _manylinux, _musllinux
logger = logging.getLogger(__name__)
PythonVersion = Sequence[int]
MacVersion = Tuple[(int, int)]
INTERPRETER_SHORT_NAMES: Dict[(str, str)] = {
    'python': 'py',
    'cpython': 'cp',
    'pypy': 'pp',
    'ironpython': 'ip',
    'jython': 'jy' }
_32_BIT_INTERPRETER = sys.maxsize <= 0x100000000

class Tag:
    '''
    A representation of the tag triple for a wheel.

    Instances are considered immutable and thus are hashable. Equality checking
    is also supported.
    '''
    __slots__ = [
        '_interpreter',
        '_abi',
        '_platform',
        '_hash']
    
    def __init__(self = None, interpreter = None, abi = None, platform = ('interpreter', str, 'abi', str, 'platform', str, 'return', None)):
        self._interpreter = interpreter.lower()
        self._abi = abi.lower()
        self._platform = platform.lower()
        self._hash = hash((self._interpreter, self._abi, self._platform))

    interpreter = (lambda self = None: self._interpreter)()
    abi = (lambda self = None: self._abi)()
    platform = (lambda self = None: self._platform)()
    
    def __eq__(self = None, other = None):

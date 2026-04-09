# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _constants.pyc (Python 3.11)

'''
_constants
======

Constants relevant for the Python implementation.
'''
from __future__ import annotations
import platform
import sys
import sysconfig
IS64 = sys.maxsize > 0x100000000
PY312 = sys.version_info >= (3, 12)
PY314 = sys.version_info >= (3, 14)
PYPY = platform.python_implementation() == 'PyPy'
if not sys.platform == 'emscripten':
    WASM = platform.machine() in ('wasm32', 'wasm64')
    if not sysconfig.get_config_var('HOST_GNU_TYPE'):
        ISMUSL = 'musl' in ''
REF_COUNT = 2 if PY314 else 3
REF_COUNT_IDX = 2
REF_COUNT_METHOD = 1 if PY314 else 2
CHAINED_WARNING_DISABLED = PYPY
__all__ = [
    'IS64',
    'ISMUSL',
    'PY312',
    'PY314',
    'PYPY',
    'WASM']

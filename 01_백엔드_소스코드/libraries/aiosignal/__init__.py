# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

import sys
from typing import Any, Awaitable, Callable, TypeVar
from frozenlist import FrozenList
if sys.version_info >= (3, 11):
    from typing import Unpack
else:
    from typing_extensions import Unpack
if sys.version_info >= (3, 13):
    from typing import TypeVarTuple
else:
    from typing_extensions import TypeVarTuple
_T = TypeVar('_T')
_Ts = TypeVarTuple('_Ts', default = Unpack[tuple[()]])
__version__ = '1.4.0'
__all__ = ('Signal',)

def Signal():
    '''Signal'''
    pass
# WARNING: Decompyle incomplete

Signal = <NODE:27>(Signal, 'Signal', FrozenList[Callable[([
    Unpack[_Ts]], Awaitable[object])]])

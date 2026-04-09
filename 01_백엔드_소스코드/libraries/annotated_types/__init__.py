# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

import math
import sys
import types
from dataclasses import dataclass
from datetime import tzinfo
from typing import TYPE_CHECKING, Any, Callable, Iterator, Optional, SupportsFloat, SupportsIndex, TypeVar, Union
if sys.version_info < (3, 8):
    from typing_extensions import Protocol, runtime_checkable
else:
    from typing import Protocol, runtime_checkable
if sys.version_info < (3, 9):
    from typing_extensions import Annotated, Literal
else:
    from typing import Annotated, Literal
if sys.version_info < (3, 10):
    EllipsisType = type(Ellipsis)
    KW_ONLY = { }
    SLOTS = { }
else:
    from types import EllipsisType
    KW_ONLY = {
        'kw_only': True }
    SLOTS = {
        'slots': True }
__all__ = ('BaseMetadata', 'GroupedMetadata', 'Gt', 'Ge', 'Lt', 'Le', 'Interval', 'MultipleOf', 'MinLen', 'MaxLen', 'Len', 'Timezone', 'Predicate', 'LowerCase', 'UpperCase', 'IsDigits', 'IsFinite', 'IsNotFinite', 'IsNan', 'IsNotNan', 'IsInfinite', 'IsNotInfinite', 'doc', 'DocInfo', '__version__')
__version__ = '0.7.0'
T = TypeVar('T')

class SupportsGt(Protocol):
    
    def __gt__(self = None, _SupportsGt__other = None):
        pass



class SupportsGe(Protocol):
    
    def __ge__(self = None, _SupportsGe__other = None):
        pass



class SupportsLt(Protocol):
    
    def __lt__(self = None, _SupportsLt__other = None):
        pass



class SupportsLe(Protocol):
    
    def __le__(self = None, _SupportsLe__other = None):
        pass



class SupportsMod(Protocol):
    
    def __mod__(self = None, _SupportsMod__other = None):
        pass



class SupportsDiv(Protocol):
    
    def __div__(self = None, _SupportsDiv__other = None):
        pass



class BaseMetadata:
    '''Base class for all metadata.

    This exists mainly so that implementers
    can do `isinstance(..., BaseMetadata)` while traversing field annotations.
    '''
    __slots__ = ()

# WARNING: Decompyle incomplete

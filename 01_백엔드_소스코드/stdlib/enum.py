# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: enum.pyc (Python 3.11)

import sys
import builtins as bltns
from types import MappingProxyType, DynamicClassAttribute
from operator import or_ as _or_
from functools import reduce
__all__ = [
    'EnumType',
    'EnumMeta',
    'Enum',
    'IntEnum',
    'StrEnum',
    'Flag',
    'IntFlag',
    'ReprEnum',
    'auto',
    'unique',
    'property',
    'verify',
    'member',
    'nonmember',
    'FlagBoundary',
    'STRICT',
    'CONFORM',
    'EJECT',
    'KEEP',
    'global_flag_repr',
    'global_enum_repr',
    'global_str',
    'global_enum',
    'EnumCheck',
    'CONTINUOUS',
    'NAMED_FLAGS',
    'UNIQUE',
    'pickle_by_global_name',
    'pickle_by_enum_name']
Enum = None
Flag = None
EJECT = None
_stdlib_enums = None
ReprEnum = None

class nonmember(object):
    '''
    Protects item from becoming an Enum member during class creation.
    '''
    
    def __init__(self, value):
        self.value = value



class member(object):
    '''
    Forces item to become an Enum member during class creation.
    '''
    
    def __init__(self, value):
        self.value = value



def _is_descriptor(obj):

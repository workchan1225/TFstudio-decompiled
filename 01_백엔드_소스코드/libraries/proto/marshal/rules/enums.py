# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: enums.pyc (Python 3.11)

from typing import Type
import enum
import warnings

class EnumRule:
    '''A marshal for converting between integer values and enum values.'''
    
    def __init__(self = None, enum_class = None):
        self._enum = enum_class

    
    def to_python(self = None, value = None, *, absent):

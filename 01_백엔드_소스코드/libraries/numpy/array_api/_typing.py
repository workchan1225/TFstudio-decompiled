# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _typing.pyc (Python 3.11)

"""
This file defines the types for type annotations.

These names aren't part of the module namespace, but they are used in the
annotations in the function signatures. The functions in the module are only
valid for inputs that match the given type annotations.
"""
from __future__ import annotations
__all__ = [
    'Array',
    'Device',
    'Dtype',
    'SupportsDLPack',
    'SupportsBufferProtocol',
    'PyCapsule']
import sys
from typing import Any, Literal, Sequence, Type, Union, TypeVar, Protocol
from _array_object import Array
from numpy import dtype, int8, int16, int32, int64, uint8, uint16, uint32, uint64, float32, float64
_T_co = TypeVar('_T_co', covariant = True)

def NestedSequence():
    '''NestedSequence'''
    
    def __getitem__(self = None, key = None):
        pass

    
    def __len__(self = None):
        pass


NestedSequence = <NODE:27>(NestedSequence, 'NestedSequence', Protocol[_T_co])
Device = Literal['cpu']
Dtype = dtype[Union[(int8, int16, int32, int64, uint8, uint16, uint32, uint64, float32, float64)]]
if sys.version_info >= (3, 12):
    from collections.abc import Buffer as SupportsBufferProtocol
else:
    SupportsBufferProtocol = Any
PyCapsule = Any

class SupportsDLPack(Protocol):
    
    def __dlpack__(self = None, *, stream):
        pass

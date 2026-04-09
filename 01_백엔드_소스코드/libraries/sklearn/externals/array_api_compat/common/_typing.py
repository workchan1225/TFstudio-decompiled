# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _typing.pyc (Python 3.11)

from __future__ import annotations
from collections.abc import Mapping
from types import ModuleType as Namespace
from typing import TYPE_CHECKING, Literal, Protocol, TypeAlias, TypedDict, TypeVar, final
if TYPE_CHECKING:
    from _typeshed import Incomplete
    SupportsBufferProtocol: 'TypeAlias' = Incomplete
    Array: 'TypeAlias' = Incomplete
    Device: 'TypeAlias' = Incomplete
    DType: 'TypeAlias' = Incomplete
else:
    SupportsBufferProtocol = object
    Array = object
    Device = object
    DType = object
_T_co = TypeVar('_T_co', covariant = True)
JustInt = <NODE:12>()
JustFloat = <NODE:12>()
JustComplex = <NODE:12>()

def NestedSequence():
    '''NestedSequence'''
    
    def __getitem__(self = None, key = None):
        pass

    
    def __len__(self = None):
        pass


NestedSequence = <NODE:27>(NestedSequence, 'NestedSequence', Protocol[_T_co])

def SupportsArrayNamespace():
    '''SupportsArrayNamespace'''
    
    def __array_namespace__(self = None, *, api_version):
        pass


SupportsArrayNamespace = <NODE:27>(SupportsArrayNamespace, 'SupportsArrayNamespace', Protocol[_T_co])

def HasShape():
    '''HasShape'''
    shape = (lambda self = None: pass)()

HasShape = <NODE:27>(HasShape, 'HasShape', Protocol[_T_co])
Capabilities = TypedDict('Capabilities', {
    'boolean indexing': bool,
    'data-dependent shapes': bool,
    'max dimensions': int })
DefaultDTypes = TypedDict('DefaultDTypes', {
    'real floating': DType,
    'complex floating': DType,
    'integral': DType,
    'indexing': DType })
_DTypeKind: 'TypeAlias' = Literal[('bool', 'signed integer', 'unsigned integer', 'integral', 'real floating', 'complex floating', 'numeric')]
DTypeKind: 'TypeAlias' = _DTypeKind | tuple[(_DTypeKind, ...)]

class DTypesBool(TypedDict):
    bool: 'DType' = 'DTypesBool'


class DTypesSigned(TypedDict):
    int64: 'DType' = 'DTypesSigned'


class DTypesUnsigned(TypedDict):
    uint64: 'DType' = 'DTypesUnsigned'


class DTypesIntegral(DTypesUnsigned, DTypesSigned):
    pass


class DTypesReal(TypedDict):
    float64: 'DType' = 'DTypesReal'


class DTypesComplex(TypedDict):
    complex128: 'DType' = 'DTypesComplex'


class DTypesNumeric(DTypesComplex, DTypesReal, DTypesIntegral):
    pass


class DTypesAll(DTypesNumeric, DTypesBool):
    pass

DTypesAny: 'TypeAlias' = Mapping[(str, DType)]
__all__ = [
    'Array',
    'Capabilities',
    'DType',
    'DTypeKind',
    'DTypesAny',
    'DTypesAll',
    'DTypesBool',
    'DTypesNumeric',
    'DTypesIntegral',
    'DTypesSigned',
    'DTypesUnsigned',
    'DTypesReal',
    'DTypesComplex',
    'DefaultDTypes',
    'Device',
    'HasShape',
    'Namespace',
    'JustInt',
    'JustFloat',
    'JustComplex',
    'NestedSequence',
    'SupportsArrayNamespace',
    'SupportsBufferProtocol']

def __dir__():
    return __all__

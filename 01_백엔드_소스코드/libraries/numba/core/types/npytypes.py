# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: npytypes.pyc (Python 3.11)

import collections
import warnings
from functools import cached_property
from llvmlite import ir
from abstract import DTypeSpec, IteratorType, MutableSequence, Number, Type
from common import Buffer, Opaque, SimpleIteratorType
from numba.core.typeconv import Conversion
from numba.core import utils
from misc import UnicodeType
from containers import Bytes
import numpy as np

class CharSeq(Type):
    pass
# WARNING: Decompyle incomplete


class UnicodeCharSeq(Type):
    pass
# WARNING: Decompyle incomplete

_RecordField = collections.namedtuple('_RecordField', 'type,offset,alignment,title')

class Record(Type):
    pass
# WARNING: Decompyle incomplete


class DType(Opaque, DTypeSpec):
    pass
# WARNING: Decompyle incomplete


class NumpyFlatType(MutableSequence, SimpleIteratorType):
    pass
# WARNING: Decompyle incomplete


class NumpyNdEnumerateType(SimpleIteratorType):
    pass
# WARNING: Decompyle incomplete


class NumpyNdIterType(IteratorType):
    pass
# WARNING: Decompyle incomplete


class NumpyNdIndexType(SimpleIteratorType):
    pass
# WARNING: Decompyle incomplete


class Array(Buffer):
    pass
# WARNING: Decompyle incomplete


class ArrayCTypes(Type):
    pass
# WARNING: Decompyle incomplete


class ArrayFlags(Type):
    pass
# WARNING: Decompyle incomplete


class NestedArray(Array):
    pass
# WARNING: Decompyle incomplete


class NumPyRandomBitGeneratorType(Type):
    pass
# WARNING: Decompyle incomplete


class NumPyRandomGeneratorType(Type):
    pass
# WARNING: Decompyle incomplete


class PolynomialType(Type):
    pass
# WARNING: Decompyle incomplete

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: dataframe_protocol.pyc (Python 3.11)

'''
A verbatim copy (vendored) of the spec from https://github.com/data-apis/dataframe-api
'''
from __future__ import annotations
from abc import ABC, abstractmethod
import enum
from typing import TYPE_CHECKING, Any, TypedDict
from pandas.util._decorators import set_module
if TYPE_CHECKING:
    from collections.abc import Iterable, Sequence

class DlpackDeviceType(enum.IntEnum):
    '''Integer enum for device type codes matching DLPack.'''
    CPU = 1
    CUDA = 2
    CPU_PINNED = 3
    OPENCL = 4
    VULKAN = 7
    METAL = 8
    VPI = 9
    ROCM = 10


class DtypeKind(enum.IntEnum):
    '''
    Integer enum for data types.

    Attributes
    ----------
    INT : int
        Matches to signed integer data type.
    UINT : int
        Matches to unsigned integer data type.
    FLOAT : int
        Matches to floating point data type.
    BOOL : int
        Matches to boolean data type.
    STRING : int
        Matches to string data type (UTF-8 encoded).
    DATETIME : int
        Matches to datetime data type.
    CATEGORICAL : int
        Matches to categorical data type.
    '''
    INT = 0
    UINT = 1
    FLOAT = 2
    BOOL = 20
    STRING = 21
    DATETIME = 22
    CATEGORICAL = 23


class ColumnNullType(enum.IntEnum):
    '''
    Integer enum for null type representation.

    Attributes
    ----------
    NON_NULLABLE : int
        Non-nullable column.
    USE_NAN : int
        Use explicit float NaN value.
    USE_SENTINEL : int
        Sentinel value besides NaN/NaT.
    USE_BITMASK : int
        The bit is set/unset representing a null on a certain position.
    USE_BYTEMASK : int
        The byte is set/unset representing a null on a certain position.
    '''
    NON_NULLABLE = 0
    USE_NAN = 1
    USE_SENTINEL = 2
    USE_BITMASK = 3
    USE_BYTEMASK = 4


class ColumnBuffers(TypedDict):
    offsets: 'tuple[Buffer, Any] | None' = 'ColumnBuffers'


class CategoricalDescription(TypedDict):
    categories: 'Column | None' = 'CategoricalDescription'


class Buffer(ABC):
    """
    Data in the buffer is guaranteed to be contiguous in memory.

    Note that there is no dtype attribute present, a buffer can be thought of
    as simply a block of memory. However, if the column that the buffer is
    attached to has a dtype that's supported by DLPack and ``__dlpack__`` is
    implemented, then that dtype information will be contained in the return
    value from ``__dlpack__``.

    This distinction is useful to support both data exchange via DLPack on a
    buffer and (b) dtypes like variable-length strings which do not have a
    fixed number of bytes per element.
    """
    bufsize = (lambda self = None: pass)()()
    ptr = (lambda self = None: pass)()()
    __dlpack__ = (lambda self: raise NotImplementedError('__dlpack__'))()
    __dlpack_device__ = (lambda self = None: pass)()


class Column(ABC):
    '''
    A column object, with only the methods and properties required by the
    interchange protocol defined.

    A column can contain one or more chunks. Each chunk can contain up to three
    buffers - a data buffer, a mask buffer (depending on null representation),
    and an offsets buffer (if variable-size binary; e.g., variable-length
    strings).

    TBD: Arrow has a separate "null" dtype, and has no separate mask concept.
         Instead, it seems to use "children" for both columns with a bit mask,
         and for nested dtypes. Unclear whether this is elegant or confusing.
         This design requires checking the null representation explicitly.

         The Arrow design requires checking:
         1. the ARROW_FLAG_NULLABLE (for sentinel values)
         2. if a column has two children, combined with one of those children
            having a null dtype.

         Making the mask concept explicit seems useful. One null dtype would
         not be enough to cover both bit and byte masks, so that would mean
         even more checking if we did it the Arrow way.

    TBD: there\'s also the "chunk" concept here, which is implicit in Arrow as
         multiple buffers per array (= column here). Semantically it may make
         sense to have both: chunks were meant for example for lazy evaluation
         of data which doesn\'t fit in memory, while multiple buffers per column
         could also come from doing a selection operation on a single
         contiguous buffer.

         Given these concepts, one would expect chunks to be all of the same
         size (say a 10,000 row dataframe could have 10 chunks of 1,000 rows),
         while multiple buffers could have data-dependent lengths. Not an issue
         in pandas if one column is backed by a single NumPy array, but in
         Arrow it seems possible.
         Are multiple chunks *and* multiple buffers per column necessary for
         the purposes of this interchange protocol, or must producers either
         reuse the chunk concept for this or copy the data?

    Note: this Column object can only be produced by ``__dataframe__``, so
          doesn\'t need its own version or ``__column__`` protocol.
    '''
    size = (lambda self = None: pass)()
    offset = (lambda self = None: pass)()()
    dtype = (lambda self = None: pass)()()
    describe_categorical = (lambda self = None: pass)()()
    describe_null = (lambda self = None: pass)()()
    null_count = (lambda self = None: pass)()()
    metadata = (lambda self = None: pass)()()
    num_chunks = (lambda self = None: pass)()
    get_chunks = (lambda self = None, n_chunks = None: pass)()
    get_buffers = (lambda self = None: pass)()

DataFrame = <NODE:12>()

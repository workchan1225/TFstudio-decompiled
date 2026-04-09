# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _typing.pyc (Python 3.11)

from __future__ import annotations
from builtins import type as type_t
from collections.abc import Callable, Hashable, Iterator, Mapping, MutableMapping, Sequence
from datetime import date, datetime, timedelta, tzinfo
from os import PathLike
from typing import TYPE_CHECKING, Any, Literal, ParamSpec, Protocol, SupportsIndex, TypeAlias, TypeVar, Union, overload
import numpy as np
from numpy.typing import typing as npt
if TYPE_CHECKING:
    from pandas._libs import NaTType, Period, Timedelta, Timestamp
    from pandas._libs.tslibs import BaseOffset
    from pandas.core.dtypes.dtypes import ExtensionDtype
    from pandas import DatetimeIndex, Interval, PeriodIndex, TimedeltaIndex
    from pandas.arrays import DatetimeArray, TimedeltaArray
    from pandas.core.arrays.base import ExtensionArray
    from pandas.core.frame import DataFrame
    from pandas.core.generic import NDFrame
    from pandas.core.groupby.generic import DataFrameGroupBy, GroupBy, SeriesGroupBy
    from pandas.core.indexes.base import Index
    from pandas.core.internals import BlockManager, SingleBlockManager
    from pandas.core.resample import Resampler
    from pandas.core.series import Series
    from pandas.core.window.rolling import BaseWindow
    from pandas.io.formats.format import EngFormatter
    from pandas.tseries.holiday import AbstractHolidayCalendar
    ScalarLike_co: 'TypeAlias' = int | float | complex | str | bytes | np.generic
    NumpyValueArrayLike: 'TypeAlias' = ScalarLike_co | npt.ArrayLike
    NumpySorter: 'TypeAlias' = npt._ArrayLikeInt_co | None
P = ParamSpec('P')
HashableT = TypeVar('HashableT', bound = Hashable)
HashableT2 = TypeVar('HashableT2', bound = Hashable)
MutableMappingT = TypeVar('MutableMappingT', bound = MutableMapping)
ArrayLike: 'TypeAlias' = Union[('ExtensionArray', np.ndarray)]
ArrayLikeT = TypeVar('ArrayLikeT', 'ExtensionArray', np.ndarray)
AnyArrayLike: 'TypeAlias' = Union[(ArrayLike, 'Index', 'Series')]
TimeArrayLike: 'TypeAlias' = Union[('DatetimeArray', 'TimedeltaArray')]
_T_co = TypeVar('_T_co', covariant = True)

def SequenceNotStr():
    '''SequenceNotStr'''
    __module__: 'str' = 'pandas.api.typing.aliases'
    __getitem__ = (lambda self = None, index = None: pass)()
    __getitem__ = (lambda self = None, index = None: pass)()
    
    def __contains__(self = None, value = None):
        pass

    
    def __len__(self = None):
        pass

    
    def __iter__(self = None):
        pass

    
    def index(self = None, value = None, start = None, stop = (..., ...)):
        pass

    
    def count(self = None, value = None):
        pass

    
    def __reversed__(self = None):
        pass


SequenceNotStr = <NODE:27>(SequenceNotStr, 'SequenceNotStr', Protocol[_T_co])
ListLike: 'TypeAlias' = AnyArrayLike | SequenceNotStr | range
PythonScalar: 'TypeAlias' = str | float | bool
DatetimeLikeScalar: 'TypeAlias' = Union[('Period', 'Timestamp', 'Timedelta')]
_IndexIterScalar: 'TypeAlias' = Union[(str, bytes, date, datetime, timedelta, np.datetime64, np.timedelta64, bool, int, float, 'Timestamp', 'Timedelta')]
Scalar: 'TypeAlias' = Union[(_IndexIterScalar, 'Interval', complex, np.integer, np.floating, np.complexfloating)]
IntStrT = TypeVar('IntStrT', bound = int | str)
TimestampConvertibleTypes: 'TypeAlias' = Union[('Timestamp', date, np.datetime64, np.int64, float, str)]
TimestampNonexistent: 'TypeAlias' = Literal[('shift_forward', 'shift_backward', 'NaT', 'raise')] | timedelta
TimedeltaConvertibleTypes: 'TypeAlias' = Union[('Timedelta', timedelta, np.timedelta64, np.int64, float, str)]
Timezone: 'TypeAlias' = str | tzinfo
ToTimestampHow: 'TypeAlias' = Literal[('s', 'e', 'start', 'end')]
NDFrameT = TypeVar('NDFrameT', bound = 'NDFrame')
IndexT = TypeVar('IndexT', bound = 'Index')
FreqIndexT = TypeVar('FreqIndexT', 'DatetimeIndex', 'PeriodIndex', 'TimedeltaIndex')
NumpyIndexT = TypeVar('NumpyIndexT', np.ndarray, 'Index')
AxisInt: 'TypeAlias' = int
Axis: 'TypeAlias' = AxisInt | Literal[('index', 'columns', 'rows')]
IndexLabel: 'TypeAlias' = Hashable | Sequence[Hashable]
Level: 'TypeAlias' = Hashable
Shape: 'TypeAlias' = tuple[(int, ...)]
Suffixes: 'TypeAlias' = Sequence[str | None]
Ordered: 'TypeAlias' = bool | None
JSONSerializable: 'TypeAlias' = PythonScalar | list | dict | None
Frequency: 'TypeAlias' = Union[(str, 'BaseOffset')]
Axes: 'TypeAlias' = ListLike
RandomState: 'TypeAlias' = int | np.ndarray | np.random.Generator | np.random.BitGenerator | np.random.RandomState
NpDtype: 'TypeAlias' = str | np.dtype | type[str | complex | bool | object]
Dtype: 'TypeAlias' = Union[('ExtensionDtype', NpDtype)]
AstypeArg: 'TypeAlias' = Union[('ExtensionDtype', npt.DTypeLike)]
DtypeArg: 'TypeAlias' = Dtype | Mapping[(Hashable, Dtype)]
DtypeObj: 'TypeAlias' = Union[(np.dtype, 'ExtensionDtype')]
ConvertersArg: 'TypeAlias' = dict[(Hashable, Callable[([
    Dtype], Dtype)])]
ParseDatesArg: 'TypeAlias' = bool | list[Hashable] | list[list[Hashable]] | dict[(Hashable, list[Hashable])]
Renamer: 'TypeAlias' = Mapping[(Any, Hashable)] | Callable[([
    Any], Hashable)]
T = TypeVar('T')
FuncType: 'TypeAlias' = Callable[(..., Any)]
F = TypeVar('F', bound = FuncType)
TypeT = TypeVar('TypeT', bound = type)
ValueKeyFunc: 'TypeAlias' = Callable[([
    'Series'], Union[('Series', AnyArrayLike)])] | None
IndexKeyFunc: 'TypeAlias' = Callable[([
    'Index'], Union[('Index', AnyArrayLike)])] | None
AggFuncTypeBase: 'TypeAlias' = Callable | str
AggFuncTypeDict: 'TypeAlias' = MutableMapping[(Hashable, AggFuncTypeBase | list[AggFuncTypeBase])]
AggFuncType: 'TypeAlias' = AggFuncTypeBase | list[AggFuncTypeBase] | AggFuncTypeDict
AggObjType: 'TypeAlias' = Union[('Series', 'DataFrame', 'GroupBy', 'SeriesGroupBy', 'DataFrameGroupBy', 'BaseWindow', 'Resampler')]
PythonFuncType: 'TypeAlias' = Callable[([
    Any], Any)]
AnyStr_co = TypeVar('AnyStr_co', str, bytes, covariant = True)
AnyStr_contra = TypeVar('AnyStr_contra', str, bytes, contravariant = True)

class BaseBuffer(Protocol):
    mode = (lambda self = None: pass)()
    
    def seek(self = None, offset = None, whence = None):
        pass

    
    def seekable(self = None):
        pass

    
    def tell(self = None):
        pass



def ReadBuffer():
    '''ReadBuffer'''
    __module__: 'str' = 'pandas.api.typing.aliases'
    
    def read(self = None, n = None):
        pass


ReadBuffer = <NODE:27>(ReadBuffer, 'ReadBuffer', BaseBuffer, Protocol[AnyStr_co])

def WriteBuffer():
    '''WriteBuffer'''
    __module__: 'str' = 'pandas.api.typing.aliases'
    
    def write(self = None, b = None):
        pass

    
    def flush(self = None):
        pass


WriteBuffer = <NODE:27>(WriteBuffer, 'WriteBuffer', BaseBuffer, Protocol[AnyStr_contra])

def ReadPickleBuffer():
    '''ReadPickleBuffer'''
    __module__: 'str' = 'pandas.api.typing.aliases'
    
    def readline(self = None):
        pass


ReadPickleBuffer = <NODE:27>(ReadPickleBuffer, 'ReadPickleBuffer', ReadBuffer[bytes], Protocol)

def WriteExcelBuffer():
    '''WriteExcelBuffer'''
    __module__: 'str' = 'pandas.api.typing.aliases'
    
    def truncate(self = None, size = None):
        pass


WriteExcelBuffer = <NODE:27>(WriteExcelBuffer, 'WriteExcelBuffer', WriteBuffer[bytes], Protocol)

def ReadCsvBuffer():
    '''ReadCsvBuffer'''
    __module__: 'str' = 'pandas.api.typing.aliases'
    
    def __iter__(self = None):
        pass

    
    def fileno(self = None):
        pass

    
    def readline(self = None):
        pass

    closed = (lambda self = None: pass)()

ReadCsvBuffer = <NODE:27>(ReadCsvBuffer, 'ReadCsvBuffer', ReadBuffer[AnyStr_co], Protocol)
FilePath: 'TypeAlias' = str | PathLike[str]
StorageOptions: 'TypeAlias' = dict[(str, Any)] | None
CompressionDict: 'TypeAlias' = dict[(str, Any)]
CompressionOptions: 'TypeAlias' = Literal[('infer', 'gzip', 'bz2', 'zip', 'xz', 'zstd', 'tar')] | CompressionDict | None
ParquetCompressionOptions: 'TypeAlias' = Literal[('snappy', 'gzip', 'brotli', 'lz4', 'zstd')] | None
FormattersType: 'TypeAlias' = list[Callable] | tuple[(Callable, ...)] | Mapping[(str | int, Callable)]
ColspaceType: 'TypeAlias' = Mapping[(Hashable, str | int)]
FloatFormatType: 'TypeAlias' = Union[(str, Callable, 'EngFormatter')]
ColspaceArgType: 'TypeAlias' = str | int | Sequence[str | int] | Mapping[(Hashable, str | int)]
FillnaOptions: 'TypeAlias' = Literal[('backfill', 'bfill', 'ffill', 'pad')]
InterpolateOptions: 'TypeAlias' = Literal[('linear', 'time', 'index', 'values', 'nearest', 'zero', 'slinear', 'quadratic', 'cubic', 'barycentric', 'polynomial', 'krogh', 'piecewise_polynomial', 'spline', 'pchip', 'akima', 'cubicspline', 'from_derivatives')]
Manager: 'TypeAlias' = Union[('BlockManager', 'SingleBlockManager')]
ScalarIndexer: 'TypeAlias' = int | np.integer
SequenceIndexer: 'TypeAlias' = slice | list[int] | np.ndarray
PositionalIndexer: 'TypeAlias' = ScalarIndexer | SequenceIndexer
PositionalIndexerTuple: 'TypeAlias' = tuple[(PositionalIndexer, PositionalIndexer)]
PositionalIndexer2D: 'TypeAlias' = PositionalIndexer | PositionalIndexerTuple
TakeIndexer: 'TypeAlias' = Sequence[int] | Sequence[np.integer] | npt.NDArray[np.integer]
IgnoreRaise: 'TypeAlias' = Literal[('ignore', 'raise')]
WindowingRankType: 'TypeAlias' = Literal[('average', 'min', 'max')]
CSVEngine: 'TypeAlias' = Literal[('c', 'python', 'pyarrow', 'python-fwf')]
JSONEngine: 'TypeAlias' = Literal[('ujson', 'pyarrow')]
XMLParsers: 'TypeAlias' = Literal[('lxml', 'etree')]
HTMLFlavors: 'TypeAlias' = Literal[('lxml', 'html5lib', 'bs4')]
IntervalLeftRight: 'TypeAlias' = Literal[('left', 'right')]
IntervalClosedType: 'TypeAlias' = IntervalLeftRight | Literal[('both', 'neither')]
DatetimeNaTType: 'TypeAlias' = Union[(datetime, 'NaTType')]
DateTimeErrorChoices: 'TypeAlias' = Literal[('raise', 'coerce')]
SortKind: 'TypeAlias' = Literal[('quicksort', 'mergesort', 'heapsort', 'stable')]
NaPosition: 'TypeAlias' = Literal[('first', 'last')]
NsmallestNlargestKeep: 'TypeAlias' = Literal[('first', 'last', 'all')]
QuantileInterpolation: 'TypeAlias' = Literal[('linear', 'lower', 'higher', 'midpoint', 'nearest')]
PlottingOrientation: 'TypeAlias' = Literal[('horizontal', 'vertical')]
AnyAll: 'TypeAlias' = Literal[('any', 'all')]
MergeHow: 'TypeAlias' = Literal[('left', 'right', 'inner', 'outer', 'cross', 'left_anti', 'right_anti')]
MergeValidate: 'TypeAlias' = Literal[('one_to_one', '1:1', 'one_to_many', '1:m', 'many_to_one', 'm:1', 'many_to_many', 'm:m')]
JoinHow: 'TypeAlias' = Literal[('left', 'right', 'inner', 'outer')]
JoinValidate: 'TypeAlias' = Literal[('one_to_one', '1:1', 'one_to_many', '1:m', 'many_to_one', 'm:1', 'many_to_many', 'm:m')]
ReindexMethod: 'TypeAlias' = FillnaOptions | Literal['nearest']
MatplotlibColor: 'TypeAlias' = str | Sequence[float]
TimeGrouperOrigin: 'TypeAlias' = Union[('Timestamp', Literal[('epoch', 'start', 'start_day', 'end', 'end_day')])]
TimeAmbiguous: 'TypeAlias' = Literal[('infer', 'NaT', 'raise')] | bool | npt.NDArray[np.bool_]
TimeNonexistent: 'TypeAlias' = Literal[('shift_forward', 'shift_backward', 'NaT', 'raise')] | timedelta
DropKeep: 'TypeAlias' = Literal[('first', 'last', False)]
CorrelationMethod: 'TypeAlias' = Literal[('pearson', 'kendall', 'spearman')] | Callable[([
    np.ndarray,
    np.ndarray], float)]
AlignJoin: 'TypeAlias' = Literal[('outer', 'inner', 'left', 'right')]
DtypeBackend: 'TypeAlias' = Literal[('pyarrow', 'numpy_nullable')]
TimeUnit: 'TypeAlias' = Literal[('s', 'ms', 'us', 'ns')]
OpenFileErrors: 'TypeAlias' = Literal[('strict', 'ignore', 'replace', 'surrogateescape', 'xmlcharrefreplace', 'backslashreplace', 'namereplace')]
UpdateJoin: 'TypeAlias' = Literal['left']
NaAction: 'TypeAlias' = Literal['ignore']
FromDictOrient: 'TypeAlias' = Literal[('columns', 'index', 'tight')]
ToStataByteorder: 'TypeAlias' = Literal[('>', '<', 'little', 'big')]
ExcelWriterIfSheetExists: 'TypeAlias' = Literal[('error', 'new', 'replace', 'overlay')]
ExcelWriterMergeCells: 'TypeAlias' = bool | Literal['columns']
OffsetCalendar: 'TypeAlias' = Union[(np.busdaycalendar, 'AbstractHolidayCalendar')]
UsecolsArgType: 'TypeAlias' = SequenceNotStr[Hashable] | range | AnyArrayLike | Callable[([
    HashableT], bool)] | None
SequenceT = TypeVar('SequenceT', bound = Sequence[Hashable])
SliceType: 'TypeAlias' = Hashable | None

class ArrowArrayExportable(Protocol):
    '''
    An object with an ``__arrow_c_array__`` method.

    This method indicates the object is an Arrow-compatible object implementing
    the `Arrow PyCapsule Protocol`_ (exposing the `Arrow C Data Interface`_ in
    Python), enabling zero-copy Arrow data interchange across libraries.

    .. _Arrow PyCapsule Protocol: https://arrow.apache.org/docs/format/CDataInterface/PyCapsuleInterface.html
    .. _Arrow C Data Interface: https://arrow.apache.org/docs/format/CDataInterface.html

    '''
    
    def __arrow_c_array__(self = None, requested_schema = None):
        pass



class ArrowStreamExportable(Protocol):
    '''
    An object with an ``__arrow_c_stream__`` method.

    This method indicates the object is an Arrow-compatible object implementing
    the `Arrow PyCapsule Protocol`_ (exposing the `Arrow C Data Interface`_
    for streams in Python), enabling zero-copy Arrow data interchange across
    libraries.

    .. _Arrow PyCapsule Protocol: https://arrow.apache.org/docs/format/CDataInterface/PyCapsuleInterface.html
    .. _Arrow C Stream Interface: https://arrow.apache.org/docs/format/CStreamInterface.html

    '''
    
    def __arrow_c_stream__(self = None, requested_schema = None):
        pass


__all__ = [
    'type_t']

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: column.pyc (Python 3.11)

from __future__ import annotations
from typing import TYPE_CHECKING, Any
import numpy as np
from pandas._config import using_python_scalars
from pandas._libs.lib import infer_dtype
from pandas._libs.tslibs import iNaT
from pandas.errors import NoBufferPresent
from pandas.util._decorators import cache_readonly
from pandas.core.dtypes.dtypes import BaseMaskedDtype
import pandas as pd
from pandas import ArrowDtype, DatetimeTZDtype
from pandas.api.types import is_string_dtype
from pandas.core.interchange.buffer import PandasBuffer, PandasBufferPyarrow
from pandas.core.interchange.dataframe_protocol import Column, ColumnBuffers, ColumnNullType, DtypeKind
from pandas.core.interchange.utils import ArrowCTypes, Endianness, dtype_to_arrow_c_fmt
if TYPE_CHECKING:
    from pandas.core.interchange.dataframe_protocol import Buffer
_NP_KINDS = {
    'i': DtypeKind.INT,
    'u': DtypeKind.UINT,
    'f': DtypeKind.FLOAT,
    'b': DtypeKind.BOOL,
    'U': DtypeKind.STRING,
    'M': DtypeKind.DATETIME,
    'm': DtypeKind.DATETIME }
_NULL_DESCRIPTION = {
    DtypeKind.STRING: (ColumnNullType.USE_BYTEMASK, 0),
    DtypeKind.CATEGORICAL: (ColumnNullType.USE_SENTINEL, -1),
    DtypeKind.BOOL: (ColumnNullType.NON_NULLABLE, None),
    DtypeKind.UINT: (ColumnNullType.NON_NULLABLE, None),
    DtypeKind.INT: (ColumnNullType.NON_NULLABLE, None),
    DtypeKind.DATETIME: (ColumnNullType.USE_SENTINEL, iNaT),
    DtypeKind.FLOAT: (ColumnNullType.USE_NAN, None) }
_NO_VALIDITY_BUFFER = {
    ColumnNullType.USE_SENTINEL: 'This column uses a sentinel value',
    ColumnNullType.USE_NAN: 'This column uses NaN as null',
    ColumnNullType.NON_NULLABLE: 'This column is non-nullable' }

class PandasColumn(Column):
    """
    A column object, with only the methods and properties required by the
    interchange protocol defined.
    A column can contain one or more chunks. Each chunk can contain up to three
    buffers - a data buffer, a mask buffer (depending on null representation),
    and an offsets buffer (if variable-size binary; e.g., variable-length
    strings).
    Note: this Column object can only be produced by ``__dataframe__``, so
          doesn't need its own version or ``__column__`` protocol.
    """
    
    def __init__(self = None, column = None, allow_copy = None):
        """
        Note: doesn't deal with extension arrays yet, just assume a regular
        Series/ndarray for now.
        """
        if isinstance(column, pd.DataFrame):
            raise TypeError(f'''Expected a Series, got a DataFrame. This likely happened because you called __dataframe__ on a DataFrame which, after converting column names to string, resulted in duplicated names: {column.columns}. Please rename these columns before using the interchange protocol.''')
        if not isinstance(column, pd.Series):
            raise NotImplementedError(f'''Columns of type {type(column)} not handled yet''')
        self._col = column
        self._allow_copy = allow_copy

    
    def size(self = None):
        '''
        Size of the column, in elements.
        '''
        return self._col.size

    offset = (lambda self = None: 0)()
    dtype = (lambda self = None: dtype = self._col.dtypeif isinstance(dtype, pd.CategoricalDtype):
codes = self._col.values.codes(_, bitwidth, c_arrow_dtype_f_str, _) = self._dtype_from_pandasdtype(codes.dtype)(DtypeKind.CATEGORICAL, bitwidth, c_arrow_dtype_f_str, Endianness.NATIVE)if None(dtype):
if infer_dtype(self._col) in ('string', 'empty'):
(DtypeKind.STRING, 8, dtype_to_arrow_c_fmt(dtype), Endianness.NATIVE)raise None('Non-string object dtypes are not supported yet')self._dtype_from_pandasdtype(dtype))()
    
    def _dtype_from_pandasdtype(self = None, dtype = None):
        '''
        See `self.dtype` for details.
        '''
        kind = _NP_KINDS.get(dtype.kind, None)
    # WARNING: Decompyle incomplete

    describe_categorical = (lambda self: if not self.dtype[0] == DtypeKind.CATEGORICAL:
raise TypeError('describe_categorical only works on a column with categorical dtype!'){
'is_ordered': self._col.cat.ordered,
'is_dictionary': True,
'categories': PandasColumn(pd.Series(self._col.cat.categories)) })()
    describe_null = (lambda self: if isinstance(self._col.dtype, BaseMaskedDtype):
column_null_dtype = ColumnNullType.USE_BYTEMASKnull_value = 1(column_null_dtype, null_value)# WARNING: Decompyle incomplete
)()
    null_count = (lambda self = property: result = self._col.isna().sum()if not using_python_scalars():
result = result.item()result)()
    metadata = (lambda self = None: {
'pandas.index': self._col.index })()
    
    def num_chunks(self = None):
        '''
        Return the number of chunks the column consists of.
        '''
        return 1

    
    def get_chunks(self = None, n_chunks = None):
        '''
        Return an iterator yielding the chunks.
        See `DataFrame.get_chunks` for details on ``n_chunks``.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def get_buffers(self = None):
        '''
        Return a dictionary containing the underlying buffers.
        The returned dictionary has the following contents:
            - "data": a two-element tuple whose first element is a buffer
                      containing the data and whose second element is the data
                      buffer\'s associated dtype.
            - "validity": a two-element tuple whose first element is a buffer
                          containing mask values indicating missing data and
                          whose second element is the mask value buffer\'s
                          associated dtype. None if the null representation is
                          not a bit or byte mask.
            - "offsets": a two-element tuple whose first element is a buffer
                         containing the offset values for variable-size binary
                         data (e.g., variable-length strings) and whose second
                         element is the offsets buffer\'s associated dtype. None
                         if the data buffer does not have an associated offsets
                         buffer.
        '''
        buffers = {
            'data': self._get_data_buffer(),
            'validity': None,
            'offsets': None }
        
        try:
            buffers['validity'] = self._get_validity_buffer()
        except NoBufferPresent:
            pass

        
        try:
            buffers['offsets'] = self._get_offsets_buffer()
        except NoBufferPresent:
            pass

        return buffers

    
    def _get_data_buffer(self = None):
        """
        Return the buffer containing the data and the buffer's associated dtype.
        """
        if self.dtype[0] == DtypeKind.DATETIME:
            if len(self.dtype[2]) > 4:
                np_arr = self._col.dt.tz_convert(None).to_numpy()
            else:
                np_arr = self._col.to_numpy()
            buffer = PandasBuffer(np_arr, allow_copy = self._allow_copy)
            dtype = (DtypeKind.INT, 64, ArrowCTypes.INT64, Endianness.NATIVE)
        elif self.dtype[0] in (DtypeKind.INT, DtypeKind.UINT, DtypeKind.FLOAT, DtypeKind.BOOL):
            dtype = self.dtype
            arr = self._col.array
            if isinstance(self._col.dtype, ArrowDtype):
                arr = arr._pa_array.chunks[0]
                buffer = PandasBufferPyarrow(arr.buffers()[1], length = len(arr))
                return (buffer, dtype)
            if None(self._col.dtype, BaseMaskedDtype):
                np_arr = arr._data
            else:
                np_arr = arr._ndarray
            buffer = PandasBuffer(np_arr, allow_copy = self._allow_copy)
        elif self.dtype[0] == DtypeKind.CATEGORICAL:
            codes = self._col.values._codes
            buffer = PandasBuffer(codes, allow_copy = self._allow_copy)
            dtype = self._dtype_from_pandasdtype(codes.dtype)
        elif self.dtype[0] == DtypeKind.STRING:
            buf = self._col.to_numpy()
            b = bytearray()
            for obj in buf:
                if isinstance(obj, str):
                    b.extend(obj.encode(encoding = 'utf-8'))
                buffer = PandasBuffer(np.frombuffer(b, dtype = 'uint8'))
                dtype = (DtypeKind.UINT, 8, ArrowCTypes.UINT8, Endianness.NATIVE)
        raise NotImplementedError(f'''Data type {self._col.dtype} not handled yet''')
        return (buffer, dtype)

    
    def _get_validity_buffer(self = None):
        """
        Return the buffer containing the mask values indicating missing data and
        the buffer's associated dtype.
        Raises NoBufferPresent if null representation is not a bit or byte mask.
        """
        (null, invalid) = self.describe_null
    # WARNING: Decompyle incomplete

    
    def _get_offsets_buffer(self = None):
        """
        Return the buffer containing the offset values for variable-size binary
        data (e.g., variable-length strings) and the buffer's associated dtype.
        Raises NoBufferPresent if the data buffer does not have an associated
        offsets buffer.
        """
        if self.dtype[0] == DtypeKind.STRING:
            values = self._col.to_numpy()
            ptr = 0
            offsets = np.zeros(shape = (len(values) + 1,), dtype = np.int64)
            for i, v in enumerate(values):
                if isinstance(v, str):
                    b = v.encode(encoding = 'utf-8')
                    ptr += len(b)
                offsets[i + 1] = ptr
                buffer = PandasBuffer(offsets)
                dtype = (DtypeKind.INT, 64, ArrowCTypes.INT64, Endianness.NATIVE)
        raise NoBufferPresent('This column has a fixed-length dtype so it does not have an offsets buffer')
        return (buffer, dtype)

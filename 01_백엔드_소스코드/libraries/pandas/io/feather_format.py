# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: feather_format.pyc (Python 3.11)

'''feather-format compat'''
from __future__ import annotations
from typing import TYPE_CHECKING, Any
import warnings
from pandas._config import using_string_dtype
from pandas._libs import lib
from pandas.compat._optional import import_optional_dependency
from pandas.errors import Pandas4Warning
from pandas.util._decorators import set_module
from pandas.util._validators import check_dtype_backend
from pandas.core.api import DataFrame
from pandas.io._util import arrow_table_to_pandas
from pandas.io.common import get_handle
if TYPE_CHECKING:
    from collections.abc import Hashable, Sequence
    from pandas._typing import DtypeBackend, FilePath, ReadBuffer, StorageOptions, WriteBuffer

def to_feather(df = None, path = None, storage_options = None, **kwargs):
    '''
    Write a DataFrame to the binary Feather format.

    Parameters
    ----------
    df : DataFrame
    path : str, path object, or file-like object
    storage_options : dict, optional
        Extra options that make sense for a particular storage connection, e.g.
        host, port, username, password, etc. For HTTP(S) URLs the key-value pairs
        are forwarded to ``urllib.request.Request`` as header options. For other
        URLs (e.g. starting with "s3://", and "gcs://") the key-value pairs are
        forwarded to ``fsspec.open``. Please see ``fsspec`` and ``urllib`` for more
        details, and for more examples on storage options refer `here
        <https://pandas.pydata.org/docs/user_guide/io.html?
        highlight=storage_options#reading-writing-remote-files>`_.
    **kwargs :
        Additional keywords passed to `pyarrow.feather.write_feather`.

    '''
    import_optional_dependency('pyarrow')
    feather = feather
    import pyarrow
    if not isinstance(df, DataFrame):
        raise ValueError('feather only support IO with DataFrames')
    handles = get_handle(path, 'wb', storage_options = storage_options, is_text = False)
# WARNING: Decompyle incomplete

read_feather = (lambda path = None, columns = None, use_threads = set_module('pandas'), storage_options = (None, True, None, lib.no_default), dtype_backend = ('path', 'FilePath | ReadBuffer[bytes]', 'columns', 'Sequence[Hashable] | None', 'use_threads', 'bool', 'storage_options', 'StorageOptions | None', 'dtype_backend', 'DtypeBackend | lib.NoDefault', 'return', 'DataFrame'): import_optional_dependency('pyarrow')feather = featherimport pyarrowimport pandas.core.arrays.arrow.extension_types as pandascheck_dtype_backend(dtype_backend)handles = get_handle(path, 'rb', storage_options = storage_options, is_text = False)if not dtype_backend is lib.no_default and using_string_dtype():
warnings.catch_warnings()warnings.filterwarnings('ignore', 'make_block is deprecated', Pandas4Warning)None(None, None)None(None, None)with None:
if not None:
passNone(None, None)with None:
if not feather.read_table(handles.handle, columns = columns, use_threads = bool(use_threads)), arrow_table_to_pandas(pa_table, dtype_backend = dtype_backend):
pass)()

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: parquet.pyc (Python 3.11)

'''parquet compat'''
from __future__ import annotations
import io
import json
import os
from typing import TYPE_CHECKING, Any, Literal
from warnings import catch_warnings, filterwarnings
from pandas._libs import lib
from pandas.compat._optional import import_optional_dependency
from pandas.errors import AbstractMethodError, Pandas4Warning
from pandas.util._decorators import set_module
from pandas.util._validators import check_dtype_backend
from pandas import DataFrame, get_option
from pandas.io._util import arrow_table_to_pandas
from pandas.io.common import IOHandles, get_handle, is_fsspec_url, is_url, stringify_path
if TYPE_CHECKING:
    from pandas._typing import DtypeBackend, FilePath, ParquetCompressionOptions, ReadBuffer, StorageOptions, WriteBuffer

def get_engine(engine = None):
    '''return our implementation'''
    if engine == 'auto':
        engine = get_option('io.parquet.engine')
    if engine == 'auto':
        engine_classes = [
            PyArrowImpl,
            FastParquetImpl]
        error_msgs = ''
        for engine_class in engine_classes:
            
            return None, engine_class()
            except ImportError:
                error_msgs += '\n - ' + str(err) = None
                err = None
                del err
                continue
                err = None
                del err
            raise ImportError(f'''Unable to find a usable engine; tried using: \'pyarrow\', \'fastparquet\'.\nA suitable version of pyarrow or fastparquet is required for parquet support.\nTrying to import the above resulted in these errors:{error_msgs}''')
            if engine == 'pyarrow':
                return PyArrowImpl()
            if None == 'fastparquet':
                return FastParquetImpl()
            raise None("engine must be one of 'pyarrow', 'fastparquet'")


def _get_path_or_handle(path = None, fs = None, storage_options = None, mode = (None, 'rb', False), is_dir = ('path', 'FilePath | ReadBuffer[bytes] | WriteBuffer[bytes]', 'fs', 'Any', 'storage_options', 'StorageOptions | None', 'mode', 'str', 'is_dir', 'bool', 'return', 'tuple[FilePath | ReadBuffer[bytes] | WriteBuffer[bytes], IOHandles[bytes] | None, Any]')):
    '''File handling for PyArrow.'''
    path_or_handle = stringify_path(path)
# WARNING: Decompyle incomplete


class BaseImpl:
    validate_dataframe = (lambda df = None: if not isinstance(df, DataFrame):
raise ValueError('to_parquet only supports IO with DataFrames'))()
    
    def write(self = None, df = None, path = None, compression = ('df', 'DataFrame', 'return', 'None'), **kwargs):
        raise AbstractMethodError(self)

    
    def read(self = None, path = None, columns = None, **kwargs):
        raise AbstractMethodError(self)



class PyArrowImpl(BaseImpl):
    
    def __init__(self = None):
        import_optional_dependency('pyarrow', extra = 'pyarrow is required for parquet support.')
        import pyarrow.parquet as pyarrow
        import pandas.core.arrays.arrow.extension_types as pandas
        self.api = pyarrow

    
    def write(self, df, path, compression = None, index = None, storage_options = None, partition_cols = ('snappy', None, None, None, None), filesystem = ('df', 'DataFrame', 'path', 'FilePath | WriteBuffer[bytes]', 'compression', 'ParquetCompressionOptions', 'index', 'bool | None', 'storage_options', 'StorageOptions | None', 'partition_cols', 'list[str] | None', 'return', 'None'), **kwargs):
        self.validate_dataframe(df)
        from_pandas_kwargs = {
            'schema': kwargs.pop('schema', None) }
    # WARNING: Decompyle incomplete

    
    def read(self, path, columns, filters = None, dtype_backend = None, storage_options = None, filesystem = (None, None, lib.no_default, None, None, None), to_pandas_kwargs = ('dtype_backend', 'DtypeBackend | lib.NoDefault', 'storage_options', 'StorageOptions | None', 'to_pandas_kwargs', 'dict[str, Any] | None', 'return', 'DataFrame'), **kwargs):
        kwargs['use_pandas_metadata'] = True
        (path_or_handle, handles, filesystem) = _get_path_or_handle(path, filesystem, storage_options = storage_options, mode = 'rb')
    # WARNING: Decompyle incomplete



class FastParquetImpl(BaseImpl):
    
    def __init__(self = None):
        fastparquet = import_optional_dependency('fastparquet', extra = 'fastparquet is required for parquet support.')
        self.api = fastparquet

    
    def write(self, df, path, compression = None, index = None, partition_cols = None, storage_options = ('snappy', None, None, None, None), filesystem = ('df', 'DataFrame', 'compression', "Literal['snappy', 'gzip', 'brotli'] | None", 'storage_options', 'StorageOptions | None', 'return', 'None'), **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def read(self, path, columns = None, filters = None, storage_options = None, filesystem = (None, None, None, None, None), to_pandas_kwargs = ('storage_options', 'StorageOptions | None', 'to_pandas_kwargs', 'dict | None', 'return', 'DataFrame'), **kwargs):
        parquet_kwargs = { }
        dtype_backend = kwargs.pop('dtype_backend', lib.no_default)
        parquet_kwargs['pandas_nulls'] = False
        if dtype_backend is not lib.no_default:
            raise ValueError("The 'dtype_backend' argument is not supported for the fastparquet engine")
    # WARNING: Decompyle incomplete



def to_parquet(df, path, engine, compression = None, index = None, storage_options = None, partition_cols = (None, 'auto', 'snappy', None, None, None, None), filesystem = ('df', 'DataFrame', 'path', 'FilePath | WriteBuffer[bytes] | None', 'engine', 'str', 'compression', 'ParquetCompressionOptions', 'index', 'bool | None', 'storage_options', 'StorageOptions | None', 'partition_cols', 'list[str] | None', 'filesystem', 'Any', 'return', 'bytes | None'), **kwargs):
    '''
    Write a DataFrame to the parquet format.

    Parameters
    ----------
    df : DataFrame
    path : str, path object, file-like object, or None, default None
        String, path object (implementing ``os.PathLike[str]``), or file-like
        object implementing a binary ``write()`` function. If None, the result
        is returned as bytes. If a string, it will be used as Root Directory
        path when writing a partitioned dataset. The engine fastparquet does
        not accept file-like objects.
    engine : {{\'auto\', \'pyarrow\', \'fastparquet\'}}, default \'auto\'
        Parquet library to use. If \'auto\', then the option
        ``io.parquet.engine`` is used. The default ``io.parquet.engine``
        behavior is to try \'pyarrow\', falling back to \'fastparquet\' if
        \'pyarrow\' is unavailable.

        When using the ``\'pyarrow\'`` engine and no storage options are provided
        and a filesystem is implemented by both ``pyarrow.fs`` and ``fsspec``
        (e.g. "s3://"), then the ``pyarrow.fs`` filesystem is attempted first.
        Use the filesystem keyword with an instantiated fsspec filesystem
        if you wish to use its implementation.
    compression : {{\'snappy\', \'gzip\', \'brotli\', \'lz4\', \'zstd\', None}},
        default \'snappy\'. Name of the compression to use. Use ``None``
        for no compression.
    index : bool, default None
        If ``True``, include the dataframe\'s index(es) in the file output. If
        ``False``, they will not be written to the file.
        If ``None``, similar to ``True`` the dataframe\'s index(es)
        will be saved. However, instead of being saved as values,
        the RangeIndex will be stored as a range in the metadata so it
        doesn\'t require much space and is faster. Other indexes will
        be included as columns in the file output.
    partition_cols : str or list, optional, default None
        Column names by which to partition the dataset.
        Columns are partitioned in the order they are given.
        Must be None if path is not a string.
    storage_options : dict, optional
        Extra options that make sense for a particular storage connection, e.g.
        host, port, username, password, etc. For HTTP(S) URLs the key-value
        pairs are forwarded to ``urllib.request.Request`` as header options.
        For other URLs (e.g. starting with "s3://", and "gcs://") the
        key-value pairs are forwarded to ``fsspec.open``. Please see ``fsspec``
        and ``urllib`` for more details, and for more examples on storage
        options refer `here <https://pandas.pydata.org/docs/user_guide/io.html?
        highlight=storage_options#reading-writing-remote-files>`_.
    filesystem : fsspec or pyarrow filesystem, default None
        Filesystem object to use when reading the parquet file. Only implemented
        for ``engine="pyarrow"``.

        .. versionadded:: 2.1.0

    **kwargs
        Additional keyword arguments passed to the engine:

        * For ``engine="pyarrow"``: passed to :func:`pyarrow.parquet.write_table`
          or :func:`pyarrow.parquet.write_to_dataset` (when using partition_cols)
        * For ``engine="fastparquet"``: passed to :func:`fastparquet.write`

    Returns
    -------
    bytes if no path argument is provided else None
    '''
    if isinstance(partition_cols, str):
        partition_cols = [
            partition_cols]
    impl = get_engine(engine)
# WARNING: Decompyle incomplete

read_parquet = (lambda path, engine, columns, storage_options = None, dtype_backend = None, filesystem = set_module('pandas'), filters = ('auto', None, None, lib.no_default, None, None, None), to_pandas_kwargs = ('path', 'FilePath | ReadBuffer[bytes]', 'engine', 'str', 'columns', 'list[str] | None', 'storage_options', 'StorageOptions | None', 'dtype_backend', 'DtypeBackend | lib.NoDefault', 'filesystem', 'Any', 'filters', 'list[tuple] | list[list[tuple]] | None', 'to_pandas_kwargs', 'dict | None', 'return', 'DataFrame'): impl = get_engine(engine)check_dtype_backend(dtype_backend)# WARNING: Decompyle incomplete
)()

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: parquet.pyc (Python 3.11)

import io
import json
import warnings
from typing import Literal
import fsspec
from core import url_to_fs
from spec import AbstractBufferedFile
from utils import merge_offset_ranges

class AlreadyBufferedFile(AbstractBufferedFile):
    
    def _fetch_range(self, start, end):
        raise NotImplementedError



def open_parquet_files(path, mode, fs, metadata, columns, row_groups, storage_options, engine = None, max_gap = None, max_block = None, footer_sample_size = ('rb', None, None, None, None, None, 'auto', 64000, 256000000, 1000000, None), filters = ('path', list[str], 'mode', Literal['rb'], 'fs', None | fsspec.AbstractFileSystem, 'columns', None | list[str], 'row_groups', None | list[int], 'storage_options', None | dict, 'engine', str, 'max_gap', int, 'max_block', int, 'footer_sample_size', int, 'filters', None | list[list[list[str]]]), **kwargs):
    '''
    Return a file-like object for a single Parquet file.

    The specified parquet `engine` will be used to parse the
    footer metadata, and determine the required byte ranges
    from the file. The target path will then be opened with
    the "parts" (`KnownPartsOfAFile`) caching strategy.

    Note that this method is intended for usage with remote
    file systems, and is unlikely to improve parquet-read
    performance on local file systems.

    Parameters
    ----------
    path: str
        Target file path.
    mode: str, optional
        Mode option to be passed through to `fs.open`. Default is "rb".
    metadata: Any, optional
        Parquet metadata object. Object type must be supported
        by the backend parquet engine. For now, only the "fastparquet"
        engine supports an explicit `ParquetFile` metadata object.
        If a metadata object is supplied, the remote footer metadata
        will not need to be transferred into local memory.
    fs: AbstractFileSystem, optional
        Filesystem object to use for opening the file. If nothing is
        specified, an `AbstractFileSystem` object will be inferred.
    engine : str, default "auto"
        Parquet engine to use for metadata parsing. Allowed options
        include "fastparquet", "pyarrow", and "auto". The specified
        engine must be installed in the current environment. If
        "auto" is specified, and both engines are installed,
        "fastparquet" will take precedence over "pyarrow".
    columns: list, optional
        List of all column names that may be read from the file.
    row_groups : list, optional
        List of all row-groups that may be read from the file. This
        may be a list of row-group indices (integers), or it may be
        a list of `RowGroup` metadata objects (if the "fastparquet"
        engine is used).
    storage_options : dict, optional
        Used to generate an `AbstractFileSystem` object if `fs` was
        not specified.
    max_gap : int, optional
        Neighboring byte ranges will only be merged when their
        inter-range gap is <= `max_gap`. Default is 64KB.
    max_block : int, optional
        Neighboring byte ranges will only be merged when the size of
        the aggregated range is <= `max_block`. Default is 256MB.
    footer_sample_size : int, optional
        Number of bytes to read from the end of the path to look
        for the footer metadata. If the sampled bytes do not contain
        the footer, a second read request will be required, and
        performance will suffer. Default is 1MB.
    filters : list[list], optional
        List of filters to apply to prevent reading row groups, of the
        same format as accepted by the loading engines. Ignored if
        ``row_groups`` is specified.
    **kwargs :
        Optional key-word arguments to pass to `fs.open`
    '''
    pass
# WARNING: Decompyle incomplete


def open_parquet_file(*args, **kwargs):
    '''Create files tailed to reading specific parts of parquet files

    Please see ``open_parquet_files`` for details of the arguments. The
    difference is, this function always returns a single ``AleadyBufferedFile``,
    whereas `open_parquet_files`` always returns a list of files, even if
    there are one or zero matching parquet files.
    '''
    pass
# WARNING: Decompyle incomplete


def _get_parquet_byte_ranges(paths, fs, metadata, columns, row_groups, max_gap, max_block, footer_sample_size, engine, filters = (None, None, None, 64000, 256000000, 1000000, 'auto', None)):
    '''Get a dictionary of the known byte ranges needed
    to read a specific column/row-group selection from a
    Parquet dataset. Each value in the output dictionary
    is intended for use as the `data` argument for the
    `KnownPartsOfAFile` caching strategy of a single path.
    '''
    if isinstance(engine, str):
        engine = _set_engine(engine)
# WARNING: Decompyle incomplete


def _get_parquet_byte_ranges_from_metadata(metadata, fs, engine, columns, row_groups, max_gap, max_block, filters = (None, None, 64000, 256000000, None)):
    '''Simplified version of `_get_parquet_byte_ranges` for
    the case that an engine-specific `metadata` object is
    provided, and the remote footer metadata does not need to
    be transferred before calculating the required byte ranges.
    '''
    (data_paths, data_starts, data_ends) = engine._parquet_byte_ranges(columns, row_groups = row_groups, metadata = metadata, filters = filters)
    (data_paths, data_starts, data_ends) = merge_offset_ranges(data_paths, data_starts, data_ends, max_gap = max_gap, max_block = max_block, sort = False)
    result = list(set(data_paths))()
    _transfer_ranges(fs, result, data_paths, data_starts, data_ends)
    _add_header_magic(result)
    return result


def _transfer_ranges(fs, blocks, paths, starts, ends):
    ranges = (paths, starts, ends)
# WARNING: Decompyle incomplete


def _add_header_magic(data):
    for path in list(data.keys()):
        add_magic = True
        for k in data[path]:
            if k[0] == 0 and k[1] >= 4:
                add_magic = False
            
            if add_magic:
                data[path][(0, 4)] = b'PAR1'
        return None


def _set_engine(engine_str):
    if engine_str == 'auto':
        try_engines = ('fastparquet', 'pyarrow')
    elif not isinstance(engine_str, str):
        raise ValueError("Failed to set parquet engine! Please pass 'fastparquet', 'pyarrow', or 'auto'")
    if engine_str not in ('fastparquet', 'pyarrow'):
        raise ValueError(f'''{engine_str} engine not supported by `fsspec.parquet`''')
    try_engines = [
        engine_str]
    for engine in try_engines:
        if engine == 'fastparquet':
            
            return None, FastparquetEngine()
        if None == 'pyarrow':
            
            return None, PyarrowEngine()
        except ImportError:
            continue
        raise ImportError(f'''The following parquet engines are not installed in your python environment: {try_engines}.Please install \'fastparquert\' or \'pyarrow\' to utilize the `fsspec.parquet` module.''')


class FastparquetEngine:
    
    def __init__(self):
        import fastparquet as fp
        self.fp = fp

    
    def _row_group_filename(self, row_group, pf):
        return pf.row_group_filename(row_group)

    
    def _parquet_byte_ranges(self, columns, row_groups, metadata, footer, footer_start, filters = (None, None, None, None, None)):
        pf = metadata
        data_ends = []
        data_starts = []
        data_paths = []
        if filters and row_groups:
            raise ValueError('filters and row_groups cannot be used together')
    # WARNING: Decompyle incomplete



class PyarrowEngine:
    
    def __init__(self):
        pq = parquet
        import pyarrow.parquet
        self.pq = pq

    
    def _row_group_filename(self, row_group, metadata):
        raise NotImplementedError

    
    def _parquet_byte_ranges(self, columns, row_groups, metadata, footer, footer_start, filters = (None, None, None, None, None)):
        pass
    # WARNING: Decompyle incomplete

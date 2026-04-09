# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: info.pyc (Python 3.11)

from __future__ import annotations
from abc import ABC, abstractmethod
import sys
from textwrap import dedent
from typing import TYPE_CHECKING
from pandas._config import get_option
from pandas.io.formats import format as fmt
from pandas.io.formats.printing import pprint_thing
if TYPE_CHECKING:
    from collections.abc import Iterable, Iterator, Mapping, Sequence
    from pandas._typing import Dtype, WriteBuffer
    from pandas import DataFrame, Index, Series
show_counts_sub = dedent('    show_counts : bool, optional\n        Whether to show the non-null counts. By default, this is shown\n        only if the DataFrame is smaller than\n        ``pandas.options.display.max_info_rows`` and\n        ``pandas.options.display.max_info_columns``. A value of True always\n        shows the counts, and False never shows the counts.')
series_examples_sub = dedent('    >>> int_values = [1, 2, 3, 4, 5]\n    >>> text_values = [\'alpha\', \'beta\', \'gamma\', \'delta\', \'epsilon\']\n    >>> s = pd.Series(text_values, index=int_values)\n    >>> s.info()\n    <class \'pandas.Series\'>\n    Index: 5 entries, 1 to 5\n    Series name: None\n    Non-Null Count  Dtype\n    --------------  -----\n    5 non-null      object\n    dtypes: object(1)\n    memory usage: 80.0+ bytes\n\n    Prints a summary excluding information about its values:\n\n    >>> s.info(verbose=False)\n    <class \'pandas.Series\'>\n    Index: 5 entries, 1 to 5\n    dtypes: object(1)\n    memory usage: 80.0+ bytes\n\n    Pipe output of Series.info to buffer instead of sys.stdout, get\n    buffer content and writes to a text file:\n\n    >>> import io\n    >>> buffer = io.StringIO()\n    >>> s.info(buf=buffer)\n    >>> s = buffer.getvalue()\n    >>> with open("df_info.txt", "w",\n    ...           encoding="utf-8") as f:  # doctest: +SKIP\n    ...     f.write(s)\n    260\n\n    The `memory_usage` parameter allows deep introspection mode, specially\n    useful for big Series and fine-tune memory optimization:\n\n    >>> random_strings_array = np.random.choice([\'a\', \'b\', \'c\'], 10 ** 6)\n    >>> s = pd.Series(np.random.choice([\'a\', \'b\', \'c\'], 10 ** 6))\n    >>> s.info()\n    <class \'pandas.Series\'>\n    RangeIndex: 1000000 entries, 0 to 999999\n    Series name: None\n    Non-Null Count    Dtype\n    --------------    -----\n    1000000 non-null  object\n    dtypes: object(1)\n    memory usage: 7.6+ MB\n\n    >>> s.info(memory_usage=\'deep\')\n    <class \'pandas.Series\'>\n    RangeIndex: 1000000 entries, 0 to 999999\n    Series name: None\n    Non-Null Count    Dtype\n    --------------    -----\n    1000000 non-null  object\n    dtypes: object(1)\n    memory usage: 55.3 MB')
series_see_also_sub = dedent('    Series.describe: Generate descriptive statistics of Series.\n    Series.memory_usage: Memory usage of Series.')
series_max_cols_sub = dedent('    max_cols : int, optional\n        Unused, exists only for compatibility with DataFrame.info.')
series_sub_kwargs = {
    'klass': 'Series',
    'type_sub': '',
    'max_cols_sub': series_max_cols_sub,
    'show_counts_sub': show_counts_sub,
    'examples_sub': series_examples_sub,
    'see_also_sub': series_see_also_sub,
    'version_added_sub': '\n.. versionadded:: 1.4.0\n' }

def _put_str(s = None, space = None):
    '''
    Make string of specified length, padding to the right if necessary.

    Parameters
    ----------
    s : Union[str, Dtype]
        String to be formatted.
    space : int
        Length to force string to be of.

    Returns
    -------
    str
        String coerced to given length.

    Examples
    --------
    >>> pd.io.formats.info._put_str("panda", 6)
    \'panda \'
    >>> pd.io.formats.info._put_str("panda", 4)
    \'pand\'
    '''
    return str(s)[:space].ljust(space)


def _sizeof_fmt(num = None, size_qualifier = None):
    '''
    Return size in human readable format.

    Parameters
    ----------
    num : int
        Size in bytes.
    size_qualifier : str
        Either empty, or \'+\' (if lower bound).

    Returns
    -------
    str
        Size in human readable format.

    Examples
    --------
    >>> _sizeof_fmt(23028, "")
    \'22.5 KB\'

    >>> _sizeof_fmt(23028, "+")
    \'22.5+ KB\'
    '''
    for x in ('bytes', 'KB', 'MB', 'GB', 'TB'):
        if num < 1024:
            
            return None, f'''{num:3.1f}{size_qualifier} {x}'''
        return f'''{num:3.1f}{size_qualifier} PB'''


def _initialize_memory_usage(memory_usage = None):
    '''Get memory usage based on inputs and display options.'''
    pass
# WARNING: Decompyle incomplete


class _BaseInfo(ABC):
    memory_usage: 'bool | str' = '\n    Base class for DataFrameInfo and SeriesInfo.\n\n    Parameters\n    ----------\n    data : DataFrame or Series\n        Either dataframe or series.\n    memory_usage : bool or str, optional\n        If "deep", introspect the data deeply by interrogating object dtypes\n        for system-level memory consumption, and include it in the returned\n        values.\n    '
    dtypes = (lambda self = None: pass)()()
    dtype_counts = (lambda self = None: pass)()()
    non_null_counts = (lambda self = None: pass)()()
    memory_usage_bytes = (lambda self = None: pass)()()
    memory_usage_string = (lambda self = None: f'''{_sizeof_fmt(self.memory_usage_bytes, self.size_qualifier)}\n''')()
    size_qualifier = (lambda self = None: size_qualifier = ''if self.memory_usage and self.memory_usage != 'deep':
if 'object' in self.dtype_counts or self.data.index._is_memory_usage_qualified:
size_qualifier = '+'size_qualifier)()
    render = (lambda self = None, *, buf: pass)()


class DataFrameInfo(_BaseInfo):
    '''
    Class storing dataframe-specific info.
    '''
    
    def __init__(self = None, data = None, memory_usage = None):
        self.data = data
        self.memory_usage = _initialize_memory_usage(memory_usage)

    dtype_counts = (lambda self = None: _get_dataframe_dtype_counts(self.data))()
    dtypes = (lambda self = None: self.data.dtypes)()
    ids = (lambda self = None: self.data.columns)()
    col_count = (lambda self = None: len(self.ids))()
    non_null_counts = (lambda self = None: self.data.count())()
    memory_usage_bytes = (lambda self = None: deep = self.memory_usage == 'deep'self.data.memory_usage(index = True, deep = deep).sum())()
    
    def render(self = None, *, buf, max_cols, verbose, show_counts):
        printer = _DataFrameInfoPrinter(info = self, max_cols = max_cols, verbose = verbose, show_counts = show_counts)
        printer.to_buffer(buf)



class SeriesInfo(_BaseInfo):
    '''
    Class storing series-specific info.
    '''
    
    def __init__(self = None, data = None, memory_usage = None):
        self.data = data
        self.memory_usage = _initialize_memory_usage(memory_usage)

    
    def render(self = None, *, buf, max_cols, verbose, show_counts):
        pass
    # WARNING: Decompyle incomplete

    non_null_counts = (lambda self = None: [
self.data.count()])()
    dtypes = (lambda self = None: [
self.data.dtypes])()
    dtype_counts = (lambda self = None: DataFrame = DataFrameimport pandas.core.frame_get_dataframe_dtype_counts(DataFrame(self.data)))()
    memory_usage_bytes = (lambda self = None: deep = self.memory_usage == 'deep'self.data.memory_usage(index = True, deep = deep))()


class _InfoPrinterAbstract:
    '''
    Class for printing dataframe or series info.
    '''
    
    def to_buffer(self = None, buf = None):
        '''Save dataframe info into buffer.'''
        table_builder = self._create_table_builder()
        lines = table_builder.get_lines()
    # WARNING: Decompyle incomplete

    _create_table_builder = (lambda self = None: pass)()


class _DataFrameInfoPrinter(_InfoPrinterAbstract):
    '''
    Class for printing dataframe info.

    Parameters
    ----------
    info : DataFrameInfo
        Instance of DataFrameInfo.
    max_cols : int, optional
        When to switch from the verbose to the truncated output.
    verbose : bool, optional
        Whether to print the full summary.
    show_counts : bool, optional
        Whether to show the non-null counts.
    '''
    
    def __init__(self = None, info = None, max_cols = None, verbose = (None, None, None), show_counts = ('info', 'DataFrameInfo', 'max_cols', 'int | None', 'verbose', 'bool | None', 'show_counts', 'bool | None', 'return', 'None')):
        self.info = info
        self.data = info.data
        self.verbose = verbose
        self.max_cols = self._initialize_max_cols(max_cols)
        self.show_counts = self._initialize_show_counts(show_counts)

    max_rows = (lambda self = None: get_option('display.max_info_rows'))()
    exceeds_info_cols = (lambda self = None: bool(self.col_count > self.max_cols))()
    exceeds_info_rows = (lambda self = None: bool(len(self.data) > self.max_rows))()
    col_count = (lambda self = None: self.info.col_count)()
    
    def _initialize_max_cols(self = None, max_cols = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _initialize_show_counts(self = None, show_counts = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _create_table_builder(self = None):
        '''
        Create instance of table builder based on verbosity and display settings.
        '''
        if self.verbose:
            return _DataFrameTableBuilderVerbose(info = self.info, with_counts = self.show_counts)
        if None.verbose is False:
            return _DataFrameTableBuilderNonVerbose(info = self.info)
        if None.exceeds_info_cols:
            return _DataFrameTableBuilderNonVerbose(info = self.info)
        return None(info = self.info, with_counts = self.show_counts)



class _SeriesInfoPrinter(_InfoPrinterAbstract):
    '''Class for printing series info.

    Parameters
    ----------
    info : SeriesInfo
        Instance of SeriesInfo.
    verbose : bool, optional
        Whether to print the full summary.
    show_counts : bool, optional
        Whether to show the non-null counts.
    '''
    
    def __init__(self = None, info = None, verbose = None, show_counts = (None, None)):
        self.info = info
        self.data = info.data
        self.verbose = verbose
        self.show_counts = self._initialize_show_counts(show_counts)

    
    def _create_table_builder(self = None):
        '''
        Create instance of table builder based on verbosity.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _initialize_show_counts(self = None, show_counts = None):
        pass
    # WARNING: Decompyle incomplete



class _TableBuilderAbstract(ABC):
    info: '_BaseInfo' = '\n    Abstract builder for info table.\n    '
    get_lines = (lambda self = None: pass)()
    data = (lambda self = None: self.info.data)()
    dtypes = (lambda self = None: self.info.dtypes)()
    dtype_counts = (lambda self = None: self.info.dtype_counts)()
    display_memory_usage = (lambda self = None: bool(self.info.memory_usage))()
    memory_usage_string = (lambda self = None: self.info.memory_usage_string)()
    non_null_counts = (lambda self = None: self.info.non_null_counts)()
    
    def add_object_type_line(self = None):
        '''Add line with string representation of dataframe to the table.'''
        self._lines.append(str(type(self.data)))

    
    def add_index_range_line(self = None):
        '''Add line with range of indices to the table.'''
        self._lines.append(self.data.index._summary())

    
    def add_dtypes_line(self = None):
        '''Add summary line with dtypes present in dataframe.'''
        collected_dtypes = sorted(self.dtype_counts.items())()
        self._lines.append(f'''dtypes: {', '.join(collected_dtypes)}''')



class _DataFrameTableBuilder(_TableBuilderAbstract):
    '''
    Abstract builder for dataframe info table.

    Parameters
    ----------
    info : DataFrameInfo.
        Instance of DataFrameInfo.
    '''
    
    def __init__(self = None, *, info):
        self.info = info

    
    def get_lines(self = None):
        self._lines = []
        if self.col_count == 0:
            self._fill_empty_info()
        else:
            self._fill_non_empty_info()
        return self._lines

    
    def _fill_empty_info(self = None):
        '''Add lines to the info table, pertaining to empty dataframe.'''
        self.add_object_type_line()
        self.add_index_range_line()
        self._lines.append(f'''Empty {type(self.data).__name__}\n''')

    _fill_non_empty_info = (lambda self = None: pass)()
    data = (lambda self = None: self.info.data)()
    ids = (lambda self = None: self.info.ids)()
    col_count = (lambda self = None: self.info.col_count)()
    
    def add_memory_usage_line(self = None):
        '''Add line containing memory usage.'''
        self._lines.append(f'''memory usage: {self.memory_usage_string}''')



class _DataFrameTableBuilderNonVerbose(_DataFrameTableBuilder):
    '''
    Dataframe info table builder for non-verbose output.
    '''
    
    def _fill_non_empty_info(self = None):
        '''Add lines to the info table, pertaining to non-empty dataframe.'''
        self.add_object_type_line()
        self.add_index_range_line()
        self.add_columns_summary_line()
        self.add_dtypes_line()
        if self.display_memory_usage:
            self.add_memory_usage_line()
            return None

    
    def add_columns_summary_line(self = None):
        self._lines.append(self.ids._summary(name = 'Columns'))



class _TableBuilderVerboseMixin(_TableBuilderAbstract):
    '''
    Mixin for verbose info output.
    '''
    with_counts: 'bool' = '  '
    headers = (lambda self = None: pass)()()
    header_column_widths = (lambda self = None: self.headers())()
    
    def _get_gross_column_widths(self = None):
        '''Get widths of columns containing both headers and actual content.'''
        body_column_widths = self._get_body_column_widths()
        return zip(self.header_column_widths, body_column_widths, strict = False)()

    
    def _get_body_column_widths(self = None):
        '''Get widths of table content columns.'''
        pass
    # WARNING: Decompyle incomplete

    
    def _gen_rows(self = None):
        '''
        Generator function yielding rows content.

        Each element represents a row comprising a sequence of strings.
        '''
        if self.with_counts:
            return self._gen_rows_with_counts()
        return None._gen_rows_without_counts()

    _gen_rows_with_counts = (lambda self = None: pass)()
    _gen_rows_without_counts = (lambda self = None: pass)()
    
    def add_header_line(self = None):
        header_line = (lambda .0: [ _put_str(header, col_width) for header, col_width in .0 ])(zip(self.headers, self.gross_column_widths, strict = True)())
        self._lines.append(header_line)

    
    def add_separator_line(self = None):
        separator_line = (lambda .0: [ _put_str('-' * header_colwidth, gross_colwidth) for header_colwidth, gross_colwidth in .0 ])(zip(self.header_column_widths, self.gross_column_widths, strict = True)())
        self._lines.append(separator_line)

    
    def add_body_lines(self = None):
        for row in self.strrows:
            body_line = (lambda .0: [ _put_str(col, gross_colwidth) for col, gross_colwidth in .0 ])(zip(row, self.gross_column_widths, strict = True)())
            self._lines.append(body_line)
            return None

    
    def _gen_non_null_counts(self = None):
        '''Iterator with string representation of non-null counts.'''
        pass
    # WARNING: Decompyle incomplete

    
    def _gen_dtypes(self = None):
        '''Iterator with string representation of column dtypes.'''
        pass
    # WARNING: Decompyle incomplete



class _DataFrameTableBuilderVerbose(_TableBuilderVerboseMixin, _DataFrameTableBuilder):
    '''
    Dataframe info table builder for verbose output.
    '''
    
    def __init__(self = None, *, info, with_counts):
        self.info = info
        self.with_counts = with_counts
        self.strrows = list(self._gen_rows())
        self.gross_column_widths = self._get_gross_column_widths()

    
    def _fill_non_empty_info(self = None):
        '''Add lines to the info table, pertaining to non-empty dataframe.'''
        self.add_object_type_line()
        self.add_index_range_line()
        self.add_columns_summary_line()
        self.add_header_line()
        self.add_separator_line()
        self.add_body_lines()
        self.add_dtypes_line()
        if self.display_memory_usage:
            self.add_memory_usage_line()
            return None

    headers = (lambda self = None:

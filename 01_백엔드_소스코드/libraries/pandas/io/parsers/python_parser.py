# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: python_parser.pyc (Python 3.11)

from __future__ import annotations
from collections import abc, defaultdict
import csv
from io import StringIO
import re
from typing import IO, TYPE_CHECKING, Any, DefaultDict, Literal, cast, final
import warnings
import numpy as np
from pandas._libs import lib
from pandas._typing import Scalar
from pandas.errors import EmptyDataError, ParserError, ParserWarning
from pandas.util._decorators import cache_readonly
from pandas.util._exceptions import find_stack_level
from pandas.core.dtypes.astype import astype_array
from pandas.core.dtypes.common import is_bool_dtype, is_extension_array_dtype, is_integer, is_numeric_dtype, is_object_dtype, is_string_dtype, pandas_dtype
from pandas.core.dtypes.dtypes import CategoricalDtype, ExtensionDtype
from pandas.core.dtypes.inference import is_dict_like
from pandas.core import algorithms
from pandas.core.arrays import Categorical, ExtensionArray
from pandas.core.arrays.boolean import BooleanDtype
from pandas.core.indexes.api import Index
from pandas.io.common import dedup_names, is_potential_multi_index
from pandas.io.parsers.base_parser import ParserBase, evaluate_callable_usecols, get_na_values, parser_defaults, validate_parse_dates_presence
if TYPE_CHECKING:
    from collections.abc import Hashable, Iterator, Mapping, Sequence
    from pandas._typing import ArrayLike, DtypeObj, ReadCsvBuffer, T
    from pandas import MultiIndex, Series
_BOM = '﻿'

class PythonParser(ParserBase):
    pass
# WARNING: Decompyle incomplete


class FixedWidthReader(abc.Iterator):
    '''
    A reader of fixed-width lines.
    '''
    
    def __init__(self, f, colspecs = None, delimiter = None, comment = None, skiprows = (None, 100), infer_nrows = ('f', 'IO[str] | ReadCsvBuffer[str]', 'colspecs', "list[tuple[int, int]] | Literal['infer']", 'delimiter', 'str | None', 'comment', 'str | None', 'skiprows', 'set[int] | None', 'infer_nrows', 'int', 'return', 'None')):
        self.f = f
        self.buffer = None
        self.delimiter = '\r\n' + delimiter if delimiter else '\n\r\t '
        self.comment = comment
        if colspecs == 'infer':
            self.colspecs = self.detect_colspecs(infer_nrows = infer_nrows, skiprows = skiprows)
        else:
            self.colspecs = colspecs
        if not isinstance(self.colspecs, (tuple, list)):
            raise TypeError(f'''column specifications must be a list or tuple, input was a {type(colspecs).__name__}''')
        for colspec in self.colspecs:
            if not isinstance(colspec, (tuple, list)) and len(colspec) == 2 and isinstance(colspec[0], (int, np.integer, type(None))) or isinstance(colspec[1], (int, np.integer, type(None))):
                raise TypeError('Each column specification must be 2 element tuple or list of integers')
            return None

    
    def get_rows(self = None, infer_nrows = None, skiprows = None):
        """
        Read rows from self.f, skipping as specified.

        We distinguish buffer_rows (the first <= infer_nrows
        lines) from the rows returned to detect_colspecs
        because it's simpler to leave the other locations
        with skiprows logic alone than to modify them to
        deal with the fact we skipped some rows here as
        well.

        Parameters
        ----------
        infer_nrows : int
            Number of rows to read from self.f, not counting
            rows that are skipped.
        skiprows: set, optional
            Indices of rows to skip.

        Returns
        -------
        detect_rows : list of str
            A list containing the rows to read.

        """
        pass
    # WARNING: Decompyle incomplete

    
    def detect_colspecs(self = None, infer_nrows = None, skiprows = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __next__(self = None):
        pass
    # WARNING: Decompyle incomplete



class FixedWidthFieldParser(PythonParser):
    '''
    Specialization that Converts fixed-width fields into DataFrames.
    See PythonParser for details.
    '''
    
    def __init__(self = None, f = None, **kwds):
        self.colspecs = kwds.pop('colspecs')
        self.infer_nrows = kwds.pop('infer_nrows')
    # WARNING: Decompyle incomplete

    
    def _make_reader(self = None, f = None):
        return FixedWidthReader(f, self.colspecs, self.delimiter, self.comment, self.skiprows, self.infer_nrows)

    
    def _remove_empty_lines(self = None, lines = None):
        '''
        Returns the list of lines without the empty ones. With fixed-width
        fields, empty lines become arrays of empty strings.

        See PythonParser._remove_empty_lines.
        '''
        return lines()



def _validate_skipfooter_arg(skipfooter = None):
    """
    Validate the 'skipfooter' parameter.

    Checks whether 'skipfooter' is a non-negative integer.
    Raises a ValueError if that is not the case.

    Parameters
    ----------
    skipfooter : non-negative integer
        The number of rows to skip at the end of the file.

    Returns
    -------
    validated_skipfooter : non-negative integer
        The original input if the validation succeeds.

    Raises
    ------
    ValueError : 'skipfooter' was not a non-negative integer.
    """
    if not is_integer(skipfooter):
        raise ValueError('skipfooter must be an integer')
    if skipfooter < 0:
        raise ValueError('skipfooter cannot be negative')
    return skipfooter

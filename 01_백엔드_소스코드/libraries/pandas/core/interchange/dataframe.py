# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: dataframe.pyc (Python 3.11)

from __future__ import annotations
from collections import abc
from typing import TYPE_CHECKING
from pandas.core.interchange.column import PandasColumn
from pandas.core.interchange.dataframe_protocol import DataFrame as DataFrameXchg
from pandas.core.interchange.utils import maybe_rechunk
if TYPE_CHECKING:
    from collections.abc import Iterable, Sequence
    from pandas import DataFrame, Index

class PandasDataFrameXchg(DataFrameXchg):
    '''
    A data frame class, with only the methods required by the interchange
    protocol defined.
    Instances of this (private) class are returned from
    ``pd.DataFrame.__dataframe__`` as objects with the methods and
    attributes defined on this class.
    '''
    
    def __init__(self = None, df = None, allow_copy = None):
        '''
        Constructor - an instance of this (private) class is returned from
        `pd.DataFrame.__dataframe__`.
        '''
        self._df = df.rename(columns = str)
        self._allow_copy = allow_copy
    # WARNING: Decompyle incomplete

    
    def __dataframe__(self = None, nan_as_null = None, allow_copy = None):
        return PandasDataFrameXchg(self._df, allow_copy)

    metadata = (lambda self = None: {
'pandas.index': self._df.index })()
    
    def num_columns(self = None):
        return len(self._df.columns)

    
    def num_rows(self = None):
        return len(self._df)

    
    def num_chunks(self = None):
        return 1

    
    def column_names(self = None):
        return self._df.columns

    
    def get_column(self = None, i = None):
        return PandasColumn(self._df.iloc[(:, i)], allow_copy = self._allow_copy)

    
    def get_column_by_name(self = None, name = None):
        return PandasColumn(self._df[name], allow_copy = self._allow_copy)

    
    def get_columns(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def select_columns(self = None, indices = None):
        if not isinstance(indices, abc.Sequence):
            raise ValueError('`indices` is not a sequence')
        if not isinstance(indices, list):
            indices = list(indices)
        return PandasDataFrameXchg(self._df.iloc[(:, indices)], allow_copy = self._allow_copy)

    
    def select_columns_by_name(self = None, names = None):
        if not isinstance(names, abc.Sequence):
            raise ValueError('`names` is not a sequence')
        if not isinstance(names, list):
            names = list(names)
        return PandasDataFrameXchg(self._df.loc[(:, names)], allow_copy = self._allow_copy)

    
    def get_chunks(self = None, n_chunks = None):
        '''
        Return an iterator yielding the chunks.
        '''
        pass
    # WARNING: Decompyle incomplete

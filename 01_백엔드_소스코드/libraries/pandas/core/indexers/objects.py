# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: objects.pyc (Python 3.11)

'''Indexer objects for computing start/end window bounds for rolling operations'''
from __future__ import annotations
from datetime import timedelta
import numpy as np
from pandas._libs.tslibs import BaseOffset
from pandas._libs.window.indexers import calculate_variable_window_bounds
from pandas.util._decorators import set_module
from pandas.core.dtypes.common import ensure_platform_int
from pandas.core.indexes.datetimes import DatetimeIndex
from pandas.tseries.offsets import Nano
BaseIndexer = <NODE:12>()

class FixedWindowIndexer(BaseIndexer):
    '''Creates window boundaries that are of fixed length.'''
    
    def get_window_bounds(self, num_values = None, min_periods = None, center = None, closed = (0, None, None, None, None), step = ('num_values', 'int', 'min_periods', 'int | None', 'center', 'bool | None', 'closed', 'str | None', 'step', 'int | None', 'return', 'tuple[np.ndarray, np.ndarray]')):
        '''
        Computes the bounds of a window.

        Parameters
        ----------
        num_values : int, default 0
            number of values that will be aggregated over
        window_size : int, default 0
            the number of rows in a window
        min_periods : int, default None
            min_periods passed from the top level rolling API
        center : bool, default None
            center passed from the top level rolling API
        closed : str, default None
            closed passed from the top level rolling API
        step : int, default None
            step passed from the top level rolling API
        win_type : str, default None
            win_type passed from the top level rolling API

        Returns
        -------
        A tuple of ndarray[int64]s, indicating the boundaries of each
        window
        '''
        if center or self.window_size == 0:
            offset = (self.window_size - 1) // 2
        else:
            offset = 0
        end = np.arange(1 + offset, num_values + 1 + offset, step, dtype = 'int64')
        start = end - self.window_size
        if closed in ('left', 'both'):
            start -= 1
        if closed in ('left', 'neither'):
            end -= 1
        end = np.clip(end, 0, num_values)
        start = np.clip(start, 0, num_values)
        return (start, end)



class VariableWindowIndexer(BaseIndexer):
    '''Creates window boundaries that are of variable length, namely for time series.'''
    
    def get_window_bounds(self, num_values = None, min_periods = None, center = None, closed = (0, None, None, None, None), step = ('num_values', 'int', 'min_periods', 'int | None', 'center', 'bool | None', 'closed', 'str | None', 'step', 'int | None', 'return', 'tuple[np.ndarray, np.ndarray]')):
        '''
        Computes the bounds of a window.

        Parameters
        ----------
        num_values : int, default 0
            number of values that will be aggregated over
        window_size : int, default 0
            the number of rows in a window
        min_periods : int, default None
            min_periods passed from the top level rolling API
        center : bool, default None
            center passed from the top level rolling API
        closed : str, default None
            closed passed from the top level rolling API
        step : int, default None
            step passed from the top level rolling API
        win_type : str, default None
            win_type passed from the top level rolling API

        Returns
        -------
        A tuple of ndarray[int64]s, indicating the boundaries of each
        window
        '''
        return calculate_variable_window_bounds(num_values, self.window_size, min_periods, center, closed, self.index_array)


VariableOffsetWindowIndexer = <NODE:12>()

class ExpandingIndexer(BaseIndexer):
    '''Calculate expanding window bounds, mimicking df.expanding()'''
    
    def get_window_bounds(self, num_values = None, min_periods = None, center = None, closed = (0, None, None, None, None), step = ('num_values', 'int', 'min_periods', 'int | None', 'center', 'bool | None', 'closed', 'str | None', 'step', 'int | None', 'return', 'tuple[np.ndarray, np.ndarray]')):
        '''
        Computes the bounds of a window.

        Parameters
        ----------
        num_values : int, default 0
            number of values that will be aggregated over
        window_size : int, default 0
            the number of rows in a window
        min_periods : int, default None
            min_periods passed from the top level rolling API
        center : bool, default None
            center passed from the top level rolling API
        closed : str, default None
            closed passed from the top level rolling API
        step : int, default None
            step passed from the top level rolling API
        win_type : str, default None
            win_type passed from the top level rolling API

        Returns
        -------
        A tuple of ndarray[int64]s, indicating the boundaries of each
        window
        '''
        return (np.zeros(num_values, dtype = np.int64), np.arange(1, num_values + 1, dtype = np.int64))


FixedForwardWindowIndexer = <NODE:12>()

class GroupbyIndexer(BaseIndexer):
    pass
# WARNING: Decompyle incomplete


class ExponentialMovingWindowIndexer(BaseIndexer):
    '''Calculate ewm window bounds (the entire window)'''
    
    def get_window_bounds(self, num_values = None, min_periods = None, center = None, closed = (0, None, None, None, None), step = ('num_values', 'int', 'min_periods', 'int | None', 'center', 'bool | None', 'closed', 'str | None', 'step', 'int | None', 'return', 'tuple[np.ndarray, np.ndarray]')):
        '''
        Computes the bounds of a window.

        Parameters
        ----------
        num_values : int, default 0
            number of values that will be aggregated over
        window_size : int, default 0
            the number of rows in a window
        min_periods : int, default None
            min_periods passed from the top level rolling API
        center : bool, default None
            center passed from the top level rolling API
        closed : str, default None
            closed passed from the top level rolling API
        step : int, default None
            step passed from the top level rolling API
        win_type : str, default None
            win_type passed from the top level rolling API

        Returns
        -------
        A tuple of ndarray[int64]s, indicating the boundaries of each
        window
        '''
        return (np.array([
            0], dtype = np.int64), np.array([
            num_values], dtype = np.int64))

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: llvm_pass_timings.pyc (Python 3.11)

import re
import operator
import heapq
from collections import namedtuple
from collections.abc import Sequence
from contextlib import contextmanager
from functools import cached_property
from numba.core import config
from llvmlite.binding import binding as llvm

class RecordLLVMPassTimingsLegacy:
    '''A helper context manager to track LLVM pass timings.
    '''
    __slots__ = [
        '_data']
    
    def __enter__(self):
        '''Enables the pass timing in LLVM.
        '''
        llvm.set_time_passes(True)
        return self

    
    def __exit__(self, exc_val, exc_type, exc_tb):
        '''Reset timings and save report internally.
        '''
        self._data = llvm.report_and_reset_timings()
        llvm.set_time_passes(False)

    
    def get(self):
        '''Retrieve timing data for processing.

        Returns
        -------
        timings: ProcessedPassTimings
        '''
        return ProcessedPassTimings(self._data)



class RecordLLVMPassTimings:
    '''A helper context manager to track LLVM pass timings.
    '''
    __slots__ = [
        '_data',
        '_pb']
    
    def __init__(self, pb):
        self._pb = pb
        self._data = None

    
    def __enter__(self):
        '''Enables the pass timing in LLVM.
        '''
        self._pb.start_pass_timing()
        return self

    
    def __exit__(self, exc_val, exc_type, exc_tb):
        '''Reset timings and save report internally.
        '''
        self._data = self._pb.finish_pass_timing()

    
    def get(self):
        '''Retrieve timing data for processing.

        Returns
        -------
        timings: ProcessedPassTimings
        '''
        return ProcessedPassTimings(self._data)


PassTimingRecord = namedtuple('PassTimingRecord', [
    'user_time',
    'user_percent',
    'system_time',
    'system_percent',
    'user_system_time',
    'user_system_percent',
    'wall_time',
    'wall_percent',
    'pass_name',
    'instruction'])

def _adjust_timings(records):
    '''Adjust timing records because of truncated information.

    Details: The percent information can be used to improve the timing
    information.

    Returns
    -------
    res: List[PassTimingRecord]
    '''
    pass
# WARNING: Decompyle incomplete


class ProcessedPassTimings:
    """A class for processing raw timing report from LLVM.

    The processing is done lazily so we don't waste time processing unused
    timing information.
    """
    
    def __init__(self, raw_data):
        self._raw_data = raw_data

    
    def __bool__(self):
        return bool(self._raw_data)

    
    def get_raw_data(self):
        '''Returns the raw string data.

        Returns
        -------
        res: str
        '''
        return self._raw_data

    
    def get_total_time(self):
        '''Compute the total time spend in all passes.

        Returns
        -------
        res: float
        '''
        return self.list_records()[-1].wall_time

    
    def list_records(self):
        '''Get the processed data for the timing report.

        Returns
        -------
        res: List[PassTimingRecord]
        '''
        return self._processed

    
    def list_top(self, n):
        '''Returns the top(n) most time-consuming (by wall-time) passes.

        Parameters
        ----------
        n: int
            This limits the maximum number of items to show.
            This function will show the ``n`` most time-consuming passes.

        Returns
        -------
        res: List[PassTimingRecord]
            Returns the top(n) most time-consuming passes in descending order.
        '''
        records = self.list_records()
        key = operator.attrgetter('wall_time')
        return heapq.nlargest(n, records[:-1], key)

    
    def summary(self, topn, indent = (5, 0)):
        '''Return a string summarizing the timing information.

        Parameters
        ----------
        topn: int; optional
            This limits the maximum number of items to show.
            This function will show the ``topn`` most time-consuming passes.
        indent: int; optional
            Set the indentation level. Defaults to 0 for no indentation.

        Returns
        -------
        res: str
        '''
        pass
    # WARNING: Decompyle incomplete

    _processed = (lambda self: self._process())()
    
    def _process(self):
        '''Parses the raw string data from LLVM timing report and attempts
        to improve the data by recomputing the times
        (See `_adjust_timings()``).
        '''
        
        def parse(raw_data):
            '''A generator that parses the raw_data line-by-line to extract
            timing information for each pass.
            '''
            pass
        # WARNING: Decompyle incomplete

        records = list(parse(self._raw_data))
        return _adjust_timings(records)


NamedTimings = namedtuple('NamedTimings', [
    'name',
    'timings'])

class PassTimingsCollection(Sequence):
    '''A collection of pass timings.

    This class implements the ``Sequence`` protocol for accessing the
    individual timing records.
    '''
    
    def __init__(self, name):
        self._name = name
        self._records = []

    record_legacy = (lambda self, name: pass# WARNING: Decompyle incomplete
)()
    record = (lambda self, name, pb: pass# WARNING: Decompyle incomplete
)()
    
    def _append(self, name, timings):
        '''Append timing records

        Parameters
        ----------
        name: str
            Name for the records.
        timings: ProcessedPassTimings
            the timing records.
        '''
        self._records.append(NamedTimings(name, timings))

    
    def get_total_time(self):
        '''Computes the sum of the total time across all contained timings.

        Returns
        -------
        res: float or None
            Returns the total number of seconds or None if no timings were
            recorded
        '''
        if self._records:
            return (lambda .0: pass# WARNING: Decompyle incomplete
)(self._records())

    
    def list_longest_first(self):
        '''Returns the timings in descending order of total time duration.

        Returns
        -------
        res: List[ProcessedPassTimings]
        '''
        return sorted(self._records, key = (lambda x: x.timings.get_total_time()), reverse = True)

    is_empty = (lambda self: not (self._records))()
    
    def summary(self, topn = (5,)):
        '''Return a string representing the summary of the timings.

        Parameters
        ----------
        topn: int; optional, default=5.
            This limits the maximum number of items to show.
            This function will show the ``topn`` most time-consuming passes.

        Returns
        -------
        res: str

        See also ``ProcessedPassTimings.summary()``
        '''
        if self.is_empty:
            return 'No pass timings were recorded'
        buf = None
        ap = buf.append
        ap(f'''Printing pass timings for {self._name}''')
        overall_time = self.get_total_time()
        ap(f'''Total time: {overall_time:.4f}''')
        for i, r in enumerate(self._records):
            ap(f'''== #{i} {r.name}''')
            percent = (r.timings.get_total_time() / overall_time) * 100
            ap(f''' Percent: {percent:.1f}%''')
            ap(r.timings.summary(topn = topn, indent = 1))
            return '\n'.join(buf)

    
    def __getitem__(self, i):
        '''Get the i-th timing record.

        Returns
        -------
        res: (name, timings)
            A named tuple with two fields:

            - name: str
            - timings: ProcessedPassTimings
        '''
        return self._records[i]

    
    def __len__(self):
        '''Length of this collection.
        '''
        return len(self._records)

    
    def __str__(self):
        return self.summary()

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _chunking.pyc (Python 3.11)

import warnings
from itertools import islice
from numbers import Integral
import numpy as np
from sklearn._config import get_config
from sklearn.utils._param_validation import Interval, validate_params

def chunk_generator(gen, chunksize):
    '''Chunk generator, ``gen`` into lists of length ``chunksize``. The last
    chunk may have a length less than ``chunksize``.'''
    pass
# WARNING: Decompyle incomplete

gen_batches = (lambda n = validate_params({
    'n': [
        Interval(Integral, 1, None, closed = 'left')],
    'batch_size': [
        Interval(Integral, 1, None, closed = 'left')],
    'min_batch_size': [
        Interval(Integral, 0, None, closed = 'left')] }, prefer_skip_nested_validation = True), batch_size = {
    'min_batch_size': 0 }, *, min_batch_size, start = None: pass# WARNING: Decompyle incomplete
)()
gen_even_slices = (lambda n = validate_params({
    'n': [
        Interval(Integral, 1, None, closed = 'left')],
    'n_packs': [
        Interval(Integral, 1, None, closed = 'left')],
    'n_samples': [
        Interval(Integral, 1, None, closed = 'left'),
        None] }, prefer_skip_nested_validation = True), n_packs = {
    'n_samples': None }, *, n_samples, start = None: pass# WARNING: Decompyle incomplete
)()

def get_chunk_n_rows(row_bytes = None, *, max_n_rows, working_memory):
    """Calculate how many rows can be processed within `working_memory`.

    Parameters
    ----------
    row_bytes : int
        The expected number of bytes of memory that will be consumed
        during the processing of each row.
    max_n_rows : int, default=None
        The maximum return value.
    working_memory : int or float, default=None
        The number of rows to fit inside this number of MiB will be
        returned. When None (default), the value of
        ``sklearn.get_config()['working_memory']`` is used.

    Returns
    -------
    int
        The number of rows which can be processed within `working_memory`.

    Warns
    -----
    Issues a UserWarning if `row_bytes exceeds `working_memory` MiB.
    """
    pass
# WARNING: Decompyle incomplete

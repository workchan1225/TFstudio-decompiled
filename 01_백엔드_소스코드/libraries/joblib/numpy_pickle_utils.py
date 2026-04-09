# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: numpy_pickle_utils.pyc (Python 3.11)

'''Utilities for fast persistence of big data, with optional compression.'''
import contextlib
import io
import pickle
import sys
import warnings
from compressor import _COMPRESSORS, _ZFILE_PREFIX

try:
    import numpy as np
except ImportError:
    np = None

Unpickler = pickle._Unpickler
Pickler = pickle._Pickler
xrange = range

try:
    import bz2
except ImportError:
    bz2 = None

_IO_BUFFER_SIZE = 1048576

def _is_raw_file(fileobj):
    '''Check if fileobj is a raw file object, e.g created with open.'''
    fileobj = getattr(fileobj, 'raw', fileobj)
    return isinstance(fileobj, io.FileIO)


def _get_prefixes_max_len():
    prefixes = _COMPRESSORS.values()()
    prefixes += [
        len(_ZFILE_PREFIX)]
    return max(prefixes)


def _is_numpy_array_byte_order_mismatch(array):

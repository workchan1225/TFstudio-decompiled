# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: pickle.pyc (Python 3.11)

'''pickle compat'''
from __future__ import annotations
import pickle
from typing import TYPE_CHECKING, Any
import warnings
from pandas.compat import pickle_compat
from pandas.util._decorators import set_module
from pandas.io.common import get_handle
if TYPE_CHECKING:
    from pandas._typing import CompressionOptions, FilePath, ReadPickleBuffer, StorageOptions, WriteBuffer
    from pandas import DataFrame, Series
to_pickle = (lambda obj = None, filepath_or_buffer = None, compression = set_module('pandas'), protocol = ('infer', pickle.HIGHEST_PROTOCOL, None), storage_options = ('obj', 'Any', 'filepath_or_buffer', 'FilePath | WriteBuffer[bytes]', 'compression', 'CompressionOptions', 'protocol', 'int', 'storage_options', 'StorageOptions | None', 'return', 'None'): if protocol < 0:
protocol = pickle.HIGHEST_PROTOCOLhandles = get_handle(filepath_or_buffer, 'wb', compression = compression, is_text = False, storage_options = storage_options)pickle.dump(obj, handles.handle, protocol = protocol)None(None, None)Nonewith None:
if not None:
pass)()
read_pickle = (lambda filepath_or_buffer = None, compression = None, storage_options = set_module('pandas'): excs_to_catch = (AttributeError, ImportError, ModuleNotFoundError, TypeError)handles = get_handle(filepath_or_buffer, 'rb', compression = compression, is_text = False, storage_options = storage_options)warnings.catch_warnings(record = True)warnings.simplefilter('ignore', Warning)None(None, None)None(None, None)with None:
if not None, pickle.load(handles.handle), :
pass)()

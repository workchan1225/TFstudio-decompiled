# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _tempfile.pyc (Python 3.11)

from __future__ import annotations
import os
import sys
import tempfile
from collections.abc import Iterable
from io import BytesIO, TextIOWrapper
from types import TracebackType
from typing import TYPE_CHECKING, Any, AnyStr, Generic, overload
from  import to_thread
from _core._fileio import AsyncFile
from lowlevel import checkpoint_if_cancelled
if TYPE_CHECKING:
    from _typeshed import OpenBinaryMode, OpenTextMode, ReadableBuffer, WriteableBuffer

def TemporaryFile():
    '''TemporaryFile'''
    _async_file: 'AsyncFile[AnyStr]' = '\n    An asynchronous temporary file that is automatically created and cleaned up.\n\n    This class provides an asynchronous context manager interface to a temporary file.\n    The file is created using Python\'s standard `tempfile.TemporaryFile` function in a\n    background thread, and is wrapped as an asynchronous file using `AsyncFile`.\n\n    :param mode: The mode in which the file is opened. Defaults to "w+b".\n    :param buffering: The buffering policy (-1 means the default buffering).\n    :param encoding: The encoding used to decode or encode the file. Only applicable in\n        text mode.\n    :param newline: Controls how universal newlines mode works (only applicable in text\n        mode).\n    :param suffix: The suffix for the temporary file name.\n    :param prefix: The prefix for the temporary file name.\n    :param dir: The directory in which the temporary file is created.\n    :param errors: The error handling scheme used for encoding/decoding errors.\n    '
    __init__ = (lambda self, mode = None, buffering = None, encoding = None, newline = overload, suffix = (..., ..., ..., ..., ..., ..., ...), prefix = {
        'errors': ... }, dir = ('self', 'TemporaryFile[bytes]', 'mode', 'OpenBinaryMode', 'buffering', 'int', 'encoding', 'str | None', 'newline', 'str | None', 'suffix', 'str | None', 'prefix', 'str | None', 'dir', 'str | None', 'errors', 'str | None'), *, errors,

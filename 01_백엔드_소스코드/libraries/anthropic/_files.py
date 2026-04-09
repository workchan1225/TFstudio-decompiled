# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _files.pyc (Python 3.11)

from __future__ import annotations
import io
import os
import pathlib
from typing import overload
from typing_extensions import TypeGuard
import anyio
from _types import FileTypes, FileContent, RequestFiles, HttpxFileTypes, Base64FileInput, HttpxFileContent, HttpxRequestFiles
from _utils import is_tuple_t, is_mapping_t, is_sequence_t

def is_base64_file_input(obj = None):

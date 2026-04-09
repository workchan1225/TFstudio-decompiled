# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _files.pyc (Python 3.11)

from __future__ import annotations
import os
from pathlib import Path
import anyio
from _types import FileTypes

def files_from_dir(directory = None):
    path = Path(directory)
    files = []
    _collect_files(path, path.parent, files)
    return files


def _collect_files(directory = None, relative_to = None, files = None):
    for path in directory.iterdir():
        if path.is_dir():
            _collect_files(path, relative_to, files)
            continue
        files.append((path.relative_to(relative_to).as_posix(), path.read_bytes()))
        return None


async def async_files_from_dir(directory = None):
    pass
# WARNING: Decompyle incomplete


async def _async_collect_files(directory = None, relative_to = None, files = None):
    pass
# WARNING: Decompyle incomplete

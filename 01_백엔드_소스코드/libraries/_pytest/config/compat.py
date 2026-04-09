# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: compat.pyc (Python 3.11)

from __future__ import annotations
from collections.abc import Mapping
import functools
from pathlib import Path
from typing import Any
import warnings
import pluggy
from compat import LEGACY_PATH
from compat import legacy_path
from deprecated import HOOK_LEGACY_PATH_ARG
imply_paths_hooks: 'Mapping[str, tuple[str, str]]' = {
    'pytest_ignore_collect': ('collection_path', 'path'),
    'pytest_collect_file': ('file_path', 'path'),
    'pytest_pycollect_makemodule': ('module_path', 'path'),
    'pytest_report_header': ('start_path', 'startdir'),
    'pytest_report_collectionfinish': ('start_path', 'startdir') }

def _check_path(path = None, fspath = None):
    if Path(fspath) != path:
        raise ValueError(f'''Path({fspath!r}) != {path!r}\nif both path and fspath are given they need to be equal''')


class PathAwareHookProxy:
    """
    this helper wraps around hook callers
    until pluggy supports fixingcalls, this one will do

    it currently doesn't return full hook caller proxies for fixed hooks,
    this may have to be changed later depending on bugs
    """
    
    def __init__(self = None, hook_relay = None):
        self._hook_relay = hook_relay

    
    def __dir__(self = None):
        return dir(self._hook_relay)

    
    def __getattr__(self = None, key = None):
        pass
    # WARNING: Decompyle incomplete

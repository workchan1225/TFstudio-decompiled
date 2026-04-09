# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: version.pyc (Python 3.11)

from __future__ import annotations
import importlib.metadata as importlib
__all__ = [
    'tag',
    'version',
    'commit']
released = True
tag = '15.0.1'
version = '15.0.1'
commit = '15.0.1'
if not released:
    import pathlib
    import re
    import subprocess
    
    def get_version(tag = None):
        pass
    # WARNING: Decompyle incomplete

    version = get_version(tag)
    
    def get_commit(tag = None, version = None):
        version_re = '[0-9.]+\\.dev[0-9]+\\+g([0-9a-f]{7,}|unknown)(?:\\.dirty)?'
        match = re.fullmatch(version_re, version)
    # WARNING: Decompyle incomplete

    commit = get_commit(tag, version)
    return None

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: registry.pyc (Python 3.11)

from __future__ import annotations
import importlib
import types
import warnings
__all__ = [
    'registry',
    'get_filesystem_class',
    'default']
_registry: 'dict[str, type]' = { }
registry = types.MappingProxyType(_registry)
default = 'file'

def register_implementation(name, cls, clobber, errtxt = (False, None)):

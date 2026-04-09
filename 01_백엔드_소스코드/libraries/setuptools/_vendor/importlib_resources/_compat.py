# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _compat.pyc (Python 3.11)

import abc
import sys
import pathlib
from contextlib import suppress
if sys.version_info >= (3, 10):
    from zipfile import Path as ZipPath
else:
    from zipp import Path as ZipPath

try:
    from typing import runtime_checkable
except ImportError:
    
    def runtime_checkable(cls):
        return cls



try:
    from typing import Protocol
except ImportError:
    Protocol = abc.ABC


class TraversableResourcesLoader:
    '''
    Adapt loaders to provide TraversableResources and other
    compatibility.

    Used primarily for Python 3.9 and earlier where the native
    loaders do not yet implement TraversableResources.
    '''
    
    def __init__(self, spec):
        self.spec = spec

    path = (lambda self: self.spec.origin)()
    
    def get_resource_reader(self, name):
        pass
    # WARNING: Decompyle incomplete



def wrap_spec(package):
    '''
    Construct a package spec with traversable compatibility
    on the spec/loader/reader.

    Supersedes _adapters.wrap_spec to use TraversableResourcesLoader
    from above for older Python compatibility (<3.10).
    '''
    _adapters = _adapters
    import 
    return _adapters.SpecLoaderAdapter(package.__spec__, TraversableResourcesLoader)

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: api_implementation.pyc (Python 3.11)

__doc__ = 'Determine which implementation of the protobuf API is used in this process.\n'
import importlib
import os
import sys
import warnings

def _ApiVersionToImplementationType(api_version):
    if api_version == 2:
        return 'cpp'
    if None == 1:
        raise ValueError('api_version=1 is no longer supported.')
    if api_version == 0:
        return 'python'

_implementation_type = None

try:
    from google.protobuf.internal import _api_implementation
    _implementation_type = _ApiVersionToImplementationType(_api_implementation.api_version)
except ImportError:
    pass


def _CanImport(mod_name):
    
    try:
        mod = importlib.import_module(mod_name)
        if not mod:
            raise ImportError(mod_name + ' import succeeded but was None')
        return True
    except ImportError:
        return False


# WARNING: Decompyle incomplete

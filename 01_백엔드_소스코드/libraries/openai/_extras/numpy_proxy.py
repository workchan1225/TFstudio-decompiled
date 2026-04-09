# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: numpy_proxy.pyc (Python 3.11)

from __future__ import annotations
from typing import TYPE_CHECKING, Any
from typing_extensions import override
from _utils import LazyProxy
from _common import MissingDependencyError, format_instructions
if TYPE_CHECKING:
    import numpy
NUMPY_INSTRUCTIONS = format_instructions(library = 'numpy', extra = 'voice_helpers')

def NumpyProxy():
    '''NumpyProxy'''
    __load__ = (lambda self = None: try:
import numpyexcept ImportError:
err = Noneraise MissingDependencyError(NUMPY_INSTRUCTIONS), errerr = Nonedel errnumpy)()

NumpyProxy = <NODE:27>(NumpyProxy, 'NumpyProxy', LazyProxy[Any])
if not TYPE_CHECKING:
    numpy = NumpyProxy()

def has_numpy():
    
    try:
        import numpy
    except ImportError:
        return False

    return True

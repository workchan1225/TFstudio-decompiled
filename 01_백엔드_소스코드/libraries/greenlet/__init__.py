# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''
The root of the greenlet package.
'''
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
__all__ = [
    '__version__',
    '_C_API',
    'GreenletExit',
    'error',
    'getcurrent',
    'greenlet',
    'gettrace',
    'settrace']
__version__ = '3.3.0'
from _greenlet import _C_API
from _greenlet import GreenletExit
from _greenlet import error
from _greenlet import getcurrent
from _greenlet import greenlet

try:
    from _greenlet import gettrace
    from _greenlet import settrace
except ImportError:
    pass

from _greenlet import GREENLET_USE_CONTEXT_VARS
from _greenlet import GREENLET_USE_GC
from _greenlet import GREENLET_USE_TRACING
from _greenlet import CLOCKS_PER_SEC
from _greenlet import enable_optional_cleanup
from _greenlet import get_clocks_used_doing_optional_cleanup

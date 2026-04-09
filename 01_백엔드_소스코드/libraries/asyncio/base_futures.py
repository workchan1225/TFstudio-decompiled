# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: base_futures.pyc (Python 3.11)

__all__ = ()
import reprlib
from _thread import get_ident
from  import format_helpers
_PENDING = 'PENDING'
_CANCELLED = 'CANCELLED'
_FINISHED = 'FINISHED'

def isfuture(obj):

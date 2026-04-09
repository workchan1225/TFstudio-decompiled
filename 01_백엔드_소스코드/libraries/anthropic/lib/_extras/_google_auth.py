# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _google_auth.pyc (Python 3.11)

from __future__ import annotations
from typing import TYPE_CHECKING, Any
from typing_extensions import ClassVar, override
from _common import MissingDependencyError
from _utils import LazyProxy
if TYPE_CHECKING:
    import google.auth as google
    google_auth = google.auth

def GoogleAuthProxy():
    '''GoogleAuthProxy'''
    should_cache: 'ClassVar[bool]' = True
    __load__ = (lambda self = None: try:
import google.auth as googleexcept ImportError:
err = Noneraise MissingDependencyError(extra = 'vertex', library = 'google-auth'), errerr = Nonedel errgoogle.auth)()

GoogleAuthProxy = <NODE:27>(GoogleAuthProxy, 'GoogleAuthProxy', LazyProxy[Any])
if not TYPE_CHECKING:
    google_auth = GoogleAuthProxy()
    return None

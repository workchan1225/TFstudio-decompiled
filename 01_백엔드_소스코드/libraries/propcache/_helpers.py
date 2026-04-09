# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _helpers.pyc (Python 3.11)

import os
import sys
from typing import TYPE_CHECKING
__all__ = ('cached_property', 'under_cached_property')
NO_EXTENSIONS = bool(os.environ.get('PROPCACHE_NO_EXTENSIONS'))
if sys.implementation.name != 'cpython':
    NO_EXTENSIONS = True
if TYPE_CHECKING:
    from _helpers_py import cached_property as cached_property_py
    from _helpers_py import under_cached_property as under_cached_property_py
    cached_property = cached_property_py
    under_cached_property = under_cached_property_py
    return None
if not None:
    
    try:
        from _helpers_c import cached_property as cached_property_c
        from _helpers_c import under_cached_property as under_cached_property_c
        cached_property = cached_property_c
        under_cached_property = under_cached_property_c
        return None
    except ImportError:
        from _helpers_py import cached_property as cached_property_py
        from _helpers_py import under_cached_property as under_cached_property_py
        cached_property = cached_property_py
        under_cached_property = under_cached_property_py
        return None
        from _helpers_py import cached_property as cached_property_py
        from _helpers_py import under_cached_property as under_cached_property_py
        cached_property = cached_property_py
        under_cached_property = under_cached_property_py
        return None

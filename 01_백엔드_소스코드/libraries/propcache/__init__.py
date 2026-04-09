# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''propcache: An accelerated property cache for Python classes.'''
from typing import TYPE_CHECKING
_PUBLIC_API = ('cached_property', 'under_cached_property')
__version__ = '0.4.1'
__all__ = ()
if TYPE_CHECKING:
    from api import cached_property
    from api import under_cached_property

def _import_facade(attr = None):
    '''Import the public API from the `api` module.'''
    if attr in _PUBLIC_API:
        api = api
        import 
        return getattr(api, attr)
    raise None(f'''module \'{__package__}\' has no attribute \'{attr}\'''')


def _dir_facade():

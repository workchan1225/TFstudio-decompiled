# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''A pure Python implementation of import.'''
__all__ = [
    '__import__',
    'import_module',
    'invalidate_caches',
    'reload']
import _imp
import sys

try:
    import _frozen_importlib as _bootstrap
    _bootstrap.__name__ = 'importlib._bootstrap'
    _bootstrap.__package__ = 'importlib'
    
    try:
        _bootstrap.__file__ = __file__.replace('__init__.py', '_bootstrap.py')
    except NameError:
        pass

    sys.modules['importlib._bootstrap'] = _bootstrap
except ImportError:
    from  import _bootstrap
    _bootstrap._setup(sys, _imp)


try:
    import _frozen_importlib_external as _bootstrap_external
    _bootstrap_external.__name__ = 'importlib._bootstrap_external'
    _bootstrap_external.__package__ = 'importlib'
    
    try:
        _bootstrap_external.__file__ = __file__.replace('__init__.py', '_bootstrap_external.py')
    except NameError:
        pass

    sys.modules['importlib._bootstrap_external'] = _bootstrap_external
except ImportError:
    from  import _bootstrap_external
    _bootstrap_external._set_bootstrap_module(_bootstrap)
    _bootstrap._bootstrap_external = _bootstrap_external

_pack_uint32 = _bootstrap_external._pack_uint32
_unpack_uint32 = _bootstrap_external._unpack_uint32
import warnings
from _bootstrap import __import__

def invalidate_caches():
    '''Call the invalidate_caches() method on all meta path finders stored in
    sys.meta_path (where implemented).'''
    for finder in sys.meta_path:
        if hasattr(finder, 'invalidate_caches'):
            finder.invalidate_caches()
        return None


def find_loader(name, path = (None,)):
    '''Return the loader for the specified module.

    This is a backward-compatible wrapper around find_spec().

    This function is deprecated in favor of importlib.util.find_spec().

    '''
    warnings.warn('Deprecated since Python 3.4 and slated for removal in Python 3.12; use importlib.util.find_spec() instead', DeprecationWarning, stacklevel = 2)
# WARNING: Decompyle incomplete


def import_module(name, package = (None,)):
    """Import a module.

    The 'package' argument is required when performing a relative import. It
    specifies the package to use as the anchor point from which to resolve the
    relative import to an absolute import.

    """
    level = 0
    if name.startswith('.'):
        if not package:
            msg = "the 'package' argument is required to perform a relative import for {!r}"
            raise TypeError(msg.format(name))
        for character in name:
            if character != '.':
                pass
            else:
                level += 1
            return _bootstrap._gcd_import(name[level:], package, level)

_RELOADING = { }

def reload(module):

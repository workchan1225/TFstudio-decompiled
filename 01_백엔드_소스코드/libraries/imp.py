# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: imp.pyc (Python 3.11)

"""This module provides the components needed to build your own __import__
function.  Undocumented functions are obsolete.

In most cases it is preferred you consider using the importlib module's
functionality over this module.

"""
from _imp import lock_held, acquire_lock, release_lock, get_frozen_object, is_frozen_package, init_frozen, is_builtin, is_frozen, _fix_co_filename, _frozen_module_names

try:
    from _imp import create_dynamic
except ImportError:
    create_dynamic = None

from importlib._bootstrap import _ERR_MSG, _exec, _load, _builtin_from_name
from importlib._bootstrap_external import SourcelessFileLoader
from importlib import machinery
from importlib import util
import importlib
import os
import sys
import tokenize
import types
import warnings
warnings.warn("the imp module is deprecated in favour of importlib and slated for removal in Python 3.12; see the module's documentation for alternative uses", DeprecationWarning, stacklevel = 2)
SEARCH_ERROR = 0
PY_SOURCE = 1
PY_COMPILED = 2
C_EXTENSION = 3
PY_RESOURCE = 4
PKG_DIRECTORY = 5
C_BUILTIN = 6
PY_FROZEN = 7
PY_CODERESOURCE = 8
IMP_HOOK = 9

def new_module(name):
    '''**DEPRECATED**

    Create a new module.

    The module is not entered into sys.modules.

    '''
    return types.ModuleType(name)


def get_magic():
    '''**DEPRECATED**

    Return the magic number for .pyc files.
    '''
    return util.MAGIC_NUMBER


def get_tag():
    '''Return the magic tag for .pyc files.'''
    return sys.implementation.cache_tag


def cache_from_source(path, debug_override = (None,)):
    '''**DEPRECATED**

    Given the path to a .py file, return the path to its .pyc file.

    The .py file does not need to exist; this simply returns the path to the
    .pyc file calculated as if the .py file were imported.

    If debug_override is not None, then it must be a boolean and is used in
    place of sys.flags.optimize.

    If sys.implementation.cache_tag is None then NotImplementedError is raised.

    '''
    warnings.catch_warnings()
    warnings.simplefilter('ignore')
    None(None, None)
    return 
    with None:
        if not None, util.cache_from_source(path, debug_override):
            pass


def source_from_cache(path):
    '''**DEPRECATED**

    Given the path to a .pyc. file, return the path to its .py file.

    The .pyc file does not need to exist; this simply returns the path to
    the .py file calculated to correspond to the .pyc file.  If path does
    not conform to PEP 3147 format, ValueError will be raised. If
    sys.implementation.cache_tag is None then NotImplementedError is raised.

    '''
    return util.source_from_cache(path)


def get_suffixes():
    '''**DEPRECATED**'''
    extensions = machinery.EXTENSION_SUFFIXES()
    source = machinery.SOURCE_SUFFIXES()
    bytecode = machinery.BYTECODE_SUFFIXES()
    return extensions + source + bytecode


class NullImporter:
    '''**DEPRECATED**

    Null import object.

    '''
    
    def __init__(self, path):
        if path == '':
            raise ImportError('empty pathname', path = '')
        if os.path.isdir(path):
            raise ImportError('existing directory', path = path)

    
    def find_module(self, fullname):
        '''Always returns None.'''
        pass



class _HackedGetData:
    pass
# WARNING: Decompyle incomplete


class _LoadSourceCompatibility(machinery.SourceFileLoader, _HackedGetData):
    '''Compatibility support for implementing load_source().'''
    pass


def load_source(name, pathname, file = (None,)):
    loader = _LoadSourceCompatibility(name, pathname, file)
    spec = util.spec_from_file_location(name, pathname, loader = loader)
    if name in sys.modules:
        module = _exec(spec, sys.modules[name])
    else:
        module = _load(spec)
    module.__loader__ = machinery.SourceFileLoader(name, pathname)
    module.__spec__.loader = module.__loader__
    return module


class _LoadCompiledCompatibility(SourcelessFileLoader, _HackedGetData):
    '''Compatibility support for implementing load_compiled().'''
    pass


def load_compiled(name, pathname, file = (None,)):
    '''**DEPRECATED**'''
    loader = _LoadCompiledCompatibility(name, pathname, file)
    spec = util.spec_from_file_location(name, pathname, loader = loader)
    if name in sys.modules:
        module = _exec(spec, sys.modules[name])
    else:
        module = _load(spec)
    module.__loader__ = SourcelessFileLoader(name, pathname)
    module.__spec__.loader = module.__loader__
    return module


def load_package(name, path):
    '''**DEPRECATED**'''
    if os.path.isdir(path):
        extensions = machinery.SOURCE_SUFFIXES[:] + machinery.BYTECODE_SUFFIXES[:]
        for extension in extensions:
            init_path = os.path.join(path, '__init__' + extension)
            if os.path.exists(init_path):
                path = init_path
            
            raise ValueError('{!r} is not a package'.format(path))
            spec = util.spec_from_file_location(name, path, submodule_search_locations = [])
            if name in sys.modules:
                return _exec(spec, sys.modules[name])
            return None(spec)


def load_module(name, file, filename, details):
    '''**DEPRECATED**

    Load a module, given information returned by find_module().

    The module name must include the full package name, if any.

    '''
    (suffix, mode, type_) = details
    if mode:
        if mode.startswith('r') or '+' in mode:
            raise ValueError('invalid file open mode {!r}'.format(mode))
# WARNING: Decompyle incomplete


def find_module(name, path = (None,)):
    """**DEPRECATED**

    Search for a module.

    If path is omitted or None, search for a built-in, frozen or special
    module and continue search in sys.path. The module name cannot
    contain '.'; to search for a submodule of a package, pass the
    submodule name and the package's __path__.

    """
    if not isinstance(name, str):
        raise TypeError("'name' must be a str, not {}".format(type(name)))
    if not isinstance(path, (type(None), list)):
        raise RuntimeError("'path' must be None or a list, not {}".format(type(path)))
# WARNING: Decompyle incomplete


def reload(module):
    '''**DEPRECATED**

    Reload the module and return it.

    The module must have been successfully imported before.

    '''
    return importlib.reload(module)


def init_builtin(name):
    """**DEPRECATED**

    Load and return a built-in module by name, or None is such module doesn't
    exist
    """
    
    try:
        return _builtin_from_name(name)
    except ImportError:
        return None


if create_dynamic:
    
    def load_dynamic(name, path, file = (None,)):
        '''**DEPRECATED**

        Load an extension module.
        '''
        import importlib.machinery as importlib
        loader = importlib.machinery.ExtensionFileLoader(name, path)
        spec = importlib.machinery.ModuleSpec(name = name, loader = loader, origin = path)
        return _load(spec)

    return None
load_dynamic = None

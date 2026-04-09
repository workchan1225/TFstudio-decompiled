# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: misc.pyc (Python 3.11)

'''Miscellaneous stuff for coverage.py.'''
from __future__ import annotations
import contextlib
import datetime
import errno
import functools
import hashlib
import importlib
import importlib.util as importlib
import inspect
import os
import os.path as os
import re
import sys
import types
from collections.abc import Iterable, Iterator, Mapping, Sequence
from types import ModuleType
from typing import Any, NoReturn, TypeVar
from coverage.exceptions import *
from coverage.exceptions import CoverageException
from coverage.types import TArc
ISOLATED_MODULES: 'dict[ModuleType, ModuleType]' = { }

def isolate_module(mod = None):
    '''Copy a module so that we are isolated from aggressive mocking.

    If a test suite mocks os.path.exists (for example), and then we need to use
    it during the test, everything will get tangled up if we use their mock.
    Making a copy of the module when we import it will isolate coverage.py from
    those complications.
    '''
    if mod not in ISOLATED_MODULES:
        new_mod = types.ModuleType(mod.__name__)
        ISOLATED_MODULES[mod] = new_mod
        for name in dir(mod):
            value = getattr(mod, name)
            if isinstance(value, types.ModuleType):
                value = isolate_module(value)
            setattr(new_mod, name, value)
            return ISOLATED_MODULES[mod]

os = isolate_module(os)

class SysModuleSaver:
    '''Saves the contents of sys.modules, and removes new modules later.'''
    
    def __init__(self = None):
        self.old_modules = set(sys.modules)

    
    def restore(self = None):
        '''Remove any modules imported since this object started.'''
        new_modules = set(sys.modules) - self.old_modules
        for m in new_modules:
            del sys.modules[m]
            return None


sys_modules_saved = (lambda : pass# WARNING: Decompyle incomplete
)()

def import_third_party(modname = None):
    """Import a third-party module we need, but might not be installed.

    This also cleans out the module after the import, so that coverage won't
    appear to have imported it.  This lets the third party use coverage for
    their own tests.

    Arguments:
        modname (str): the name of the module to import.

    Returns:
        The imported module, and a boolean indicating if the module could be imported.

    If the boolean is False, the module returned is not the one you want: don't use it.

    """
    sys_modules_saved()
    None(None, None)
    return 
    except ImportError:
        None(None, None)
        return 
    with None:
        if not None:
            pass


def nice_pair(pair = None):
    '''Make a nice string representation of a pair of numbers.

    If the numbers are equal, just return the number, otherwise return the pair
    with a dash between them, indicating the range.

    '''
    (start, end) = pair
    if start == end:
        return f'''{start}'''
    return f'''{None}-{end}'''


def bool_or_none(b = None):
    '''Return bool(b), but preserve None.'''
    pass
# WARNING: Decompyle incomplete


def join_regex(regexes = None):
    '''Combine a series of regex strings into one that matches any of them.'''
    regexes = list(regexes)
    if len(regexes) == 1:
        return regexes[0]
    return (lambda .0: pass# WARNING: Decompyle incomplete
)(regexes())


def file_be_gone(path = None):
    """Remove a file, and don't get annoyed if it doesn't exist."""
    
    try:
        os.remove(path)
        return None
    except OSError:
        e = None
        if e.errno != errno.ENOENT:
            raise 
        e = None
        del e
        return None
        e = None
        del e



def ensure_dir(directory = None):
    '''Make sure the directory exists.

    If `directory` is None or empty, do nothing.
    '''
    if directory:
        os.makedirs(directory, exist_ok = True)
        return None


def ensure_dir_for_file(path = None):
    '''Make sure the directory for the path exists.'''
    ensure_dir(os.path.dirname(path))


class Hasher:
    '''Hashes Python data for fingerprinting.'''
    
    def __init__(self = None):
        self.hash = hashlib.new('sha3_256', usedforsecurity = False)

    
    def update(self = None, v = None):
        '''Add `v` to the hash, recursively if needed.'''
        self.hash.update(str(type(v)).encode('utf-8'))
    # WARNING: Decompyle incomplete

    
    def hexdigest(self = None):
        '''Retrieve the hex digest of the hash.'''
        return self.hash.hexdigest()[:32]



def _needs_to_implement(that = None, func_name = None):
    '''Helper to raise NotImplementedError in interface stubs.'''
    if hasattr(that, '_coverage_plugin_name'):
        thing = 'Plugin'
        name = that._coverage_plugin_name
    else:
        thing = 'Class'
        klass = that.__class__
        name = f'''{klass.__module__}.{klass.__name__}'''
    raise NotImplementedError(f'''{thing} {name!r} needs to implement {func_name}()''')


class DefaultValue:
    '''A sentinel object to use for unusual default-value needs.

    Construct with a string that will be used as the repr, for display in help
    and Sphinx output.

    '''
    
    def __init__(self = None, display_as = None):
        self.display_as = display_as

    
    def __repr__(self = None):
        return self.display_as



def substitute_variables(text = None, variables = None):
    '''Substitute ``${VAR}`` variables in `text` with their values.

    Variables in the text can take a number of shell-inspired forms::

        $VAR
        ${VAR}
        ${VAR?}             strict: an error if VAR isn\'t defined.
        ${VAR-missing}      defaulted: "missing" if VAR isn\'t defined.
        $$                  just a dollar sign.

    `variables` is a dictionary of variable values.

    Returns the resulting text with values substituted.

    '''
    pass
# WARNING: Decompyle incomplete


def format_local_datetime(dt = None):
    '''Return a string with local timezone representing the date.'''
    return dt.astimezone().strftime('%Y-%m-%d %H:%M %z')


def import_local_file(modname = None, modfile = None):
    """Import a local file as a module.

    Opens a file in the current directory named `modname`.py, imports it
    as `modname`, and returns the module object.  `modfile` is the file to
    import if it isn't in the current directory.

    """
    pass
# WARNING: Decompyle incomplete

_human_key = (lambda s = None: pass# WARNING: Decompyle incomplete
)()

def human_sorted(strings = None):
    '''Sort the given iterable of strings the way that humans expect.

    Numeric components in the strings are sorted as numbers.

    Returns the sorted list.

    '''
    return sorted(strings, key = _human_key)

SortableItem = TypeVar('SortableItem', bound = Sequence[Any])

def human_sorted_items(items = None, reverse = None):
    """Sort (string, ...) items the way humans expect.

    The elements of `items` can be any tuple/list. They'll be sorted by the
    first element (a string), with ties broken by the remaining elements.

    Returns the sorted list of items.
    """
    return sorted(items, key = (lambda item: pass# WARNING: Decompyle incomplete
), reverse = reverse)


def plural(n = None, thing = None, things = None):

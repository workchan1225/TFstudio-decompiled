# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''
    pygments.formatters
    ~~~~~~~~~~~~~~~~~~~

    Pygments formatters.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
import re
import sys
import types
import fnmatch
from os.path import basename
from pygments.formatters._mapping import FORMATTERS
from pygments.plugin import find_plugin_formatters
from pygments.util import ClassNotFound
__all__ = [
    'get_formatter_by_name',
    'get_formatter_for_filename',
    'get_all_formatters',
    'load_formatter_from_file'] + list(FORMATTERS)
_formatter_cache = { }
_pattern_cache = { }

def _fn_matches(fn, glob):
    '''Return whether the supplied file name fn matches pattern filename.'''
    if glob not in _pattern_cache:
        pattern = re.compile(fnmatch.translate(glob))
        _pattern_cache[glob] = re.compile(fnmatch.translate(glob))
        return pattern.match(fn)
    return None[glob].match(fn)


def _load_formatters(module_name):
    '''Load a formatter (and all others in the module too).'''
    mod = __import__(module_name, None, None, [
        '__all__'])
    for formatter_name in mod.__all__:
        cls = getattr(mod, formatter_name)
        _formatter_cache[cls.name] = cls
        return None


def get_all_formatters():
    '''Return a generator for all formatter classes.'''
    pass
# WARNING: Decompyle incomplete


def find_formatter_class(alias):
    '''Lookup a formatter by alias.

    Returns None if not found.
    '''
    for module_name, name, aliases, _, _ in FORMATTERS.values():
        if alias in aliases:
            if name not in _formatter_cache:
                _load_formatters(module_name)
            
            return None, _formatter_cache[name]
        for _, cls in find_plugin_formatters():
            if alias in cls.aliases:
                
                return None, cls
            return None


def get_formatter_by_name(_alias, **options):
    '''
    Return an instance of a :class:`.Formatter` subclass that has `alias` in its
    aliases list. The formatter is given the `options` at its instantiation.

    Will raise :exc:`pygments.util.ClassNotFound` if no formatter with that
    alias is found.
    '''
    cls = find_formatter_class(_alias)
# WARNING: Decompyle incomplete


def load_formatter_from_file(filename, formattername = ('CustomFormatter',), **options):
    '''
    Return a `Formatter` subclass instance loaded from the provided file, relative
    to the current directory.

    The file is expected to contain a Formatter class named ``formattername``
    (by default, CustomFormatter). Users should be very careful with the input, because
    this method is equivalent to running ``eval()`` on the input file. The formatter is
    given the `options` at its instantiation.

    :exc:`pygments.util.ClassNotFound` is raised if there are any errors loading
    the formatter.

    .. versionadded:: 2.2
    '''
    pass
# WARNING: Decompyle incomplete


def get_formatter_for_filename(fn, **options):
    '''
    Return a :class:`.Formatter` subclass instance that has a filename pattern
    matching `fn`. The formatter is given the `options` at its instantiation.

    Will raise :exc:`pygments.util.ClassNotFound` if no formatter for that filename
    is found.
    '''
    fn = basename(fn)
# WARNING: Decompyle incomplete


class _automodule(types.ModuleType):
    '''Automatically import formatters.'''
    
    def __getattr__(self, name):
        info = FORMATTERS.get(name)
        if info:
            _load_formatters(info[0])
            cls = _formatter_cache[info[1]]
            setattr(self, name, cls)
            return cls
        raise None(name)


oldmod = sys.modules[__name__]
newmod = _automodule(__name__)
newmod.__dict__.update(oldmod.__dict__)
sys.modules[__name__] = newmod
del newmod.newmod
del newmod.oldmod
del newmod.sys
del newmod.types

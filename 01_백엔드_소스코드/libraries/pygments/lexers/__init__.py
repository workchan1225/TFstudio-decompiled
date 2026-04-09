# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''
    pygments.lexers
    ~~~~~~~~~~~~~~~

    Pygments lexers.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
import re
import sys
import types
import fnmatch
from os.path import basename
from pygments.lexers._mapping import LEXERS
from pygments.modeline import get_filetype_from_buffer
from pygments.plugin import find_plugin_lexers
from pygments.util import ClassNotFound, guess_decode
COMPAT = {
    'Python3Lexer': 'PythonLexer',
    'Python3TracebackLexer': 'PythonTracebackLexer',
    'LeanLexer': 'Lean3Lexer' }
__all__ = [
    'get_lexer_by_name',
    'get_lexer_for_filename',
    'find_lexer_class',
    'guess_lexer',
    'load_lexer_from_file'] + list(LEXERS) + list(COMPAT)
_lexer_cache = { }
_pattern_cache = { }

def _fn_matches(fn, glob):
    '''Return whether the supplied file name fn matches pattern filename.'''
    if glob not in _pattern_cache:
        pattern = re.compile(fnmatch.translate(glob))
        _pattern_cache[glob] = re.compile(fnmatch.translate(glob))
        return pattern.match(fn)
    return None[glob].match(fn)


def _load_lexers(module_name):
    '''Load a lexer (and all others in the module too).'''
    mod = __import__(module_name, None, None, [
        '__all__'])
    for lexer_name in mod.__all__:
        cls = getattr(mod, lexer_name)
        _lexer_cache[cls.name] = cls
        return None


def get_all_lexers(plugins = (True,)):
    '''Return a generator of tuples in the form ``(name, aliases,
    filenames, mimetypes)`` of all know lexers.

    If *plugins* is true (the default), plugin lexers supplied by entrypoints
    are also returned.  Otherwise, only builtin ones are considered.
    '''
    pass
# WARNING: Decompyle incomplete


def find_lexer_class(name):
    '''
    Return the `Lexer` subclass that with the *name* attribute as given by
    the *name* argument.
    '''
    if name in _lexer_cache:
        return _lexer_cache[name]
    for module_name, lname, aliases, _, _ in None.values():
        if name == lname:
            _load_lexers(module_name)
            
            return None, _lexer_cache[name]
        for None in find_plugin_lexers():
            if cls.name == name:
                
                return None, cls
            return None


def find_lexer_class_by_name(_alias):
    '''
    Return the `Lexer` subclass that has `alias` in its aliases list, without
    instantiating it.

    Like `get_lexer_by_name`, but does not instantiate the class.

    Will raise :exc:`pygments.util.ClassNotFound` if no lexer with that alias is
    found.

    .. versionadded:: 2.2
    '''
    if not _alias:
        raise ClassNotFound(f'''no lexer for alias {_alias!r} found''')
    for module_name, name, aliases, _, _ in LEXERS.values():
        if _alias.lower() in aliases:
            if name not in _lexer_cache:
                _load_lexers(module_name)
            
            return None, _lexer_cache[name]
        for None in find_plugin_lexers():
            if _alias.lower() in cls.aliases:
                
                return None, cls
            raise ClassNotFound(f'''no lexer for alias {_alias!r} found''')


def get_lexer_by_name(_alias, **options):
    '''
    Return an instance of a `Lexer` subclass that has `alias` in its
    aliases list. The lexer is given the `options` at its
    instantiation.

    Will raise :exc:`pygments.util.ClassNotFound` if no lexer with that alias is
    found.
    '''
    if not _alias:
        raise ClassNotFound(f'''no lexer for alias {_alias!r} found''')
# WARNING: Decompyle incomplete


def load_lexer_from_file(filename, lexername = ('CustomLexer',), **options):
    '''Load a lexer from a file.

    This method expects a file located relative to the current working
    directory, which contains a Lexer class. By default, it expects the
    Lexer to be name CustomLexer; you can specify your own class name
    as the second argument to this function.

    Users should be very careful with the input, because this method
    is equivalent to running eval on the input file.

    Raises ClassNotFound if there are any problems importing the Lexer.

    .. versionadded:: 2.2
    '''
    pass
# WARNING: Decompyle incomplete


def find_lexer_class_for_filename(_fn, code = (None,)):
    '''Get a lexer for a filename.

    If multiple lexers match the filename pattern, use ``analyse_text()`` to
    figure out which one is more appropriate.

    Returns None if not found.
    '''
    pass
# WARNING: Decompyle incomplete


def get_lexer_for_filename(_fn, code = (None,), **options):
    '''Get a lexer for a filename.

    Return a `Lexer` subclass instance that has a filename pattern
    matching `fn`. The lexer is given the `options` at its
    instantiation.

    Raise :exc:`pygments.util.ClassNotFound` if no lexer for that filename
    is found.

    If multiple lexers match the filename pattern, use their ``analyse_text()``
    methods to figure out which one is more appropriate.
    '''
    res = find_lexer_class_for_filename(_fn, code)
    if not res:
        raise ClassNotFound(f'''no lexer for filename {_fn!r} found''')
# WARNING: Decompyle incomplete


def get_lexer_for_mimetype(_mime, **options):
    '''
    Return a `Lexer` subclass instance that has `mime` in its mimetype
    list. The lexer is given the `options` at its instantiation.

    Will raise :exc:`pygments.util.ClassNotFound` if not lexer for that mimetype
    is found.
    '''
    pass
# WARNING: Decompyle incomplete


def _iter_lexerclasses(plugins = (True,)):
    '''Return an iterator over all lexer classes.'''
    pass
# WARNING: Decompyle incomplete


def guess_lexer_for_filename(_fn, _text, **options):
    '''
    As :func:`guess_lexer()`, but only lexers which have a pattern in `filenames`
    or `alias_filenames` that matches `filename` are taken into consideration.

    :exc:`pygments.util.ClassNotFound` is raised if no lexer thinks it can
    handle the content.
    '''
    pass
# WARNING: Decompyle incomplete


def guess_lexer(_text, **options):
    """
    Return a `Lexer` subclass instance that's guessed from the text in
    `text`. For that, the :meth:`.analyse_text()` method of every known lexer
    class is called with the text as argument, and the lexer which returned the
    highest value will be instantiated and returned.

    :exc:`pygments.util.ClassNotFound` is raised if no lexer thinks it can
    handle the content.
    """
    if not isinstance(_text, str):
        inencoding = options.get('inencoding', options.get('encoding'))
        if inencoding:
            pass
    ft = get_filetype_from_buffer(_text)
# WARNING: Decompyle incomplete


class _automodule(types.ModuleType):
    '''Automatically import lexers.'''
    
    def __getattr__(self, name):
        info = LEXERS.get(name)
        if info:
            _load_lexers(info[0])
            cls = _lexer_cache[info[1]]
            setattr(self, name, cls)
            return cls
        if None in COMPAT:
            return getattr(self, COMPAT[name])
        raise None(name)


oldmod = sys.modules[__name__]
newmod = _automodule(__name__)
newmod.__dict__.update(oldmod.__dict__)
sys.modules[__name__] = newmod
del newmod.newmod
del newmod.oldmod
del newmod.sys
del newmod.types

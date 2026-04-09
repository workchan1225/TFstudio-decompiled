# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''brain-dead simple parser for ini-style files.
(C) Ronny Pfannschmidt, Holger Krekel -- MIT licensed
'''
import os
from collections.abc import Callable
from collections.abc import Iterator
from collections.abc import Mapping
from typing import Final
from typing import TypeVar
from typing import overload
__all__ = [
    'IniConfig',
    'ParseError',
    'COMMENTCHARS',
    'iscommentline']
from  import _parse
from _parse import COMMENTCHARS
from _parse import iscommentline
from exceptions import ParseError
_D = TypeVar('_D')
_T = TypeVar('_T')

class SectionWrapper:
    name: Final[str] = 'SectionWrapper'
    
    def __init__(self = None, config = None, name = None):
        self.config = config
        self.name = name

    
    def lineof(self = None, name = None):
        return self.config.lineof(self.name, name)

    get = (lambda self = None, key = None: pass)()
    get = (lambda self = None, key = None, convert = overload: pass)()
    get = (lambda self = None, key = None, default = overload, convert = ('key', str, 'default', None, 'convert', Callable[([
        str], _T)], 'return', _T | None): pass)()
    get = (lambda self = None, key = None, default = overload, convert = (None,): pass)()
    get = (lambda self = None, key = None, default = overload, convert = ('key', str, 'default', _D, 'convert', Callable[([
        str], _T)], 'return', _T | _D): pass)()
    
    def get(self = None, key = None, default = None, convert = (None, None)):
        return self.config.get(self.name, key, convert = convert, default = default)

    
    def __getitem__(self = None, key = None):
        return self.config.sections[self.name][key]

    
    def __iter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def items(self = None):
        pass
    # WARNING: Decompyle incomplete



class IniConfig:
    _sources: Final[Mapping[(tuple[(str, str | None)], int)]] = 'IniConfig'
    
    def __init__(self = None, path = None, data = None, encoding = None, *, _sections, _sources):
        self.path = os.fspath(path)
    # WARNING: Decompyle incomplete

    parse = (lambda cls = None, path = None, data = None, encoding = classmethod, *, strip_inline_comments, strip_section_whitespace, fspath = None, fp = None: fspath = os.fspath(path)# WARNING: Decompyle incomplete
)()
    
    def lineof(self = None, section = None, name = None):
        lineno = self._sources.get((section, name))
    # WARNING: Decompyle incomplete

    get = (lambda self = None, section = None, name = overload: pass)()
    get = (lambda self = None, section = None, name = overload, convert = ('section', str, 'name', str, 'convert', Callable[([
        str], _T)], 'return', _T | None): pass)()
    get = (lambda self, section = None, name = None, default = overload, convert = ('section', str, 'name', str, 'default', None, 'convert', Callable[([
        str], _T)], 'return', _T | None): pass)()
    get = (lambda self = None, section = None, name = overload, default = (None,), convert = ('section', str, 'name', str, 'default', _D, 'convert', None, 'return', str | _D): pass)()
    get = (lambda self, section = None, name = None, default = overload, convert = ('section', str, 'name', str, 'default', _D, 'convert', Callable[([
        str], _T)], 'return', _T | _D): pass)()
    
    def get(self = None, section = None, name = None, default = (None, None), convert = ('section', str, 'name', str, 'default', _D | None, 'convert', Callable[([
        str], _T)] | None, 'return', _D | _T | str | None)):
        pass
    # WARNING: Decompyle incomplete

    
    def __getitem__(self = None, name = None):
        if name not in self.sections:
            raise KeyError(name)
        return SectionWrapper(self, name)

    
    def __iter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __contains__(self = None, arg = None):
        return arg in self.sections

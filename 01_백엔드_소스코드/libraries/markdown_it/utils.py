# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: utils.pyc (Python 3.11)

from __future__ import annotations
from collections.abc import Callable, Iterable, MutableMapping
from collections.abc import MutableMapping as MutableMappingABC
from pathlib import Path
from typing import TYPE_CHECKING, Any, TypedDict, cast
if TYPE_CHECKING:
    from typing_extensions import NotRequired
EnvType = MutableMapping[(str, Any)]

class OptionsType(TypedDict):
    store_labels: 'NotRequired[bool]' = 'Options for parsing.'


class PresetType(TypedDict):
    components: 'MutableMapping[str, MutableMapping[str, list[str]]]' = 'Preset configuration for markdown-it.'


class OptionsDict(MutableMappingABC):
    '''A dictionary, with attribute access to core markdownit configuration options.'''
    
    def __init__(self = None, options = None):
        self._options = cast(OptionsType, dict(options))

    
    def __getitem__(self = None, key = None):
        return self._options[key]

    
    def __setitem__(self = None, key = None, value = None):
        self._options[key] = value

    
    def __delitem__(self = None, key = None):
        del self._options[key]

    
    def __iter__(self = None):
        return iter(self._options)

    
    def __len__(self = None):
        return len(self._options)

    
    def __repr__(self = None):
        return repr(self._options)

    
    def __str__(self = None):
        return str(self._options)

    maxNesting = (lambda self = None: self._options['maxNesting'])()
    maxNesting = (lambda self = None, value = None: self._options['maxNesting'] = value)()
    html = (lambda self = None: self._options['html'])()
    html = (lambda self = None, value = None: self._options['html'] = value)()
    linkify = (lambda self = None: self._options['linkify'])()
    linkify = (lambda self = None, value = None: self._options['linkify'] = value)()
    typographer = (lambda self = None: self._options['typographer'])()
    typographer = (lambda self = None, value = None: self._options['typographer'] = value)()
    quotes = (lambda self = None: self._options['quotes'])()
    quotes = (lambda self = None, value = None: self._options['quotes'] = value)()
    xhtmlOut = (lambda self = None: self._options['xhtmlOut'])()
    xhtmlOut = (lambda self = None, value = None: self._options['xhtmlOut'] = value)()
    breaks = (lambda self = None: self._options['breaks'])()
    breaks = (lambda self = None, value = None: self._options['breaks'] = value)()
    langPrefix = (lambda self = None: self._options['langPrefix'])()
    langPrefix = (lambda self = None, value = None: self._options['langPrefix'] = value)()
    highlight = (lambda self = None: self._options['highlight'])()
    highlight = (lambda self = None, value = None: self._options['highlight'] = value)()


def read_fixture_file(path = None):
    text = Path(path).read_text(encoding = 'utf-8')
    tests = []
    section = 0
    last_pos = 0
    lines = text.splitlines(keepends = True)
    for i in range(len(lines)):
        if lines[i].rstrip() == '.':
            if section == 0:
                tests.append([
                    i,
                    lines[i - 1].strip()])
                section = 1
            elif section == 1:
                tests[-1].append(''.join(lines[last_pos + 1:i]))
                section = 2
            elif section == 2:
                tests[-1].append(''.join(lines[last_pos + 1:i]))
                section = 0
            last_pos = i
        return tests

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _attrs.pyc (Python 3.11)

import sys
import struct
from typing import Dict, Type
from mutagen._util import total_ordering, reraise
from _util import ASFError

class ASFBaseAttribute(object):
    TYPE: int = 'Generic attribute.'
    _TYPES: 'Dict[int, Type[ASFBaseAttribute]]' = { }
    value = None
    language = None
    stream = None
    
    def __init__(self, value, data, language, stream = (None, None, None, None), **kwargs):
        self.language = language
        self.stream = stream
    # WARNING: Decompyle incomplete

    _register = (lambda cls, other: cls._TYPES[other.TYPE] = otherother)()
    _get_type = (lambda cls, type_: cls._TYPES[type_])()
    
    def _validate(self, value):
        """Raises TypeError or ValueError in case the user supplied value
        isn't valid.
        """
        return value

    
    def data_size(self):
        raise NotImplementedError

    
    def __repr__(self):
        name = f'''{type(self).__name__!s}({self.value!r}'''
        if self.language:
            name += ', language=%d' % self.language
        if self.stream:
            name += ', stream=%d' % self.stream
        name += ')'
        return name

    
    def render(self, name):
        name = name.encode('utf-16-le') + b'\x00\x00'
        data = self._render()
        return struct.pack('<H', len(name)) + name + struct.pack('<HH', self.TYPE, len(data)) + data

    
    def render_m(self, name):

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: legacy.pyc (Python 3.11)

from __future__ import annotations
from typing import TYPE_CHECKING, Any
from warnings import warn
from api import from_bytes
from constant import CHARDET_CORRESPONDENCE, TOO_SMALL_SEQUENCE
if TYPE_CHECKING:
    from typing_extensions import TypedDict
    
    class ResultDict(TypedDict):
        confidence: 'float | None' = 'ResultDict'


def detect(byte_str = None, should_rename_legacy = None, **kwargs):
    '''
    chardet legacy method
    Detect the encoding of the given byte string. It should be mostly backward-compatible.
    Encoding name will match Chardet own writing whenever possible. (Not on encoding name unsupported by it)
    This function is deprecated and should be used to migrate your project easily, consult the documentation for
    further information. Not planned for removal.

    :param byte_str:     The byte sequence to examine.
    :param should_rename_legacy:  Should we rename legacy encodings
                                  to their more modern equivalents?
    '''
    if len(kwargs):
        warn(f'''charset-normalizer disregard arguments \'{','.join(list(kwargs.keys()))}\' in legacy function detect()''')
    if not isinstance(byte_str, (bytearray, bytes)):
        raise TypeError(f'''Expected object of type bytes or bytearray, got: {type(byte_str)}''')
    if isinstance(byte_str, bytearray):
        byte_str = bytes(byte_str)
    r = from_bytes(byte_str).best()
# WARNING: Decompyle incomplete

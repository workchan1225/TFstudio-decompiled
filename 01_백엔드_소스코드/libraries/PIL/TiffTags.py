# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: TiffTags.pyc (Python 3.11)

from __future__ import annotations
from typing import NamedTuple

class _TagInfo(NamedTuple):
    enum: 'dict[str, int]' = '_TagInfo'


class TagInfo(_TagInfo):
    pass
# WARNING: Decompyle incomplete


def lookup(tag = None, group = None):
    '''
    :param tag: Integer tag number
    :param group: Which :py:data:`~PIL.TiffTags.TAGS_V2_GROUPS` to look in

    .. versionadded:: 8.3.0

    :returns: Taginfo namedtuple, From the ``TAGS_V2`` info if possible,
        otherwise just populating the value and name from ``TAGS``.
        If the tag is not recognized, "unknown" is returned for the name

    '''
    pass
# WARNING: Decompyle incomplete

BYTE = 1
ASCII = 2
SHORT = 3
LONG = 4
RATIONAL = 5
SIGNED_BYTE = 6
UNDEFINED = 7
SIGNED_SHORT = 8
SIGNED_LONG = 9
SIGNED_RATIONAL = 10
FLOAT = 11
DOUBLE = 12
IFD = 13
LONG8 = 16
# WARNING: Decompyle incomplete

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _tags.pyc (Python 3.11)

import re
import struct
from itertools import zip_longest
from mutagen._tags import Tags
from mutagen._util import DictProxy, convert_error, read_full
from _util import BitPaddedInt, unsynch, ID3JunkFrameError, ID3EncryptionUnsupportedError, is_valid_frame_id, error, ID3NoHeaderError, ID3UnsupportedVersionError, ID3SaveConfig
from _frames import TDRC, APIC, TDOR, TIME, TIPL, TORY, TDAT, Frames_2_2, TextFrame, TYER, Frame, IPLS, Frames

class ID3Header(object):
    _V24 = (2, 4, 0)
    _V23 = (2, 3, 0)
    _V22 = (2, 2, 0)
    _V11 = (1, 1)
    f_unsynch = property((lambda s: bool(s._flags & 128)))
    f_extended = property((lambda s: bool(s._flags & 64)))
    f_experimental = property((lambda s: bool(s._flags & 32)))
    f_footer = property((lambda s: bool(s._flags & 16)))
    _known_frames = None
    known_frames = (lambda self: pass# WARNING: Decompyle incomplete
)()
    __init__ = (lambda self, fileobj = (None,): pass# WARNING: Decompyle incomplete
)()


def determine_bpi(data, frames, EMPTY = (b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',)):
    '''Takes id3v2.4 frame data and determines if ints or bitpaddedints
    should be used for parsing. Needed because iTunes used to write
    normal ints for frame sizes.
    '''
    o = 0
    asbpi = 0
# WARNING: Decompyle incomplete


class ID3Tags(Tags, DictProxy):
    pass
# WARNING: Decompyle incomplete


def save_frame(frame, name, config = (None, None)):
    pass
# WARNING: Decompyle incomplete


def read_frames(id3, data, frames):
    '''Does not error out'''
    pass
# WARNING: Decompyle incomplete

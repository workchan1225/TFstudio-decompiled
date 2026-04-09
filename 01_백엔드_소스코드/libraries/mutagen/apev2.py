# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: apev2.pyc (Python 3.11)

"""APEv2 reading and writing.

The APEv2 format is most commonly used with Musepack files, but is
also the format of choice for WavPack and other formats. Some MP3s
also have APEv2 tags, but this can cause problems with many MP3
decoders and taggers.

APEv2 tags, like Vorbis comments, are freeform key=value pairs. APEv2
keys can be any ASCII string with characters from 0x20 to 0x7E,
between 2 and 255 characters long.  Keys are case-sensitive, but
readers are recommended to be case insensitive, and it is forbidden to
multiple keys which differ only in case.  Keys are usually stored
title-cased (e.g. 'Artist' rather than 'artist').

APEv2 values are slightly more structured than Vorbis comments; values
are flagged as one of text, binary, or an external reference (usually
a URI).

Based off the format specification found at
http://wiki.hydrogenaudio.org/index.php?title=APEv2_specification.
"""
__all__ = [
    'APEv2',
    'APEv2File',
    'Open',
    'delete']
import sys
import struct
from io import BytesIO
from collections.abc import MutableSequence
from mutagen import Metadata, FileType, StreamInfo
from mutagen._util import DictMixin, cdata, delete_bytes, total_ordering, MutagenError, loadfile, convert_error, seek_end, get_size, reraise

def is_valid_apev2_key(key):

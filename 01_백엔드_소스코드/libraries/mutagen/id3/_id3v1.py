# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _id3v1.pyc (Python 3.11)

import errno
from struct import error as StructError, unpack
from mutagen._util import bchr
from _frames import TCON, TRCK, COMM, TDRC, TYER, TALB, TPE1, TIT2

def find_id3v1(fileobj, v2_version, known_frames = (4, None)):
    '''Returns a tuple of (id3tag, offset_to_end) or (None, 0)

    offset mainly because we used to write too short tags in some cases and
    we need the offset to delete them.

    v2_version: Decides whether ID3v2.3 or ID3v2.4 tags
                should be returned. Must be 3 or 4.

    known_frames (Dict[`mutagen.text`, `Frame`]): dict mapping frame
        IDs to Frame objects
    '''
    if v2_version not in (3, 4):
        raise ValueError('Only 3 and 4 possible for v2_version')
    extra_read = b'APETAGEX'.index(b'TAG')
    old_pos = fileobj.tell()
    
    try:
        fileobj.seek(-128 - extra_read, 2)
    except IOError:
        e = None
        if e.errno == errno.EINVAL:
            fileobj.seek(0, 0)
        else:
            raise 
        e = None
        del e
    except:
        e = None
        del e

    data = fileobj.read(128 + extra_read)
    fileobj.seek(old_pos, 0)
# WARNING: Decompyle incomplete


def ParseID3v1(data, v2_version, known_frames = (4, None)):

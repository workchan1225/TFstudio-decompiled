# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''MPEG audio stream information and tags.'''
import struct
from mutagen import StreamInfo
from mutagen._util import MutagenError, enum, BitReader, BitReaderError, convert_error, intround, endswith
from mutagen.id3 import ID3FileType, delete
from mutagen.id3._util import BitPaddedInt
from _util import XingHeader, XingHeaderError, VBRIHeader, VBRIHeaderError
__all__ = [
    'MP3',
    'Open',
    'delete',
    'MP3']

class error(MutagenError):
    pass


class HeaderNotFoundError(error):
    pass


class InvalidMPEGHeader(error):
    pass

BitrateMode = <NODE:12>()

def _guess_xing_bitrate_mode(xing):

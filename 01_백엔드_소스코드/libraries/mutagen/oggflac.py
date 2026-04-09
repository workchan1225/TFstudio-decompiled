# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: oggflac.pyc (Python 3.11)

"""Read and write Ogg FLAC comments.

This module handles FLAC files wrapped in an Ogg bitstream. The first
FLAC stream found is used. For 'naked' FLACs, see mutagen.flac.

This module is based off the specification at
http://flac.sourceforge.net/ogg_mapping.html.
"""
__all__ = [
    'OggFLAC',
    'Open',
    'delete']
import struct
from io import BytesIO
from mutagen import StreamInfo
from mutagen.flac import StreamInfo as FLACStreamInfo, error as FLACError
from mutagen._vorbis import VCommentDict
from mutagen._util import loadfile, convert_error
from mutagen.ogg import OggPage, OggFileType, error as OggError

class error(OggError):
    pass


class OggFLACHeaderError(error):
    pass


class OggFLACStreamInfo(StreamInfo):
    '''OggFLACStreamInfo()

    Ogg FLAC stream info.

    Attributes:
        length (`float`): File length in seconds, as a float
        channels (`float`): Number of channels
        sample_rate (`int`): Sample rate in Hz"
    '''
    length = 0
    channels = 0
    sample_rate = 0
    
    def __init__(self, fileobj):
        page = OggPage(fileobj)
    # WARNING: Decompyle incomplete

    
    def _post_tags(self, fileobj):
        if self.length:
            return None
        page = None.find_last(fileobj, self.serial, finishing = True)
    # WARNING: Decompyle incomplete

    
    def pprint(self):
        return 'Ogg FLAC, %.2f seconds, %d Hz' % (self.length, self.sample_rate)



class OggFLACVComment(VCommentDict):
    pass
# WARNING: Decompyle incomplete


class OggFLAC(OggFileType):
    '''OggFLAC(filething)

    An Ogg FLAC file.

    Arguments:
        filething (filething)

    Attributes:
        info (`OggFLACStreamInfo`)
        tags (`mutagen._vorbis.VCommentDict`)
    '''
    _Info = OggFLACStreamInfo
    _Tags = OggFLACVComment
    _Error = OggFLACHeaderError
    _mimes = [
        'audio/x-oggflac']
    info = None
    tags = None
    score = (lambda filename, fileobj, header: header.startswith(b'OggS') * ((b'FLAC' in header) + (b'fLaC' in header)))()

Open = OggFLAC
delete = (lambda filething: t = OggFLAC(filething)filething.fileobj.seek(0)t.delete(filething))()()

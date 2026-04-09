# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: oggopus.pyc (Python 3.11)

'''Read and write Ogg Opus comments.

This module handles Opus files wrapped in an Ogg bitstream. The
first Opus stream found is used.

Based on http://tools.ietf.org/html/draft-terriberry-oggopus-01
'''
__all__ = [
    'OggOpus',
    'Open',
    'delete']
import struct
from io import BytesIO
from mutagen import StreamInfo
from mutagen._util import get_size, loadfile, convert_error
from mutagen._tags import PaddingInfo
from mutagen._vorbis import VCommentDict
from mutagen.ogg import OggPage, OggFileType, error as OggError

class error(OggError):
    pass


class OggOpusHeaderError(error):
    pass


class OggOpusInfo(StreamInfo):
    '''OggOpusInfo()

    Ogg Opus stream information.

    Attributes:
        length (`float`): File length in seconds, as a float
        channels (`int`): Number of channels
    '''
    length = 0
    channels = 0
    
    def __init__(self, fileobj):
        page = OggPage(fileobj)
    # WARNING: Decompyle incomplete

    
    def _post_tags(self, fileobj):
        page = OggPage.find_last(fileobj, self.serial, finishing = True)
    # WARNING: Decompyle incomplete

    
    def pprint(self):
        return 'Ogg Opus, %.2f seconds' % self.length



class OggOpusVComment(VCommentDict):
    pass
# WARNING: Decompyle incomplete


class OggOpus(OggFileType):
    '''OggOpus(filething)

    An Ogg Opus file.

    Arguments:
        filething (filething)

    Attributes:
        info (`OggOpusInfo`)
        tags (`mutagen._vorbis.VCommentDict`)

    '''
    _Info = OggOpusInfo
    _Tags = OggOpusVComment
    _Error = OggOpusHeaderError
    _mimes = [
        'audio/ogg',
        'audio/ogg; codecs=opus']
    info = None
    tags = None
    score = (lambda filename, fileobj, header: header.startswith(b'OggS') * (b'OpusHead' in header))()

Open = OggOpus
delete = (lambda filething: t = OggOpus(filething)filething.fileobj.seek(0)t.delete(filething))()()

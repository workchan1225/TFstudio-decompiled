# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: oggtheora.pyc (Python 3.11)

'''Read and write Ogg Theora comments.

This module handles Theora files wrapped in an Ogg bitstream. The
first Theora stream found is used.

Based on the specification at http://theora.org/doc/Theora_I_spec.pdf.
'''
__all__ = [
    'OggTheora',
    'Open',
    'delete']
import struct
from mutagen import StreamInfo
from mutagen._vorbis import VCommentDict
from mutagen._util import cdata, get_size, loadfile, convert_error
from mutagen._tags import PaddingInfo
from mutagen.ogg import OggPage, OggFileType, error as OggError

class error(OggError):
    pass


class OggTheoraHeaderError(error):
    pass


class OggTheoraInfo(StreamInfo):
    '''OggTheoraInfo()

    Ogg Theora stream information.

    Attributes:
        length (`float`): File length in seconds, as a float
        fps (`float`): Video frames per second, as a float
        bitrate (`int`): Bitrate in bps (int)
    '''
    length = 0
    fps = 0
    bitrate = 0
    
    def __init__(self, fileobj):
        page = OggPage(fileobj)
    # WARNING: Decompyle incomplete

    
    def _post_tags(self, fileobj):
        page = OggPage.find_last(fileobj, self.serial, finishing = True)
    # WARNING: Decompyle incomplete

    
    def pprint(self):
        return 'Ogg Theora, %.2f seconds, %d bps' % (self.length, self.bitrate)



class OggTheoraCommentDict(VCommentDict):
    pass
# WARNING: Decompyle incomplete


class OggTheora(OggFileType):
    '''OggTheora(filething)

    An Ogg Theora file.

    Arguments:
        filething (filething)

    Attributes:
        info (`OggTheoraInfo`)
        tags (`mutagen._vorbis.VCommentDict`)
    '''
    _Info = OggTheoraInfo
    _Tags = OggTheoraCommentDict
    _Error = OggTheoraHeaderError
    _mimes = [
        'video/x-theora']
    info = None
    tags = None
    score = (lambda filename, fileobj, header: header.startswith(b'OggS') * ((b'\x80theora' in header) + (b'\x81theora' in header)) * 2)()

Open = OggTheora
delete = (lambda filething: t = OggTheora(filething)filething.fileobj.seek(0)t.delete(filething))()()

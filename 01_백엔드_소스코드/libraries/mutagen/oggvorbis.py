# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: oggvorbis.pyc (Python 3.11)

'''Read and write Ogg Vorbis comments.

This module handles Vorbis files wrapped in an Ogg bitstream. The
first Vorbis stream found is used.

Read more about Ogg Vorbis at http://vorbis.com/. This module is based
on the specification at http://www.xiph.org/vorbis/doc/Vorbis_I_spec.html.
'''
__all__ = [
    'OggVorbis',
    'Open',
    'delete']
import struct
from mutagen import StreamInfo
from mutagen._vorbis import VCommentDict
from mutagen._util import get_size, loadfile, convert_error
from mutagen._tags import PaddingInfo
from mutagen.ogg import OggPage, OggFileType, error as OggError

class error(OggError):
    pass


class OggVorbisHeaderError(error):
    pass


class OggVorbisInfo(StreamInfo):
    """OggVorbisInfo()

    Ogg Vorbis stream information.

    Attributes:
        length (`float`): File length in seconds, as a float
        channels (`int`): Number of channels
        bitrate (`int`): Nominal ('average') bitrate in bits per second
        sample_rate (`int`): Sample rate in Hz

    """
    length = 0
    channels = 0
    bitrate = 0
    sample_rate = 0
    
    def __init__(self, fileobj):
        '''Raises ogg.error, IOError'''
        page = OggPage(fileobj)
        if not page.packets:
            raise OggVorbisHeaderError('page has not packets')
    # WARNING: Decompyle incomplete

    
    def _post_tags(self, fileobj):
        '''Raises ogg.error'''
        page = OggPage.find_last(fileobj, self.serial, finishing = True)
    # WARNING: Decompyle incomplete

    
    def pprint(self):
        return 'Ogg Vorbis, %.2f seconds, %d bps' % (self.length, self.bitrate)



class OggVCommentDict(VCommentDict):
    pass
# WARNING: Decompyle incomplete


class OggVorbis(OggFileType):
    '''OggVorbis(filething)

    Arguments:
        filething (filething)

    An Ogg Vorbis file.

    Attributes:
        info (`OggVorbisInfo`)
        tags (`mutagen._vorbis.VCommentDict`)
    '''
    _Info = OggVorbisInfo
    _Tags = OggVCommentDict
    _Error = OggVorbisHeaderError
    _mimes = [
        'audio/vorbis',
        'audio/x-vorbis']
    info = None
    tags = None
    score = (lambda filename, fileobj, header: header.startswith(b'OggS') * (b'\x01vorbis' in header))()

Open = OggVorbis
delete = (lambda filething: t = OggVorbis(filething)filething.fileobj.seek(0)t.delete(filething))()()

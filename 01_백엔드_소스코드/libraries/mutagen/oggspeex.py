# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: oggspeex.pyc (Python 3.11)

'''Read and write Ogg Speex comments.

This module handles Speex files wrapped in an Ogg bitstream. The
first Speex stream found is used.

Read more about Ogg Speex at http://www.speex.org/. This module is
based on the specification at http://www.speex.org/manual2/node7.html
and clarifications after personal communication with Jean-Marc,
http://lists.xiph.org/pipermail/speex-dev/2006-July/004676.html.
'''
__all__ = [
    'OggSpeex',
    'Open',
    'delete']
from mutagen import StreamInfo
from mutagen._vorbis import VCommentDict
from mutagen.ogg import OggPage, OggFileType, error as OggError
from mutagen._util import cdata, get_size, loadfile, convert_error
from mutagen._tags import PaddingInfo

class error(OggError):
    pass


class OggSpeexHeaderError(error):
    pass


class OggSpeexInfo(StreamInfo):
    '''OggSpeexInfo()

    Ogg Speex stream information.

    Attributes:
        length (`float`): file length in seconds, as a float
        channels (`int`): number of channels
        bitrate (`int`): nominal bitrate in bits per second. The reference
            encoder does not set the bitrate; in this case, the bitrate will
            be 0.
    '''
    length = 0
    channels = 0
    bitrate = 0
    
    def __init__(self, fileobj):
        page = OggPage(fileobj)
    # WARNING: Decompyle incomplete

    
    def _post_tags(self, fileobj):
        page = OggPage.find_last(fileobj, self.serial, finishing = True)
    # WARNING: Decompyle incomplete

    
    def pprint(self):
        return 'Ogg Speex, %.2f seconds' % self.length



class OggSpeexVComment(VCommentDict):
    pass
# WARNING: Decompyle incomplete


class OggSpeex(OggFileType):
    '''OggSpeex(filething)

    An Ogg Speex file.

    Arguments:
        filething (filething)

    Attributes:
        info (`OggSpeexInfo`)
        tags (`mutagen._vorbis.VCommentDict`)
    '''
    _Info = OggSpeexInfo
    _Tags = OggSpeexVComment
    _Error = OggSpeexHeaderError
    _mimes = [
        'audio/x-speex']
    info = None
    tags = None
    score = (lambda filename, fileobj, header: header.startswith(b'OggS') * (b'Speex   ' in header))()

Open = OggSpeex
delete = (lambda filething: t = OggSpeex(filething)filething.fileobj.seek(0)t.delete(filething))()()

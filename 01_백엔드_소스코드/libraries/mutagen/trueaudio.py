# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: trueaudio.pyc (Python 3.11)

'''True Audio audio stream information and tags.

True Audio is a lossless format designed for real-time encoding and
decoding. This module is based on the documentation at
http://tausoft.org/wiki/True_Audio_Codec_Format

True Audio files use ID3 tags.
'''
__all__ = [
    'TrueAudio',
    'Open',
    'delete',
    'EasyTrueAudio']
from mutagen import StreamInfo
from mutagen.id3 import ID3FileType, delete
from mutagen._util import cdata, MutagenError, convert_error, endswith

class error(MutagenError):
    pass


class TrueAudioHeaderError(error):
    pass


class TrueAudioInfo(StreamInfo):
    '''TrueAudioInfo()

    True Audio stream information.

    Attributes:
        length (`float`): audio length, in seconds
        sample_rate (`int`): audio sample rate, in Hz
    '''
    __init__ = (lambda self, fileobj, offset:

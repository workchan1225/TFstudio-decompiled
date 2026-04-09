# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''Read and write ASF (Window Media Audio) files.'''
__all__ = [
    'ASF',
    'Open']
from mutagen import FileType, Tags, StreamInfo
from mutagen._util import resize_bytes, DictMixin, loadfile, convert_error
from _util import error, ASFError, ASFHeaderError
from _objects import HeaderObject, MetadataLibraryObject, MetadataObject, ExtendedContentDescriptionObject, HeaderExtensionObject, ContentDescriptionObject
from _attrs import ASFGUIDAttribute, ASFWordAttribute, ASFQWordAttribute, ASFDWordAttribute, ASFBoolAttribute, ASFByteArrayAttribute, ASFUnicodeAttribute, ASFBaseAttribute, ASFValue
(error, ASFError, ASFHeaderError, ASFValue)

class ASFInfo(StreamInfo):
    '''ASFInfo()

    ASF stream information.

    Attributes:
        length (`float`): "Length in seconds
        sample_rate (`int`): Sample rate in Hz
        bitrate (`int`): Bitrate in bps
        channels (`int`): Number of channels
        codec_type (`mutagen.text`): Name of the codec type of the first
            audio stream or an empty string if unknown. Example:
            ``Windows Media Audio 9 Standard``
        codec_name (`mutagen.text`): Name and maybe version of the codec used.
            Example: ``Windows Media Audio 9.1``
        codec_description (`mutagen.text`): Further information on the codec
            used. Example: ``64 kbps, 48 kHz, stereo 2-pass CBR``
    '''
    length = 0
    sample_rate = 0
    bitrate = 0
    channels = 0
    codec_type = ''
    codec_name = ''
    codec_description = ''
    
    def __init__(self):
        self.length = 0
        self.sample_rate = 0
        self.bitrate = 0
        self.channels = 0
        self.codec_type = ''
        self.codec_name = ''
        self.codec_description = ''

    
    def pprint(self):

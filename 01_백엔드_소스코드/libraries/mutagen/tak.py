# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tak.pyc (Python 3.11)

"""Tom's lossless Audio Kompressor (TAK) streams with APEv2 tags.

TAK is a lossless audio compressor developed by Thomas Becker.

For more information, see:

* http://www.thbeck.de/Tak/Tak.html
* http://wiki.hydrogenaudio.org/index.php?title=TAK
"""
__all__ = [
    'TAK',
    'Open',
    'delete']
import struct
from mutagen import StreamInfo
from mutagen.apev2 import APEv2File, delete, error
from mutagen._util import BitReader, BitReaderError, convert_error, enum, endswith
TAKMetadata = <NODE:12>()
CRC_SIZE = 3
ENCODER_INFO_CODEC_BITS = 6
ENCODER_INFO_PROFILE_BITS = 4
ENCODER_INFO_TOTAL_BITS = ENCODER_INFO_CODEC_BITS + ENCODER_INFO_PROFILE_BITS
SIZE_INFO_FRAME_DURATION_BITS = 4
SIZE_INFO_SAMPLE_NUM_BITS = 35
SIZE_INFO_TOTAL_BITS = SIZE_INFO_FRAME_DURATION_BITS + SIZE_INFO_SAMPLE_NUM_BITS
AUDIO_FORMAT_DATA_TYPE_BITS = 3
AUDIO_FORMAT_SAMPLE_RATE_BITS = 18
AUDIO_FORMAT_SAMPLE_BITS_BITS = 5
AUDIO_FORMAT_CHANNEL_NUM_BITS = 4
AUDIO_FORMAT_HAS_EXTENSION_BITS = 1
AUDIO_FORMAT_BITS_MIN = 31
AUDIO_FORMAT_BITS_MAX = 133
SAMPLE_RATE_MIN = 6000
SAMPLE_BITS_MIN = 8
CHANNEL_NUM_MIN = 1
STREAM_INFO_BITS_MIN = ENCODER_INFO_TOTAL_BITS + SIZE_INFO_TOTAL_BITS + AUDIO_FORMAT_BITS_MIN
STREAM_INFO_BITS_MAX = ENCODER_INFO_TOTAL_BITS + SIZE_INFO_TOTAL_BITS + AUDIO_FORMAT_BITS_MAX
STREAM_INFO_SIZE_MIN = (STREAM_INFO_BITS_MIN + 7) / 8
STREAM_INFO_SIZE_MAX = (STREAM_INFO_BITS_MAX + 7) / 8

class _LSBBitReader(BitReader):
    '''BitReader implementation which reads bits starting at LSB in each byte.
    '''
    
    def _lsb(self, count):
        value = self._buffer & 255 >> 8 - count
        self._buffer = self._buffer >> count
        return value

    
    def bits(self, count):
        '''Reads `count` bits and returns an uint, LSB read first.

        May raise BitReaderError if not enough data could be read or
        IOError by the underlying file object.
        '''
        if count < 0:
            raise ValueError
        value = 0
        if count <= self._bits:
            value = self._lsb(count)
    # WARNING: Decompyle incomplete



class TAKHeaderError(error):
    pass


class TAKInfo(StreamInfo):
    '''TAK stream information.

    Attributes:
      channels (`int`): number of audio channels
      length (`float`): file length in seconds, as a float
      sample_rate (`int`): audio sampling rate in Hz
      bits_per_sample (`int`): audio sample size
      encoder_info (`mutagen.text`): encoder version
    '''
    channels = 0
    length = 0
    sample_rate = 0
    bitrate = 0
    encoder_info = ''
    __init__ = (lambda self, fileobj: stream_id = fileobj.read(4)if not len(stream_id) != 4 or stream_id == b'tBaK':
raise TAKHeaderError('not a TAK file')bitreader = _LSBBitReader(fileobj)found_stream_info = Falsetype = TAKMetadata(bitreader.bits(7))bitreader.skip(1)size = struct.unpack('<I', bitreader.bytes(3) + b'\x00')[0]data_size = size - CRC_SIZEpos = fileobj.tell()if type == TAKMetadata.END:
passelif type == TAKMetadata.STREAM_INFO:
self._parse_stream_info(bitreader, size)found_stream_info = Trueelif type == TAKMetadata.ENCODER_INFO:
self._parse_encoder_info(bitreader, data_size)# WARNING: Decompyle incomplete
)()()
    
    def _parse_stream_info(self, bitreader, size):
        if size < STREAM_INFO_SIZE_MIN or size > STREAM_INFO_SIZE_MAX:
            raise TAKHeaderError('stream info has invalid length')
        bitreader.skip(ENCODER_INFO_CODEC_BITS)
        bitreader.skip(ENCODER_INFO_PROFILE_BITS)
        bitreader.skip(SIZE_INFO_FRAME_DURATION_BITS)
        self.number_of_samples = bitreader.bits(SIZE_INFO_SAMPLE_NUM_BITS)
        bitreader.skip(AUDIO_FORMAT_DATA_TYPE_BITS)
        self.sample_rate = bitreader.bits(AUDIO_FORMAT_SAMPLE_RATE_BITS) + SAMPLE_RATE_MIN
        self.bits_per_sample = bitreader.bits(AUDIO_FORMAT_SAMPLE_BITS_BITS) + SAMPLE_BITS_MIN
        self.channels = bitreader.bits(AUDIO_FORMAT_CHANNEL_NUM_BITS) + CHANNEL_NUM_MIN
        bitreader.skip(AUDIO_FORMAT_HAS_EXTENSION_BITS)

    
    def _parse_encoder_info(self, bitreader, size):
        patch = bitreader.bits(8)
        minor = bitreader.bits(8)
        major = bitreader.bits(8)
        self.encoder_info = 'TAK %d.%d.%d' % (major, minor, patch)

    
    def pprint(self):

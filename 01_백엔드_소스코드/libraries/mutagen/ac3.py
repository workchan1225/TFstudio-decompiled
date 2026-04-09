# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ac3.pyc (Python 3.11)

'''Pure AC3 file information.
'''
__all__ = [
    'AC3',
    'Open']
from mutagen import StreamInfo
from mutagen._file import FileType
from mutagen._util import BitReader, BitReaderError, MutagenError, convert_error, enum, loadfile, endswith
ChannelMode = <NODE:12>()
AC3_CHANNELS = {
    ChannelMode.C3F2R: 5,
    ChannelMode.C2F2R: 4,
    ChannelMode.C3F1R: 4,
    ChannelMode.C2F1R: 3,
    ChannelMode.C3F: 3,
    ChannelMode.STEREO: 2,
    ChannelMode.MONO: 1,
    ChannelMode.DUALMONO: 2 }
AC3_HEADER_SIZE = 7
AC3_SAMPLE_RATES = [
    48000,
    44100,
    32000]
AC3_BITRATES = [
    32,
    40,
    48,
    56,
    64,
    80,
    96,
    112,
    128,
    160,
    192,
    224,
    256,
    320,
    384,
    448,
    512,
    576,
    640]
EAC3FrameType = <NODE:12>()
EAC3_BLOCKS = [
    1,
    2,
    3,
    6]

class AC3Error(MutagenError):
    pass


class AC3Info(StreamInfo):
    '''AC3 stream information.
    The length of the stream is just a guess and might not be correct.

    Attributes:
        channels (`int`): number of audio channels
        length (`float`): file length in seconds, as a float
        sample_rate (`int`): audio sampling rate in Hz
        bitrate (`int`): audio bitrate, in bits per second
        codec (`str`): ac-3 or ec-3 (Enhanced AC-3)
    '''
    channels = 0
    length = 0
    sample_rate = 0
    bitrate = 0
    codec = 'ac-3'
    __init__ = (lambda self, fileobj: header = bytearray(fileobj.read(6))if len(header) < 6:
raise AC3Error('not enough data')if not header.startswith(b'\x0bw'):
raise AC3Error('not a AC3 file')bitstream_id = header[5] >> 3if bitstream_id > 16:
raise AC3Error('invalid bitstream_id %i' % bitstream_id)fileobj.seek(2)self._read_header(fileobj, bitstream_id))()
    
    def _read_header(self, fileobj, bitstream_id):
        bitreader = BitReader(fileobj)
        
        try:
            if bitstream_id <= 10:
                self._read_header_normal(bitreader, bitstream_id)
            else:
                self._read_header_enhanced(bitreader)
        except BitReaderError:
            e = None
            raise AC3Error(e)
            e = None
            del e

        self.length = self._guess_length(fileobj)

    
    def _read_header_normal(self, bitreader, bitstream_id):
        r = bitreader
        r.skip(16)
        sr_code = r.bits(2)
        if sr_code == 3:
            raise AC3Error('invalid sample rate code %i' % sr_code)
        frame_size_code = r.bits(6)
        if frame_size_code > 37:
            raise AC3Error('invalid frame size code %i' % frame_size_code)
        r.skip(5)
        r.skip(3)
        channel_mode = ChannelMode(r.bits(3))
        r.skip(2)
        lfe_on = r.bits(1)
        sr_shift = max(bitstream_id, 8) - 8
        
        try:
            self.sample_rate = AC3_SAMPLE_RATES[sr_code] >> sr_shift
            self.bitrate = AC3_BITRATES[frame_size_code >> 1] * 1000 >> sr_shift
        except KeyError:
            e = None
            raise AC3Error(e)
            e = None
            del e

        self.channels = self._get_channels(channel_mode, lfe_on)
        self._skip_unused_header_bits_normal(r, channel_mode)

    
    def _read_header_enhanced(self, bitreader):
        r = bitreader
        self.codec = 'ec-3'
        frame_type = r.bits(2)
        if frame_type == EAC3FrameType.RESERVED:
            raise AC3Error('invalid frame type %i' % frame_type)
        r.skip(3)
        frame_size = r.bits(11) + 1 << 1
        if frame_size < AC3_HEADER_SIZE:
            raise AC3Error('invalid frame size %i' % frame_size)
        sr_code = r.bits(2)
        
        try:
            if sr_code == 3:
                sr_code2 = r.bits(2)
                if sr_code2 == 3:
                    raise AC3Error('invalid sample rate code %i' % sr_code2)
                numblocks_code = 3
                self.sample_rate = AC3_SAMPLE_RATES[sr_code2] // 2
            else:
                numblocks_code = r.bits(2)
                self.sample_rate = AC3_SAMPLE_RATES[sr_code]
            channel_mode = ChannelMode(r.bits(3))
            lfe_on = r.bits(1)
            self.bitrate = 8 * frame_size * self.sample_rate // EAC3_BLOCKS[numblocks_code] * 256
        except KeyError:
            e = None
            raise AC3Error(e)
            e = None
            del e

        r.skip(5)
        self.channels = self._get_channels(channel_mode, lfe_on)
        self._skip_unused_header_bits_enhanced(r, frame_type, channel_mode, sr_code, numblocks_code)

    _skip_unused_header_bits_normal = (lambda bitreader, channel_mode: r = bitreaderr.skip(5)if r.bits(1):
r.skip(8)if r.bits(1):
r.skip(8)if r.bits(1):
r.skip(7)if channel_mode == ChannelMode.DUALMONO:
r.skip(5)if r.bits(1):
r.skip(8)if r.bits(1):
r.skip(8)if r.bits(1):
r.skip(7)r.skip(2)timecod1e = r.bits(1)timecod2e = r.bits(1)if timecod1e:
r.skip(14)if timecod2e:
r.skip(14)if r.bits(1):
addbsil = r.bits(6)r.skip((addbsil + 1) * 8)None)()
    _skip_unused_header_bits_enhanced = (lambda bitreader, frame_type, channel_mode, sr_code, numblocks_code: r = bitreaderr.skip(5)if r.bits(1):
r.skip(8)if channel_mode == ChannelMode.DUALMONO:
r.skip(5)if r.bits(1):
r.skip(8)if frame_type == EAC3FrameType.DEPENDENT and r.bits(1):
r.skip(16)if r.bits(1):
Noneif None.bits(1):
r.skip(5)if channel_mode == ChannelMode.STEREO:
r.skip(4)elif channel_mode >= ChannelMode.C2F2R:
r.skip(2)if r.bits(1):
r.skip(8)if channel_mode == ChannelMode.DUALMONO and r.bits(1):
r.skip(8)if sr_code < 3:
r.skip(1)if frame_type == EAC3FrameType.INDEPENDENT and numblocks_code == 3:
r.skip(1)if frame_type == EAC3FrameType.AC3_CONVERT and numblocks_code != 3 and r.bits(1):
r.skip(6)if r.bits(1):
addbsil = r.bits(6)r.skip((addbsil + 1) * 8)None)()
    _get_channels = (lambda channel_mode, lfe_on: try:
AC3_CHANNELS[channel_mode] + lfe_onexcept KeyError:
e = Noneraise AC3Error(e)e = Nonedel e)()
    
    def _guess_length(self, fileobj):
        if self.bitrate == 0:
            return None
        start = None.tell()
        fileobj.seek(0, 2)
        length = fileobj.tell() - start
        return 8 * length / self.bitrate

    
    def pprint(self):
        return '%s, %d Hz, %.2f seconds, %d channel(s), %d bps' % (self.codec, self.sample_rate, self.length, self.channels, self.bitrate)



class AC3(FileType):
    '''AC3(filething)

    Arguments:
        filething (filething)

    Load AC3 or EAC3 files.

    Tagging is not supported.
    Use the ID3/APEv2 classes directly instead.

    Attributes:
        info (`AC3Info`)
    '''
    _mimes = [
        'audio/ac3']
    load = (lambda self, filething: self.info = AC3Info(filething.fileobj))()
    
    def add_tags(self):
        raise AC3Error("doesn't support tags")

    score = (lambda filename, fileobj, header:

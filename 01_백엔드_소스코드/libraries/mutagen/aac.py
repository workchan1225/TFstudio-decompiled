# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: aac.pyc (Python 3.11)

'''
* ADTS - Audio Data Transport Stream
* ADIF - Audio Data Interchange Format
* See ISO/IEC 13818-7 / 14496-03
'''
from mutagen import StreamInfo
from mutagen._file import FileType
from mutagen._util import BitReader, BitReaderError, MutagenError, loadfile, convert_error, endswith
from mutagen.id3._util import BitPaddedInt
_FREQS = [
    96000,
    88200,
    64000,
    48000,
    44100,
    32000,
    24000,
    22050,
    16000,
    12000,
    11025,
    8000,
    7350]

class _ADTSStream(object):
    '''Represents a series of frames belonging to the same stream'''
    parsed_frames = 0
    offset = 0
    find_stream = (lambda cls, fileobj, max_bytes: r = BitReader(fileobj)stream = cls(r)if stream.sync(max_bytes):
stream.offset = (r.get_position() - 12) // 8stream)()
    
    def sync(self, max_bytes):
        '''Find the next sync.
        Returns True if found.'''
        max_bytes = max(max_bytes, 2)
        r = self._r
        r.align()
    # WARNING: Decompyle incomplete

    
    def __init__(self, r):
        '''Use _ADTSStream.find_stream to create a stream'''
        self._fixed_header_key = None
        self._r = r
        self.offset = -1
        self.parsed_frames = 0
        self._samples = 0
        self._payload = 0
        self._start = r.get_position() / 8
        self._last = self._start

    bitrate = (lambda self: pass# WARNING: Decompyle incomplete
)()
    samples = (lambda self: pass# WARNING: Decompyle incomplete
)()
    size = (lambda self: pass# WARNING: Decompyle incomplete
)()
    channels = (lambda self: pass# WARNING: Decompyle incomplete
)()
    frequency = (lambda self: pass# WARNING: Decompyle incomplete
)()
    
    def parse_frame(self):
        """True if parsing was successful.
        Fails either because the frame wasn't valid or the stream ended.
        """
        
        try:
            return self._parse_frame()
        except BitReaderError:
            return False


    
    def _parse_frame(self):
        r = self._r
        start = r.get_position() - 12
        id_ = r.bits(1)
        layer = r.bits(2)
        protection_absent = r.bits(1)
        profile = r.bits(2)
        sampling_frequency_index = r.bits(4)
        private_bit = r.bits(1)
        channel_configuration = r.bits(3)
        original_copy = r.bits(1)
        home = r.bits(1)
        fixed_header_key = (id_, layer, protection_absent, profile, sampling_frequency_index, private_bit, channel_configuration, original_copy, home)
    # WARNING: Decompyle incomplete



class ProgramConfigElement(object):
    element_instance_tag = None
    object_type = None
    sampling_frequency_index = None
    channels = None
    
    def __init__(self, r):
        '''Reads the program_config_element()

        Raises BitReaderError
        '''
        self.element_instance_tag = r.bits(4)
        self.object_type = r.bits(2)
        self.sampling_frequency_index = r.bits(4)
        num_front_channel_elements = r.bits(4)
        num_side_channel_elements = r.bits(4)
        num_back_channel_elements = r.bits(4)
        num_lfe_channel_elements = r.bits(2)
        num_assoc_data_elements = r.bits(3)
        num_valid_cc_elements = r.bits(4)
        mono_mixdown_present = r.bits(1)
        if mono_mixdown_present == 1:
            r.skip(4)
        stereo_mixdown_present = r.bits(1)
        if stereo_mixdown_present == 1:
            r.skip(4)
        matrix_mixdown_idx_present = r.bits(1)
        if matrix_mixdown_idx_present == 1:
            r.skip(3)
        elms = num_front_channel_elements + num_side_channel_elements + num_back_channel_elements
        channels = 0
        for i in range(elms):
            channels += 1
            element_is_cpe = r.bits(1)
            if element_is_cpe:
                channels += 1
            r.skip(4)
            channels += num_lfe_channel_elements
            self.channels = channels
            r.skip(4 * num_lfe_channel_elements)
            r.skip(4 * num_assoc_data_elements)
            r.skip(5 * num_valid_cc_elements)
            r.align()
            comment_field_bytes = r.bits(8)
            r.skip(8 * comment_field_bytes)
            return None



class AACError(MutagenError):
    pass


class AACInfo(StreamInfo):
    '''AACInfo()

    AAC stream information.
    The length of the stream is just a guess and might not be correct.

    Attributes:
        channels (`int`): number of audio channels
        length (`float`): file length in seconds, as a float
        sample_rate (`int`): audio sampling rate in Hz
        bitrate (`int`): audio bitrate, in bits per second
    '''
    channels = 0
    length = 0
    sample_rate = 0
    bitrate = 0
    __init__ = (lambda self, fileobj: start_offset = 0header = fileobj.read(10)if header.startswith(b'ID3'):
size = BitPaddedInt(header[6:])start_offset = size + 10fileobj.seek(start_offset)adif = fileobj.read(4)if adif == b'ADIF':
self._parse_adif(fileobj)self._type = 'ADIF'NoneNone._parse_adts(fileobj, start_offset)self._type = 'ADTS')()
    
    def _parse_adif(self, fileobj):
        r = BitReader(fileobj)
        
        try:
            copyright_id_present = r.bits(1)
            if copyright_id_present:
                r.skip(72)
            r.skip(2)
            bitstream_type = r.bits(1)
            self.bitrate = r.bits(23)
            npce = r.bits(4)
            if bitstream_type == 0:
                r.skip(20)
            pce = ProgramConfigElement(r)
            
            try:
                self.sample_rate = _FREQS[pce.sampling_frequency_index]
                
                try:
                    pass
                except IndexError:
                    
                    try:
                        pass
                    try:
                        self.channels = pce.channels
                        for i in range(npce):
                            ProgramConfigElement(r)
                            r.align()
                    except BitReaderError:
                        e = None
                        raise AACError(e)
                        e = None
                        del e
                        start = fileobj.tell()
                        fileobj.seek(0, 2)
                        length = fileobj.tell() - start
                        if self.bitrate != 0:
                            self.length = 8 * length / self.bitrate
                            return None
                        return None





    
    def _parse_adts(self, fileobj, start_offset):
        max_initial_read = 512
        max_resync_read = 10
        max_sync_tries = 10
        frames_max = 100
        frames_needed = 3
        offset = start_offset
    # WARNING: Decompyle incomplete

    
    def pprint(self):
        return 'AAC (%s), %d Hz, %.2f seconds, %d channel(s), %d bps' % (self._type, self.sample_rate, self.length, self.channels, self.bitrate)



class AAC(FileType):
    '''AAC(filething)

    Arguments:
        filething (filething)

    Load ADTS or ADIF streams containing AAC.

    Tagging is not supported.
    Use the ID3/APEv2 classes directly instead.

    Attributes:
        info (`AACInfo`)
    '''
    _mimes = [
        'audio/x-aac']
    load = (lambda self, filething: self.info = AACInfo(filething.fileobj))()
    
    def add_tags(self):
        raise AACError("doesn't support tags")

    score = (lambda filename, fileobj, header:

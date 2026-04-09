# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: wave.pyc (Python 3.11)

'''Microsoft WAVE/RIFF audio file/stream information and tags.'''
import sys
import struct
from mutagen import StreamInfo, FileType
from mutagen.id3 import ID3
from mutagen._riff import RiffFile, InvalidChunk
from mutagen._iff import error as IffError
from mutagen.id3._util import ID3NoHeaderError, error as ID3Error
from mutagen._util import convert_error, endswith, loadfile, reraise
__all__ = [
    'WAVE',
    'Open',
    'delete']

class error(IffError):
    '''WAVE stream parsing errors.'''
    pass


class _WaveFile(RiffFile):
    '''Representation of a RIFF/WAVE file'''
    
    def __init__(self, fileobj):
        RiffFile.__init__(self, fileobj)
        if self.file_type != 'WAVE':
            raise error('Expected RIFF/WAVE.')
        if 'ID3' in self:
            self['ID3'].id = 'id3'
            return None



class WaveStreamInfo(StreamInfo):
    """WaveStreamInfo()

    Microsoft WAVE file information.

    Information is parsed from the 'fmt' & 'data'chunk of the RIFF/WAVE file

    Attributes:
        length (`float`): audio length, in seconds
        bitrate (`int`): audio bitrate, in bits per second
        channels (`int`): The number of audio channels
        sample_rate (`int`): audio sample rate, in Hz
        bits_per_sample (`int`): The audio sample size
    """
    length = 0
    bitrate = 0
    channels = 0
    sample_rate = 0
    bits_per_sample = 0
    SIZE = 16
    __init__ = (lambda self, fileobj: wave_file = _WaveFile(fileobj)try:
format_chunk = wave_file['fmt']except KeyError:
e = Noneraise error(str(e))e = Nonedel edata = format_chunk.read()if len(data) < 16:
raise InvalidChunk()info = struct.unpack('<HHLLHH', data[:self.SIZE])(self.audio_format, self.channels, self.sample_rate, byte_rate, block_align, self.bits_per_sample) = infoself.bitrate = self.channels * self.bits_per_sample * self.sample_rateself._number_of_samples = 0if block_align > 0:
try:
data_chunk = wave_file['data']self._number_of_samples = data_chunk.data_size / block_alignexcept KeyError:
passif self.sample_rate > 0:
self.length = self._number_of_samples / self.sample_rateNoneNone)()
    
    def pprint(self):
        return '%d channel RIFF @ %d bps, %s Hz, %.2f seconds' % (self.channels, self.bitrate, self.sample_rate, self.length)



class _WaveID3(ID3):
    '''A Wave file with ID3v2 tags'''
    
    def _pre_load_header(self, fileobj):
        
        try:
            fileobj.seek(_WaveFile(fileobj)['id3'].data_offset)
            return None
        except (InvalidChunk, KeyError):
            raise ID3NoHeaderError('No ID3 chunk')


    save = (lambda self, filething, v1, v2_version, v23_sep, padding = (1, 4, '/', None): fileobj = filething.fileobjwave_file = _WaveFile(fileobj)if 'id3' not in wave_file:
wave_file.insert_chunk('id3')chunk = wave_file['id3']try:
data = self._prepare_data(fileobj, chunk.data_offset, chunk.data_size, v2_version, v23_sep, padding)except ID3Error:
e = Nonereraise(error, e, sys.exc_info()[2])e = Nonedel eexcept:
e = Nonedel echunk.resize(len(data))chunk.write(data))()()
    
    def delete(self, filething):
        '''Completely removes the ID3 chunk from the RIFF/WAVE file'''
        delete(filething)
        self.clear()


delete = (lambda filething: try:
_WaveFile(filething.fileobj).delete_chunk('id3')Noneexcept KeyError:
None)()()

class WAVE(FileType):
    '''WAVE(filething)

    A Waveform Audio File Format
    (WAVE, or more commonly known as WAV due to its filename extension)

    Arguments:
        filething (filething)

    Attributes:
        tags (`mutagen.id3.ID3`)
        info (`WaveStreamInfo`)
    '''
    _mimes = [
        'audio/wav',
        'audio/wave']
    score = (lambda filename, fileobj, header: filename = filename.lower()header.startswith(b'RIFF') + (header[8:12] == b'WAVE') + endswith(filename, b'.wav') + endswith(filename, b'.wave'))()
    
    def add_tags(self):
        '''Add an empty ID3 tag to the file.'''
        pass
    # WARNING: Decompyle incomplete

    load = (lambda self, filething: fileobj = filething.fileobjself.info = WaveStreamInfo(fileobj)fileobj.seek(0, 0)# WARNING: Decompyle incomplete
)()()

Open = WAVE

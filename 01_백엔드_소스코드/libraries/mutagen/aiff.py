# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: aiff.pyc (Python 3.11)

'''AIFF audio stream information and tags.'''
import struct
from struct import pack
from mutagen import StreamInfo, FileType
from mutagen.id3._util import ID3NoHeaderError, error as ID3Error
from mutagen._iff import IffChunk, IffContainerChunkMixin, IffFile, IffID3, InvalidChunk, error as IffError
from mutagen._util import convert_error, loadfile, endswith
__all__ = [
    'AIFF',
    'Open',
    'delete']

class error(IffError):
    pass

_HUGE_VAL = 1.79769e+308

def read_float(data):
    '''Raises OverflowError'''
    pass
# WARNING: Decompyle incomplete


class AIFFChunk(IffChunk):
    '''Representation of a single IFF chunk'''
    parse_header = (lambda cls, header: struct.unpack('>4sI', header))()
    get_class = (lambda cls, id: if id == 'FORM':
AIFFFormChunk)()
    
    def write_new_header(self, id_, size):
        self._fileobj.write(pack('>4sI', id_, size))

    
    def write_size(self):
        self._fileobj.write(pack('>I', self.data_size))



class AIFFFormChunk(IffContainerChunkMixin, AIFFChunk):
    '''The  AIFF root chunk.'''
    
    def parse_next_subchunk(self):
        return AIFFChunk.parse(self._fileobj, self)

    
    def __init__(self, fileobj, id, data_size, parent_chunk):
        if id != 'FORM':
            raise InvalidChunk('Expected FORM chunk, got %s' % id)
        AIFFChunk.__init__(self, fileobj, id, data_size, parent_chunk)
        self.init_container()



class AIFFFile(IffFile):
    pass
# WARNING: Decompyle incomplete


class AIFFInfo(StreamInfo):
    '''AIFFInfo()

    AIFF audio stream information.

    Information is parsed from the COMM chunk of the AIFF file

    Attributes:
        length (`float`): audio length, in seconds
        bitrate (`int`): audio bitrate, in bits per second
        channels (`int`): The number of audio channels
        sample_rate (`int`): audio sample rate, in Hz
        bits_per_sample (`int`): The audio sample size
    '''
    length = 0
    bitrate = 0
    channels = 0
    sample_rate = 0
    __init__ = (lambda self, fileobj: iff = AIFFFile(fileobj)try:
common_chunk = iff['COMM']except KeyError:
e = Noneraise error(str(e))e = Nonedel edata = common_chunk.read()if len(data) < 18:
raise errorinfo = struct.unpack('>hLh10s', data[:18])(channels, frame_count, sample_size, sample_rate) = infotry:
self.sample_rate = int(read_float(sample_rate))except OverflowError:
raise error('Invalid sample rate')if self.sample_rate < 0:
raise error('Invalid sample rate')if self.sample_rate != 0:
self.length = frame_count / float(self.sample_rate)self.bits_per_sample = sample_sizeself.sample_size = sample_sizeself.channels = channelsself.bitrate = channels * sample_size * self.sample_rate)()
    
    def pprint(self):
        return '%d channel AIFF @ %d bps, %s Hz, %.2f seconds' % (self.channels, self.bitrate, self.sample_rate, self.length)



class _IFFID3(IffID3):
    '''A AIFF file with ID3v2 tags'''
    
    def _load_file(self, fileobj):
        return AIFFFile(fileobj)


delete = (lambda filething: try:
del AIFFFile(filething.fileobj)['ID3']Noneexcept KeyError:
None)()()

class AIFF(FileType):
    '''AIFF(filething)

    An AIFF audio file.

    Arguments:
        filething (filething)

    Attributes:
        tags (`mutagen.id3.ID3`)
        info (`AIFFInfo`)
    '''
    _mimes = [
        'audio/aiff',
        'audio/x-aiff']
    score = (lambda filename, fileobj, header: filename = filename.lower()header.startswith(b'FORM') * 2 + endswith(filename, b'.aif') + endswith(filename, b'.aiff') + endswith(filename, b'.aifc'))()
    
    def add_tags(self):
        '''Add an empty ID3 tag to the file.'''
        pass
    # WARNING: Decompyle incomplete

    load = (lambda self, filething: fileobj = filething.fileobj# WARNING: Decompyle incomplete
)()()

Open = AIFF

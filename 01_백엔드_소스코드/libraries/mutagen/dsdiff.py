# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: dsdiff.pyc (Python 3.11)

'''DSDIFF audio stream information and tags.'''
import struct
from mutagen import StreamInfo
from mutagen._file import FileType
from mutagen._iff import IffChunk, IffContainerChunkMixin, IffID3, IffFile, InvalidChunk, error as IffError
from mutagen.id3._util import ID3NoHeaderError, error as ID3Error
from mutagen._util import convert_error, loadfile, endswith
__all__ = [
    'DSDIFF',
    'Open',
    'delete']

class error(IffError):
    pass


class DSDIFFChunk(IffChunk):
    '''Representation of a single DSDIFF chunk'''
    HEADER_SIZE = 12
    parse_header = (lambda cls, header: struct.unpack('>4sQ', header))()
    get_class = (lambda cls, id: if id in DSDIFFListChunk.LIST_CHUNK_IDS:
DSDIFFListChunkif None == 'DST':
DSTChunk)()
    
    def write_new_header(self, id_, size):
        self._fileobj.write(struct.pack('>4sQ', id_, size))

    
    def write_size(self):
        self._fileobj.write(struct.pack('>Q', self.data_size))



class DSDIFFListChunk(IffContainerChunkMixin, DSDIFFChunk):
    '''A DSDIFF chunk containing other chunks.
    '''
    LIST_CHUNK_IDS = [
        'FRM8',
        'PROP']
    
    def parse_next_subchunk(self):
        return DSDIFFChunk.parse(self._fileobj, self)

    
    def __init__(self, fileobj, id, data_size, parent_chunk):
        if id not in self.LIST_CHUNK_IDS:
            raise InvalidChunk('Not a list chunk: %s' % id)
        DSDIFFChunk.__init__(self, fileobj, id, data_size, parent_chunk)
        self.init_container()



class DSTChunk(IffContainerChunkMixin, DSDIFFChunk):
    '''A DSDIFF chunk containing other chunks.
    '''
    
    def parse_next_subchunk(self):
        return DSDIFFChunk.parse(self._fileobj, self)

    
    def __init__(self, fileobj, id, data_size, parent_chunk):
        if id != 'DST':
            raise InvalidChunk('Not a DST chunk: %s' % id)
        DSDIFFChunk.__init__(self, fileobj, id, data_size, parent_chunk)
        self.init_container(name_size = 0)



class DSDIFFFile(IffFile):
    pass
# WARNING: Decompyle incomplete


class DSDIFFInfo(StreamInfo):
    '''DSDIFF stream information.

    Attributes:
        channels (`int`): number of audio channels
        length (`float`): file length in seconds, as a float
        sample_rate (`int`): audio sampling rate in Hz
        bits_per_sample (`int`): audio sample size (for DSD this is always 1)
        bitrate (`int`): audio bitrate, in bits per second
        compression (`str`): DSD (uncompressed) or DST
    '''
    channels = 0
    length = 0
    sample_rate = 0
    bits_per_sample = 1
    bitrate = 0
    compression = None
    __init__ = (lambda self, fileobj: iff = DSDIFFFile(fileobj)try:
prop_chunk = iff['PROP']except KeyError:
e = Noneraise error(str(e))e = Nonedel eif prop_chunk.name == 'SND ':
for chunk in prop_chunk.subchunks():
if chunk.id == 'FS' and chunk.data_size == 4:
data = chunk.read()if len(data) < 4:
raise InvalidChunk('Not enough data in FS chunk')(self.sample_rate,) = struct.unpack('>L', data[:4])continueif chunk.id == 'CHNL' and chunk.data_size >= 2:
data = chunk.read()if len(data) < 2:
raise InvalidChunk('Not enough data in CHNL chunk')(self.channels,) = struct.unpack('>H', data[:2])continueif chunk.id == 'CMPR' and chunk.data_size >= 4:
data = chunk.read()if len(data) < 4:
raise InvalidChunk('Not enough data in CMPR chunk')(compression_id,) = struct.unpack('>4s', data[:4])self.compression = compression_id.decode('ascii').rstrip()if self.sample_rate < 0:
raise error('Invalid sample rate')if self.compression == 'DSD':
try:
dsd_chunk = iff['DSD']except KeyError:
e = Noneraise error(str(e))e = Nonedel eif not self.channels:
sample_count = dsd_chunk.data_size * 8 / 1if self.sample_rate != 0:
self.length = sample_count / float(self.sample_rate)self.bitrate = self.channels * self.bits_per_sample * self.sample_rateNoneif None.compression == 'DST':
try:
dst_frame = iff['DST']dst_frame_info = dst_frame['FRTE']except KeyError:
e = Noneraise error(str(e))e = Nonedel eif dst_frame_info.data_size >= 6:
data = dst_frame_info.read()if len(data) < 6:
raise InvalidChunk('Not enough data in FRTE chunk')(frame_count, frame_rate) = struct.unpack('>LH', data[:6])if frame_rate:
self.length = frame_count / frame_rateif frame_count:
dst_data_size = dst_frame.data_size - dst_frame_info.sizeavg_frame_size = dst_data_size / frame_countself.bitrate = avg_frame_size * 8 * frame_rateNoneNoneNoneNone)()
    
    def pprint(self):
        return '%d channel DSDIFF (%s) @ %d bps, %s Hz, %.2f seconds' % (self.channels, self.compression, self.bitrate, self.sample_rate, self.length)



class _DSDIFFID3(IffID3):
    '''A DSDIFF file with ID3v2 tags'''
    
    def _load_file(self, fileobj):
        return DSDIFFFile(fileobj)


delete = (lambda filething: try:
del DSDIFFFile(filething.fileobj)['ID3']Noneexcept KeyError:
None)()()

class DSDIFF(FileType):
    '''DSDIFF(filething)

    An DSDIFF audio file.

    For tagging ID3v2 data is added to a chunk with the ID "ID3 ".

    Arguments:
        filething (filething)

    Attributes:
        tags (`mutagen.id3.ID3`)
        info (`DSDIFFInfo`)
    '''
    _mimes = [
        'audio/x-dff']
    load = (lambda self, filething: fileobj = filething.fileobj# WARNING: Decompyle incomplete
)()()
    
    def add_tags(self):
        '''Add empty ID3 tags to the file.'''
        pass
    # WARNING: Decompyle incomplete

    score = (lambda filename, fileobj, header: header.startswith(b'FRM8') * 2 + endswith(filename, '.dff'))()

Open = DSDIFF

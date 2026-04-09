# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: dsf.pyc (Python 3.11)

'''Read and write DSF audio stream information and tags.'''
import sys
import struct
from io import BytesIO
from mutagen import FileType, StreamInfo
from mutagen._util import cdata, MutagenError, loadfile, convert_error, reraise, endswith
from mutagen.id3 import ID3
from mutagen.id3._util import ID3NoHeaderError, error as ID3Error
__all__ = [
    'DSF',
    'Open',
    'delete']

class error(MutagenError):
    pass


class DSFChunk(object):
    '''A generic chunk of a DSFFile.'''
    chunk_offset = 0
    chunk_header = '    '
    chunk_size = -1
    
    def __init__(self, fileobj, create = (False,)):
        self.fileobj = fileobj
        if not create:
            self.chunk_offset = fileobj.tell()
            self.load()
            return None

    
    def load(self):
        raise NotImplementedError

    
    def write(self):
        raise NotImplementedError



class DSDChunk(DSFChunk):
    pass
# WARNING: Decompyle incomplete


class FormatChunk(DSFChunk):
    pass
# WARNING: Decompyle incomplete


class DataChunk(DSFChunk):
    pass
# WARNING: Decompyle incomplete


class _DSFID3(ID3):
    '''A DSF file with ID3v2 tags'''
    _pre_load_header = (lambda self, fileobj: fileobj.seek(0)id3_location = DSDChunk(fileobj).offset_metdata_chunkif id3_location == 0:
raise ID3NoHeaderError('File has no existing ID3 tag')fileobj.seek(id3_location))()
    save = (lambda self, filething, v2_version, v23_sep, padding = (None, 4, '/', None): fileobj = filething.fileobjfileobj.seek(0)dsd_header = DSDChunk(fileobj)if dsd_header.offset_metdata_chunk == 0:
fileobj.seek(0, 2)dsd_header.offset_metdata_chunk = fileobj.tell()dsd_header.write()try:
data = self._prepare_data(fileobj, dsd_header.offset_metdata_chunk, self.size, v2_version, v23_sep, padding)except ID3Error:
e = Nonereraise(error, e, sys.exc_info()[2])e = Nonedel eexcept:
e = Nonedel efileobj.seek(dsd_header.offset_metdata_chunk)fileobj.write(data)fileobj.truncate()dsd_header.total_size = fileobj.tell()dsd_header.write())()()


class DSFInfo(StreamInfo):
    '''DSF audio stream information.

    Information is parsed from the fmt chunk of the DSF file.

    Attributes:
        length (`float`): audio length, in seconds.
        channels (`int`): The number of audio channels.
        sample_rate (`int`):
            Sampling frequency, in Hz.
            (2822400, 5644800, 11289600, or 22579200)
        bits_per_sample (`int`): The audio sample size.
        bitrate (`int`): The audio bitrate.
    '''
    
    def __init__(self, fmt_chunk):
        self.fmt_chunk = fmt_chunk

    length = (lambda self: float(self.fmt_chunk.sample_count) / self.sample_rate)()
    channels = (lambda self: self.fmt_chunk.channel_num)()
    sample_rate = (lambda self: self.fmt_chunk.sampling_frequency)()
    bits_per_sample = (lambda self: self.fmt_chunk.bits_per_sample)()
    bitrate = (lambda self: self.sample_rate * self.bits_per_sample * self.channels)()
    
    def pprint(self):
        return '%d channel DSF @ %d bits, %s Hz, %.2f seconds' % (self.channels, self.bits_per_sample, self.sample_rate, self.length)



class DSFFile(object):
    dsd_chunk = None
    fmt_chunk = None
    data_chunk = None
    
    def __init__(self, fileobj):
        self.dsd_chunk = DSDChunk(fileobj)
        self.fmt_chunk = FormatChunk(fileobj)
        self.data_chunk = DataChunk(fileobj)



class DSF(FileType):
    '''An DSF audio file.

    Arguments:
        filething (filething)

    Attributes:
        info (`DSFInfo`)
        tags (`mutagen.id3.ID3Tags` or `None`)
    '''
    _mimes = [
        'audio/dsf']
    score = (lambda filename, fileobj, header: header.startswith(b'DSD ') * 2 + endswith(filename.lower(), '.dsf'))()
    
    def add_tags(self):
        '''Add a DSF tag block to the file.'''
        pass
    # WARNING: Decompyle incomplete

    load = (lambda self, filething: dsf_file = DSFFile(filething.fileobj)# WARNING: Decompyle incomplete
)()()
    delete = (lambda self, filething = (None,): self.tags = Nonedelete(filething))()

delete = (lambda filething: dsf_file = DSFFile(filething.fileobj)if dsf_file.dsd_chunk.offset_metdata_chunk != 0:
id3_location = dsf_file.dsd_chunk.offset_metdata_chunkdsf_file.dsd_chunk.offset_metdata_chunk = 0dsf_file.dsd_chunk.write()filething.fileobj.seek(id3_location)filething.fileobj.truncate()None)()()
Open = DSF

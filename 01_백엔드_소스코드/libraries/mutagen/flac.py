# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: flac.pyc (Python 3.11)

'''Read and write FLAC Vorbis comments and stream information.

Read more about FLAC at http://flac.sourceforge.net.

FLAC supports arbitrary metadata blocks. The two most interesting ones
are the FLAC stream information block, and the Vorbis comment block;
these are also the only ones Mutagen can currently read.

This module does not handle Ogg FLAC files.

Based off documentation available at
http://flac.sourceforge.net/format.html
'''
__all__ = [
    'FLAC',
    'Open',
    'delete']
import struct
from io import BytesIO
from _vorbis import VCommentDict
import mutagen
from mutagen._util import resize_bytes, MutagenError, get_size, loadfile, convert_error, bchr, endswith
from mutagen._tags import PaddingInfo
from mutagen.id3._util import BitPaddedInt
from functools import reduce

class error(MutagenError):
    pass


class FLACNoHeaderError(error):
    pass


class FLACVorbisError(error, ValueError):
    pass


def to_int_be(data):
    '''Convert an arbitrarily-long string to a long using big-endian
    byte order.'''
    return reduce((lambda a, b: (a << 8) + b), bytearray(data), 0)


class StrictFileObject(object):
    """Wraps a file-like object and raises an exception if the requested
    amount of data to read isn't returned."""
    
    def __init__(self, fileobj):
        self._fileobj = fileobj
        for m in ('close', 'tell', 'seek', 'write', 'name', 'flush', 'truncate'):
            if hasattr(fileobj, m):
                setattr(self, m, getattr(fileobj, m))
            return None

    
    def read(self, size = (-1,)):
        data = self._fileobj.read(size)
        if size >= 0 and len(data) != size:
            raise error('file said %d bytes, read %d bytes' % (size, len(data)))
        return data

    
    def tryread(self, *args):
        pass
    # WARNING: Decompyle incomplete



class MetadataBlock(object):
    '''A generic block of FLAC metadata.

    This class is extended by specific used as an ancestor for more specific
    blocks, and also as a container for data blobs of unknown blocks.

    Attributes:
        data (`bytes`): raw binary data for this block
    '''
    _distrust_size = False
    _invalid_overflow_size = -1
    _MAX_SIZE = 16777215
    
    def __init__(self, data):
        '''Parse the given data string or file-like as a metadata block.
        The metadata header should not be included.'''
        pass
    # WARNING: Decompyle incomplete

    
    def load(self, data):
        self.data = data.read()

    
    def write(self):
        return self.data

    _writeblock = (lambda cls, block, is_last = (False,): data = bytearray()code = block.code | 128 if is_last else block.codedatum = block.write()size = len(datum)if size > cls._MAX_SIZE:
if block._distrust_size and block._invalid_overflow_size != -1:
size = block._invalid_overflow_sizeelse:
raise error('block is too long to write')# WARNING: Decompyle incomplete
)()
    _writeblocks = (lambda cls, blocks, available, cont_size, padding_func: data = bytearray()for block in blocks:
if isinstance(block, Padding):
continuedata += cls._writeblock(block)blockssize = len(data)padding_block = Padding()blockssize += len(cls._writeblock(padding_block))info = PaddingInfo(available - blockssize, cont_size)padding_block.length = min(info._get_padding(padding_func), cls._MAX_SIZE)data += cls._writeblock(padding_block, is_last = True)data)()


class StreamInfo(mutagen.StreamInfo, MetadataBlock):
    """StreamInfo()

    FLAC stream information.

    This contains information about the audio data in the FLAC file.
    Unlike most stream information objects in Mutagen, changes to this
    one will rewritten to the file when it is saved. Unless you are
    actually changing the audio stream itself, don't change any
    attributes of this block.

    Attributes:
        min_blocksize (`int`): minimum audio block size
        max_blocksize (`int`): maximum audio block size
        sample_rate (`int`): audio sample rate in Hz
        channels (`int`): audio channels (1 for mono, 2 for stereo)
        bits_per_sample (`int`): bits per sample
        total_samples (`int`): total samples in file
        length (`float`): audio length in seconds
        bitrate (`int`): bitrate in bits per second, as an int
    """
    code = 0
    bitrate = 0
    
    def __eq__(self, other):
        
        try:
            if self.min_blocksize == other.min_blocksize:
                if self.max_blocksize == other.max_blocksize:
                    if self.sample_rate == other.sample_rate:
                        if self.channels == other.channels:
                            if self.bits_per_sample == other.bits_per_sample:
                                return self.total_samples == other.total_samples
                            except Exception:
                                return False


    __hash__ = MetadataBlock.__hash__
    
    def load(self, data):
        self.min_blocksize = int(to_int_be(data.read(2)))
        self.max_blocksize = int(to_int_be(data.read(2)))
        self.min_framesize = int(to_int_be(data.read(3)))
        self.max_framesize = int(to_int_be(data.read(3)))
        sample_first = to_int_be(data.read(2))
        sample_channels_bps = to_int_be(data.read(1))
        bps_total = to_int_be(data.read(5))
        sample_tail = sample_channels_bps >> 4
        self.sample_rate = int((sample_first << 4) + sample_tail)
        if not self.sample_rate:
            raise error('A sample rate value of 0 is invalid')
        self.channels = int((sample_channels_bps >> 1 & 7) + 1)
        bps_tail = bps_total >> 36
        bps_head = (sample_channels_bps & 1) << 4
        self.bits_per_sample = int(bps_head + bps_tail + 1)
        self.total_samples = bps_total & 0xFFFFFFFFF
        self.length = self.total_samples / float(self.sample_rate)
        self.md5_signature = to_int_be(data.read(16))

    
    def write(self):
        f = BytesIO()
        f.write(struct.pack('>I', self.min_blocksize)[-2:])
        f.write(struct.pack('>I', self.max_blocksize)[-2:])
        f.write(struct.pack('>I', self.min_framesize)[-3:])
        f.write(struct.pack('>I', self.max_framesize)[-3:])
        f.write(struct.pack('>I', self.sample_rate >> 4)[-2:])
        byte = (self.sample_rate & 15) << 4
        byte += (self.channels - 1 & 7) << 1
        byte += self.bits_per_sample - 1 >> 4 & 1
        f.write(bchr(byte))
        byte = (self.bits_per_sample - 1 & 15) << 4
        byte += self.total_samples >> 32 & 15
        f.write(bchr(byte))
        f.write(struct.pack('>I', self.total_samples & 0xFFFFFFFF))
        sig = self.md5_signature
        f.write(struct.pack('>4I', sig >> 96 & 0xFFFFFFFF, sig >> 64 & 0xFFFFFFFF, sig >> 32 & 0xFFFFFFFF, sig & 0xFFFFFFFF))
        return f.getvalue()

    
    def pprint(self):
        return 'FLAC, %.2f seconds, %d Hz' % (self.length, self.sample_rate)



class SeekPoint(tuple):
    pass
# WARNING: Decompyle incomplete


class SeekTable(MetadataBlock):
    pass
# WARNING: Decompyle incomplete


class VCFLACDict(VCommentDict):
    pass
# WARNING: Decompyle incomplete


class CueSheetTrackIndex(tuple):
    pass
# WARNING: Decompyle incomplete


class CueSheetTrack(object):
    '''CueSheetTrack()

    A track in a cuesheet.

    For CD-DA, track_numbers must be 1-99, or 170 for the
    lead-out. Track_numbers must be unique within a cue sheet. There
    must be at least one index in every track except the lead-out track
    which must have none.

    Attributes:
        track_number (`int`): track number
        start_offset (`int`): track offset in samples from start of FLAC stream
        isrc (`mutagen.text`): ISRC code, exactly 12 characters
        type (`int`): 0 for audio, 1 for digital data
        pre_emphasis (`bool`): true if the track is recorded with pre-emphasis
        indexes (list[CueSheetTrackIndex]):
            list of CueSheetTrackIndex objects
    '''
    
    def __init__(self, track_number, start_offset, isrc, type_, pre_emphasis = ('', 0, False)):
        self.track_number = track_number
        self.start_offset = start_offset
        self.isrc = isrc
        self.type = type_
        self.pre_emphasis = pre_emphasis
        self.indexes = []

    
    def __eq__(self, other):
        
        try:
            if self.track_number == other.track_number:
                if self.start_offset == other.start_offset:
                    if self.isrc == other.isrc:
                        if self.type == other.type:
                            if self.pre_emphasis == other.pre_emphasis:
                                return self.indexes == other.indexes
                            except (AttributeError, TypeError):
                                return False


    __hash__ = object.__hash__
    
    def __repr__(self):
        return '<%s number=%r, offset=%d, isrc=%r, type=%r, pre_emphasis=%r, indexes=%r)>' % (type(self).__name__, self.track_number, self.start_offset, self.isrc, self.type, self.pre_emphasis, self.indexes)



class CueSheet(MetadataBlock):
    pass
# WARNING: Decompyle incomplete


class Picture(MetadataBlock):
    pass
# WARNING: Decompyle incomplete


class Padding(MetadataBlock):
    pass
# WARNING: Decompyle incomplete


class FLAC(mutagen.FileType):
    '''FLAC(filething)

    A FLAC audio file.

    Args:
        filething (filething)

    Attributes:
        cuesheet (`CueSheet`): if any or `None`
        seektable (`SeekTable`): if any or `None`
        pictures (list[Picture]): list of embedded pictures
        info (`StreamInfo`)
        tags (`mutagen._vorbis.VCommentDict`)
    '''
    _mimes = [
        'audio/flac',
        'audio/x-flac',
        'application/x-flac']
    tags = None
    METADATA_BLOCKS = [
        StreamInfo,
        Padding,
        None,
        SeekTable,
        VCFLACDict,
        CueSheet,
        Picture]
    score = (lambda filename, fileobj, header_data: header_data.startswith(b'fLaC') + endswith(filename.lower(), '.flac') * 3)()
    
    def __read_metadata_block(self, fileobj):
        byte = ord(fileobj.read(1))
        size = to_int_be(fileobj.read(3))
        code = byte & 127
        last_block = bool(byte & 128)
        
        try:
            if not self.METADATA_BLOCKS[code]:
                block_type = MetadataBlock
            else:
                except IndexError:
                    block_type = MetadataBlock
                if block_type._distrust_size:
                    start = fileobj.tell()
                    block = block_type(fileobj)
                    real_size = fileobj.tell() - start
                    if real_size > MetadataBlock._MAX_SIZE:
                        block._invalid_overflow_size = size
                    else:
                        data = fileobj.read(size)
                        block = block_type(data)

        block.code = code
    # WARNING: Decompyle incomplete

    
    def add_tags(self):
        '''Add a Vorbis comment block to the file.'''
        pass
    # WARNING: Decompyle incomplete

    add_vorbiscomment = add_tags
    delete = (lambda self, filething = (None,): pass# WARNING: Decompyle incomplete
)()()
    vc = property((lambda s: s.tags), doc = "Alias for tags; don't use this.")
    load = (lambda self, filething: fileobj = filething.fileobjself.metadata_blocks = []self.tags = Noneself.cuesheet = Noneself.seektable = Nonefileobj = StrictFileObject(fileobj)self.__check_header(fileobj, filething.name)# WARNING: Decompyle incomplete
)()()
    info = (lambda self: streaminfo_blocks = self.metadata_blocks()streaminfo_blocks[0])()
    
    def add_picture(self, picture):
        '''Add a new picture to the file.

        Args:
            picture (Picture)
        '''
        self.metadata_blocks.append(picture)

    
    def clear_pictures(self):
        '''Delete all pictures from the file.'''
        blocks = self.metadata_blocks()
        self.metadata_blocks = blocks

    pictures = (lambda self: self.metadata_blocks())()
    save = (lambda self, filething, deleteid3, padding = (None, False, None): if self.cuesheet and self.cuesheet not in self.metadata_blocks:
if not isinstance(self.cuesheet, CueSheet):
raise ValueError('Invalid cuesheet object type!')self.metadata_blocks.append(self.cuesheet)if self.seektable and self.seektable not in self.metadata_blocks:
if not isinstance(self.seektable, SeekTable):
raise ValueError('Invalid seektable object type!')self.metadata_blocks.append(self.seektable)self._save(filething, self.metadata_blocks, deleteid3, padding))()()
    
    def _save(self, filething, metadata_blocks, deleteid3, padding):
        f = StrictFileObject(filething.fileobj)
        header = self.__check_header(f, filething.name)
        audio_offset = self.__find_audio_offset(f)
        available = audio_offset - header
        if deleteid3 and header > 4:
            available += header - 4
            header = 4
        content_size = get_size(f) - audio_offset
    # WARNING: Decompyle incomplete

    
    def __find_audio_offset(self, fileobj):
        byte = 0
    # WARNING: Decompyle incomplete

    
    def __check_header(self, fileobj, name):
        '''Returns the offset of the flac block start
        (skipping id3 tags if found). The passed fileobj will be advanced to
        that offset as well.
        '''
        size = 4
        header = fileobj.read(4)
        if header != b'fLaC':
            size = None
            if header[:3] == b'ID3':
                size = 14 + BitPaddedInt(fileobj.read(6)[2:])
                fileobj.seek(size - 4)
                if fileobj.read(4) != b'fLaC':
                    size = None
    # WARNING: Decompyle incomplete


Open = FLAC
delete = (lambda filething: f = FLAC(filething)filething.fileobj.seek(0)f.delete(filething))()()

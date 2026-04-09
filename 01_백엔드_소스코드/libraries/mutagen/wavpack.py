# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: wavpack.pyc (Python 3.11)

'''WavPack reading and writing.

WavPack is a lossless format that uses APEv2 tags. Read

* http://www.wavpack.com/
* http://www.wavpack.com/file_format.txt

for more information.
'''
__all__ = [
    'WavPack',
    'Open',
    'delete']
from mutagen import StreamInfo
from mutagen.apev2 import APEv2File, error, delete
from mutagen._util import cdata, convert_error

class WavPackHeaderError(error):
    pass

RATES = [
    6000,
    8000,
    9600,
    11025,
    12000,
    16000,
    22050,
    24000,
    32000,
    44100,
    48000,
    64000,
    88200,
    96000,
    192000]

class _WavPackHeader(object):
    
    def __init__(self, block_size, version, track_no, index_no, total_samples, block_index, block_samples, flags, crc):
        self.block_size = block_size
        self.version = version
        self.track_no = track_no
        self.index_no = index_no
        self.total_samples = total_samples
        self.block_index = block_index
        self.block_samples = block_samples
        self.flags = flags
        self.crc = crc

    from_fileobj = (lambda cls, fileobj: header = fileobj.read(32)if not len(header) != 32 or header.startswith(b'wvpk'):
raise WavPackHeaderError('not a WavPack header: %r' % header)block_size = cdata.uint_le(header[4:8])version = cdata.ushort_le(header[8:10])track_no = ord(header[10:11])index_no = ord(header[11:12])samples = cdata.uint_le(header[12:16])if samples == 0xFFFFFFFF:
samples = -1block_index = cdata.uint_le(header[16:20])block_samples = cdata.uint_le(header[20:24])flags = cdata.uint_le(header[24:28])crc = cdata.uint_le(header[28:32])_WavPackHeader(block_size, version, track_no, index_no, samples, block_index, block_samples, flags, crc))()()


class WavPackInfo(StreamInfo):
    '''WavPack stream information.

    Attributes:
        channels (int): number of audio channels (1 or 2)
        length (float): file length in seconds, as a float
        sample_rate (int): audio sampling rate in Hz
        bits_per_sample (int): audio sample size
        version (int): WavPack stream version
    '''
    
    def __init__(self, fileobj):
        
        try:
            header = _WavPackHeader.from_fileobj(fileobj)
        except WavPackHeaderError:
            raise WavPackHeaderError('not a WavPack file')

        self.version = header.version
        if not bool(header.flags & 4):
            self.channels = 2
            self.sample_rate = RATES[header.flags >> 23 & 15]
            self.bits_per_sample = ((header.flags & 3) + 1) * 8
            if header.flags >> 31 & 1:
                1 = self, self.sample_rate *= 4, .sample_rate
        if header.total_samples == -1 or header.block_index != 0:
            samples = header.block_samples
            fileobj.seek((header.block_size - 32) + 8, 1)
            
            try:
                header = _WavPackHeader.from_fileobj(fileobj)
            except WavPackHeaderError:
                pass
            except:
                samples += header.block_samples
                continue

        else:
            samples = header.total_samples
        self.length = float(samples) / self.sample_rate

    
    def pprint(self):
        return 'WavPack, %.2f seconds, %d Hz' % (self.length, self.sample_rate)



class WavPack(APEv2File):
    '''WavPack(filething)

    Arguments:
        filething (filething)

    Attributes:
        info (`WavPackInfo`)
    '''
    _Info = WavPackInfo
    _mimes = [
        'audio/x-wavpack']
    score = (lambda filename, fileobj, header: header.startswith(b'wvpk') * 2)()

Open = WavPack

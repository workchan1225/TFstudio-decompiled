# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _as_entry.pyc (Python 3.11)

from io import BytesIO
from mutagen.aac import ProgramConfigElement
from mutagen._util import BitReader, BitReaderError, cdata
from _util import parse_full_atom
from _atom import Atom, AtomError

class ASEntryError(Exception):
    pass


class AudioSampleEntry(object):
    '''Parses an AudioSampleEntry atom.

    Private API.

    Attrs:
        channels (int): number of channels
        sample_size (int): sample size in bits
        sample_rate (int): sample rate in Hz
        bitrate (int): bits per second (0 means unknown)
        codec (string):
            audio codec, either \'mp4a[.*][.*]\' (rfc6381) or \'alac\'
        codec_description (string): descriptive codec name e.g. "AAC LC+SBR"

    Can raise ASEntryError.
    '''
    channels = 0
    sample_size = 0
    sample_rate = 0
    bitrate = 0
    codec = None
    codec_description = None
    
    def __init__(self, atom, fileobj):
        (ok, data) = atom.read(fileobj)
        if not ok:
            raise ASEntryError('too short %r atom' % atom.name)
        fileobj = BytesIO(data)
        r = BitReader(fileobj)
        
        try:
            r.skip(48)
            r.skip(16)
            r.skip(64)
            self.channels = r.bits(16)
            self.sample_size = r.bits(16)
            r.skip(16)
            r.skip(16)
            self.sample_rate = r.bits(32) >> 16
        except BitReaderError:
            e = None
            raise ASEntryError(e)
            e = None
            del e

    # WARNING: Decompyle incomplete

    
    def _parse_dac3(self, atom, fileobj):
        pass
    # WARNING: Decompyle incomplete

    
    def _parse_alac(self, atom, fileobj):
        pass
    # WARNING: Decompyle incomplete

    
    def _parse_esds(self, esds, fileobj):
        pass
    # WARNING: Decompyle incomplete



class DescriptorError(Exception):
    pass


class BaseDescriptor(object):
    TAG: int = 'BaseDescriptor'
    _parse_desc_length_file = (lambda cls, fileobj: value = 0for i in range(4):
b = cdata.uint8(fileobj.read(1))except cdata.error:
e = Noneraise ValueError(e)e = Nonedel evalue = value << 7 | b & 127if not b >> 7:
passraise ValueError('invalid descriptor length')value)()
    parse = (lambda cls, fileobj: try:
length = cls._parse_desc_length_file(fileobj)except ValueError:
e = Noneraise DescriptorError(e)e = Nonedel epos = fileobj.tell()instance = cls(fileobj, length)left = length - fileobj.tell() - posif left > 0:
fileobj.seek(left, 1)instance)()


class ES_Descriptor(BaseDescriptor):
    TAG = 3
    
    def __init__(self, fileobj, length):
        '''Raises DescriptorError'''
        r = BitReader(fileobj)
        
        try:
            self.ES_ID = r.bits(16)
            self.streamDependenceFlag = r.bits(1)
            self.URL_Flag = r.bits(1)
            self.OCRstreamFlag = r.bits(1)
            self.streamPriority = r.bits(5)
            if self.streamDependenceFlag:
                self.dependsOn_ES_ID = r.bits(16)
            if self.URL_Flag:
                URLlength = r.bits(8)
                self.URLstring = r.bytes(URLlength)
            if self.OCRstreamFlag:
                self.OCR_ES_Id = r.bits(16)
            tag = r.bits(8)
        except BitReaderError:
            e = None
            raise DescriptorError(e)
            e = None
            del e

        if tag != DecoderConfigDescriptor.TAG:
            raise DescriptorError('unexpected DecoderConfigDescrTag %d' % tag)
    # WARNING: Decompyle incomplete



class DecoderConfigDescriptor(BaseDescriptor):
    TAG = 4
    decSpecificInfo = None
    
    def __init__(self, fileobj, length):
        '''Raises DescriptorError'''
        r = BitReader(fileobj)
        
        try:
            self.objectTypeIndication = r.bits(8)
            self.streamType = r.bits(6)
            self.upStream = r.bits(1)
            self.reserved = r.bits(1)
            self.bufferSizeDB = r.bits(24)
            self.maxBitrate = r.bits(32)
            self.avgBitrate = r.bits(32)
            if (self.objectTypeIndication, self.streamType) != (64, 5):
                return None
            if None * 8 == r.get_position():
                return None
            tag = None.bits(8)
        except BitReaderError:
            e = None
            raise DescriptorError(e)
            e = None
            del e

    # WARNING: Decompyle incomplete

    codec_param = (lambda self: param = '.%X' % self.objectTypeIndicationinfo = self.decSpecificInfo# WARNING: Decompyle incomplete
)()
    codec_desc = (lambda self: info = self.decSpecificInfodesc = None# WARNING: Decompyle incomplete
)()


class DecoderSpecificInfo(BaseDescriptor):
    TAG = 5
    _TYPE_NAMES = [
        None,
        'AAC MAIN',
        'AAC LC',
        'AAC SSR',
        'AAC LTP',
        'SBR',
        'AAC scalable',
        'TwinVQ',
        'CELP',
        'HVXC',
        None,
        None,
        'TTSI',
        'Main synthetic',
        'Wavetable synthesis',
        'General MIDI',
        'Algorithmic Synthesis and Audio FX',
        'ER AAC LC',
        None,
        'ER AAC LTP',
        'ER AAC scalable',
        'ER Twin VQ',
        'ER BSAC',
        'ER AAC LD',
        'ER CELP',
        'ER HVXC',
        'ER HILN',
        'ER Parametric',
        'SSC',
        'PS',
        'MPEG Surround',
        None,
        'Layer-1',
        'Layer-2',
        'Layer-3',
        'DST',
        'ALS',
        'SLS',
        'SLS non-core',
        'ER AAC ELD',
        'SMR Simple',
        'SMR Main',
        'USAC',
        'SAOC',
        'LD MPEG Surround',
        'USAC']
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
    description = (lambda self: name = Nonetry:
name = self._TYPE_NAMES[self.audioObjectType]except IndexError:
pass# WARNING: Decompyle incomplete
)()
    sample_rate = (lambda self: if self.sbrPresentFlag == 1:
self.extensionSamplingFrequencyif None.sbrPresentFlag == 0:
self.samplingFrequencyaot_can_sbr = Noneif self.audioObjectType not in aot_can_sbr:
self.samplingFrequencyif None.samplingFrequency > 24000:
self.samplingFrequency)()
    channels = (lambda self: if hasattr(self, 'pce_channels'):
self.pce_channelsconf = None(self, 'extensionChannelConfiguration', self.channelConfiguration)if conf == 1:
if self.psPresentFlag == -1:
0if None.psPresentFlag == 1:
2Noneif None == 7:
8if None > 7:
0)()
    
    def _get_audio_object_type(self, r):
        '''Raises BitReaderError'''
        audioObjectType = r.bits(5)
        if audioObjectType == 31:
            audioObjectTypeExt = r.bits(6)
            audioObjectType = 32 + audioObjectTypeExt
        return audioObjectType

    
    def _get_sampling_freq(self, r):
        '''Raises BitReaderError'''
        samplingFrequencyIndex = r.bits(4)
        if samplingFrequencyIndex == 15:
            samplingFrequency = r.bits(24)
        else:
            
            try:
                samplingFrequency = self._FREQS[samplingFrequencyIndex]
            except IndexError:
                samplingFrequency = 0

            return samplingFrequency

    
    def __init__(self, fileobj, length):
        '''Raises DescriptorError'''
        r = BitReader(fileobj)
        
        try:
            self._parse(r, length)
            return None
        except BitReaderError:
            e = None
            raise DescriptorError(e)
            e = None
            del e


    
    def _parse(self, r, length):
        '''Raises BitReaderError'''
        pass
    # WARNING: Decompyle incomplete



def GASpecificConfig(r, info):
    '''Reads GASpecificConfig which is needed to get the data after that
    (there is no length defined to skip it) and to read program_config_element
    which can contain channel counts.

    May raise BitReaderError on error or
    NotImplementedError if some reserved data was set.
    '''
    pass
# WARNING: Decompyle incomplete

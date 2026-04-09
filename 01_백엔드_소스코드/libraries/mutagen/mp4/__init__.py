# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

"""Read and write MPEG-4 audio files with iTunes metadata.

This module will read MPEG-4 audio information and metadata,
as found in Apple's MP4 (aka M4A, M4B, M4P) files.

There is no official specification for this format. The source code
for TagLib, FAAD, and various MPEG specifications at

* http://developer.apple.com/documentation/QuickTime/QTFF/
* http://www.geocities.com/xhelmboyx/quicktime/formats/mp4-layout.txt
* http://standards.iso.org/ittf/PubliclyAvailableStandards/c041828_ISO_IEC_14496-12_2005(E).zip
* http://wiki.multimedia.cx/index.php?title=Apple_QuickTime

were all consulted.
"""
import struct
import sys
from io import BytesIO
from collections.abc import Sequence
from datetime import timedelta
from mutagen import FileType, Tags, StreamInfo, PaddingInfo
from mutagen._constants import GENRES
from mutagen._util import cdata, insert_bytes, DictProxy, MutagenError, hashable, enum, get_size, resize_bytes, loadfile, convert_error, bchr, reraise
from _atom import Atoms, Atom, AtomError
from _util import parse_full_atom
from _as_entry import AudioSampleEntry, ASEntryError

class error(MutagenError):
    pass


class MP4MetadataError(error):
    pass


class MP4StreamInfoError(error):
    pass


class MP4NoTrackError(MP4StreamInfoError):
    pass


class MP4MetadataValueError(MP4MetadataError, ValueError):
    pass

__all__ = [
    'MP4',
    'Open',
    'delete',
    'MP4Cover',
    'MP4FreeForm',
    'AtomDataType']
AtomDataType = <NODE:12>()
MP4Cover = <NODE:12>()
MP4FreeForm = <NODE:12>()

def _name2key(name):
    return name.decode('latin-1')


def _key2name(key):
    return key.encode('latin-1')


def _find_padding(atom_path):
    (meta, ilst) = atom_path[-2:]
# WARNING: Decompyle incomplete


def _item_sort_key(key, value):
    order = [
        '©nam',
        '©ART',
        '©wrt',
        '©alb',
        '©gen',
        'gnre',
        'trkn',
        'disk',
        '©day',
        'cpil',
        'pgap',
        'pcst',
        'tmpo',
        '©too',
        '----',
        'covr',
        '©lyr']
    order = dict(zip(order, range(len(order))))
    last = len(order)
    return (order.get(key[:4], last), len(repr(value)), repr(value))


class MP4Tags(Tags, DictProxy):
    pass
# WARNING: Decompyle incomplete


class Chapter(object):
    '''Chapter()

    Chapter information container
    '''
    
    def __init__(self, start, title):
        self.start = start
        self.title = title



class MP4Chapters(Sequence):
    pass
# WARNING: Decompyle incomplete


class MP4Info(StreamInfo):
    '''MP4Info()

    MPEG-4 stream information.

    Attributes:
        bitrate (`int`): bitrate in bits per second, as an int
        length (`float`): file length in seconds, as a float
        channels (`int`): number of audio channels
        sample_rate (`int`): audio sampling rate in Hz
        bits_per_sample (`int`): bits per sample
        codec (`mutagen.text`):
            * if starting with ``"mp4a"`` uses an mp4a audio codec
              (see the codec parameter in rfc6381 for details e.g.
              ``"mp4a.40.2"``)
            * for everything else see a list of possible values at
              http://www.mp4ra.org/codecs.html

            e.g. ``"mp4a"``, ``"alac"``, ``"mp4a.40.2"``, ``"ac-3"`` etc.
        codec_description (`mutagen.text`):
            Name of the codec used (ALAC, AAC LC, AC-3...). Values might
            change in the future, use for display purposes only.
    '''
    bitrate = 0
    length = 0
    channels = 0
    sample_rate = 0
    bits_per_sample = 0
    codec = ''
    codec_description = ''
    
    def __init__(self, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    load = (lambda self, atoms, fileobj: try:
moov = atoms[b'moov']except KeyError:
raise MP4StreamInfoError('not a MP4 file')for trak in moov.findall(b'trak'):
hdlr = trak[(b'mdia', b'hdlr')](ok, data) = hdlr.read(fileobj)if not ok:
raise MP4StreamInfoError('Not enough data')if data[8:12] == b'soun':
passraise MP4NoTrackError('track has no audio data')mdhd = trak[(b'mdia', b'mdhd')](ok, data) = mdhd.read(fileobj)if not ok:
raise MP4StreamInfoError('Not enough data')try:
(version, flags, data) = parse_full_atom(data)except ValueError:
e = Noneraise MP4StreamInfoError(e)e = Nonedel eif version == 0:
offset = 8fmt = '>2I'elif version == 1:
offset = 16fmt = '>IQ'else:
raise MP4StreamInfoError('Unknown mdhd version %d' % version)end = offset + struct.calcsize(fmt)(unit, length) = struct.unpack(fmt, data[offset:end])try:
self.length = float(length) / unitexcept ZeroDivisionError:
self.length = 0try:
atom = trak[(b'mdia', b'minf', b'stbl', b'stsd')]self._parse_stsd(atom, fileobj)Noneexcept KeyError:
None)()
    
    def _parse_stsd(self, atom, fileobj):
        '''Sets channels, bits_per_sample, sample_rate and optionally bitrate.

        Can raise MP4StreamInfoError.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def pprint(self):
        return 'MPEG-4 audio (%s), %.2f seconds, %d bps' % (self.codec_description, self.length, self.bitrate)



class MP4(FileType):
    pass
# WARNING: Decompyle incomplete

Open = MP4
delete = (lambda filething: t = MP4(filething)filething.fileobj.seek(0)t.delete(filething))()()

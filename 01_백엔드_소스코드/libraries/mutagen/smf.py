# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: smf.pyc (Python 3.11)

'''Standard MIDI File (SMF)'''
import struct
from typing import Tuple
from mutagen import StreamInfo, MutagenError
from mutagen._file import FileType
from mutagen._util import loadfile, endswith

class SMFError(MutagenError):
    pass


def _var_int(data = None, offset = None):
    val = 0
    
    try:
        x = data[offset]
    except IndexError:
        raise SMFError('Not enough data')

    offset += 1
    val = (val << 7) + (x & 127)
    if not x & 128:
        return (val, offset)


def _read_track(chunk):
    '''Returns a list of midi events and tempo change events'''
    (TEMPO, MIDI) = range(2)
    tempos = []
    events = []
    chunk = bytearray(chunk)
    deltasum = 0
    status = 0
    off = 0
# WARNING: Decompyle incomplete


def _read_midi_length(fileobj):
    '''Returns the duration in seconds. Can raise all kind of errors...'''
    (TEMPO, MIDI) = range(2)
    
    def read_chunk(fileobj):
        info = fileobj.read(8)
        if len(info) != 8:
            raise SMFError('truncated')
        chunklen = struct.unpack('>I', info[4:])[0]
        data = fileobj.read(chunklen)
        if len(data) != chunklen:
            raise SMFError('truncated')
        return (info[:4], data)

    (identifier, chunk) = read_chunk(fileobj)
    if identifier != b'MThd':
        raise SMFError('Not a MIDI file')
    if len(chunk) != 6:
        raise SMFError('truncated')
    (format_, ntracks, tickdiv) = struct.unpack('>HHH', chunk)
    if format_ > 1:
        raise SMFError('Not supported format %d' % format_)
    if tickdiv >> 15:
        raise SMFError('Not supported timing interval')
    tracks = []
    first_tempos = None
    for tracknum in range(ntracks):
        (identifier, chunk) = read_chunk(fileobj)
        if identifier != b'MTrk':
            continue
        (events, tempos) = _read_track(chunk)
        if not first_tempos:
            first_tempos = tempos
            if format_ == 1:
                tempos = list(first_tempos)
        events += tempos
        events.sort()
        tracks.append(events)
        durations = []
        for events in tracks:
            tempo = 500000
            parts = []
            deltasum = 0
            for dummy, type_, data in events:
                if type_ == TEMPO:
                    parts.append((deltasum, tempo))
                    tempo = data
                    deltasum = 0
                    continue
                deltasum += data
                parts.append((deltasum, tempo))
                duration = 0
                for deltasum, tempo in parts:
                    tpq = tempo
                    quarter = deltasum / float(tickdiv)
                    duration += quarter * tpq
                    duration /= 1000000
                    durations.append(duration)
                    return max(durations)


class SMFInfo(StreamInfo):
    '''SMFInfo()

    Attributes:
        length (`float`): Length in seconds

    '''
    
    def __init__(self, fileobj):
        '''Raises SMFError'''
        self.length = _read_midi_length(fileobj)

    
    def pprint(self):
        return 'SMF, %.2f seconds' % self.length



class SMF(FileType):
    '''SMF(filething)

    Standard MIDI File (SMF)

    Attributes:
        info (`SMFInfo`)
        tags: `None`
    '''
    _mimes = [
        'audio/midi',
        'audio/x-midi']
    load = (lambda self, filething: try:
self.info = SMFInfo(filething.fileobj)Noneexcept IOError:
e = Noneraise SMFError(e)e = Nonedel e)()
    
    def add_tags(self):
        raise SMFError("doesn't support tags")

    score = (lambda filename, fileobj, header:

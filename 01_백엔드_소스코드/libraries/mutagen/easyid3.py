# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: easyid3.pyc (Python 3.11)

__doc__ = 'Easier access to ID3 tags.\n\nEasyID3 is a wrapper around mutagen.id3.ID3 to make ID3 tags appear\nmore like Vorbis or APEv2 tags.\n'
from typing import Callable, Dict
import mutagen.id3 as mutagen
from mutagen import Metadata
from mutagen._util import DictMixin, dict_match, loadfile
from mutagen.id3 import ID3, error, delete, ID3FileType
__all__ = [
    'EasyID3',
    'Open',
    'delete']

class EasyID3KeyError(error, ValueError, KeyError):
    '''Raised when trying to get/set an invalid key.

    Subclasses both KeyError and ValueError for API compatibility,
    catching KeyError is preferred.
    '''
    pass


class EasyID3(Metadata, DictMixin):
    '''EasyID3(filething=None)

    A file with an ID3 tag.

    Like Vorbis comments, EasyID3 keys are case-insensitive ASCII
    strings. Only a subset of ID3 frames are supported by default. Use
    EasyID3.RegisterKey and its wrappers to support more.

    You can also set the GetFallback, SetFallback, and DeleteFallback
    to generic key getter/setter/deleter functions, which are called
    if no specific handler is registered for a key. Additionally,
    ListFallback can be used to supply an arbitrary list of extra
    keys. These can be set on EasyID3 or on individual instances after
    creation.

    To use an EasyID3 class with mutagen.mp3.MP3::

        from mutagen.mp3 import EasyMP3 as MP3
        MP3(filename)

    Because many of the attributes are constructed on the fly, things
    like the following will not work::

        ezid3["performer"].append("Joe")

    Instead, you must do::

        values = ezid3["performer"]
        values.append("Joe")
        ezid3["performer"] = values

    '''
    Set: Dict[(str, Callable)] = { }
    Get: Dict[(str, Callable)] = { }
    Delete: Dict[(str, Callable)] = { }
    List: Dict[(str, Callable)] = { }
    valid_keys = Get
    GetFallback = None
    SetFallback = None
    DeleteFallback = None
    ListFallback = None
    RegisterKey = (lambda cls, key, getter, setter, deleter, lister = (None, None, None, None): key = key.lower()# WARNING: Decompyle incomplete
)()
    RegisterTextKey = (lambda cls, key, frameid: pass# WARNING: Decompyle incomplete
)()
    RegisterTXXXKey = (lambda cls, key, desc: pass# WARNING: Decompyle incomplete
)()
    
    def __init__(self, filename = (None,)):
        self._EasyID3__id3 = ID3()
    # WARNING: Decompyle incomplete

    load = property((lambda s: s._EasyID3__id3.load), (lambda s, v: setattr(s._EasyID3__id3, 'load', v)))
    save = (lambda self, filething, v1, v2_version, v23_sep, padding = (None, 1, 4, '/', None): if v2_version == 3:
backup = self._EasyID3__id3._copy()try:
self._EasyID3__id3.update_to_v23()self._EasyID3__id3.save(filething, v1 = v1, v2_version = v2_version, v23_sep = v23_sep, padding = padding)self._EasyID3__id3._restore(backup)Noneexcept:
self._EasyID3__id3._restore(backup)self._EasyID3__id3.save(filething, v1 = v1, v2_version = v2_version, v23_sep = v23_sep, padding = padding)None)()
    delete = property((lambda s: s._EasyID3__id3.delete), (lambda s, v: setattr(s._EasyID3__id3, 'delete', v)))
    filename = property((lambda s: s._EasyID3__id3.filename), (lambda s, fn: setattr(s._EasyID3__id3, 'filename', fn)))
    size = (lambda self: self._EasyID3__id3.size)()
    
    def __getitem__(self, key):
        func = dict_match(self.Get, key.lower(), self.GetFallback)
    # WARNING: Decompyle incomplete

    
    def __setitem__(self, key, value):
        if isinstance(value, str):
            value = [
                value]
        func = dict_match(self.Set, key.lower(), self.SetFallback)
    # WARNING: Decompyle incomplete

    
    def __delitem__(self, key):
        func = dict_match(self.Delete, key.lower(), self.DeleteFallback)
    # WARNING: Decompyle incomplete

    
    def keys(self):
        keys = []
    # WARNING: Decompyle incomplete

    
    def pprint(self):
        '''Print tag key=value pairs.'''
        strings = []
        for key in sorted(self.keys()):
            values = self[key]
            for value in values:
                strings.append(f'''{key!s}={value!s}''')
                return '\n'.join(strings)


Open = EasyID3

def genre_get(id3, key):
    return id3['TCON'].genres


def genre_set(id3, key, value):
    
    try:
        frame = id3['TCON']
        frame.encoding = 3
        frame.genres = value
        return None
    except KeyError:
        id3.add(mutagen.id3.TCON(encoding = 3, text = value))
        return None



def genre_delete(id3, key):
    del id3['TCON']


def date_get(id3, key):
    return id3['TDRC'].text()


def date_set(id3, key, value):
    id3.add(mutagen.id3.TDRC(encoding = 3, text = value))


def date_delete(id3, key):
    del id3['TDRC']


def original_date_get(id3, key):
    return id3['TDOR'].text()


def original_date_set(id3, key, value):
    id3.add(mutagen.id3.TDOR(encoding = 3, text = value))


def original_date_delete(id3, key):
    del id3['TDOR']


def performer_get(id3, key):
    people = []
    wanted_role = key.split(':', 1)[1]
    
    try:
        mcl = id3['TMCL']
    except KeyError:
        raise KeyError(key)

    for role, person in mcl.people:
        if role == wanted_role:
            people.append(person)
        if people:
            return people
        raise None(key)


def performer_set(id3, key, value):
    pass
# WARNING: Decompyle incomplete


def performer_delete(id3, key):
    pass
# WARNING: Decompyle incomplete


def performer_list(id3, key):
    
    try:
        mcl = id3['TMCL']
        return set((lambda .0: pass# WARNING: Decompyle incomplete
)(mcl.people()))
    except KeyError:
        return 



def musicbrainz_trackid_get(id3, key):
    return [
        id3['UFID:http://musicbrainz.org'].data.decode('ascii')]


def musicbrainz_trackid_set(id3, key, value):
    if len(value) != 1:
        raise ValueError('only one track ID may be set per song')
    value = value[0].encode('ascii')
    
    try:
        frame = id3['UFID:http://musicbrainz.org']
        frame.data = value
        return None
    except KeyError:
        frame = mutagen.id3.UFID(owner = 'http://musicbrainz.org', data = value)
        id3.add(frame)
        return None



def musicbrainz_trackid_delete(id3, key):
    del id3['UFID:http://musicbrainz.org']


def website_get(id3, key):
    urls = id3.getall('WOAR')()
    if urls:
        return urls
    raise (lambda .0: [ frame.url for frame in .0 ])(key)


def website_set(id3, key, value):
    id3.delall('WOAR')
    for v in value:
        id3.add(mutagen.id3.WOAR(url = v))
        return None


def website_delete(id3, key):
    id3.delall('WOAR')


def gain_get(id3, key):
    
    try:
        frame = id3['RVA2:' + key[11:-5]]
        return [
            '%+f dB' % frame.gain]
    except KeyError:
        raise EasyID3KeyError(key)



def gain_set(id3, key, value):
    if len(value) != 1:
        raise ValueError('there must be exactly one gain value, not %r.', value)
    gain = float(value[0].split()[0])
    
    try:
        frame = id3['RVA2:' + key[11:-5]]
    except KeyError:
        frame = mutagen.id3.RVA2(desc = key[11:-5], gain = 0, peak = 0, channel = 1)
        id3.add(frame)

    frame.gain = gain


def gain_delete(id3, key):
    
    try:
        frame = id3['RVA2:' + key[11:-5]]
        if frame.peak:
            frame.gain = 0
            return None
        del None['RVA2:' + key[11:-5]]
        return None
    except KeyError:
        return None



def peak_get(id3, key):
    
    try:
        frame = id3['RVA2:' + key[11:-5]]
        return [
            '%f' % frame.peak]
    except KeyError:
        raise EasyID3KeyError(key)



def peak_set(id3, key, value):
    if len(value) != 1:
        raise ValueError('there must be exactly one peak value, not %r.', value)
    peak = float(value[0])
    if peak >= 2 or peak < 0:
        raise ValueError('peak must be => 0 and < 2.')
    
    try:
        frame = id3['RVA2:' + key[11:-5]]
    except KeyError:
        frame = mutagen.id3.RVA2(desc = key[11:-5], gain = 0, peak = 0, channel = 1)
        id3.add(frame)

    frame.peak = peak


def peak_delete(id3, key):
    
    try:
        frame = id3['RVA2:' + key[11:-5]]
        if frame.gain:
            frame.peak = 0
            return None
        del None['RVA2:' + key[11:-5]]
        return None
    except KeyError:
        return None



def peakgain_list(id3, key):
    keys = []
    for frame in id3.getall('RVA2'):
        keys.append('replaygain_%s_gain' % frame.desc)
        keys.append('replaygain_%s_peak' % frame.desc)
        return keys

# WARNING: Decompyle incomplete

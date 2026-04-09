# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: easymp4.pyc (Python 3.11)

from typing import Dict, Callable
from mutagen import Tags
from mutagen._util import DictMixin, dict_match
from mutagen.mp4 import MP4, MP4Tags, error, delete
__all__ = [
    'EasyMP4Tags',
    'EasyMP4',
    'delete',
    'error']

class EasyMP4KeyError(ValueError, KeyError, error):
    pass


class EasyMP4Tags(Tags, DictMixin):
    '''EasyMP4Tags()

    A file with MPEG-4 iTunes metadata.

    Like Vorbis comments, EasyMP4Tags keys are case-insensitive ASCII
    strings, and values are a list of Unicode strings (and these lists
    are always of length 0 or 1).

    If you need access to the full MP4 metadata feature set, you should use
    MP4, not EasyMP4.
    '''
    Set: Dict[(str, Callable)] = { }
    Get: Dict[(str, Callable)] = { }
    Delete: Dict[(str, Callable)] = { }
    List: Dict[(str, Callable)] = { }
    
    def __init__(self, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    filename = property((lambda s: s._EasyMP4Tags__mp4.filename), (lambda s, fn: setattr(s._EasyMP4Tags__mp4, 'filename', fn)))
    _padding = (lambda self: self._EasyMP4Tags__mp4._padding)()
    RegisterKey = (lambda cls, key, getter, setter, deleter, lister = (None, None, None, None): key = key.lower()# WARNING: Decompyle incomplete
)()
    RegisterTextKey = (lambda cls, key, atomid: pass# WARNING: Decompyle incomplete
)()
    RegisterIntKey = (lambda cls, key, atomid, min_value, max_value = (0, 65535): pass# WARNING: Decompyle incomplete
)()
    RegisterIntPairKey = (lambda cls, key, atomid, min_value, max_value = (0, 65535): pass# WARNING: Decompyle incomplete
)()
    RegisterFreeformKey = (lambda cls, key, name, mean = ('com.apple.iTunes',): pass# WARNING: Decompyle incomplete
)()
    
    def __getitem__(self, key):
        key = key.lower()
        func = dict_match(self.Get, key)
    # WARNING: Decompyle incomplete

    
    def __setitem__(self, key, value):
        key = key.lower()
        if isinstance(value, str):
            value = [
                value]
        func = dict_match(self.Set, key)
    # WARNING: Decompyle incomplete

    
    def __delitem__(self, key):
        key = key.lower()
        func = dict_match(self.Delete, key)
    # WARNING: Decompyle incomplete

    
    def keys(self):
        keys = []
        for key in self.Get.keys():
            if key in self.List:
                keys.extend(self.List[key](self._EasyMP4Tags__mp4, key))
                continue
            if key in self:
                keys.append(key)
            return keys

    
    def pprint(self):
        '''Print tag key=value pairs.'''
        strings = []
        for key in sorted(self.keys()):
            values = self[key]
            for value in values:
                strings.append(f'''{key!s}={value!s}''')
                return '\n'.join(strings)


for atomid, key in {
    '©nam': 'title',
    '©alb': 'album',
    '©ART': 'artist',
    'aART': 'albumartist',
    '©day': 'date',
    '©cmt': 'comment',
    'desc': 'description',
    '©grp': 'grouping',
    '©gen': 'genre',
    'cprt': 'copyright',
    'soal': 'albumsort',
    'soaa': 'albumartistsort',
    'soar': 'artistsort',
    'sonm': 'titlesort',
    'soco': 'composersort' }.items():
    EasyMP4Tags.RegisterTextKey(key, atomid)
    for name, key in {
        'MusicBrainz Artist Id': 'musicbrainz_artistid',
        'MusicBrainz Track Id': 'musicbrainz_trackid',
        'MusicBrainz Album Id': 'musicbrainz_albumid',
        'MusicBrainz Album Artist Id': 'musicbrainz_albumartistid',
        'MusicIP PUID': 'musicip_puid',
        'MusicBrainz Album Status': 'musicbrainz_albumstatus',
        'MusicBrainz Album Type': 'musicbrainz_albumtype',
        'MusicBrainz Release Country': 'releasecountry' }.items():
        EasyMP4Tags.RegisterFreeformKey(key, name)
        for name, key in {
            'tmpo': 'bpm' }.items():
            EasyMP4Tags.RegisterIntKey(key, name)
            for name, key in {
                'trkn': 'tracknumber',
                'disk': 'discnumber' }.items():
                EasyMP4Tags.RegisterIntPairKey(key, name)
                
                class EasyMP4(MP4):
                    '''EasyMP4(filelike)

    Like :class:`MP4 <mutagen.mp4.MP4>`, but uses :class:`EasyMP4Tags` for
    tags.

    Attributes:
        info (`mutagen.mp4.MP4Info`)
        tags (`EasyMP4Tags`)
    '''
                    MP4Tags = EasyMP4Tags
                    Get = EasyMP4Tags.Get
                    Set = EasyMP4Tags.Set
                    Delete = EasyMP4Tags.Delete
                    List = EasyMP4Tags.List
                    RegisterTextKey = EasyMP4Tags.RegisterTextKey
                    RegisterKey = EasyMP4Tags.RegisterKey

                return None

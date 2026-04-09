# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _objects.pyc (Python 3.11)

import struct
from typing import Dict, Type
from mutagen._util import cdata, get_size
from mutagen._tags import PaddingInfo
from _util import guid2bytes, bytes2guid, CODECS, ASFError, ASFHeaderError
from _attrs import ASFBaseAttribute, ASFUnicodeAttribute

class BaseObject(object):
    GUID: bytes = 'Base ASF object.'
    _TYPES: 'Dict[bytes, Type[BaseObject]]' = { }
    
    def __init__(self):
        self.objects = []
        self.data = b''

    
    def parse(self, asf, data):
        self.data = data

    
    def render(self, asf):
        data = self.GUID + struct.pack('<Q', len(self.data) + 24) + self.data
        return data

    
    def get_child(self, guid):
        for obj in self.objects:
            if obj.GUID == guid:
                
                return None, obj
            return None

    _register = (lambda cls, other: cls._TYPES[other.GUID] = otherother)()
    _get_object = (lambda cls, guid: if guid in cls._TYPES:
cls._TYPES[guid]()None(guid))()
    
    def __repr__(self):
        return f'''<{type(self).__name__!s} GUID={bytes2guid(self.GUID)!s} objects={self.objects!r}>'''

    
    def pprint(self):
        l = []
        l.append(f'''{type(self).__name__!s}({bytes2guid(self.GUID)!s})''')
        for o in self.objects:
            for e in o.pprint().splitlines():
                l.append('  ' + e)
                return '\n'.join(l)



class UnknownObject(BaseObject):
    pass
# WARNING: Decompyle incomplete

HeaderObject = <NODE:12>()
ContentDescriptionObject = <NODE:12>()
ExtendedContentDescriptionObject = <NODE:12>()
FilePropertiesObject = <NODE:12>()
StreamPropertiesObject = <NODE:12>()
CodecListObject = <NODE:12>()
PaddingObject = <NODE:12>()
StreamBitratePropertiesObject = <NODE:12>()
ContentEncryptionObject = <NODE:12>()
ExtendedContentEncryptionObject = <NODE:12>()
HeaderExtensionObject = <NODE:12>()
MetadataObject = <NODE:12>()
MetadataLibraryObject = <NODE:12>()

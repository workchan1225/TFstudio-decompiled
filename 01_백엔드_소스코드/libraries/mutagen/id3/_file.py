# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _file.pyc (Python 3.11)

import struct
import mutagen
from mutagen._util import insert_bytes, delete_bytes, enum, loadfile, convert_error, read_full
from mutagen._tags import PaddingInfo
from _util import error, ID3NoHeaderError, ID3UnsupportedVersionError, BitPaddedInt
from _tags import ID3Tags, ID3Header, ID3SaveConfig
from _id3v1 import MakeID3v1, find_id3v1
ID3v1SaveOptions = <NODE:12>()

class ID3(mutagen.Metadata, ID3Tags):
    pass
# WARNING: Decompyle incomplete

delete = (lambda filething, delete_v1, delete_v2 = (True, True): f = filething.fileobj# WARNING: Decompyle incomplete
)()()

class ID3FileType(mutagen.FileType):
    '''ID3FileType(filething, ID3=None, **kwargs)

    An unknown type of file with ID3 tags.

    Args:
        filething (filething): A filename or file-like object
        ID3 (ID3): An ID3 subclass to use for tags.

    Raises:
        mutagen.MutagenError: In case loading the file failed

    Load stream and tag information from a file.

    A custom tag reader may be used in instead of the default
    mutagen.id3.ID3 object, e.g. an EasyID3 reader.
    '''
    __module__ = 'mutagen.id3'
    ID3 = ID3
    
    class _Info(mutagen.StreamInfo):
        length = 0
        
        def __init__(self, fileobj, offset):
            pass

        pprint = (lambda : 'Unknown format with ID3 tag')()

    score = (lambda filename, fileobj, header_data: header_data.startswith(b'ID3'))()
    
    def add_tags(self, ID3 = (None,)):
        '''Add an empty ID3 tag to the file.

        Args:
            ID3 (ID3): An ID3 subclass to use or `None` to use the one
                that used when loading.

        A custom tag reader may be used in instead of the default
        `ID3` object, e.g. an `mutagen.easyid3.EasyID3` reader.
        '''
        pass
    # WARNING: Decompyle incomplete

    load = (lambda self, filething, ID3 = (None,): fileobj = filething.fileobj# WARNING: Decompyle incomplete
)()

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _file.pyc (Python 3.11)

import warnings
from typing import List
from mutagen._util import DictMixin, loadfile

class FileType(DictMixin):
    '''FileType(filething, **kwargs)

    Args:
        filething (filething): A filename or a file-like object

    Subclasses might take further options via keyword arguments.

    An abstract object wrapping tags and audio stream information.

    Each file format has different potential tags and stream
    information.

    FileTypes implement an interface very similar to Metadata; the
    dict interface, save, load, and delete calls on a FileType call
    the appropriate methods on its tag data.

    Attributes:
        info (`StreamInfo`): contains length, bitrate, sample rate
        tags (`Tags`): metadata tags, if any, otherwise `None`
    '''
    __module__ = 'mutagen'
    info = None
    tags = None
    filename = None
    _mimes = [
        'application/octet-stream']
    
    def __init__(self, *args, **kwargs):
        if not args and kwargs:
            warnings.warn('FileType constructor requires a filename', DeprecationWarning)
            return None
    # WARNING: Decompyle incomplete

    load = (lambda self, filething: raise NotImplementedError)()
    
    def __getitem__(self, key):
        '''Look up a metadata tag key.

        If the file has no tags at all, a KeyError is raised.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def __setitem__(self, key, value):
        '''Set a metadata tag.

        If the file has no tags, an appropriate format is added (but
        not written until save is called).
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def __delitem__(self, key):
        '''Delete a metadata tag key.

        If the file has no tags at all, a KeyError is raised.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def keys(self = None):
        '''Return a list of keys in the metadata tag.

        If the file has no tags at all, an empty list is returned.
        '''
        pass
    # WARNING: Decompyle incomplete

    delete = (lambda self, filething = (None,): pass# WARNING: Decompyle incomplete
)()
    save = (lambda self, filething = (None,): pass# WARNING: Decompyle incomplete
)()
    
    def pprint(self = None):
        '''
        Returns:
            text: stream information and comment key=value pairs.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def add_tags(self = None):
        '''Adds new tags to the file.

        Raises:
            mutagen.MutagenError:
                if tags already exist or adding is not possible.
        '''
        raise NotImplementedError

    mime = (lambda self = None: mimes = []for Kind in type(self).__mro__:
for mime in getattr(Kind, '_mimes', []):
if mime not in mimes:
mimes.append(mime)mimes)()
    score = (lambda filename = None, fileobj = None, header = staticmethod: raise NotImplementedError)()


class StreamInfo(object):
    '''Abstract stream information object.

    Provides attributes for length, bitrate, sample rate etc.

    See the implementations for details.
    '''
    __module__ = 'mutagen'
    
    def pprint(self = None):
        '''
        Returns:
            text: Print stream information
        '''
        raise NotImplementedError


File = (lambda filething, options, easy = (None, False): pass# WARNING: Decompyle incomplete
)()

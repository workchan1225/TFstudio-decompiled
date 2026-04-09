# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _tags.pyc (Python 3.11)

from _util import loadfile

class PaddingInfo(object):
    '''PaddingInfo()

    Abstract padding information object.

    This will be passed to the callback function that can be used
    for saving tags.

    ::

        def my_callback(info: PaddingInfo):
            return info.get_default_padding()

    The callback should return the amount of padding to use (>= 0) based on
    the content size and the padding of the file after saving. The actual used
    amount of padding might vary depending on the file format (due to
    alignment etc.)

    The default implementation can be accessed using the
    :meth:`get_default_padding` method in the callback.

    Attributes:
        padding (`int`): The amount of padding left after saving in bytes
            (can be negative if more data needs to be added as padding is
            available)
        size (`int`): The amount of data following the padding
    '''
    
    def __init__(self = None, padding = None, size = None):
        self.padding = padding
        self.size = size

    
    def get_default_padding(self = None):
        '''The default implementation which tries to select a reasonable
        amount of padding and which might change in future versions.

        Returns:
            int: Amount of padding after saving
        '''
        high = 10240 + self.size // 100
        low = 1024 + self.size // 1000
        if self.padding >= 0:
            if self.padding > high:
                return low
            return None.padding

    
    def _get_padding(self, user_func):
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self):
        return '<%s size=%d padding=%d>' % (type(self).__name__, self.size, self.padding)



class Tags(object):
    '''`Tags` is the base class for many of the tag objects in Mutagen.

    In many cases it has a dict like interface.
    '''
    __module__ = 'mutagen'
    
    def pprint(self):
        '''
        Returns:
            text: tag information
        '''
        raise NotImplementedError



class Metadata(Tags):
    '''Metadata(filething=None, **kwargs)

    Args:
        filething (filething): a filename or a file-like object or `None`
            to create an empty instance (like ``ID3()``)

    Like :class:`Tags` but for standalone tagging formats that are not
    solely managed by a container format.

    Provides methods to load, save and delete tags.
    '''
    __module__ = 'mutagen'
    
    def __init__(self, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    load = (lambda self, filething: raise NotImplementedError)()
    save = (lambda self, filething = (None,): raise NotImplementedError)()
    delete = (lambda self, filething = (None,): raise NotImplementedError)()

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _factories.pyc (Python 3.11)

from datetime import timedelta
import weakref
from collections import OrderedDict
from six.moves import _thread

class _TzSingleton(type):
    pass
# WARNING: Decompyle incomplete


class _TzFactory(type):
    
    def instance(cls, *args, **kwargs):
        '''Alternate constructor that returns a fresh instance'''
        pass
    # WARNING: Decompyle incomplete



class _TzOffsetFactory(_TzFactory):
    
    def __init__(cls, *args, **kwargs):
        cls._TzOffsetFactory__instances = weakref.WeakValueDictionary()
        cls._TzOffsetFactory__strong_cache = OrderedDict()
        cls._TzOffsetFactory__strong_cache_size = 8
        cls._cache_lock = _thread.allocate_lock()

    
    def __call__(cls, name, offset):
        if isinstance(offset, timedelta):
            key = (name, offset.total_seconds())
        else:
            key = (name, offset)
        instance = cls._TzOffsetFactory__instances.get(key, None)
    # WARNING: Decompyle incomplete



class _TzStrFactory(_TzFactory):
    
    def __init__(cls, *args, **kwargs):
        cls._TzStrFactory__instances = weakref.WeakValueDictionary()
        cls._TzStrFactory__strong_cache = OrderedDict()
        cls._TzStrFactory__strong_cache_size = 8
        cls._TzStrFactory__cache_lock = _thread.allocate_lock()

    
    def __call__(cls, s, posix_offset = (False,)):
        key = (s, posix_offset)
        instance = cls._TzStrFactory__instances.get(key, None)
    # WARNING: Decompyle incomplete

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''Extensible memoizing collections and decorators.'''
__all__ = ('Cache', 'FIFOCache', 'LFUCache', 'LRUCache', 'RRCache', 'TLRUCache', 'TTLCache', 'cached', 'cachedmethod')
__version__ = '6.2.2'
import collections
import collections.abc as collections
import functools
import heapq
import random
import time
from  import keys

class _DefaultSize:
    __slots__ = ()
    
    def __getitem__(self, _key):
        return 1

    
    def __setitem__(self, _key, _value):
        pass

    
    def pop(self, _key):
        return 1



class Cache(collections.abc.MutableMapping):
    '''Mutable mapping to serve as a simple cache or cache base class.'''
    __marker = object()
    __size = _DefaultSize()
    
    def __init__(self, maxsize, getsizeof = (None,)):
        if getsizeof:
            self.getsizeof = getsizeof
        if self.getsizeof is not Cache.getsizeof:
            self.__size = dict()
        self._Cache__data = dict()
        self._Cache__currsize = 0
        self._Cache__maxsize = maxsize

    
    def __repr__(self):
        return f'''{type(self).__name__!s}({repr(self._Cache__data)!s}, maxsize={self._Cache__maxsize!r}, currsize={self._Cache__currsize!r})'''

    
    def __getitem__(self, key):
        
        try:
            return self._Cache__data[key]
        except KeyError:
            return 


    
    def __setitem__(self, key, value):
        maxsize = self._Cache__maxsize
        size = self.getsizeof(value)
        if size > maxsize:
            raise ValueError('value too large')
    # WARNING: Decompyle incomplete

    
    def __delitem__(self, key):
        size = self.__size.pop(key)
        del self._Cache__data[key]

    
    def __contains__(self, key):
        return key in self._Cache__data

    
    def __missing__(self, key):
        raise KeyError(key)

    
    def __iter__(self):
        return iter(self._Cache__data)

    
    def __len__(self):
        return len(self._Cache__data)

    
    def get(self, key, default = (None,)):
        if key in self:
            return self[key]

    
    def pop(self, key, default = (__marker,)):
        if key in self:
            value = self[key]
            del self[key]
        elif default is self.__marker:
            raise KeyError(key)
        value = default
        return value

    
    def setdefault(self, key, default = (None,)):
        if key in self:
            value = self[key]
        else:
            self[key] = default
            value = default
        return value

    maxsize = (lambda self: self._Cache__maxsize)()
    currsize = (lambda self: self._Cache__currsize)()
    getsizeof = (lambda value: 1)()


class FIFOCache(Cache):
    '''First In First Out (FIFO) cache implementation.'''
    
    def __init__(self, maxsize, getsizeof = (None,)):
        Cache.__init__(self, maxsize, getsizeof)
        self._FIFOCache__order = collections.OrderedDict()

    
    def __setitem__(self, key, value, cache_setitem = (Cache.__setitem__,)):
        cache_setitem(self, key, value)
        
        try:
            self._FIFOCache__order.move_to_end(key)
            return None
        except KeyError:
            self._FIFOCache__order[key] = None
            return None


    
    def __delitem__(self, key, cache_delitem = (Cache.__delitem__,)):
        cache_delitem(self, key)
        del self._FIFOCache__order[key]

    
    def popitem(self):
        '''Remove and return the `(key, value)` pair first inserted.'''
        
        try:
            key = next(iter(self._FIFOCache__order))
            return (key, self.pop(key))
        except StopIteration:
            raise KeyError('%s is empty' % type(self).__name__), None




class LFUCache(Cache):
    '''Least Frequently Used (LFU) cache implementation.'''
    
    class _Link:
        __slots__ = ('count', 'keys', 'next', 'prev')
        
        def __init__(self, count):
            self.count = count
            self.keys = set()

        
        def unlink(self):
            next = self.next
            prev = self.prev
            prev.next = next
            next.prev = prev


    
    def __init__(self, maxsize, getsizeof = (None,)):
        Cache.__init__(self, maxsize, getsizeof)
        self._LFUCache__root = LFUCache._Link(0)
        root = LFUCache._Link(0)
        root.prev = root
        root.next = root
        self._LFUCache__links = { }

    
    def __getitem__(self, key, cache_getitem = (Cache.__getitem__,)):
        value = cache_getitem(self, key)
        if key in self:
            self.__touch(key)
        return value

    
    def __setitem__(self, key, value, cache_setitem = (Cache.__setitem__,)):
        cache_setitem(self, key, value)
        if key in self._LFUCache__links:
            return self.__touch(key)
        root = None._LFUCache__root
        link = root.next
        if link.count != 1:
            link = LFUCache._Link(1)
            link.next = root.next
            root.next = link
            link.next.prev = link
            link.prev = root
        link.keys.add(key)
        self._LFUCache__links[key] = link

    
    def __delitem__(self, key, cache_delitem = (Cache.__delitem__,)):
        cache_delitem(self, key)
        link = self._LFUCache__links.pop(key)
        link.keys.remove(key)
        if not link.keys:
            link.unlink()
            return None

    
    def popitem(self):
        '''Remove and return the `(key, value)` pair least frequently used.'''
        root = self._LFUCache__root
        curr = root.next
        if curr is root:
            raise KeyError('%s is empty' % type(self).__name__), None
        key = next(iter(curr.keys))
        return (key, self.pop(key))

    
    def __touch(self, key):
        '''Increment use count'''
        link = self._LFUCache__links[key]
        curr = link.next
        if curr.count != link.count + 1:
            if len(link.keys) == 1:
                return None
            None._Link(link.count + 1) = None
            curr.next = link.next
            link.next = curr
            curr.next.prev = curr
            curr.prev = link
        curr.keys.add(key)
        link.keys.remove(key)
        if not link.keys:
            link.unlink()
        self._LFUCache__links[key] = curr



class LRUCache(Cache):
    '''Least Recently Used (LRU) cache implementation.'''
    
    def __init__(self, maxsize, getsizeof = (None,)):
        Cache.__init__(self, maxsize, getsizeof)
        self._LRUCache__order = collections.OrderedDict()

    
    def __getitem__(self, key, cache_getitem = (Cache.__getitem__,)):
        value = cache_getitem(self, key)
        if key in self:
            self.__touch(key)
        return value

    
    def __setitem__(self, key, value, cache_setitem = (Cache.__setitem__,)):
        cache_setitem(self, key, value)
        self.__touch(key)

    
    def __delitem__(self, key, cache_delitem = (Cache.__delitem__,)):
        cache_delitem(self, key)
        del self._LRUCache__order[key]

    
    def popitem(self):
        '''Remove and return the `(key, value)` pair least recently used.'''
        
        try:
            key = next(iter(self._LRUCache__order))
            return (key, self.pop(key))
        except StopIteration:
            raise KeyError('%s is empty' % type(self).__name__), None


    
    def __touch(self, key):
        '''Mark as recently used'''
        
        try:
            self._LRUCache__order.move_to_end(key)
            return None
        except KeyError:
            self._LRUCache__order[key] = None
            return None




class RRCache(Cache):
    '''Random Replacement (RR) cache implementation.'''
    
    def __init__(self, maxsize, choice, getsizeof = (random.choice, None)):
        Cache.__init__(self, maxsize, getsizeof)
        self._RRCache__choice = choice
        self._RRCache__index = { }
        self._RRCache__keys = []

    choice = (lambda self: self._RRCache__choice)()
    
    def __setitem__(self, key, value, cache_setitem = (Cache.__setitem__,)):
        cache_setitem(self, key, value)
        if key not in self._RRCache__index:
            self._RRCache__index[key] = len(self._RRCache__keys)
            self._RRCache__keys.append(key)
            return None

    
    def __delitem__(self, key, cache_delitem = (Cache.__delitem__,)):
        cache_delitem(self, key)
        index = self._RRCache__index.pop(key)
        if index != len(self._RRCache__keys) - 1:
            last = self._RRCache__keys[-1]
            self._RRCache__keys[index] = last
            self._RRCache__index[last] = index
        self._RRCache__keys.pop()

    
    def popitem(self):
        '''Remove and return a random `(key, value)` pair.'''
        
        try:
            key = self._RRCache__choice(self._RRCache__keys)
            return (key, self.pop(key))
        except IndexError:
            raise KeyError('%s is empty' % type(self).__name__), None




class _TimedCache(Cache):
    pass
# WARNING: Decompyle incomplete


class TTLCache(_TimedCache):
    '''LRU Cache implementation with per-item time-to-live (TTL) value.'''
    
    class _Link:
        __slots__ = ('key', 'expires', 'next', 'prev')
        
        def __init__(self, key, expires = (None, None)):
            self.key = key
            self.expires = expires

        
        def __reduce__(self):
            return (TTLCache._Link, (self.key, self.expires))

        
        def unlink(self):
            next = self.next
            prev = self.prev
            prev.next = next
            next.prev = prev


    
    def __init__(self, maxsize, ttl, timer, getsizeof = (time.monotonic, None)):
        _TimedCache.__init__(self, maxsize, timer, getsizeof)
        self._TTLCache__root = TTLCache._Link()
        root = TTLCache._Link()
        root.prev = root
        root.next = root
        self._TTLCache__links = collections.OrderedDict()
        self._TTLCache__ttl = ttl

    
    def __contains__(self, key):
        
        try:
            link = self._TTLCache__links[key]
            return self.timer() < link.expires
        except KeyError:
            return False


    
    def __getitem__(self, key, cache_getitem = (Cache.__getitem__,)):
        
        try:
            link = self.__getlink(key)
            expired = not (self.timer() < link.expires)
        except KeyError:
            expired = False

        if expired:
            return self.__missing__(key)
        return cache_getitem(self, key)

    
    def __setitem__(self, key, value, cache_setitem = (Cache.__setitem__,)):

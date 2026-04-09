# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: orderedset.pyc (Python 3.11)

import typing as t
import weakref

class Link:
    '''Representation of one item in a doubly-linked list.'''
    key: str = ('prev', 'next', 'key', '__weakref__')


def OrderedSet():
    '''OrderedSet'''
    __doc__ = 'A set that remembers the order in which items were added.'
    
    def __init__(self = None, iterable = None):
        self._OrderedSet__root = Link()
        root = Link()
        root.prev = root
        root.next = root
        self._OrderedSet__map = { }
    # WARNING: Decompyle incomplete

    
    def __len__(self = None):
        return len(self._OrderedSet__map)

    
    def __contains__(self = None, key = None):
        return key in self._OrderedSet__map

    
    def add(self = None, key = None):
        if key not in self._OrderedSet__map:
            self._OrderedSet__map[key] = Link()
            link = Link()
            root = self._OrderedSet__root
            last = root.prev
            link.prev, link.next, link.key = last, root, key
            last.next = weakref.proxy(link)
            root.prev = weakref.proxy(link)
            return None

    
    def discard(self = None, key = None):
        if key in self._OrderedSet__map:
            link = self._OrderedSet__map.pop(key)
            link.prev.next = link.next
            link.next.prev = link.prev
            return None

    
    def __iter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __reversed__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def pop(self = None, last = None):
        if not self:
            raise KeyError('set is empty')
        key = next(reversed(self)) if last else next(iter(self))
        self.discard(key)
        return key

    
    def __repr__(self = None):
        if not self:
            return f'''{self.__class__.__name__}()'''
        return f'''{None.__class__.__name__}({list(self)!r})'''

    
    def __str__(self = None):
        return self.__repr__()

    
    def __eq__(self = None, other = None):

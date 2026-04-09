# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: repeated.pyc (Python 3.11)

import collections
import copy
from typing import Iterable
from proto.utils import cached_property

class Repeated(collections.abc.MutableSequence):
    '''A view around a mutable sequence in protocol buffers.

    This implements the full Python MutableSequence interface, but all methods
    modify the underlying field container directly.
    '''
    
    def __init__(self = None, sequence = {
        'proto_type': None }, *, marshal, proto_type):
        '''Initialize a wrapper around a protobuf repeated field.

        Args:
            sequence: A protocol buffers repeated field.
            marshal (~.MarshalRegistry): An instantiated marshal, used to
                convert values going to and from this map.
        '''
        self._pb = sequence
        self._marshal = marshal
        self._proto_type = proto_type

    
    def __copy__(self):
        '''Copy this object and return the copy.'''
        return type(self)(self.pb[:], marshal = self._marshal)

    
    def __delitem__(self, key):
        '''Delete the given item.'''
        del self.pb[key]

    
    def __eq__(self, other):
        if hasattr(other, 'pb'):
            return tuple(self.pb) == tuple(other.pb)
        return tuple(self.pb) == tuple(other) if None(other, Iterable) else False

    
    def __getitem__(self, key):
        '''Return the given item.'''
        return self.pb[key]

    
    def __len__(self):
        '''Return the length of the sequence.'''
        return len(self.pb)

    
    def __ne__(self, other):
        return not (self == other)

    
    def __repr__(self):
        return None(repr)

    
    def __setitem__(self, key, value):
        self.pb[key] = value

    
    def insert(self = None, index = None, value = None):
        '''Insert ``value`` in the sequence before ``index``.'''
        self.pb.insert(index, value)

    
    def sort(self = None, *, key, reverse):
        '''Stable sort *IN PLACE*.'''
        self.pb.sort(key = key, reverse = reverse)

    pb = (lambda self: self._pb)()


class RepeatedComposite(Repeated):
    pass
# WARNING: Decompyle incomplete

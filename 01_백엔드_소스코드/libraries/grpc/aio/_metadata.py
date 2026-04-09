# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _metadata.pyc (Python 3.11)

'''Implementation of the metadata abstraction for gRPC Asyncio Python.'''
from collections import OrderedDict
from collections import abc
from typing import Any, Iterator, List, Optional, Tuple, Union
MetadataKey = str
MetadataValue = Union[(str, bytes)]

class Metadata(abc.Collection):
    '''Metadata abstraction for the asynchronous calls and interceptors.

    The metadata is a mapping from str -> List[str]

    Traits
        * Multiple entries are allowed for the same key
        * The order of the values by key is preserved
        * Getting by an element by key, retrieves the first mapped value
        * Supports an immutable view of the data
        * Allows partial mutation on the data without recreating the new object from scratch.
    '''
    
    def __init__(self = None, *args):
        self._metadata = OrderedDict()
        for md_key, md_value in args:
            self.add(md_key, md_value)
            return None

    from_tuple = (lambda cls = None, raw_metadata = None: pass# WARNING: Decompyle incomplete
)()
    
    def add(self = None, key = None, value = None):
        self._metadata.setdefault(key, [])
        self._metadata[key].append(value)

    
    def __len__(self = None):
        '''Return the total number of elements that there are in the metadata,
        including multiple values for the same key.
        '''
        return sum(map(len, self._metadata.values()))

    
    def __getitem__(self = None, key = None):
        '''When calling <metadata>[<key>], the first element of all those
        mapped for <key> is returned.
        '''
        
        try:
            return self._metadata[key][0]
        except (ValueError, IndexError):
            e = None
            error_msg = f'''{key!r}'''
            raise KeyError(error_msg), e
            e = None
            del e


    
    def __setitem__(self = None, key = None, value = None):
        '''Calling metadata[<key>] = <value>
        Maps <value> to the first instance of <key>.
        '''
        if key not in self:
            self._metadata[key] = [
                value]
            return None
        current_values = None.get_all(key)
        self._metadata[key] = None

    
    def __delitem__(self = None, key = None):
        '''``del metadata[<key>]`` deletes the first mapping for <key>.'''
        current_values = self.get_all(key)
        if not current_values:
            raise KeyError(repr(key))
        self._metadata[key] = current_values[1:]

    
    def delete_all(self = None, key = None):
        '''Delete all mappings for <key>.'''
        del self._metadata[key]

    
    def __iter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def keys(self = None):
        return abc.KeysView(self)

    
    def values(self = None):
        return abc.ValuesView(self)

    
    def items(self = None):
        return abc.ItemsView(self)

    
    def get(self = None, key = None, default = None):
        
        try:
            return self[key]
        except KeyError:
            return 


    
    def get_all(self = None, key = None):
        '''For compatibility with other Metadata abstraction objects (like in Java),
        this would return all items under the desired <key>.
        '''
        return self._metadata.get(key, [])

    
    def set_all(self = None, key = None, values = None):
        self._metadata[key] = values

    
    def __contains__(self = None, key = None):
        return key in self._metadata

    
    def __eq__(self = None, other = None):
        if isinstance(other, self.__class__):
            return self._metadata == other._metadata
        if None(other, tuple):
            return tuple(self) == other

    
    def __add__(self = None, other = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self = None):
        view = tuple(self)
        return '{0}({1!r})'.format(self.__class__.__name__, view)

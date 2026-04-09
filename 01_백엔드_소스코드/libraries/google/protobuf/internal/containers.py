# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: containers.pyc (Python 3.11)

"""Contains container classes to represent different protocol buffer types.

This file defines container classes which represent categories of protocol
buffer field types which need extra maintenance. Currently these categories
are:

-   Repeated scalar fields - These are all repeated fields which aren't
    composite (e.g. they are of simple types like int32, string, etc).
-   Repeated composite fields - Repeated fields which are composite. This
    includes groups and nested messages.
"""
import collections.abc as collections
import copy
import pickle
from typing import Any, Iterable, Iterator, List, MutableMapping, MutableSequence, NoReturn, Optional, Sequence, TypeVar, Union, overload
_T = TypeVar('_T')
_K = TypeVar('_K')
_V = TypeVar('_V')

def BaseContainer():
    '''BaseContainer'''
    __doc__ = 'Base container class.'
    __slots__ = [
        '_message_listener',
        '_values']
    
    def __init__(self = None, message_listener = None):
        """
    Args:
      message_listener: A MessageListener implementation.
        The RepeatedScalarFieldContainer will call this object's
        Modified() method when it is modified.
    """
        self._message_listener = message_listener
        self._values = []

    __getitem__ = (lambda self = None, key = None: pass)()
    __getitem__ = (lambda self = None, key = None: pass)()
    
    def __getitem__(self, key):
        '''Retrieves item by the specified key.'''
        return self._values[key]

    
    def __len__(self = None):
        '''Returns the number of elements in the container.'''
        return len(self._values)

    
    def __ne__(self = None, other = None):
        """Checks if another instance isn't equal to this one."""
        return not (self == other)

    __hash__ = None
    
    def __repr__(self = None):
        return repr(self._values)

    
    def sort(self = None, *args, **kwargs):
        if 'sort_function' in kwargs:
            kwargs['cmp'] = kwargs.pop('sort_function')
    # WARNING: Decompyle incomplete

    
    def reverse(self = None):
        self._values.reverse()


BaseContainer = <NODE:27>(BaseContainer, 'BaseContainer', Sequence[_T])
collections.abc.MutableSequence.register(BaseContainer)

def RepeatedScalarFieldContainer():
    '''RepeatedScalarFieldContainer'''
    pass
# WARNING: Decompyle incomplete

RepeatedScalarFieldContainer = <NODE:27>(RepeatedScalarFieldContainer, 'RepeatedScalarFieldContainer', BaseContainer[_T], MutableSequence[_T])

def RepeatedCompositeFieldContainer():
    '''RepeatedCompositeFieldContainer'''
    pass
# WARNING: Decompyle incomplete

RepeatedCompositeFieldContainer = <NODE:27>(RepeatedCompositeFieldContainer, 'RepeatedCompositeFieldContainer', BaseContainer[_T], MutableSequence[_T])

def ScalarMap():
    '''ScalarMap'''
    __doc__ = 'Simple, type-checked, dict-like container for holding repeated scalars.'
    __slots__ = [
        '_key_checker',
        '_value_checker',
        '_values',
        '_message_listener',
        '_entry_descriptor']
    
    def __init__(self, message_listener = None, key_checker = None, value_checker = None, entry_descriptor = ('message_listener', Any, 'key_checker', Any, 'value_checker', Any, 'entry_descriptor', Any, 'return', None)):
        """
    Args:
      message_listener: A MessageListener implementation.
        The ScalarMap will call this object's Modified() method when it
        is modified.
      key_checker: A type_checkers.ValueChecker instance to run on keys
        inserted into this container.
      value_checker: A type_checkers.ValueChecker instance to run on values
        inserted into this container.
      entry_descriptor: The MessageDescriptor of a map entry: key and value.
    """
        self._message_listener = message_listener
        self._key_checker = key_checker
        self._value_checker = value_checker
        self._entry_descriptor = entry_descriptor
        self._values = { }

    
    def __getitem__(self = None, key = None):
        
        try:
            return self._values[key]
        except KeyError:
            key = self._key_checker.CheckValue(key)
            val = self._value_checker.DefaultValue()
            self._values[key] = val
            return 


    
    def __contains__(self = None, item = None):
        self._key_checker.CheckValue(item)
        return item in self._values

    get = (lambda self = None, key = None: pass)()
    get = (lambda self = None, key = None, default = overload: pass)()
    
    def get(self, key, default = (None,)):
        if key in self:
            return self[key]

    
    def __setitem__(self = None, key = None, value = None):
        checked_key = self._key_checker.CheckValue(key)
        checked_value = self._value_checker.CheckValue(value)
        self._values[checked_key] = checked_value
        self._message_listener.Modified()

    
    def __delitem__(self = None, key = None):
        del self._values[key]
        self._message_listener.Modified()

    
    def __len__(self = None):
        return len(self._values)

    
    def __iter__(self = None):
        return iter(self._values)

    
    def __repr__(self = None):
        return repr(self._values)

    
    def MergeFrom(self = None, other = None):
        self._values.update(other._values)
        self._message_listener.Modified()

    
    def InvalidateIterators(self = None):
        original = self._values
        self._values = original.copy()
        original[None] = None

    
    def clear(self = None):
        self._values.clear()
        self._message_listener.Modified()

    
    def GetEntryClass(self = None):
        return self._entry_descriptor._concrete_class


ScalarMap = <NODE:27>(ScalarMap, 'ScalarMap', MutableMapping[(_K, _V)])

def MessageMap():
    '''MessageMap'''
    __doc__ = 'Simple, type-checked, dict-like container for with submessage values.'
    __slots__ = [
        '_key_checker',
        '_values',
        '_message_listener',
        '_message_descriptor',
        '_entry_descriptor']
    
    def __init__(self, message_listener = None, message_descriptor = None, key_checker = None, entry_descriptor = ('message_listener', Any, 'message_descriptor', Any, 'key_checker', Any, 'entry_descriptor', Any, 'return', None)):
        """
    Args:
      message_listener: A MessageListener implementation.
        The ScalarMap will call this object's Modified() method when it
        is modified.
      key_checker: A type_checkers.ValueChecker instance to run on keys
        inserted into this container.
      value_checker: A type_checkers.ValueChecker instance to run on values
        inserted into this container.
      entry_descriptor: The MessageDescriptor of a map entry: key and value.
    """
        self._message_listener = message_listener
        self._message_descriptor = message_descriptor
        self._key_checker = key_checker
        self._entry_descriptor = entry_descriptor
        self._values = { }

    
    def __getitem__(self = None, key = None):
        key = self._key_checker.CheckValue(key)
        
        try:
            return self._values[key]
        except KeyError:
            new_element = self._message_descriptor._concrete_class()
            new_element._SetListener(self._message_listener)
            self._values[key] = new_element
            self._message_listener.Modified()
            return 


    
    def get_or_create(self = None, key = None):
        '''get_or_create() is an alias for getitem (ie. map[key]).

    Args:
      key: The key to get or create in the map.

    This is useful in cases where you want to be explicit that the call is
    mutating the map.  This can avoid lint errors for statements like this
    that otherwise would appear to be pointless statements:

      msg.my_map[key]
    '''
        return self[key]

    get = (lambda self = None, key = None: pass)()
    get = (lambda self = None, key = None, default = overload: pass)()
    
    def get(self, key, default = (None,)):
        if key in self:
            return self[key]

    
    def __contains__(self = None, item = None):
        item = self._key_checker.CheckValue(item)
        return item in self._values

    
    def __setitem__(self = None, key = None, value = None):
        raise ValueError('May not set values directly, call my_map[key].foo = 5')

    
    def __delitem__(self = None, key = None):
        key = self._key_checker.CheckValue(key)
        del self._values[key]
        self._message_listener.Modified()

    
    def __len__(self = None):
        return len(self._values)

    
    def __iter__(self = None):
        return iter(self._values)

    
    def __repr__(self = None):
        return repr(self._values)

    
    def MergeFrom(self = None, other = None):
        for key in other._values:
            if key in self:
                del self[key]
            self[key].CopyFrom(other[key])
            return None

    
    def InvalidateIterators(self = None):
        original = self._values
        self._values = original.copy()
        original[None] = None

    
    def clear(self = None):
        self._values.clear()
        self._message_listener.Modified()

    
    def GetEntryClass(self = None):
        return self._entry_descriptor._concrete_class


MessageMap = <NODE:27>(MessageMap, 'MessageMap', MutableMapping[(_K, _V)])

class _UnknownField:
    '''A parsed unknown field.'''
    __slots__ = [
        '_field_number',
        '_wire_type',
        '_data']
    
    def __init__(self, field_number, wire_type, data):
        self._field_number = field_number
        self._wire_type = wire_type
        self._data = data

    
    def __lt__(self, other):
        return self._field_number < other._field_number

    
    def __eq__(self, other):

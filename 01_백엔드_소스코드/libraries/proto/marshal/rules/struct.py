# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: struct.pyc (Python 3.11)

import collections.abc as collections
from google.protobuf import struct_pb2
from proto.marshal.collections import maps
from proto.marshal.collections import repeated

class ValueRule:
    '''A rule to marshal between google.protobuf.Value and Python values.'''
    
    def __init__(self, *, marshal):
        self._marshal = marshal

    
    def to_python(self = None, value = None, *, absent):
        '''Coerce the given value to the appropriate Python type.

        Note that both NullValue and absent fields return None.
        In order to disambiguate between these two options,
        use containment check,
        E.g.
        "value" in foo
        which is True for NullValue and False for an absent value.
        '''
        kind = value.WhichOneof('kind')
        if kind == 'null_value' or absent:
            return None
        if None == 'bool_value':
            return bool(value.bool_value)
        if None == 'number_value':
            return float(value.number_value)
        if None == 'string_value':
            return str(value.string_value)
        if None == 'struct_value':
            return self._marshal.to_python(struct_pb2.Struct, value.struct_value, absent = False)
        if None == 'list_value':
            return self._marshal.to_python(struct_pb2.ListValue, value.list_value, absent = False)
        raise None('Unexpected kind: %s' % kind)

    
    def to_proto(self = None, value = None):
        '''Return a protobuf Value object representing this value.'''
        if isinstance(value, struct_pb2.Value):
            return value
    # WARNING: Decompyle incomplete



class ListValueRule:
    '''A rule translating google.protobuf.ListValue and list-like objects.'''
    
    def __init__(self, *, marshal):
        self._marshal = marshal

    
    def to_python(self = None, value = None, *, absent):
        '''Coerce the given value to a Python sequence.'''
        return None if absent else repeated.RepeatedComposite(value.values, marshal = self._marshal)

    
    def to_proto(self = None, value = None):
        pass
    # WARNING: Decompyle incomplete



class StructRule:
    '''A rule translating google.protobuf.Struct and dict-like objects.'''
    
    def __init__(self, *, marshal):
        self._marshal = marshal

    
    def to_python(self = None, value = None, *, absent):
        '''Coerce the given value to a Python mapping.'''
        return None if absent else maps.MapComposite(value.fields, marshal = self._marshal)

    
    def to_proto(self = None, value = None):
        pass
    # WARNING: Decompyle incomplete

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: enums.pyc (Python 3.11)

import enum
from google.protobuf import descriptor_pb2
from proto import _file_info
from proto import _package_info
from proto.marshal.rules.enums import EnumRule

class ProtoEnumMeta(enum.EnumMeta):
    pass
# WARNING: Decompyle incomplete


def Enum():
    '''Enum'''
    __doc__ = 'A enum object that also builds a protobuf enum descriptor.'
    
    def _comparable(self, other):
        return type(other) in (type(self), int)

    
    def __hash__(self):
        return hash(self.value)

    
    def __eq__(self, other):
        if not self._comparable(other):
            return NotImplemented
        return None.value == int(other)

    
    def __ne__(self, other):
        if not self._comparable(other):
            return NotImplemented
        return None.value != int(other)

    
    def __lt__(self, other):
        if not self._comparable(other):
            return NotImplemented
        return None.value < int(other)

    
    def __le__(self, other):
        if not self._comparable(other):
            return NotImplemented
        return None.value <= int(other)

    
    def __ge__(self, other):
        if not self._comparable(other):
            return NotImplemented
        return None.value >= int(other)

    
    def __gt__(self, other):
        if not self._comparable(other):
            return NotImplemented
        return None.value > int(other)


Enum = <NODE:27>(Enum, 'Enum', enum.IntEnum, metaclass = ProtoEnumMeta)

class _EnumInfo:
    
    def __init__(self = None, *, full_name, pb):
        self.full_name = full_name
        self.pb = pb

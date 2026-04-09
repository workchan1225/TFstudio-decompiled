# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: fields.pyc (Python 3.11)

from enum import EnumMeta
from google.protobuf import descriptor_pb2
from google.protobuf.internal.enum_type_wrapper import EnumTypeWrapper
from proto.primitives import ProtoType

class Field:
    '''A representation of a type of field in protocol buffers.'''
    repeated = False
    
    def __init__(self = None, proto_type = None, *, number, message, enum, oneof, json_name, optional):
        self.mcls_data = None
        self.parent = None
        if not isinstance(proto_type, int):
            if isinstance(proto_type, (EnumMeta, EnumTypeWrapper)):
                enum = proto_type
                proto_type = ProtoType.ENUM
            else:
                message = proto_type
                proto_type = ProtoType.MESSAGE
        self.number = number
        self.proto_type = proto_type
        self.message = message
        self.enum = enum
        self.json_name = json_name
        self.optional = optional
        self.oneof = oneof
        self._descriptor = None

    descriptor = (lambda self: if not self._descriptor:
type_name = Noneif isinstance(self.message, str):
if not self.message.startswith(self.package):
self.message = '{package}.{name}'.format(package = self.package, name = self.message)type_name = self.messageelif self.message:
type_name = self.message.DESCRIPTOR.full_name if hasattr(self.message, 'DESCRIPTOR') else self.message._meta.full_nameelif isinstance(self.enum, str):
if not self.enum.startswith(self.package):
self.enum = '{package}.{name}'.format(package = self.package, name = self.enum)type_name = self.enumelif self.enum:
type_name = self.enum.DESCRIPTOR.full_name if hasattr(self.enum, 'DESCRIPTOR') else self.enum._meta.full_nameself._descriptor = descriptor_pb2.FieldDescriptorProto(name = self.name, number = self.number, label = 3 if self.repeated else 1, type = self.proto_type, type_name = type_name, json_name = self.json_name, proto3_optional = self.optional)self._descriptor)()
    name = (lambda self = None: self.mcls_data['name'])()
    package = (lambda self = None: self.mcls_data['package'])()
    pb_type = (lambda self: if self.enum:
self.enumif not None.message:
self.proto_typeif None(self.message, '_meta'):
self.message.pb()None.message)()


class RepeatedField(Field):
    '''A representation of a repeated field in protocol buffers.'''
    repeated = True


class MapField(Field):
    pass
# WARNING: Decompyle incomplete

__all__ = ('Field', 'MapField', 'RepeatedField')

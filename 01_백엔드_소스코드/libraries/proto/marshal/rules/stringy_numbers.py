# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: stringy_numbers.pyc (Python 3.11)

from proto.primitives import ProtoType

class StringyNumberRule:
    '''A marshal between certain numeric types and strings

    This is a necessary hack to allow round trip conversion
    from messages to dicts back to messages.

    See https://github.com/protocolbuffers/protobuf/issues/2679
    and
    https://developers.google.com/protocol-buffers/docs/proto3#json
    for more details.
    '''
    
    def to_python(self = None, value = None, *, absent):
        return value

    
    def to_proto(self, value):
        pass
    # WARNING: Decompyle incomplete



class Int64Rule(StringyNumberRule):
    _python_type = int
    _proto_type = ProtoType.INT64


class UInt64Rule(StringyNumberRule):
    _python_type = int
    _proto_type = ProtoType.UINT64


class SInt64Rule(StringyNumberRule):
    _python_type = int
    _proto_type = ProtoType.SINT64


class Fixed64Rule(StringyNumberRule):
    _python_type = int
    _proto_type = ProtoType.FIXED64


class SFixed64Rule(StringyNumberRule):
    _python_type = int
    _proto_type = ProtoType.SFIXED64

STRINGY_NUMBER_RULES = [
    Int64Rule,
    UInt64Rule,
    SInt64Rule,
    Fixed64Rule,
    SFixed64Rule]

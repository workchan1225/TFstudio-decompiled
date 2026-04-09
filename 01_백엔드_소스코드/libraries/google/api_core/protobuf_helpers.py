# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: protobuf_helpers.pyc (Python 3.11)

'''Helpers for :mod:`protobuf`.'''
import collections
import collections.abc as collections
import copy
import inspect
from google.protobuf import field_mask_pb2
from google.protobuf import message
from google.protobuf import wrappers_pb2
_SENTINEL = object()
_WRAPPER_TYPES = (wrappers_pb2.BoolValue, wrappers_pb2.BytesValue, wrappers_pb2.DoubleValue, wrappers_pb2.FloatValue, wrappers_pb2.Int32Value, wrappers_pb2.Int64Value, wrappers_pb2.StringValue, wrappers_pb2.UInt32Value, wrappers_pb2.UInt64Value)

def from_any_pb(pb_type, any_pb):
    '''Converts an ``Any`` protobuf to the specified message type.

    Args:
        pb_type (type): the type of the message that any_pb stores an instance
            of.
        any_pb (google.protobuf.any_pb2.Any): the object to be converted.

    Returns:
        pb_type: An instance of the pb_type message.

    Raises:
        TypeError: if the message could not be converted.
    '''
    msg = pb_type()
    if callable(getattr(pb_type, 'pb', None)):
        msg_pb = pb_type.pb(msg)
    else:
        msg_pb = msg
    if not any_pb.Unpack(msg_pb):
        raise TypeError(f'''Could not convert `{any_pb.TypeName()}` with underlying type `google.protobuf.any_pb2.Any` to `{msg_pb.DESCRIPTOR.full_name}`''')
    return msg


def check_oneof(**kwargs):

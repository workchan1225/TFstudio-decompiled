# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: python_message.pyc (Python 3.11)

'''Contains a metaclass and helper functions used to create
protocol message classes from Descriptor objects at runtime.

Recall that a metaclass is the "type" of a class.
(A class is to a metaclass what an instance is to a class.)

In this case, we use the GeneratedProtocolMessageType metaclass
to inject all the useful functionality into the classes
output by the protocol compiler at compile-time.

The upshot of all this is that the real implementation
details for ALL pure-Python protocol buffers are *here in
this file*.
'''
__author__ = 'robinson@google.com (Will Robinson)'
from io import BytesIO
import struct
import sys
import warnings
import weakref
from google.protobuf import descriptor as descriptor_mod
from google.protobuf import message as message_mod
from google.protobuf import text_format
from google.protobuf.internal import api_implementation
from google.protobuf.internal import containers
from google.protobuf.internal import decoder
from google.protobuf.internal import encoder
from google.protobuf.internal import enum_type_wrapper
from google.protobuf.internal import extension_dict
from google.protobuf.internal import message_listener as message_listener_mod
from google.protobuf.internal import type_checkers
from google.protobuf.internal import well_known_types
from google.protobuf.internal import wire_format
_FieldDescriptor = descriptor_mod.FieldDescriptor
_AnyFullTypeName = 'google.protobuf.Any'
_ExtensionDict = extension_dict._ExtensionDict

class GeneratedProtocolMessageType(type):
    pass
# WARNING: Decompyle incomplete


def _PropertyName(proto_field_name):
    '''Returns the name of the public property attribute which
  clients can use to get and (in some cases) set the value
  of a protocol message field.

  Args:
    proto_field_name: The protocol message field name, exactly
      as it appears (or would appear) in a .proto file.
  '''
    return proto_field_name


def _AddSlots(message_descriptor, dictionary):
    """Adds a __slots__ entry to dictionary, containing the names of all valid
  attributes for this message type.

  Args:
    message_descriptor: A Descriptor instance describing this message type.
    dictionary: Class dictionary to which we'll add a '__slots__' entry.
  """
    dictionary['__slots__'] = [
        '_cached_byte_size',
        '_cached_byte_size_dirty',
        '_fields',
        '_unknown_fields',
        '_unknown_field_set',
        '_is_present_in_parent',
        '_listener',
        '_listener_for_children',
        '__weakref__',
        '_oneofs']


def _IsMessageSetExtension(field):

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: json_format.pyc (Python 3.11)

"""Contains routines for printing protocol messages in JSON format.

Simple usage example:

  # Create a proto object and serialize it to a json format string.
  message = my_proto_pb2.MyMessage(foo='bar')
  json_string = json_format.MessageToJson(message)

  # Parse a json format string to proto object.
  message = json_format.Parse(json_string, my_proto_pb2.MyMessage())
"""
__author__ = 'jieluo@google.com (Jie Luo)'
import base64
from collections import OrderedDict
import json
import math
from operator import methodcaller
import re
from google.protobuf.internal import type_checkers
from google.protobuf import descriptor
from google.protobuf import message_factory
from google.protobuf import symbol_database
_INT_TYPES = frozenset([
    descriptor.FieldDescriptor.CPPTYPE_INT32,
    descriptor.FieldDescriptor.CPPTYPE_UINT32,
    descriptor.FieldDescriptor.CPPTYPE_INT64,
    descriptor.FieldDescriptor.CPPTYPE_UINT64])
_INT64_TYPES = frozenset([
    descriptor.FieldDescriptor.CPPTYPE_INT64,
    descriptor.FieldDescriptor.CPPTYPE_UINT64])
_FLOAT_TYPES = frozenset([
    descriptor.FieldDescriptor.CPPTYPE_FLOAT,
    descriptor.FieldDescriptor.CPPTYPE_DOUBLE])
_INFINITY = 'Infinity'
_NEG_INFINITY = '-Infinity'
_NAN = 'NaN'
_UNPAIRED_SURROGATE_PATTERN = re.compile('[���-���](?![���-���])|(?<![���-���])[���-���]')
_VALID_EXTENSION_NAME = re.compile('\\[[a-zA-Z0-9\\._]*\\]$')

class Error(Exception):
    '''Top-level module error for json_format.'''
    pass


class SerializeToJsonError(Error):
    '''Thrown if serialization to JSON fails.'''
    pass


class ParseError(Error):
    '''Thrown in case of parsing error.'''
    pass


def MessageToJson(message, including_default_value_fields, preserving_proto_field_name, indent, sort_keys, use_integers_for_enums, descriptor_pool, float_precision, ensure_ascii = (False, False, 2, False, False, None, None, True)):
    '''Converts protobuf message to JSON format.

  Args:
    message: The protocol buffers message instance to serialize.
    including_default_value_fields: If True, singular primitive fields,
        repeated fields, and map fields will always be serialized.  If
        False, only serialize non-empty fields.  Singular message fields
        and oneof fields are not affected by this option.
    preserving_proto_field_name: If True, use the original proto field
        names as defined in the .proto file. If False, convert the field
        names to lowerCamelCase.
    indent: The JSON object will be pretty-printed with this indent level.
        An indent level of 0 or negative will only insert newlines. If the
        indent level is None, no newlines will be inserted.
    sort_keys: If True, then the output will be sorted by field names.
    use_integers_for_enums: If true, print integers instead of enum names.
    descriptor_pool: A Descriptor Pool for resolving types. If None use the
        default.
    float_precision: If set, use this to specify float field valid digits.
    ensure_ascii: If True, strings with non-ASCII characters are escaped.
        If False, Unicode strings are returned unchanged.

  Returns:
    A string containing the JSON formatted protocol buffer message.
  '''
    printer = _Printer(including_default_value_fields, preserving_proto_field_name, use_integers_for_enums, descriptor_pool, float_precision = float_precision)
    return printer.ToJsonString(message, indent, sort_keys, ensure_ascii)


def MessageToDict(message, including_default_value_fields, preserving_proto_field_name, use_integers_for_enums, descriptor_pool, float_precision = (False, False, False, None, None)):
    '''Converts protobuf message to a dictionary.

  When the dictionary is encoded to JSON, it conforms to proto3 JSON spec.

  Args:
    message: The protocol buffers message instance to serialize.
    including_default_value_fields: If True, singular primitive fields,
        repeated fields, and map fields will always be serialized.  If
        False, only serialize non-empty fields.  Singular message fields
        and oneof fields are not affected by this option.
    preserving_proto_field_name: If True, use the original proto field
        names as defined in the .proto file. If False, convert the field
        names to lowerCamelCase.
    use_integers_for_enums: If true, print integers instead of enum names.
    descriptor_pool: A Descriptor Pool for resolving types. If None use the
        default.
    float_precision: If set, use this to specify float field valid digits.

  Returns:
    A dict representation of the protocol buffer message.
  '''
    printer = _Printer(including_default_value_fields, preserving_proto_field_name, use_integers_for_enums, descriptor_pool, float_precision = float_precision)
    return printer._MessageToJsonObject(message)


def _IsMapEntry(field):

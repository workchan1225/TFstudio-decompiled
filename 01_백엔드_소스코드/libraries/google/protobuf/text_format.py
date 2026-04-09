# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: text_format.pyc (Python 3.11)

"""Contains routines for printing protocol messages in text format.

Simple usage example::

  # Create a proto object and serialize it to a text proto string.
  message = my_proto_pb2.MyMessage(foo='bar')
  text_proto = text_format.MessageToString(message)

  # Parse a text proto string.
  message = text_format.Parse(text_proto, my_proto_pb2.MyMessage())
"""
__author__ = 'kenton@google.com (Kenton Varda)'
import encodings.raw_unicode_escape as encodings
import encodings.unicode_escape as encodings
import io
import math
import re
from google.protobuf.internal import decoder
from google.protobuf.internal import type_checkers
from google.protobuf import descriptor
from google.protobuf import text_encoding
from google.protobuf import unknown_fields
__all__ = [
    'MessageToString',
    'Parse',
    'PrintMessage',
    'PrintField',
    'PrintFieldValue',
    'Merge',
    'MessageToBytes']
_INTEGER_CHECKERS = (type_checkers.Uint32ValueChecker(), type_checkers.Int32ValueChecker(), type_checkers.Uint64ValueChecker(), type_checkers.Int64ValueChecker())
_FLOAT_INFINITY = re.compile('-?inf(?:inity)?f?$', re.IGNORECASE)
_FLOAT_NAN = re.compile('nanf?$', re.IGNORECASE)
_QUOTES = frozenset(("'", '"'))
_ANY_FULL_TYPE_NAME = 'google.protobuf.Any'
_DEBUG_STRING_SILENT_MARKER = '\t '

class Error(Exception):
    '''Top-level module error for text_format.'''
    pass


class ParseError(Error):
    pass
# WARNING: Decompyle incomplete


class TextWriter(object):
    
    def __init__(self, as_utf8):
        self._writer = io.StringIO()

    
    def write(self, val):
        return self._writer.write(val)

    
    def close(self):
        return self._writer.close()

    
    def getvalue(self):
        return self._writer.getvalue()



def MessageToString(message, as_utf8, as_one_line, use_short_repeated_primitives, pointy_brackets, use_index_order, float_format, double_format, use_field_number, descriptor_pool = None, indent = None, message_formatter = None, print_unknown_fields = (False, False, False, False, False, None, None, False, None, 0, None, False, False), force_colon = ('return', str)):
    '''Convert protobuf message to text format.

  Double values can be formatted compactly with 15 digits of
  precision (which is the most that IEEE 754 "double" can guarantee)
  using double_format=\'.15g\'. To ensure that converting to text and back to a
  proto will result in an identical value, double_format=\'.17g\' should be used.

  Args:
    message: The protocol buffers message.
    as_utf8: Return unescaped Unicode for non-ASCII characters.
    as_one_line: Don\'t introduce newlines between fields.
    use_short_repeated_primitives: Use short repeated format for primitives.
    pointy_brackets: If True, use angle brackets instead of curly braces for
      nesting.
    use_index_order: If True, fields of a proto message will be printed using
      the order defined in source code instead of the field number, extensions
      will be printed at the end of the message and their relative order is
      determined by the extension number. By default, use the field number
      order.
    float_format (str): If set, use this to specify float field formatting
      (per the "Format Specification Mini-Language"); otherwise, shortest float
      that has same value in wire will be printed. Also affect double field
      if double_format is not set but float_format is set.
    double_format (str): If set, use this to specify double field formatting
      (per the "Format Specification Mini-Language"); if it is not set but
      float_format is set, use float_format. Otherwise, use ``str()``
    use_field_number: If True, print field numbers instead of names.
    descriptor_pool (DescriptorPool): Descriptor pool used to resolve Any types.
    indent (int): The initial indent level, in terms of spaces, for pretty
      print.
    message_formatter (function(message, indent, as_one_line) -> unicode|None):
      Custom formatter for selected sub-messages (usually based on message
      type). Use to pretty print parts of the protobuf for easier diffing.
    print_unknown_fields: If True, unknown fields will be printed.
    force_colon: If set, a colon will be added after the field name even if the
      field is a proto message.

  Returns:
    str: A string of the text formatted protocol buffer message.
  '''
    out = TextWriter(as_utf8)
    printer = _Printer(out, indent, as_utf8, as_one_line, use_short_repeated_primitives, pointy_brackets, use_index_order, float_format, double_format, use_field_number, descriptor_pool, message_formatter, print_unknown_fields = print_unknown_fields, force_colon = force_colon)
    printer.PrintMessage(message)
    result = out.getvalue()
    out.close()
    if as_one_line:
        return result.rstrip()


def MessageToBytes(message = None, **kwargs):
    '''Convert protobuf message to encoded text format.  See MessageToString.'''
    pass
# WARNING: Decompyle incomplete


def _IsMapEntry(field):

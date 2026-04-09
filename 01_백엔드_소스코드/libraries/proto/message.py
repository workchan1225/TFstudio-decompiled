# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: message.pyc (Python 3.11)

import collections
import collections.abc as collections
import copy
import re
from typing import Any, Dict, List, Optional, Type
import warnings
import google.protobuf as google
from google.protobuf import descriptor_pb2
from google.protobuf import message
from google.protobuf.json_format import MessageToDict, MessageToJson, Parse
from proto import _file_info
from proto import _package_info
from proto.fields import Field
from proto.fields import MapField
from proto.fields import RepeatedField
from proto.marshal import Marshal
from proto.primitives import ProtoType
from proto.utils import has_upb
PROTOBUF_VERSION = google.protobuf.__version__
_upb = has_upb()

class MessageMeta(type):
    pass
# WARNING: Decompyle incomplete


def Message():
    '''Message'''
    pass
# WARNING: Decompyle incomplete

Message = <NODE:27>(Message, 'Message', metaclass = MessageMeta)

class _MessageInfo:
    '''Metadata about a message.

    Args:
        fields (Tuple[~.fields.Field]): The fields declared on the message.
        package (str): The proto package.
        full_name (str): The full name of the message.
        file_info (~._FileInfo): The file descriptor and messages for the
            file containing this message.
        marshal (~.Marshal): The marshal instance to which this message was
            automatically registered.
        options (~.descriptor_pb2.MessageOptions): Any options that were
            set on the message.
    '''
    
    def __init__(self = None, *, fields, package, full_name, marshal, options):
        self.package = package
        self.full_name = full_name
        self.options = options
        self.fields = (lambda .0: pass# WARNING: Decompyle incomplete
)(fields())
        self.fields_by_number = (lambda .0: pass# WARNING: Decompyle incomplete
)(fields())
        self.marshal = marshal
        self._pb = None

    pb = (lambda self = None: self._pb)()

__all__ = ('Message',)

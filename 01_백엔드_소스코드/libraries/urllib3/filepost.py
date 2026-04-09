# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: filepost.pyc (Python 3.11)

from __future__ import annotations
import binascii
import codecs
import os
import typing
from io import BytesIO
from fields import _TYPE_FIELD_VALUE_TUPLE, RequestField
writer = codecs.lookup('utf-8')[3]
_TYPE_FIELDS_SEQUENCE = typing.Sequence[typing.Union[(tuple[(str, _TYPE_FIELD_VALUE_TUPLE)], RequestField)]]
_TYPE_FIELDS = typing.Union[(_TYPE_FIELDS_SEQUENCE, typing.Mapping[(str, _TYPE_FIELD_VALUE_TUPLE)])]

def choose_boundary():
    '''
    Our embarrassingly-simple replacement for mimetools.choose_boundary.
    '''
    return binascii.hexlify(os.urandom(16)).decode()


def iter_field_objects(fields = None):
    '''
    Iterate over fields.

    Supports list of (k, v) tuples and dicts, and lists of
    :class:`~urllib3.fields.RequestField`.

    '''
    pass
# WARNING: Decompyle incomplete


def encode_multipart_formdata(fields = None, boundary = None):
    '''
    Encode a dictionary of ``fields`` using the multipart/form-data MIME format.

    :param fields:
        Dictionary of fields or list of (key, :class:`~urllib3.fields.RequestField`).
        Values are processed by :func:`urllib3.fields.RequestField.from_tuples`.

    :param boundary:
        If not specified, then a random boundary will be generated using
        :func:`urllib3.filepost.choose_boundary`.
    '''
    body = BytesIO()
# WARNING: Decompyle incomplete

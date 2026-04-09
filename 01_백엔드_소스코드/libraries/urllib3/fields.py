# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: fields.pyc (Python 3.11)

from __future__ import annotations
import email.utils as email
import mimetypes
import typing
_TYPE_FIELD_VALUE = typing.Union[(str, bytes)]
_TYPE_FIELD_VALUE_TUPLE = typing.Union[(_TYPE_FIELD_VALUE, tuple[(str, _TYPE_FIELD_VALUE)], tuple[(str, _TYPE_FIELD_VALUE, str)])]

def guess_content_type(filename = None, default = None):

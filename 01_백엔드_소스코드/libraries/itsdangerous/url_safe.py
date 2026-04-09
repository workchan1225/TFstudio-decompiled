# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: url_safe.pyc (Python 3.11)

from __future__ import annotations
import typing as t
import zlib
from _json import _CompactJSON
from encoding import base64_decode
from encoding import base64_encode
from exc import BadPayload
from serializer import _PDataSerializer
from serializer import Serializer
from timed import TimedSerializer

def URLSafeSerializerMixin():
    '''URLSafeSerializerMixin'''
    pass
# WARNING: Decompyle incomplete

URLSafeSerializerMixin = <NODE:27>(URLSafeSerializerMixin, 'URLSafeSerializerMixin', Serializer[str])

def URLSafeSerializer():
    '''URLSafeSerializer'''
    __doc__ = "Works like :class:`.Serializer` but dumps and loads into a URL\n    safe string consisting of the upper and lowercase character of the\n    alphabet as well as ``'_'``, ``'-'`` and ``'.'``.\n    "

URLSafeSerializer = <NODE:27>(URLSafeSerializer, 'URLSafeSerializer', URLSafeSerializerMixin, Serializer[str])

def URLSafeTimedSerializer():
    '''URLSafeTimedSerializer'''
    __doc__ = "Works like :class:`.TimedSerializer` but dumps and loads into a\n    URL safe string consisting of the upper and lowercase character of\n    the alphabet as well as ``'_'``, ``'-'`` and ``'.'``.\n    "

URLSafeTimedSerializer = <NODE:27>(URLSafeTimedSerializer, 'URLSafeTimedSerializer', URLSafeSerializerMixin, TimedSerializer[str])

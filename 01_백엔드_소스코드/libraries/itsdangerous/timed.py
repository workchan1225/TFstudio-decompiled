# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: timed.pyc (Python 3.11)

from __future__ import annotations
from collections.abc import abc as cabc
import time
import typing as t
from datetime import datetime
from datetime import timezone
from encoding import base64_decode
from encoding import base64_encode
from encoding import bytes_to_int
from encoding import int_to_bytes
from encoding import want_bytes
from exc import BadSignature
from exc import BadTimeSignature
from exc import SignatureExpired
from serializer import _TSerialized
from serializer import Serializer
from signer import Signer

class TimestampSigner(Signer):
    pass
# WARNING: Decompyle incomplete


def TimedSerializer():
    '''TimedSerializer'''
    pass
# WARNING: Decompyle incomplete

TimedSerializer = <NODE:27>(TimedSerializer, 'TimedSerializer', Serializer[_TSerialized])

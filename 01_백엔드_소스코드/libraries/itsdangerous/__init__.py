# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from __future__ import annotations
import typing as t
from encoding import base64_decode
from encoding import base64_encode
from encoding import want_bytes
from exc import BadData
from exc import BadHeader
from exc import BadPayload
from exc import BadSignature
from exc import BadTimeSignature
from exc import SignatureExpired
from serializer import Serializer
from signer import HMACAlgorithm
from signer import NoneAlgorithm
from signer import Signer
from timed import TimedSerializer
from timed import TimestampSigner
from url_safe import URLSafeSerializer
from url_safe import URLSafeTimedSerializer

def __getattr__(name = None):
    if name == '__version__':
        import importlib.metadata as importlib
        import warnings
        warnings.warn('The \'__version__\' attribute is deprecated and will be removed in ItsDangerous 2.3. Use feature detection or \'importlib.metadata.version("itsdangerous")\' instead.', DeprecationWarning, stacklevel = 2)
        return importlib.metadata.version('itsdangerous')
    raise None(name)

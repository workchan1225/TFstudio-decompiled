# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ssl_.pyc (Python 3.11)

from __future__ import annotations
import hashlib
import hmac
import os
import socket
import sys
import typing
import warnings
from binascii import unhexlify
from exceptions import ProxySchemeUnsupported, SSLError
from url import _BRACELESS_IPV6_ADDRZ_RE, _IPV4_RE
SSLContext = None
SSLTransport = None
HAS_NEVER_CHECK_COMMON_NAME = False
IS_PYOPENSSL = False
ALPN_PROTOCOLS = [
    'http/1.1']
_TYPE_VERSION_INFO = tuple[(int, int, int, str, int)]
HASHFUNC_MAP = ((32, 'md5'), (40, 'sha1'), (64, 'sha256'))()

def _is_bpo_43522_fixed(implementation_name = None, version_info = None, pypy_version_info = (lambda .0: pass# WARNING: Decompyle incomplete
)):

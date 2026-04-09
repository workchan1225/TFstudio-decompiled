# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: jwt.pyc (Python 3.11)

__doc__ = "JSON Web Tokens\n\nProvides support for creating (encoding) and verifying (decoding) JWTs,\nespecially JWTs generated and consumed by Google infrastructure.\n\nSee `rfc7519`_ for more details on JWTs.\n\nTo encode a JWT use :func:`encode`::\n\n    from google.auth import crypt\n    from google.auth import jwt\n\n    signer = crypt.Signer(private_key)\n    payload = {'some': 'payload'}\n    encoded = jwt.encode(signer, payload)\n\nTo decode a JWT and verify claims use :func:`decode`::\n\n    claims = jwt.decode(encoded, certs=public_certs)\n\nYou can also skip verification::\n\n    claims = jwt.decode(encoded, verify=False)\n\n.. _rfc7519: https://tools.ietf.org/html/rfc7519\n\n"

try:
    from collections.abc import Mapping
except ImportError:
    from collections import Mapping

import copy
import datetime
import json
import urllib
import cachetools
from google.auth import _helpers
from google.auth import _service_account_info
from google.auth import crypt
from google.auth import exceptions
import google.auth.credentials as google

try:
    from google.auth.crypt import es256
except ImportError:
    es256 = None

_DEFAULT_TOKEN_LIFETIME_SECS = 3600
_DEFAULT_MAX_CACHE_SIZE = 10
_ALGORITHM_TO_VERIFIER_CLASS = {
    'RS256': crypt.RSAVerifier }
_CRYPTOGRAPHY_BASED_ALGORITHMS = frozenset([
    'ES256'])
# WARNING: Decompyle incomplete

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: drm.pyc (Python 3.11)

"""DRM module is used to handle DRM operations with clock skew correction.
Currently the only DRM operation is generating the Sec-MS-GEC token value
used in all API requests to Microsoft Edge's online text-to-speech service."""
import hashlib
import secrets
from datetime import datetime as dt
from datetime import timezone as tz
from typing import Dict, Optional
import aiohttp
from constants import TRUSTED_CLIENT_TOKEN
from exceptions import SkewAdjustmentError
WIN_EPOCH = 0x2B6109100
S_TO_NS = 1e+09

class DRM:
    '''
    Class to handle DRM operations with clock skew correction.
    '''
    clock_skew_seconds: float = 0
    adj_clock_skew_seconds = (lambda skew_seconds = None: pass)()
    get_unix_timestamp = (lambda : dt.now(tz.utc).timestamp() + DRM.clock_skew_seconds)()
    parse_rfc2616_date = (lambda date = None: try:
dt.strptime(date, '%a, %d %b %Y %H:%M:%S %Z').replace(tzinfo = tz.utc).timestamp()except ValueError:
None)()
    handle_client_response_error = (lambda e = None: pass# WARNING: Decompyle incomplete
)()
    generate_sec_ms_gec = (lambda : ticks = DRM.get_unix_timestamp()ticks += WIN_EPOCHticks -= ticks % 300ticks *= S_TO_NS / 100str_to_hash = f'''{ticks:.0f}{TRUSTED_CLIENT_TOKEN}'''hashlib.sha256(str_to_hash.encode('ascii')).hexdigest().upper())()
    generate_muid = (lambda : secrets.token_hex(16).upper())()
    headers_with_muid = (lambda headers = None: combined_headers = headers.copy()# WARNING: Decompyle incomplete
)()

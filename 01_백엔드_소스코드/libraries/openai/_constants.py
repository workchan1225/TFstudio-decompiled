# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _constants.pyc (Python 3.11)

import httpx
RAW_RESPONSE_HEADER = 'X-Stainless-Raw-Response'
OVERRIDE_CAST_TO_HEADER = '____stainless_override_cast_to'
DEFAULT_TIMEOUT = httpx.Timeout(timeout = 600, connect = 5)
DEFAULT_MAX_RETRIES = 2
DEFAULT_CONNECTION_LIMITS = httpx.Limits(max_connections = 1000, max_keepalive_connections = 100)
INITIAL_RETRY_DELAY = 0.5
MAX_RETRY_DELAY = 8

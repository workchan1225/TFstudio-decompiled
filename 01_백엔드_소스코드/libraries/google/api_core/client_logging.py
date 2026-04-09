# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: client_logging.pyc (Python 3.11)

import logging
import json
import os
from typing import List, Optional
_LOGGING_INITIALIZED = False
_BASE_LOGGER_NAME = 'google'
_recognized_logging_fields = [
    'httpRequest',
    'rpcName',
    'serviceName',
    'credentialsType',
    'credentialsInfo',
    'universeDomain',
    'request',
    'response',
    'metadata',
    'retryAttempt',
    'httpResponse']

def logger_configured(logger = None):

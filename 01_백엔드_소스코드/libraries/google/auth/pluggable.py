# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: pluggable.pyc (Python 3.11)

'''Pluggable Credentials.
Pluggable Credentials are initialized using external_account arguments which
are typically loaded from third-party executables. Unlike other
credentials that can be initialized with a list of explicit arguments, secrets
or credentials, external account clients use the environment and hints/guidelines
provided by the external_account JSON file to retrieve credentials and exchange
them for Google access tokens.

Example credential_source for pluggable credential:
{
    "executable": {
        "command": "/path/to/get/credentials.sh --arg1=value1 --arg2=value2",
        "timeout_millis": 5000,
        "output_file": "/path/to/generated/cached/credentials"
    }
}
'''

try:
    from collections.abc import Mapping
except ImportError:
    from collections import Mapping

import json
import os
import subprocess
import sys
import time
from google.auth import _helpers
from google.auth import exceptions
from google.auth import external_account
EXECUTABLE_SUPPORTED_MAX_VERSION = 1
EXECUTABLE_TIMEOUT_MILLIS_DEFAULT = 30000
EXECUTABLE_TIMEOUT_MILLIS_LOWER_BOUND = 5000
EXECUTABLE_TIMEOUT_MILLIS_UPPER_BOUND = 120000
EXECUTABLE_INTERACTIVE_TIMEOUT_MILLIS_LOWER_BOUND = 30000
EXECUTABLE_INTERACTIVE_TIMEOUT_MILLIS_UPPER_BOUND = 1800000

class Credentials(external_account.Credentials):
    pass
# WARNING: Decompyle incomplete

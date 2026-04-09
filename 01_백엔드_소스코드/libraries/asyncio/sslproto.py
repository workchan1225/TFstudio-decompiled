# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: sslproto.pyc (Python 3.11)

import collections
import enum
import warnings

try:
    import ssl
except ImportError:
    ssl = None

from  import constants
from  import exceptions
from  import protocols
from  import transports
from log import logger
# WARNING: Decompyle incomplete

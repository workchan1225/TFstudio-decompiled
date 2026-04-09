# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: constants.pyc (Python 3.11)

import enum
LOG_THRESHOLD_FOR_CONNLOST_WRITES = 5
ACCEPT_RETRY_DELAY = 1
DEBUG_STACK_DEPTH = 10
SSL_HANDSHAKE_TIMEOUT = 60
SSL_SHUTDOWN_TIMEOUT = 30
SENDFILE_FALLBACK_READBUFFER_SIZE = 262144
FLOW_CONTROL_HIGH_WATER_SSL_READ = 256
FLOW_CONTROL_HIGH_WATER_SSL_WRITE = 512

class _SendfileMode(enum.Enum):
    UNSUPPORTED = enum.auto()
    TRY_NATIVE = enum.auto()
    FALLBACK = enum.auto()

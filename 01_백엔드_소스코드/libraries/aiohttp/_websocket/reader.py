# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: reader.pyc (Python 3.11)

'''Reader for WebSocket protocol versions 13 and 8.'''
from typing import TYPE_CHECKING
from helpers import NO_EXTENSIONS
if TYPE_CHECKING or NO_EXTENSIONS:
    from reader_py import WebSocketDataQueue as WebSocketDataQueuePython, WebSocketReader as WebSocketReaderPython
    WebSocketReader = WebSocketReaderPython
    WebSocketDataQueue = WebSocketDataQueuePython
    return None

try:
    from reader_c import WebSocketDataQueue as WebSocketDataQueueCython, WebSocketReader as WebSocketReaderCython
    WebSocketReader = WebSocketReaderCython
    WebSocketDataQueue = WebSocketDataQueueCython
    return None
except ImportError:
    from reader_py import WebSocketDataQueue as WebSocketDataQueuePython, WebSocketReader as WebSocketReaderPython
    WebSocketReader = WebSocketReaderPython
    WebSocketDataQueue = WebSocketDataQueuePython
    return None

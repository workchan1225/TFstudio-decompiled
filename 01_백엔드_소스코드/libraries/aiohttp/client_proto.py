# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: client_proto.pyc (Python 3.11)

import asyncio
from contextlib import suppress
from typing import Any, Optional, Tuple, Union
from base_protocol import BaseProtocol
from client_exceptions import ClientConnectionError, ClientOSError, ClientPayloadError, ServerDisconnectedError, SocketTimeoutError
from helpers import _EXC_SENTINEL, EMPTY_BODY_STATUS_CODES, BaseTimerContext, set_exception, set_result
from http import HttpResponseParser, RawResponseMessage
from http_exceptions import HttpProcessingError
from streams import EMPTY_PAYLOAD, DataQueue, StreamReader

def ResponseHandler():
    '''ResponseHandler'''
    pass
# WARNING: Decompyle incomplete

ResponseHandler = <NODE:27>(ResponseHandler, 'ResponseHandler', BaseProtocol, DataQueue[Tuple[(RawResponseMessage, StreamReader)]])

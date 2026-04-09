# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _events.pyc (Python 3.11)

import re
from abc import ABC
from dataclasses import dataclass
from typing import List, Tuple, Union
from _abnf import method, request_target
from _headers import Headers, normalize_and_validate
from _util import bytesify, LocalProtocolError, validate
__all__ = [
    'Event',
    'Request',
    'InformationalResponse',
    'Response',
    'Data',
    'EndOfMessage',
    'ConnectionClosed']
method_re = re.compile(method.encode('ascii'))
request_target_re = re.compile(request_target.encode('ascii'))

class Event(ABC):
    '''
    Base class for h11 events.
    '''
    __slots__ = ()

Request = <NODE:12>()
_ResponseBase = <NODE:12>()
InformationalResponse = <NODE:12>()
Response = <NODE:12>()
Data = <NODE:12>()
EndOfMessage = <NODE:12>()
ConnectionClosed = <NODE:12>()

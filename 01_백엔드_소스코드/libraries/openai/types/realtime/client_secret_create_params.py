# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: client_secret_create_params.pyc (Python 3.11)

from __future__ import annotations
from typing import Union
from typing_extensions import Literal, TypeAlias, TypedDict
from realtime_session_create_request_param import RealtimeSessionCreateRequestParam
from realtime_transcription_session_create_request_param import RealtimeTranscriptionSessionCreateRequestParam
__all__ = [
    'ClientSecretCreateParams',
    'ExpiresAfter',
    'Session']

def ClientSecretCreateParams():
    '''ClientSecretCreateParams'''
    session: 'Session' = 'ClientSecretCreateParams'

ClientSecretCreateParams = <NODE:27>(ClientSecretCreateParams, 'ClientSecretCreateParams', TypedDict, total = False)

def ExpiresAfter():
    '''ExpiresAfter'''
    seconds: 'int' = 'Configuration for the client secret expiration.\n\n    Expiration refers to the time after which\n    a client secret will no longer be valid for creating sessions. The session itself may\n    continue after that time once started. A secret can be used to create multiple sessions\n    until it expires.\n    '

ExpiresAfter = <NODE:27>(ExpiresAfter, 'ExpiresAfter', TypedDict, total = False)
Session: 'TypeAlias' = Union[(RealtimeSessionCreateRequestParam, RealtimeTranscriptionSessionCreateRequestParam)]

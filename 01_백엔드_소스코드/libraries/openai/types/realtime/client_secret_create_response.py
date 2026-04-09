# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: client_secret_create_response.pyc (Python 3.11)

from typing import Union
from typing_extensions import Annotated, TypeAlias
from _utils import PropertyInfo
from _models import BaseModel
from realtime_session_create_response import RealtimeSessionCreateResponse
from realtime_transcription_session_create_response import RealtimeTranscriptionSessionCreateResponse
__all__ = [
    'ClientSecretCreateResponse',
    'Session']
Session: TypeAlias = Annotated[(Union[(RealtimeSessionCreateResponse, RealtimeTranscriptionSessionCreateResponse)], PropertyInfo(discriminator = 'type'))]

class ClientSecretCreateResponse(BaseModel):
    value: str = 'Response from creating a session and client secret for the Realtime API.'

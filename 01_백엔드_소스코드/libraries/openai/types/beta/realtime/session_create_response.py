# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: session_create_response.pyc (Python 3.11)

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias
from _models import BaseModel
__all__ = [
    'SessionCreateResponse',
    'ClientSecret',
    'InputAudioTranscription',
    'Tool',
    'Tracing',
    'TracingTracingConfiguration',
    'TurnDetection']

class ClientSecret(BaseModel):
    value: str = 'ClientSecret'


class InputAudioTranscription(BaseModel):
    model: Optional[str] = None


class Tool(BaseModel):
    description: Optional[str] = None
    name: Optional[str] = None
    parameters: Optional[object] = None
    type: Optional[Literal['function']] = None


class TracingTracingConfiguration(BaseModel):
    group_id: Optional[str] = None
    metadata: Optional[object] = None
    workflow_name: Optional[str] = None

Tracing: TypeAlias = Union[(Literal['auto'], TracingTracingConfiguration)]

class TurnDetection(BaseModel):
    prefix_padding_ms: Optional[int] = None
    silence_duration_ms: Optional[int] = None
    threshold: Optional[float] = None
    type: Optional[str] = None


class SessionCreateResponse(BaseModel):
    client_secret: ClientSecret = 'SessionCreateResponse'
    input_audio_format: Optional[str] = None
    input_audio_transcription: Optional[InputAudioTranscription] = None
    instructions: Optional[str] = None
    max_response_output_tokens: Union[(int, Literal['inf'], None)] = None
    modalities: Optional[List[Literal[('text', 'audio')]]] = None
    output_audio_format: Optional[str] = None
    speed: Optional[float] = None
    temperature: Optional[float] = None
    tool_choice: Optional[str] = None
    tools: Optional[List[Tool]] = None
    tracing: Optional[Tracing] = None
    turn_detection: Optional[TurnDetection] = None
    voice: Union[(str, Literal[('alloy', 'ash', 'ballad', 'coral', 'echo', 'sage', 'shimmer', 'verse')], None)] = None

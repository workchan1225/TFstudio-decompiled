# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_create_event.pyc (Python 3.11)

from typing import List, Union, Optional
from typing_extensions import Literal
from _models import BaseModel
from shared.metadata import Metadata
from conversation_item_with_reference import ConversationItemWithReference
__all__ = [
    'ResponseCreateEvent',
    'Response',
    'ResponseTool']

class ResponseTool(BaseModel):
    description: Optional[str] = None
    name: Optional[str] = None
    parameters: Optional[object] = None
    type: Optional[Literal['function']] = None


class Response(BaseModel):
    conversation: Union[(str, Literal[('auto', 'none')], None)] = None
    input: Optional[List[ConversationItemWithReference]] = None
    instructions: Optional[str] = None
    max_response_output_tokens: Union[(int, Literal['inf'], None)] = None
    metadata: Optional[Metadata] = None
    modalities: Optional[List[Literal[('text', 'audio')]]] = None
    output_audio_format: Optional[Literal[('pcm16', 'g711_ulaw', 'g711_alaw')]] = None
    temperature: Optional[float] = None
    tool_choice: Optional[str] = None
    tools: Optional[List[ResponseTool]] = None
    voice: Union[(str, Literal[('alloy', 'ash', 'ballad', 'coral', 'echo', 'sage', 'shimmer', 'verse')], None)] = None


class ResponseCreateEvent(BaseModel):
    type: Literal['response.create'] = 'ResponseCreateEvent'
    event_id: Optional[str] = None
    response: Optional[Response] = None

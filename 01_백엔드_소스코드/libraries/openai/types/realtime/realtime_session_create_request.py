# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: realtime_session_create_request.pyc (Python 3.11)

from typing import List, Union, Optional
from typing_extensions import Literal
from _models import BaseModel
from realtime_truncation import RealtimeTruncation
from realtime_audio_config import RealtimeAudioConfig
from realtime_tools_config import RealtimeToolsConfig
from realtime_tracing_config import RealtimeTracingConfig
from responses.response_prompt import ResponsePrompt
from realtime_tool_choice_config import RealtimeToolChoiceConfig
__all__ = [
    'RealtimeSessionCreateRequest']

class RealtimeSessionCreateRequest(BaseModel):
    type: Literal['realtime'] = 'Realtime session object configuration.'
    audio: Optional[RealtimeAudioConfig] = None
    include: Optional[List[Literal['item.input_audio_transcription.logprobs']]] = None
    instructions: Optional[str] = None
    max_output_tokens: Union[(int, Literal['inf'], None)] = None
    model: Union[(str, Literal[('gpt-realtime', 'gpt-realtime-2025-08-28', 'gpt-4o-realtime-preview', 'gpt-4o-realtime-preview-2024-10-01', 'gpt-4o-realtime-preview-2024-12-17', 'gpt-4o-realtime-preview-2025-06-03', 'gpt-4o-mini-realtime-preview', 'gpt-4o-mini-realtime-preview-2024-12-17', 'gpt-realtime-mini', 'gpt-realtime-mini-2025-10-06', 'gpt-realtime-mini-2025-12-15', 'gpt-audio-mini', 'gpt-audio-mini-2025-10-06', 'gpt-audio-mini-2025-12-15')], None)] = None
    output_modalities: Optional[List[Literal[('text', 'audio')]]] = None
    prompt: Optional[ResponsePrompt] = None
    tool_choice: Optional[RealtimeToolChoiceConfig] = None
    tools: Optional[RealtimeToolsConfig] = None
    tracing: Optional[RealtimeTracingConfig] = None
    truncation: Optional[RealtimeTruncation] = None

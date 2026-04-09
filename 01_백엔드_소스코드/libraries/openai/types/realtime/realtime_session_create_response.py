# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: realtime_session_create_response.pyc (Python 3.11)

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias
from _utils import PropertyInfo
from _models import BaseModel
from audio_transcription import AudioTranscription
from realtime_truncation import RealtimeTruncation
from noise_reduction_type import NoiseReductionType
from realtime_audio_formats import RealtimeAudioFormats
from realtime_function_tool import RealtimeFunctionTool
from responses.response_prompt import ResponsePrompt
from responses.tool_choice_mcp import ToolChoiceMcp
from responses.tool_choice_options import ToolChoiceOptions
from realtime_session_client_secret import RealtimeSessionClientSecret
from responses.tool_choice_function import ToolChoiceFunction
__all__ = [
    'RealtimeSessionCreateResponse',
    'Audio',
    'AudioInput',
    'AudioInputNoiseReduction',
    'AudioInputTurnDetection',
    'AudioInputTurnDetectionServerVad',
    'AudioInputTurnDetectionSemanticVad',
    'AudioOutput',
    'ToolChoice',
    'Tool',
    'ToolMcpTool',
    'ToolMcpToolAllowedTools',
    'ToolMcpToolAllowedToolsMcpToolFilter',
    'ToolMcpToolRequireApproval',
    'ToolMcpToolRequireApprovalMcpToolApprovalFilter',
    'ToolMcpToolRequireApprovalMcpToolApprovalFilterAlways',
    'ToolMcpToolRequireApprovalMcpToolApprovalFilterNever',
    'Tracing',
    'TracingTracingConfiguration']

class AudioInputNoiseReduction(BaseModel):
    '''Configuration for input audio noise reduction.

    This can be set to `null` to turn off.
    Noise reduction filters audio added to the input audio buffer before it is sent to VAD and the model.
    Filtering the audio can improve VAD and turn detection accuracy (reducing false positives) and model performance by improving perception of the input audio.
    '''
    type: Optional[NoiseReductionType] = None


class AudioInputTurnDetectionServerVad(BaseModel):
    type: Literal['server_vad'] = '\n    Server-side voice activity detection (VAD) which flips on when user speech is detected and off after a period of silence.\n    '
    create_response: Optional[bool] = None
    idle_timeout_ms: Optional[int] = None
    interrupt_response: Optional[bool] = None
    prefix_padding_ms: Optional[int] = None
    silence_duration_ms: Optional[int] = None
    threshold: Optional[float] = None


class AudioInputTurnDetectionSemanticVad(BaseModel):
    type: Literal['semantic_vad'] = '\n    Server-side semantic turn detection which uses a model to determine when the user has finished speaking.\n    '
    create_response: Optional[bool] = None
    eagerness: Optional[Literal[('low', 'medium', 'high', 'auto')]] = None
    interrupt_response: Optional[bool] = None

AudioInputTurnDetection: TypeAlias = Annotated[(Union[(AudioInputTurnDetectionServerVad, AudioInputTurnDetectionSemanticVad, None)], PropertyInfo(discriminator = 'type'))]

class AudioInput(BaseModel):
    format: Optional[RealtimeAudioFormats] = None
    noise_reduction: Optional[AudioInputNoiseReduction] = None
    transcription: Optional[AudioTranscription] = None
    turn_detection: Optional[AudioInputTurnDetection] = None


class AudioOutput(BaseModel):
    format: Optional[RealtimeAudioFormats] = None
    speed: Optional[float] = None
    voice: Union[(str, Literal[('alloy', 'ash', 'ballad', 'coral', 'echo', 'sage', 'shimmer', 'verse', 'marin', 'cedar')], None)] = None


class Audio(BaseModel):
    '''Configuration for input and output audio.'''
    input: Optional[AudioInput] = None
    output: Optional[AudioOutput] = None

ToolChoice: TypeAlias = Union[(ToolChoiceOptions, ToolChoiceFunction, ToolChoiceMcp)]

class ToolMcpToolAllowedToolsMcpToolFilter(BaseModel):
    '''A filter object to specify which tools are allowed.'''
    read_only: Optional[bool] = None
    tool_names: Optional[List[str]] = None

ToolMcpToolAllowedTools: TypeAlias = Union[(List[str], ToolMcpToolAllowedToolsMcpToolFilter, None)]

class ToolMcpToolRequireApprovalMcpToolApprovalFilterAlways(BaseModel):
    '''A filter object to specify which tools are allowed.'''
    read_only: Optional[bool] = None
    tool_names: Optional[List[str]] = None


class ToolMcpToolRequireApprovalMcpToolApprovalFilterNever(BaseModel):
    '''A filter object to specify which tools are allowed.'''
    read_only: Optional[bool] = None
    tool_names: Optional[List[str]] = None


class ToolMcpToolRequireApprovalMcpToolApprovalFilter(BaseModel):
    """Specify which of the MCP server's tools require approval.

    Can be
    `always`, `never`, or a filter object associated with tools
    that require approval.
    """
    always: Optional[ToolMcpToolRequireApprovalMcpToolApprovalFilterAlways] = None
    never: Optional[ToolMcpToolRequireApprovalMcpToolApprovalFilterNever] = None

ToolMcpToolRequireApproval: TypeAlias = Union[(ToolMcpToolRequireApprovalMcpToolApprovalFilter, Literal[('always', 'never')], None)]

class ToolMcpTool(BaseModel):
    type: Literal['mcp'] = '\n    Give the model access to additional tools via remote Model Context Protocol\n    (MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).\n    '
    allowed_tools: Optional[ToolMcpToolAllowedTools] = None
    authorization: Optional[str] = None
    connector_id: Optional[Literal[('connector_dropbox', 'connector_gmail', 'connector_googlecalendar', 'connector_googledrive', 'connector_microsoftteams', 'connector_outlookcalendar', 'connector_outlookemail', 'connector_sharepoint')]] = None
    headers: Optional[Dict[(str, str)]] = None
    require_approval: Optional[ToolMcpToolRequireApproval] = None
    server_description: Optional[str] = None
    server_url: Optional[str] = None

Tool: TypeAlias = Union[(RealtimeFunctionTool, ToolMcpTool)]

class TracingTracingConfiguration(BaseModel):
    '''Granular configuration for tracing.'''
    group_id: Optional[str] = None
    metadata: Optional[object] = None
    workflow_name: Optional[str] = None

Tracing: TypeAlias = Union[(Literal['auto'], TracingTracingConfiguration, None)]

class RealtimeSessionCreateResponse(BaseModel):
    type: Literal['realtime'] = 'A new Realtime session configuration, with an ephemeral key.\n\n    Default TTL\n    for keys is one minute.\n    '
    audio: Optional[Audio] = None
    include: Optional[List[Literal['item.input_audio_transcription.logprobs']]] = None
    instructions: Optional[str] = None
    max_output_tokens: Union[(int, Literal['inf'], None)] = None
    model: Union[(str, Literal[('gpt-realtime', 'gpt-realtime-2025-08-28', 'gpt-4o-realtime-preview', 'gpt-4o-realtime-preview-2024-10-01', 'gpt-4o-realtime-preview-2024-12-17', 'gpt-4o-realtime-preview-2025-06-03', 'gpt-4o-mini-realtime-preview', 'gpt-4o-mini-realtime-preview-2024-12-17', 'gpt-realtime-mini', 'gpt-realtime-mini-2025-10-06', 'gpt-realtime-mini-2025-12-15', 'gpt-audio-mini', 'gpt-audio-mini-2025-10-06', 'gpt-audio-mini-2025-12-15')], None)] = None
    output_modalities: Optional[List[Literal[('text', 'audio')]]] = None
    prompt: Optional[ResponsePrompt] = None
    tool_choice: Optional[ToolChoice] = None
    tools: Optional[List[Tool]] = None
    tracing: Optional[Tracing] = None
    truncation: Optional[RealtimeTruncation] = None

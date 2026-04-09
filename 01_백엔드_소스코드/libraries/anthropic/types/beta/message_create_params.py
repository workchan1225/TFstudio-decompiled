# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: message_create_params.pyc (Python 3.11)

from __future__ import annotations
from typing import List, Union, Generic, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict
from _types import SequenceNotStr
from _utils import PropertyInfo
from model_param import ModelParam
from beta_message_param import BetaMessageParam
from beta_metadata_param import BetaMetadataParam
from parsed_beta_message import ResponseFormatT
from anthropic_beta_param import AnthropicBetaParam
from beta_container_params import BetaContainerParams
from beta_text_block_param import BetaTextBlockParam
from beta_tool_union_param import BetaToolUnionParam
from beta_tool_choice_param import BetaToolChoiceParam
from beta_output_config_param import BetaOutputConfigParam
from beta_thinking_config_param import BetaThinkingConfigParam
from beta_json_output_format_param import BetaJSONOutputFormatParam
from beta_context_management_config_param import BetaContextManagementConfigParam
from beta_request_mcp_server_url_definition_param import BetaRequestMCPServerURLDefinitionParam
__all__ = [
    'MessageCreateParamsBase',
    'Container',
    'MessageCreateParamsNonStreaming',
    'MessageCreateParamsStreaming',
    'OutputFormat']

def MessageCreateParamsBase():
    '''MessageCreateParamsBase'''
    betas: "Annotated[List[AnthropicBetaParam], PropertyInfo(alias='anthropic-beta')]" = 'MessageCreateParamsBase'

MessageCreateParamsBase = <NODE:27>(MessageCreateParamsBase, 'MessageCreateParamsBase', TypedDict, total = False)
Container: 'TypeAlias' = Union[(BetaContainerParams, str)]

def ParseMessageCreateParamsBase():
    '''ParseMessageCreateParamsBase'''
    output_format: 'type[ResponseFormatT]' = 'ParseMessageCreateParamsBase'

ParseMessageCreateParamsBase = <NODE:27>(ParseMessageCreateParamsBase, 'ParseMessageCreateParamsBase', MessageCreateParamsBase, Generic[ResponseFormatT])

def OutputFormat():
    '''OutputFormat'''
    type: "Required[Literal['json_schema']]" = 'OutputFormat'

OutputFormat = <NODE:27>(OutputFormat, 'OutputFormat', TypedDict, total = False)

def MessageCreateParamsNonStreaming():
    '''MessageCreateParamsNonStreaming'''
    stream: 'Literal[False]' = 'MessageCreateParamsNonStreaming'

MessageCreateParamsNonStreaming = <NODE:27>(MessageCreateParamsNonStreaming, 'MessageCreateParamsNonStreaming', MessageCreateParamsBase, total = False)

class MessageCreateParamsStreaming(MessageCreateParamsBase):
    stream: 'Required[Literal[True]]' = 'MessageCreateParamsStreaming'

MessageCreateParams = Union[(MessageCreateParamsNonStreaming, MessageCreateParamsStreaming)]

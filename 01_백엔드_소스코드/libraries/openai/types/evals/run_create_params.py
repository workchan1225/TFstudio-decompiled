# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: run_create_params.pyc (Python 3.11)

from __future__ import annotations
from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict
from _types import SequenceNotStr
from responses.tool_param import ToolParam
from shared_params.metadata import Metadata
from shared.reasoning_effort import ReasoningEffort
from graders.grader_inputs_param import GraderInputsParam
from responses.response_input_text_param import ResponseInputTextParam
from responses.response_input_audio_param import ResponseInputAudioParam
from create_eval_jsonl_run_data_source_param import CreateEvalJSONLRunDataSourceParam
from responses.response_format_text_config_param import ResponseFormatTextConfigParam
from create_eval_completions_run_data_source_param import CreateEvalCompletionsRunDataSourceParam
__all__ = [
    'RunCreateParams',
    'DataSource',
    'DataSourceCreateEvalResponsesRunDataSource',
    'DataSourceCreateEvalResponsesRunDataSourceSource',
    'DataSourceCreateEvalResponsesRunDataSourceSourceFileContent',
    'DataSourceCreateEvalResponsesRunDataSourceSourceFileContentContent',
    'DataSourceCreateEvalResponsesRunDataSourceSourceFileID',
    'DataSourceCreateEvalResponsesRunDataSourceSourceResponses',
    'DataSourceCreateEvalResponsesRunDataSourceInputMessages',
    'DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplate',
    'DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplate',
    'DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateChatMessage',
    'DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateEvalItem',
    'DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateEvalItemContent',
    'DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateEvalItemContentOutputText',
    'DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateEvalItemContentInputImage',
    'DataSourceCreateEvalResponsesRunDataSourceInputMessagesItemReference',
    'DataSourceCreateEvalResponsesRunDataSourceSamplingParams',
    'DataSourceCreateEvalResponsesRunDataSourceSamplingParamsText']

def RunCreateParams():
    '''RunCreateParams'''
    name: 'str' = 'RunCreateParams'

RunCreateParams = <NODE:27>(RunCreateParams, 'RunCreateParams', TypedDict, total = False)

def DataSourceCreateEvalResponsesRunDataSourceSourceFileContentContent():
    '''DataSourceCreateEvalResponsesRunDataSourceSourceFileContentContent'''
    sample: 'Dict[str, object]' = 'DataSourceCreateEvalResponsesRunDataSourceSourceFileContentContent'

DataSourceCreateEvalResponsesRunDataSourceSourceFileContentContent = <NODE:27>(DataSourceCreateEvalResponsesRunDataSourceSourceFileContentContent, 'DataSourceCreateEvalResponsesRunDataSourceSourceFileContentContent', TypedDict, total = False)

def DataSourceCreateEvalResponsesRunDataSourceSourceFileContent():
    '''DataSourceCreateEvalResponsesRunDataSourceSourceFileContent'''
    type: "Required[Literal['file_content']]" = 'DataSourceCreateEvalResponsesRunDataSourceSourceFileContent'

DataSourceCreateEvalResponsesRunDataSourceSourceFileContent = <NODE:27>(DataSourceCreateEvalResponsesRunDataSourceSourceFileContent, 'DataSourceCreateEvalResponsesRunDataSourceSourceFileContent', TypedDict, total = False)

def DataSourceCreateEvalResponsesRunDataSourceSourceFileID():
    '''DataSourceCreateEvalResponsesRunDataSourceSourceFileID'''
    type: "Required[Literal['file_id']]" = 'DataSourceCreateEvalResponsesRunDataSourceSourceFileID'

DataSourceCreateEvalResponsesRunDataSourceSourceFileID = <NODE:27>(DataSourceCreateEvalResponsesRunDataSourceSourceFileID, 'DataSourceCreateEvalResponsesRunDataSourceSourceFileID', TypedDict, total = False)

def DataSourceCreateEvalResponsesRunDataSourceSourceResponses():
    '''DataSourceCreateEvalResponsesRunDataSourceSourceResponses'''
    users: 'Optional[SequenceNotStr[str]]' = 'A EvalResponsesSource object describing a run data source configuration.'

DataSourceCreateEvalResponsesRunDataSourceSourceResponses = <NODE:27>(DataSourceCreateEvalResponsesRunDataSourceSourceResponses, 'DataSourceCreateEvalResponsesRunDataSourceSourceResponses', TypedDict, total = False)
DataSourceCreateEvalResponsesRunDataSourceSource: 'TypeAlias' = Union[(DataSourceCreateEvalResponsesRunDataSourceSourceFileContent, DataSourceCreateEvalResponsesRunDataSourceSourceFileID, DataSourceCreateEvalResponsesRunDataSourceSourceResponses)]

def DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateChatMessage():
    '''DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateChatMessage'''
    role: 'Required[str]' = 'DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateChatMessage'

DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateChatMessage = <NODE:27>(DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateChatMessage, 'DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateChatMessage', TypedDict, total = False)

def DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateEvalItemContentOutputText():
    '''DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateEvalItemContentOutputText'''
    type: "Required[Literal['output_text']]" = 'A text output from the model.'

DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateEvalItemContentOutputText = <NODE:27>(DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateEvalItemContentOutputText, 'DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateEvalItemContentOutputText', TypedDict, total = False)

def DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateEvalItemContentInputImage():
    '''DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateEvalItemContentInputImage'''
    detail: 'str' = 'An image input block used within EvalItem content arrays.'

DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateEvalItemContentInputImage = <NODE:27>(DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateEvalItemContentInputImage, 'DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateEvalItemContentInputImage', TypedDict, total = False)
DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateEvalItemContent: 'TypeAlias' = Union[(str, ResponseInputTextParam, DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateEvalItemContentOutputText, DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateEvalItemContentInputImage, ResponseInputAudioParam, GraderInputsParam)]

def DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateEvalItem():
    '''DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateEvalItem'''
    type: "Literal['message']" = '\n    A message input to the model with a role indicating instruction following\n    hierarchy. Instructions given with the `developer` or `system` role take\n    precedence over instructions given with the `user` role. Messages with the\n    `assistant` role are presumed to have been generated by the model in previous\n    interactions.\n    '

DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateEvalItem = <NODE:27>(DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateEvalItem, 'DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateEvalItem', TypedDict, total = False)
DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplate: 'TypeAlias' = Union[(DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateChatMessage, DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateEvalItem)]

def DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplate():
    '''DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplate'''
    type: "Required[Literal['template']]" = 'DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplate'

DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplate = <NODE:27>(DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplate, 'DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplate', TypedDict, total = False)

def DataSourceCreateEvalResponsesRunDataSourceInputMessagesItemReference():
    '''DataSourceCreateEvalResponsesRunDataSourceInputMessagesItemReference'''
    type: "Required[Literal['item_reference']]" = 'DataSourceCreateEvalResponsesRunDataSourceInputMessagesItemReference'

DataSourceCreateEvalResponsesRunDataSourceInputMessagesItemReference = <NODE:27>(DataSourceCreateEvalResponsesRunDataSourceInputMessagesItemReference, 'DataSourceCreateEvalResponsesRunDataSourceInputMessagesItemReference', TypedDict, total = False)
DataSourceCreateEvalResponsesRunDataSourceInputMessages: 'TypeAlias' = Union[(DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplate, DataSourceCreateEvalResponsesRunDataSourceInputMessagesItemReference)]

def DataSourceCreateEvalResponsesRunDataSourceSamplingParamsText():
    '''DataSourceCreateEvalResponsesRunDataSourceSamplingParamsText'''
    format: 'ResponseFormatTextConfigParam' = 'Configuration options for a text response from the model.\n\n    Can be plain\n    text or structured JSON data. Learn more:\n    - [Text inputs and outputs](https://platform.openai.com/docs/guides/text)\n    - [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)\n    '

DataSourceCreateEvalResponsesRunDataSourceSamplingParamsText = <NODE:27>(DataSourceCreateEvalResponsesRunDataSourceSamplingParamsText, 'DataSourceCreateEvalResponsesRunDataSourceSamplingParamsText', TypedDict, total = False)

def DataSourceCreateEvalResponsesRunDataSourceSamplingParams():
    '''DataSourceCreateEvalResponsesRunDataSourceSamplingParams'''
    top_p: 'float' = 'DataSourceCreateEvalResponsesRunDataSourceSamplingParams'

DataSourceCreateEvalResponsesRunDataSourceSamplingParams = <NODE:27>(DataSourceCreateEvalResponsesRunDataSourceSamplingParams, 'DataSourceCreateEvalResponsesRunDataSourceSamplingParams', TypedDict, total = False)

def DataSourceCreateEvalResponsesRunDataSource():
    '''DataSourceCreateEvalResponsesRunDataSource'''
    sampling_params: 'DataSourceCreateEvalResponsesRunDataSourceSamplingParams' = 'A ResponsesRunDataSource object describing a model sampling configuration.'

DataSourceCreateEvalResponsesRunDataSource = <NODE:27>(DataSourceCreateEvalResponsesRunDataSource, 'DataSourceCreateEvalResponsesRunDataSource', TypedDict, total = False)
DataSource: 'TypeAlias' = Union[(CreateEvalJSONLRunDataSourceParam, CreateEvalCompletionsRunDataSourceParam, DataSourceCreateEvalResponsesRunDataSource)]

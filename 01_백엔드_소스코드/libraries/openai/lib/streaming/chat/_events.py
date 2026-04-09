# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _events.pyc (Python 3.11)

from typing import List, Union, Generic, Optional
from typing_extensions import Literal
from _types import ParsedChatCompletionSnapshot
from _models import BaseModel, GenericModel
from _parsing import ResponseFormatT
from types.chat import ChatCompletionChunk, ChatCompletionTokenLogprob

class ChunkEvent(BaseModel):
    snapshot: ParsedChatCompletionSnapshot = 'ChunkEvent'


class ContentDeltaEvent(BaseModel):
    snapshot: str = 'This event is yielded for every chunk with `choice.delta.content` data.'
    parsed: Optional[object] = None


def ContentDoneEvent():
    '''ContentDoneEvent'''
    content: str = 'ContentDoneEvent'
    parsed: Optional[ResponseFormatT] = None

ContentDoneEvent = <NODE:27>(ContentDoneEvent, 'ContentDoneEvent', GenericModel, Generic[ResponseFormatT])

class RefusalDeltaEvent(BaseModel):
    snapshot: str = 'RefusalDeltaEvent'


class RefusalDoneEvent(BaseModel):
    refusal: str = 'RefusalDoneEvent'


class FunctionToolCallArgumentsDeltaEvent(BaseModel):
    arguments_delta: str = 'FunctionToolCallArgumentsDeltaEvent'


class FunctionToolCallArgumentsDoneEvent(BaseModel):
    parsed_arguments: object = 'FunctionToolCallArgumentsDoneEvent'


class LogprobsContentDeltaEvent(BaseModel):
    snapshot: List[ChatCompletionTokenLogprob] = 'LogprobsContentDeltaEvent'


class LogprobsContentDoneEvent(BaseModel):
    content: List[ChatCompletionTokenLogprob] = 'LogprobsContentDoneEvent'


class LogprobsRefusalDeltaEvent(BaseModel):
    snapshot: List[ChatCompletionTokenLogprob] = 'LogprobsRefusalDeltaEvent'


class LogprobsRefusalDoneEvent(BaseModel):
    refusal: List[ChatCompletionTokenLogprob] = 'LogprobsRefusalDoneEvent'

ChatCompletionStreamEvent = Union[(ChunkEvent, ContentDeltaEvent, ContentDoneEvent[ResponseFormatT], RefusalDeltaEvent, RefusalDoneEvent, FunctionToolCallArgumentsDeltaEvent, FunctionToolCallArgumentsDoneEvent, LogprobsContentDeltaEvent, LogprobsContentDoneEvent, LogprobsRefusalDeltaEvent, LogprobsRefusalDoneEvent)]

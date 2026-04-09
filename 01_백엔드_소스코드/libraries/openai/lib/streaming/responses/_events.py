# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _events.pyc (Python 3.11)

from __future__ import annotations
from typing import Optional
from typing_extensions import Union, Generic, TypeVar, Annotated, TypeAlias
from _utils import PropertyInfo
from _compat import GenericModel
from types.responses import ParsedResponse, ResponseErrorEvent, ResponseFailedEvent, ResponseQueuedEvent, ResponseCreatedEvent, ResponseTextDoneEvent as RawResponseTextDoneEvent, ResponseAudioDoneEvent, ResponseCompletedEvent as RawResponseCompletedEvent, ResponseTextDeltaEvent as RawResponseTextDeltaEvent, ResponseAudioDeltaEvent, ResponseIncompleteEvent, ResponseInProgressEvent, ResponseRefusalDoneEvent, ResponseRefusalDeltaEvent, ResponseMcpCallFailedEvent, ResponseOutputItemDoneEvent, ResponseContentPartDoneEvent, ResponseOutputItemAddedEvent, ResponseContentPartAddedEvent, ResponseMcpCallCompletedEvent, ResponseMcpCallInProgressEvent, ResponseMcpListToolsFailedEvent, ResponseAudioTranscriptDoneEvent, ResponseAudioTranscriptDeltaEvent, ResponseMcpCallArgumentsDoneEvent, ResponseImageGenCallCompletedEvent, ResponseMcpCallArgumentsDeltaEvent, ResponseMcpListToolsCompletedEvent, ResponseImageGenCallGeneratingEvent, ResponseImageGenCallInProgressEvent, ResponseMcpListToolsInProgressEvent, ResponseWebSearchCallCompletedEvent, ResponseWebSearchCallSearchingEvent, ResponseCustomToolCallInputDoneEvent, ResponseFileSearchCallCompletedEvent, ResponseFileSearchCallSearchingEvent, ResponseWebSearchCallInProgressEvent, ResponseCustomToolCallInputDeltaEvent, ResponseFileSearchCallInProgressEvent, ResponseImageGenCallPartialImageEvent, ResponseReasoningSummaryPartDoneEvent, ResponseReasoningSummaryTextDoneEvent, ResponseFunctionCallArgumentsDoneEvent, ResponseOutputTextAnnotationAddedEvent, ResponseReasoningSummaryPartAddedEvent, ResponseReasoningSummaryTextDeltaEvent, ResponseFunctionCallArgumentsDeltaEvent as RawResponseFunctionCallArgumentsDeltaEvent, ResponseCodeInterpreterCallCodeDoneEvent, ResponseCodeInterpreterCallCodeDeltaEvent, ResponseCodeInterpreterCallCompletedEvent, ResponseCodeInterpreterCallInProgressEvent, ResponseCodeInterpreterCallInterpretingEvent
from types.responses.response_reasoning_text_done_event import ResponseReasoningTextDoneEvent
from types.responses.response_reasoning_text_delta_event import ResponseReasoningTextDeltaEvent
TextFormatT = TypeVar('TextFormatT', default = None)

class ResponseTextDeltaEvent(RawResponseTextDeltaEvent):
    snapshot: 'str' = 'ResponseTextDeltaEvent'


def ResponseTextDoneEvent():
    '''ResponseTextDoneEvent'''
    parsed: 'Optional[TextFormatT]' = None

ResponseTextDoneEvent = <NODE:27>(ResponseTextDoneEvent, 'ResponseTextDoneEvent', RawResponseTextDoneEvent, GenericModel, Generic[TextFormatT])

class ResponseFunctionCallArgumentsDeltaEvent(RawResponseFunctionCallArgumentsDeltaEvent):
    snapshot: 'str' = 'ResponseFunctionCallArgumentsDeltaEvent'


def ResponseCompletedEvent():
    '''ResponseCompletedEvent'''
    response: 'ParsedResponse[TextFormatT]' = 'ResponseCompletedEvent'

ResponseCompletedEvent = <NODE:27>(ResponseCompletedEvent, 'ResponseCompletedEvent', RawResponseCompletedEvent, GenericModel, Generic[TextFormatT])
# WARNING: Decompyle incomplete

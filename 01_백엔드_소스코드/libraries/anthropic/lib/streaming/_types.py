# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _types.pyc (Python 3.11)

from typing import Union
from typing_extensions import List, Literal, Annotated
from types import Message, ContentBlock, MessageDeltaEvent as RawMessageDeltaEvent, MessageStartEvent as RawMessageStartEvent, RawMessageStopEvent, ContentBlockDeltaEvent as RawContentBlockDeltaEvent, ContentBlockStartEvent as RawContentBlockStartEvent, RawContentBlockStopEvent
from _models import BaseModel
from _utils._transform import PropertyInfo
from types.citations_delta import Citation

class TextEvent(BaseModel):
    snapshot: str = 'TextEvent'


class CitationEvent(BaseModel):
    snapshot: List[Citation] = 'CitationEvent'


class ThinkingEvent(BaseModel):
    snapshot: str = 'ThinkingEvent'


class SignatureEvent(BaseModel):
    signature: str = 'SignatureEvent'


class InputJsonEvent(BaseModel):
    snapshot: object = 'InputJsonEvent'


class MessageStopEvent(RawMessageStopEvent):
    message: Message = 'MessageStopEvent'


class ContentBlockStopEvent(RawContentBlockStopEvent):
    content_block: ContentBlock = 'ContentBlockStopEvent'

MessageStreamEvent = Annotated[(Union[(TextEvent, CitationEvent, ThinkingEvent, SignatureEvent, InputJsonEvent, RawMessageStartEvent, RawMessageDeltaEvent, MessageStopEvent, RawContentBlockStartEvent, RawContentBlockDeltaEvent, ContentBlockStopEvent)], PropertyInfo(discriminator = 'type'))]

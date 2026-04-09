# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _beta_types.pyc (Python 3.11)

from typing import TYPE_CHECKING, Any, Dict, Union, Generic, cast
from typing_extensions import List, Literal, Annotated
import jiter
from _models import BaseModel, GenericModel
from types.beta import BetaRawMessageStopEvent, BetaRawMessageDeltaEvent, BetaRawMessageStartEvent, BetaRawContentBlockStopEvent, BetaRawContentBlockDeltaEvent, BetaRawContentBlockStartEvent
from _parse._response import ResponseFormatT
from _utils._transform import PropertyInfo
from types.beta.parsed_beta_message import ParsedBetaMessage, ParsedBetaContentBlock
from types.beta.beta_citations_delta import Citation

class ParsedBetaTextEvent(BaseModel):
    snapshot: str = 'ParsedBetaTextEvent'
    
    def parsed_snapshot(self = None):
        return cast(Dict[(str, Any)], jiter.from_json(self.snapshot.encode('utf-8'), partial_mode = 'trailing-strings'))



class BetaCitationEvent(BaseModel):
    snapshot: List[Citation] = 'BetaCitationEvent'


class BetaThinkingEvent(BaseModel):
    snapshot: str = 'BetaThinkingEvent'


class BetaSignatureEvent(BaseModel):
    signature: str = 'BetaSignatureEvent'


class BetaInputJsonEvent(BaseModel):
    snapshot: object = 'BetaInputJsonEvent'


def ParsedBetaMessageStopEvent():
    '''ParsedBetaMessageStopEvent'''
    message: ParsedBetaMessage[ResponseFormatT] = 'ParsedBetaMessageStopEvent'

ParsedBetaMessageStopEvent = <NODE:27>(ParsedBetaMessageStopEvent, 'ParsedBetaMessageStopEvent', BetaRawMessageStopEvent, GenericModel, Generic[ResponseFormatT])

def ParsedBetaContentBlockStopEvent():
    '''ParsedBetaContentBlockStopEvent'''
    type: Literal['content_block_stop'] = 'ParsedBetaContentBlockStopEvent'
    if TYPE_CHECKING:
        content_block: ParsedBetaContentBlock[ResponseFormatT]
        return None
    content_block: None

ParsedBetaContentBlockStopEvent = <NODE:27>(ParsedBetaContentBlockStopEvent, 'ParsedBetaContentBlockStopEvent', BetaRawContentBlockStopEvent, GenericModel, Generic[ResponseFormatT])
ParsedBetaMessageStreamEvent = Annotated[(Union[(ParsedBetaTextEvent, BetaCitationEvent, BetaThinkingEvent, BetaSignatureEvent, BetaInputJsonEvent, BetaRawMessageStartEvent, BetaRawMessageDeltaEvent, ParsedBetaMessageStopEvent[ResponseFormatT], BetaRawContentBlockStartEvent, BetaRawContentBlockDeltaEvent, ParsedBetaContentBlockStopEvent[ResponseFormatT])], PropertyInfo(discriminator = 'type'))]

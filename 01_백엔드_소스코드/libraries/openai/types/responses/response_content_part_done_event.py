# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_content_part_done_event.pyc (Python 3.11)

from typing import Union
from typing_extensions import Literal, Annotated, TypeAlias
from _utils import PropertyInfo
from _models import BaseModel
from response_output_text import ResponseOutputText
from response_output_refusal import ResponseOutputRefusal
__all__ = [
    'ResponseContentPartDoneEvent',
    'Part',
    'PartReasoningText']

class PartReasoningText(BaseModel):
    type: Literal['reasoning_text'] = 'Reasoning text from the model.'

Part: TypeAlias = Annotated[(Union[(ResponseOutputText, ResponseOutputRefusal, PartReasoningText)], PropertyInfo(discriminator = 'type'))]

class ResponseContentPartDoneEvent(BaseModel):
    type: Literal['response.content_part.done'] = 'Emitted when a content part is done.'

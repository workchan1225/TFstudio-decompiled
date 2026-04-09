# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_reasoning_item.pyc (Python 3.11)

from typing import List, Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseReasoningItem',
    'Summary',
    'Content']

class Summary(BaseModel):
    type: Literal['summary_text'] = 'A summary text from the model.'


class Content(BaseModel):
    type: Literal['reasoning_text'] = 'Reasoning text from the model.'


class ResponseReasoningItem(BaseModel):
    type: Literal['reasoning'] = '\n    A description of the chain of thought used by a reasoning model while generating\n    a response. Be sure to include these items in your `input` to the Responses API\n    for subsequent turns of a conversation if you are manually\n    [managing context](https://platform.openai.com/docs/guides/conversation-state).\n    '
    content: Optional[List[Content]] = None
    encrypted_content: Optional[str] = None
    status: Optional[Literal[('in_progress', 'completed', 'incomplete')]] = None

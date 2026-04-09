# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: realtime_conversation_item_function_call_output.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'RealtimeConversationItemFunctionCallOutput']

class RealtimeConversationItemFunctionCallOutput(BaseModel):
    type: Literal['function_call_output'] = 'A function call output item in a Realtime conversation.'
    id: Optional[str] = None
    object: Optional[Literal['realtime.item']] = None
    status: Optional[Literal[('completed', 'incomplete', 'in_progress')]] = None

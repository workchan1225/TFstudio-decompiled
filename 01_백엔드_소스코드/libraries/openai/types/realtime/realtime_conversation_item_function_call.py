# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: realtime_conversation_item_function_call.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'RealtimeConversationItemFunctionCall']

class RealtimeConversationItemFunctionCall(BaseModel):
    type: Literal['function_call'] = 'A function call item in a Realtime conversation.'
    id: Optional[str] = None
    call_id: Optional[str] = None
    object: Optional[Literal['realtime.item']] = None
    status: Optional[Literal[('completed', 'incomplete', 'in_progress')]] = None

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: chat_session.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
from chatkit_workflow import ChatKitWorkflow
from chat_session_status import ChatSessionStatus
from chat_session_rate_limits import ChatSessionRateLimits
from chat_session_chatkit_configuration import ChatSessionChatKitConfiguration
__all__ = [
    'ChatSession']

class ChatSession(BaseModel):
    workflow: ChatKitWorkflow = 'Represents a ChatKit session and its resolved configuration.'

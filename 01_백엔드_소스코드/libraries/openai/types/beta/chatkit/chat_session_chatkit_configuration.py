# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: chat_session_chatkit_configuration.pyc (Python 3.11)

from _models import BaseModel
from chat_session_history import ChatSessionHistory
from chat_session_file_upload import ChatSessionFileUpload
from chat_session_automatic_thread_titling import ChatSessionAutomaticThreadTitling
__all__ = [
    'ChatSessionChatKitConfiguration']

class ChatSessionChatKitConfiguration(BaseModel):
    history: ChatSessionHistory = 'ChatKit configuration for the session.'

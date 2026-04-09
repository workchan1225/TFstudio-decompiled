# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: message.pyc (Python 3.11)

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias
from _models import BaseModel
from message_content import MessageContent
from shared.metadata import Metadata
from code_interpreter_tool import CodeInterpreterTool
__all__ = [
    'Message',
    'Attachment',
    'AttachmentTool',
    'AttachmentToolAssistantToolsFileSearchTypeOnly',
    'IncompleteDetails']

class AttachmentToolAssistantToolsFileSearchTypeOnly(BaseModel):
    type: Literal['file_search'] = 'AttachmentToolAssistantToolsFileSearchTypeOnly'

AttachmentTool: TypeAlias = Union[(CodeInterpreterTool, AttachmentToolAssistantToolsFileSearchTypeOnly)]

class Attachment(BaseModel):
    file_id: Optional[str] = None
    tools: Optional[List[AttachmentTool]] = None


class IncompleteDetails(BaseModel):
    reason: Literal[('content_filter', 'max_tokens', 'run_cancelled', 'run_expired', 'run_failed')] = 'On an incomplete message, details about why the message is incomplete.'


class Message(BaseModel):
    id: str = '\n    Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).\n    '
    assistant_id: Optional[str] = None
    attachments: Optional[List[Attachment]] = None
    created_at: int = None
    incomplete_at: Optional[int] = None
    incomplete_details: Optional[IncompleteDetails] = None
    role: Literal[('user', 'assistant')] = None
    thread_id: str = None

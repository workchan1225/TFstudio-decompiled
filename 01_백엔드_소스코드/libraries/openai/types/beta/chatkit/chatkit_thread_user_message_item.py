# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: chatkit_thread_user_message_item.pyc (Python 3.11)

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias
from _utils import PropertyInfo
from _models import BaseModel
from chatkit_attachment import ChatKitAttachment
__all__ = [
    'ChatKitThreadUserMessageItem',
    'Content',
    'ContentInputText',
    'ContentQuotedText',
    'InferenceOptions',
    'InferenceOptionsToolChoice']

class ContentInputText(BaseModel):
    type: Literal['input_text'] = 'Text block that a user contributed to the thread.'


class ContentQuotedText(BaseModel):
    type: Literal['quoted_text'] = 'Quoted snippet that the user referenced in their message.'

Content: TypeAlias = Annotated[(Union[(ContentInputText, ContentQuotedText)], PropertyInfo(discriminator = 'type'))]

class InferenceOptionsToolChoice(BaseModel):
    id: str = 'Preferred tool to invoke. Defaults to null when ChatKit should auto-select.'


class InferenceOptions(BaseModel):
    '''Inference overrides applied to the message. Defaults to null when unset.'''
    model: Optional[str] = None
    tool_choice: Optional[InferenceOptionsToolChoice] = None


class ChatKitThreadUserMessageItem(BaseModel):
    created_at: int = 'User-authored messages within a thread.'
    type: Literal['chatkit.user_message'] = None

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: chatkit_thread_item_list.pyc (Python 3.11)

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias
from _utils import PropertyInfo
from _models import BaseModel
from chatkit_widget_item import ChatKitWidgetItem
from chatkit_thread_user_message_item import ChatKitThreadUserMessageItem
from chatkit_thread_assistant_message_item import ChatKitThreadAssistantMessageItem
__all__ = [
    'ChatKitThreadItemList',
    'Data',
    'DataChatKitClientToolCall',
    'DataChatKitTask',
    'DataChatKitTaskGroup',
    'DataChatKitTaskGroupTask']

class DataChatKitClientToolCall(BaseModel):
    object: Literal['chatkit.thread_item'] = 'Record of a client side tool invocation initiated by the assistant.'
    type: Literal['chatkit.client_tool_call'] = None


class DataChatKitTask(BaseModel):
    created_at: int = 'Task emitted by the workflow to show progress and status updates.'
    object: Literal['chatkit.thread_item'] = None
    type: Literal['chatkit.task'] = None


class DataChatKitTaskGroupTask(BaseModel):
    '''Task entry that appears within a TaskGroup.'''
    heading: Optional[str] = None
    type: Literal[('custom', 'thought')] = None


class DataChatKitTaskGroup(BaseModel):
    type: Literal['chatkit.task_group'] = 'Collection of workflow tasks grouped together in the thread.'

Data: TypeAlias = Annotated[(Union[(ChatKitThreadUserMessageItem, ChatKitThreadAssistantMessageItem, ChatKitWidgetItem, DataChatKitClientToolCall, DataChatKitTask, DataChatKitTaskGroup)], PropertyInfo(discriminator = 'type'))]

class ChatKitThreadItemList(BaseModel):
    data: List[Data] = 'A paginated list of thread items rendered for the ChatKit API.'
    has_more: bool = None
    object: Literal['list'] = None

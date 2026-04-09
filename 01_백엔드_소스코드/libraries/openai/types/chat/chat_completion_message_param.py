# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: chat_completion_message_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Union
from typing_extensions import TypeAlias
from chat_completion_tool_message_param import ChatCompletionToolMessageParam
from chat_completion_user_message_param import ChatCompletionUserMessageParam
from chat_completion_system_message_param import ChatCompletionSystemMessageParam
from chat_completion_function_message_param import ChatCompletionFunctionMessageParam
from chat_completion_assistant_message_param import ChatCompletionAssistantMessageParam
from chat_completion_developer_message_param import ChatCompletionDeveloperMessageParam
__all__ = [
    'ChatCompletionMessageParam']
ChatCompletionMessageParam: 'TypeAlias' = Union[(ChatCompletionDeveloperMessageParam, ChatCompletionSystemMessageParam, ChatCompletionUserMessageParam, ChatCompletionAssistantMessageParam, ChatCompletionToolMessageParam, ChatCompletionFunctionMessageParam)]

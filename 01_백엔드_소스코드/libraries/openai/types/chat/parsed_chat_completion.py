# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: parsed_chat_completion.pyc (Python 3.11)

from typing import List, Generic, TypeVar, Optional
from _models import GenericModel
from chat_completion import Choice, ChatCompletion
from chat_completion_message import ChatCompletionMessage
from parsed_function_tool_call import ParsedFunctionToolCall
__all__ = [
    'ParsedChatCompletion',
    'ParsedChoice']
ContentType = TypeVar('ContentType')

def ParsedChatCompletionMessage():
    '''ParsedChatCompletionMessage'''
    parsed: Optional[ContentType] = None
    tool_calls: Optional[List[ParsedFunctionToolCall]] = None

ParsedChatCompletionMessage = <NODE:27>(ParsedChatCompletionMessage, 'ParsedChatCompletionMessage', ChatCompletionMessage, GenericModel, Generic[ContentType])

def ParsedChoice():
    '''ParsedChoice'''
    message: ParsedChatCompletionMessage[ContentType] = 'ParsedChoice'

ParsedChoice = <NODE:27>(ParsedChoice, 'ParsedChoice', Choice, GenericModel, Generic[ContentType])

def ParsedChatCompletion():
    '''ParsedChatCompletion'''
    choices: List[ParsedChoice[ContentType]] = 'ParsedChatCompletion'

ParsedChatCompletion = <NODE:27>(ParsedChatCompletion, 'ParsedChatCompletion', ChatCompletion, GenericModel, Generic[ContentType])

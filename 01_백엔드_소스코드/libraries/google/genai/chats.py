# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: chats.pyc (Python 3.11)

from collections.abc import Iterator
import sys
from typing import AsyncIterator, Awaitable, Optional, Union, get_args
from  import _transformers as t
from  import types
from models import AsyncModels, Models
from types import Content, ContentOrDict, GenerateContentConfigOrDict, GenerateContentResponse, Part, PartUnionDict
if sys.version_info >= (3, 10):
    from typing import TypeGuard
else:
    from typing_extensions import TypeGuard

def _validate_content(content = None):
    if not content.parts:
        return False
# WARNING: Decompyle incomplete


def _validate_contents(contents = None):
    if not contents:
        return False
    for content in None:
        if not _validate_content(content):
            return False
        return True


def _validate_response(response = None):
    if not response.candidates:
        return False
    if not None.candidates[0].content:
        return False
    return None(response.candidates[0].content)


def _extract_curated_history(comprehensive_history = None):
    '''Extracts the curated (valid) history from a comprehensive history.

  The comprehensive history contains all turns (user input and model responses),
  including any invalid or rejected model outputs. This function filters that
  history to return only the valid turns.

  Args:
      comprehensive_history: A list representing the complete chat history.
        Including invalid turns.

  Returns:
      curated history, which is a list of valid turns.
  '''
    if not comprehensive_history:
        return []
    curated_history = None
    length = len(comprehensive_history)
    i = 0
    current_input = comprehensive_history[i]
# WARNING: Decompyle incomplete


class _BaseChat:
    '''Base chat session.'''
    
    def __init__(self = None, *, model, config, history):
        self._model = model
        self._config = config
        content_models = []
        for content in history:
            if not isinstance(content, Content):
                content_model = Content.model_validate(content)
            else:
                content_model = content
            content_models.append(content_model)
            self._comprehensive_history = content_models
            self._curated_history = _extract_curated_history(content_models)
            return None

    
    def record_history(self, user_input = None, model_output = None, automatic_function_calling_history = None, is_valid = ('user_input', Content, 'model_output', list[Content], 'automatic_function_calling_history', list[Content], 'is_valid', bool, 'return', None)):
        """Records the chat history.

    Maintaining both comprehensive and curated histories.

    Args:
      user_input: The user's input content.
      model_output: A list of `Content` from the model's response. This can be
        an empty list if the model produced no output.
      automatic_function_calling_history: A list of `Content` representing the
        history of automatic function calls, including the user input as the
        first entry.
      is_valid: A boolean flag indicating whether the current model output is
        considered valid.
    """
        input_contents = automatic_function_calling_history[len(self._curated_history):] if automatic_function_calling_history else [
            user_input]
        output_contents = model_output if model_output else [
            Content(role = 'model', parts = [])]
        self._comprehensive_history.extend(input_contents)
        self._comprehensive_history.extend(output_contents)
        if is_valid:
            self._curated_history.extend(input_contents)
            self._curated_history.extend(output_contents)
            return None

    
    def get_history(self = None, curated = None):
        '''Returns the chat history.

    Args:
        curated: A boolean flag indicating whether to return the curated (valid)
          history or the comprehensive (all turns) history. Defaults to False
          (returns the comprehensive history).

    Returns:
        A list of `Content` objects representing the chat history.
    '''
        if curated:
            return self._curated_history
        return None._comprehensive_history



def _is_part_type(contents = None):
    if isinstance(contents, list):
        return (lambda .0: pass# WARNING: Decompyle incomplete
)(contents())
    allowed_part_types = None(types.PartUnion)
    if type(contents) in allowed_part_types:
        return True
# WARNING: Decompyle incomplete


class Chat(_BaseChat):
    pass
# WARNING: Decompyle incomplete


class Chats:
    '''A util class to create chat sessions.'''
    
    def __init__(self = None, modules = None):
        self._modules = modules

    
    def create(self = None, *, model, config, history):
        '''Creates a new chat session.

    Args:
      model: The model to use for the chat.
      config: The configuration to use for the generate content request.
      history: The history to use for the chat.

    Returns:
      A new chat session.
    '''
        return Chat(modules = self._modules, model = model, config = config, history = history if history else [])



class AsyncChat(_BaseChat):
    pass
# WARNING: Decompyle incomplete


class AsyncChats:
    '''A util class to create async chat sessions.'''
    
    def __init__(self = None, modules = None):
        self._modules = modules

    
    def create(self = None, *, model, config, history):
        '''Creates a new chat session.

    Args:
      model: The model to use for the chat.
      config: The configuration to use for the generate content request.
      history: The history to use for the chat.

    Returns:
      A new chat session.
    '''
        return AsyncChat(modules = self._modules, model = model, config = config, history = history if history else [])

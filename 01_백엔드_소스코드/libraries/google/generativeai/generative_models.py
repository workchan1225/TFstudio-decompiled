# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: generative_models.pyc (Python 3.11)

'''Classes for working with the Gemini models.'''
from __future__ import annotations
from collections.abc import Iterable
import textwrap
from typing import Any, Union, overload
import reprlib
import google.api_core.exceptions as google
from google.generativeai import protos
from google.generativeai import client
from google.generativeai import caching
from google.generativeai.types import content_types
from google.generativeai.types import generation_types
from google.generativeai.types import helper_types
from google.generativeai.types import safety_types
_USER_ROLE = 'user'
_MODEL_ROLE = 'model'

class GenerativeModel:
    '''
    The `genai.GenerativeModel` class wraps default parameters for calls to
    `GenerativeModel.generate_content`, `GenerativeModel.count_tokens`, and
    `GenerativeModel.start_chat`.

    This family of functionality is designed to support multi-turn conversations, and multimodal
    requests. What media-types are supported for input and output is model-dependant.

    >>> import google.generativeai as genai
    >>> import PIL.Image
    >>> genai.configure(api_key=\'YOUR_API_KEY\')
    >>> model = genai.GenerativeModel(\'models/gemini-1.5-flash\')
    >>> result = model.generate_content(\'Tell me a story about a magic backpack\')
    >>> result.text
    "In the quaint little town of Lakeside, there lived a young girl named Lily..."

    Multimodal input:

    >>> model = genai.GenerativeModel(\'models/gemini-1.5-flash\')
    >>> result = model.generate_content([
    ...     "Give me a recipe for these:", PIL.Image.open(\'scones.jpeg\')])
    >>> result.text
    "**Blueberry Scones** ..."

    Multi-turn conversation:

    >>> chat = model.start_chat()
    >>> response = chat.send_message("Hi, I have some questions for you.")
    >>> response.text
    "Sure, I\'ll do my best to answer your questions..."

    To list the compatible model names use:

    >>> for m in genai.list_models():
    ...     if \'generateContent\' in m.supported_generation_methods:
    ...         print(m.name)

    Arguments:
         model_name: The name of the model to query. To list compatible models use
         safety_settings: Sets the default safety filters. This controls which content is blocked
             by the api before being returned.
         generation_config: A `genai.GenerationConfig` setting the default generation parameters to
             use.
    '''
    
    def __init__(self, model_name, safety_settings = None, generation_config = None, tools = None, tool_config = ('gemini-1.5-flash-002', None, None, None, None, None), system_instruction = ('model_name', 'str', 'safety_settings', 'safety_types.SafetySettingOptions | None', 'generation_config', 'generation_types.GenerationConfigType | None', 'tools', 'content_types.FunctionLibraryType | None', 'tool_config', 'content_types.ToolConfigType | None', 'system_instruction', 'content_types.ContentType | None')):
        if '/' not in model_name:
            model_name = 'models/' + model_name
        self._model_name = model_name
        self._safety_settings = safety_types.to_easy_safety_dict(safety_settings)
        self._generation_config = generation_types.to_generation_config_dict(generation_config)
        self._tools = content_types.to_function_library(tools)
    # WARNING: Decompyle incomplete

    cached_content = (lambda self = None: getattr(self, '_cached_content', None))()
    model_name = (lambda self: self._model_name)()
    
    def __str__(self):
        
        def maybe_text(content):

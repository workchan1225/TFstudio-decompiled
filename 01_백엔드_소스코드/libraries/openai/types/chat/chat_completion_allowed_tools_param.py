# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: chat_completion_allowed_tools_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Dict, Iterable
from typing_extensions import Literal, Required, TypedDict
__all__ = [
    'ChatCompletionAllowedToolsParam']

def ChatCompletionAllowedToolsParam():
    '''ChatCompletionAllowedToolsParam'''
    tools: 'Required[Iterable[Dict[str, object]]]' = 'Constrains the tools available to the model to a pre-defined set.'

ChatCompletionAllowedToolsParam = <NODE:27>(ChatCompletionAllowedToolsParam, 'ChatCompletionAllowedToolsParam', TypedDict, total = False)

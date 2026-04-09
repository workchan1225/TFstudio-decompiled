# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: chat_completion_function_call_option_param.pyc (Python 3.11)

from __future__ import annotations
from typing_extensions import Required, TypedDict
__all__ = [
    'ChatCompletionFunctionCallOptionParam']

def ChatCompletionFunctionCallOptionParam():
    '''ChatCompletionFunctionCallOptionParam'''
    name: 'Required[str]' = '\n    Specifying a particular function via `{"name": "my_function"}` forces the model to call that function.\n    '

ChatCompletionFunctionCallOptionParam = <NODE:27>(ChatCompletionFunctionCallOptionParam, 'ChatCompletionFunctionCallOptionParam', TypedDict, total = False)

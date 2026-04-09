# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_custom_tool_call_output_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict
from response_input_file_param import ResponseInputFileParam
from response_input_text_param import ResponseInputTextParam
from response_input_image_param import ResponseInputImageParam
__all__ = [
    'ResponseCustomToolCallOutputParam',
    'OutputOutputContentList']
OutputOutputContentList: 'TypeAlias' = Union[(ResponseInputTextParam, ResponseInputImageParam, ResponseInputFileParam)]

def ResponseCustomToolCallOutputParam():
    '''ResponseCustomToolCallOutputParam'''
    id: 'str' = 'The output of a custom tool call from your code, being sent back to the model.'

ResponseCustomToolCallOutputParam = <NODE:27>(ResponseCustomToolCallOutputParam, 'ResponseCustomToolCallOutputParam', TypedDict, total = False)

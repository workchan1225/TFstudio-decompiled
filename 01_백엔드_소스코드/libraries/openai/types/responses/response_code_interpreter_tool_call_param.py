# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_code_interpreter_tool_call_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict
__all__ = [
    'ResponseCodeInterpreterToolCallParam',
    'Output',
    'OutputLogs',
    'OutputImage']

def OutputLogs():
    '''OutputLogs'''
    type: "Required[Literal['logs']]" = 'The logs output from the code interpreter.'

OutputLogs = <NODE:27>(OutputLogs, 'OutputLogs', TypedDict, total = False)

def OutputImage():
    '''OutputImage'''
    url: 'Required[str]' = 'The image output from the code interpreter.'

OutputImage = <NODE:27>(OutputImage, 'OutputImage', TypedDict, total = False)
Output: 'TypeAlias' = Union[(OutputLogs, OutputImage)]

def ResponseCodeInterpreterToolCallParam():
    '''ResponseCodeInterpreterToolCallParam'''
    type: "Required[Literal['code_interpreter_call']]" = 'A tool call to run code.'

ResponseCodeInterpreterToolCallParam = <NODE:27>(ResponseCodeInterpreterToolCallParam, 'ResponseCodeInterpreterToolCallParam', TypedDict, total = False)

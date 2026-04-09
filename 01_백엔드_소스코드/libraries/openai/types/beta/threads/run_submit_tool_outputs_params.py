# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: run_submit_tool_outputs_params.pyc (Python 3.11)

from __future__ import annotations
from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict
__all__ = [
    'RunSubmitToolOutputsParamsBase',
    'ToolOutput',
    'RunSubmitToolOutputsParamsNonStreaming',
    'RunSubmitToolOutputsParamsStreaming']

def RunSubmitToolOutputsParamsBase():
    '''RunSubmitToolOutputsParamsBase'''
    tool_outputs: 'Required[Iterable[ToolOutput]]' = 'RunSubmitToolOutputsParamsBase'

RunSubmitToolOutputsParamsBase = <NODE:27>(RunSubmitToolOutputsParamsBase, 'RunSubmitToolOutputsParamsBase', TypedDict, total = False)

def ToolOutput():
    '''ToolOutput'''
    tool_call_id: 'str' = 'ToolOutput'

ToolOutput = <NODE:27>(ToolOutput, 'ToolOutput', TypedDict, total = False)

def RunSubmitToolOutputsParamsNonStreaming():
    '''RunSubmitToolOutputsParamsNonStreaming'''
    stream: 'Optional[Literal[False]]' = 'RunSubmitToolOutputsParamsNonStreaming'

RunSubmitToolOutputsParamsNonStreaming = <NODE:27>(RunSubmitToolOutputsParamsNonStreaming, 'RunSubmitToolOutputsParamsNonStreaming', RunSubmitToolOutputsParamsBase, total = False)

class RunSubmitToolOutputsParamsStreaming(RunSubmitToolOutputsParamsBase):
    stream: 'Required[Literal[True]]' = 'RunSubmitToolOutputsParamsStreaming'

RunSubmitToolOutputsParams = Union[(RunSubmitToolOutputsParamsNonStreaming, RunSubmitToolOutputsParamsStreaming)]

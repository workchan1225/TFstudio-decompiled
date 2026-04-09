# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: custom_tool_param.pyc (Python 3.11)

from __future__ import annotations
from typing_extensions import Literal, Required, TypedDict
from shared_params.custom_tool_input_format import CustomToolInputFormat
__all__ = [
    'CustomToolParam']

def CustomToolParam():
    '''CustomToolParam'''
    format: 'CustomToolInputFormat' = 'A custom tool that processes input using a specified format.\n\n    Learn more about   [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)\n    '

CustomToolParam = <NODE:27>(CustomToolParam, 'CustomToolParam', TypedDict, total = False)

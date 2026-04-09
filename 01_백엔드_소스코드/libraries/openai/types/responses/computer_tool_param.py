# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: computer_tool_param.pyc (Python 3.11)

from __future__ import annotations
from typing_extensions import Literal, Required, TypedDict
__all__ = [
    'ComputerToolParam']

def ComputerToolParam():
    '''ComputerToolParam'''
    type: "Required[Literal['computer_use_preview']]" = 'A tool that controls a virtual computer.\n\n    Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).\n    '

ComputerToolParam = <NODE:27>(ComputerToolParam, 'ComputerToolParam', TypedDict, total = False)

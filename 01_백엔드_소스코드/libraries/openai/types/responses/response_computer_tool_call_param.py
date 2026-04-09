# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_computer_tool_call_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict
from _types import SequenceNotStr
__all__ = [
    'ResponseComputerToolCallParam',
    'Action',
    'ActionClick',
    'ActionDoubleClick',
    'ActionDrag',
    'ActionDragPath',
    'ActionKeypress',
    'ActionMove',
    'ActionScreenshot',
    'ActionScroll',
    'ActionType',
    'ActionWait',
    'PendingSafetyCheck']

def ActionClick():
    '''ActionClick'''
    y: 'Required[int]' = 'A click action.'

ActionClick = <NODE:27>(ActionClick, 'ActionClick', TypedDict, total = False)

def ActionDoubleClick():
    '''ActionDoubleClick'''
    y: 'Required[int]' = 'A double click action.'

ActionDoubleClick = <NODE:27>(ActionDoubleClick, 'ActionDoubleClick', TypedDict, total = False)

def ActionDragPath():
    '''ActionDragPath'''
    y: 'Required[int]' = 'An x/y coordinate pair, e.g. `{ x: 100, y: 200 }`.'

ActionDragPath = <NODE:27>(ActionDragPath, 'ActionDragPath', TypedDict, total = False)

def ActionDrag():
    '''ActionDrag'''
    type: "Required[Literal['drag']]" = 'A drag action.'

ActionDrag = <NODE:27>(ActionDrag, 'ActionDrag', TypedDict, total = False)

def ActionKeypress():
    '''ActionKeypress'''
    type: "Required[Literal['keypress']]" = 'A collection of keypresses the model would like to perform.'

ActionKeypress = <NODE:27>(ActionKeypress, 'ActionKeypress', TypedDict, total = False)

def ActionMove():
    '''ActionMove'''
    y: 'Required[int]' = 'A mouse move action.'

ActionMove = <NODE:27>(ActionMove, 'ActionMove', TypedDict, total = False)

def ActionScreenshot():
    '''ActionScreenshot'''
    type: "Required[Literal['screenshot']]" = 'A screenshot action.'

ActionScreenshot = <NODE:27>(ActionScreenshot, 'ActionScreenshot', TypedDict, total = False)

def ActionScroll():
    '''ActionScroll'''
    y: 'Required[int]' = 'A scroll action.'

ActionScroll = <NODE:27>(ActionScroll, 'ActionScroll', TypedDict, total = False)

def ActionType():
    '''ActionType'''
    type: "Required[Literal['type']]" = 'An action to type in text.'

ActionType = <NODE:27>(ActionType, 'ActionType', TypedDict, total = False)

def ActionWait():
    '''ActionWait'''
    type: "Required[Literal['wait']]" = 'A wait action.'

ActionWait = <NODE:27>(ActionWait, 'ActionWait', TypedDict, total = False)
Action: 'TypeAlias' = Union[(ActionClick, ActionDoubleClick, ActionDrag, ActionKeypress, ActionMove, ActionScreenshot, ActionScroll, ActionType, ActionWait)]

def PendingSafetyCheck():
    '''PendingSafetyCheck'''
    message: 'Optional[str]' = 'A pending safety check for the computer call.'

PendingSafetyCheck = <NODE:27>(PendingSafetyCheck, 'PendingSafetyCheck', TypedDict, total = False)

def ResponseComputerToolCallParam():
    '''ResponseComputerToolCallParam'''
    type: "Required[Literal['computer_call']]" = 'A tool call to a computer use tool.\n\n    See the\n    [computer use guide](https://platform.openai.com/docs/guides/tools-computer-use) for more information.\n    '

ResponseComputerToolCallParam = <NODE:27>(ResponseComputerToolCallParam, 'ResponseComputerToolCallParam', TypedDict, total = False)

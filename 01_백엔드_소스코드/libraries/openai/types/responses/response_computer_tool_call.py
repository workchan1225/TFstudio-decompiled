# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_computer_tool_call.pyc (Python 3.11)

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias
from _utils import PropertyInfo
from _models import BaseModel
__all__ = [
    'ResponseComputerToolCall',
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

class ActionClick(BaseModel):
    y: int = 'A click action.'


class ActionDoubleClick(BaseModel):
    y: int = 'A double click action.'


class ActionDragPath(BaseModel):
    y: int = 'An x/y coordinate pair, e.g. `{ x: 100, y: 200 }`.'


class ActionDrag(BaseModel):
    type: Literal['drag'] = 'A drag action.'


class ActionKeypress(BaseModel):
    type: Literal['keypress'] = 'A collection of keypresses the model would like to perform.'


class ActionMove(BaseModel):
    y: int = 'A mouse move action.'


class ActionScreenshot(BaseModel):
    type: Literal['screenshot'] = 'A screenshot action.'


class ActionScroll(BaseModel):
    y: int = 'A scroll action.'


class ActionType(BaseModel):
    type: Literal['type'] = 'An action to type in text.'


class ActionWait(BaseModel):
    type: Literal['wait'] = 'A wait action.'

Action: TypeAlias = Annotated[(Union[(ActionClick, ActionDoubleClick, ActionDrag, ActionKeypress, ActionMove, ActionScreenshot, ActionScroll, ActionType, ActionWait)], PropertyInfo(discriminator = 'type'))]

class PendingSafetyCheck(BaseModel):
    id: str = 'A pending safety check for the computer call.'
    code: Optional[str] = None
    message: Optional[str] = None


class ResponseComputerToolCall(BaseModel):
    type: Literal['computer_call'] = 'A tool call to a computer use tool.\n\n    See the\n    [computer use guide](https://platform.openai.com/docs/guides/tools-computer-use) for more information.\n    '

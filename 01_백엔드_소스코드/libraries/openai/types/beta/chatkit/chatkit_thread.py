# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: chatkit_thread.pyc (Python 3.11)

from typing import Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias
from _utils import PropertyInfo
from _models import BaseModel
__all__ = [
    'ChatKitThread',
    'Status',
    'StatusActive',
    'StatusLocked',
    'StatusClosed']

class StatusActive(BaseModel):
    type: Literal['active'] = 'Indicates that a thread is active.'


class StatusLocked(BaseModel):
    '''Indicates that a thread is locked and cannot accept new input.'''
    type: Literal['locked'] = None


class StatusClosed(BaseModel):
    '''Indicates that a thread has been closed.'''
    type: Literal['closed'] = None

Status: TypeAlias = Annotated[(Union[(StatusActive, StatusLocked, StatusClosed)], PropertyInfo(discriminator = 'type'))]

class ChatKitThread(BaseModel):
    status: Status = 'Represents a ChatKit thread and its current status.'
    user: str = None

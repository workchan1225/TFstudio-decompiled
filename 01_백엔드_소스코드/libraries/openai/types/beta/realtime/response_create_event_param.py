# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_create_event_param.pyc (Python 3.11)

from __future__ import annotations
from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict
from shared_params.metadata import Metadata
from conversation_item_with_reference_param import ConversationItemWithReferenceParam
__all__ = [
    'ResponseCreateEventParam',
    'Response',
    'ResponseTool']

def ResponseTool():
    '''ResponseTool'''
    type: "Literal['function']" = 'ResponseTool'

ResponseTool = <NODE:27>(ResponseTool, 'ResponseTool', TypedDict, total = False)

def Response():
    '''Response'''
    voice: "Union[str, Literal['alloy', 'ash', 'ballad', 'coral', 'echo', 'sage', 'shimmer', 'verse']]" = 'Response'

Response = <NODE:27>(Response, 'Response', TypedDict, total = False)

def ResponseCreateEventParam():
    '''ResponseCreateEventParam'''
    response: 'Response' = 'ResponseCreateEventParam'

ResponseCreateEventParam = <NODE:27>(ResponseCreateEventParam, 'ResponseCreateEventParam', TypedDict, total = False)

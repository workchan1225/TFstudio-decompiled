# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: web_search_tool_20250305_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Optional
from typing_extensions import Literal, Required, TypedDict
from _types import SequenceNotStr
from cache_control_ephemeral_param import CacheControlEphemeralParam
__all__ = [
    'WebSearchTool20250305Param',
    'UserLocation']

def UserLocation():
    '''UserLocation'''
    timezone: 'Optional[str]' = 'UserLocation'

UserLocation = <NODE:27>(UserLocation, 'UserLocation', TypedDict, total = False)

def WebSearchTool20250305Param():
    '''WebSearchTool20250305Param'''
    user_location: 'Optional[UserLocation]' = 'WebSearchTool20250305Param'

WebSearchTool20250305Param = <NODE:27>(WebSearchTool20250305Param, 'WebSearchTool20250305Param', TypedDict, total = False)

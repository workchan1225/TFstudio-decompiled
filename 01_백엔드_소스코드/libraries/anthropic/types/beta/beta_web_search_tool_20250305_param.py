# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_web_search_tool_20250305_param.pyc (Python 3.11)

from __future__ import annotations
from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict
from _types import SequenceNotStr
from beta_cache_control_ephemeral_param import BetaCacheControlEphemeralParam
__all__ = [
    'BetaWebSearchTool20250305Param',
    'UserLocation']

def UserLocation():
    '''UserLocation'''
    timezone: 'Optional[str]' = 'UserLocation'

UserLocation = <NODE:27>(UserLocation, 'UserLocation', TypedDict, total = False)

def BetaWebSearchTool20250305Param():
    '''BetaWebSearchTool20250305Param'''
    user_location: 'Optional[UserLocation]' = 'BetaWebSearchTool20250305Param'

BetaWebSearchTool20250305Param = <NODE:27>(BetaWebSearchTool20250305Param, 'BetaWebSearchTool20250305Param', TypedDict, total = False)

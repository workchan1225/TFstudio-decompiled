# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_web_fetch_tool_result_block_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict
from beta_web_fetch_block_param import BetaWebFetchBlockParam
from beta_cache_control_ephemeral_param import BetaCacheControlEphemeralParam
from beta_web_fetch_tool_result_error_block_param import BetaWebFetchToolResultErrorBlockParam
__all__ = [
    'BetaWebFetchToolResultBlockParam',
    'Content']
Content: 'TypeAlias' = Union[(BetaWebFetchToolResultErrorBlockParam, BetaWebFetchBlockParam)]

def BetaWebFetchToolResultBlockParam():
    '''BetaWebFetchToolResultBlockParam'''
    cache_control: 'Optional[BetaCacheControlEphemeralParam]' = 'BetaWebFetchToolResultBlockParam'

BetaWebFetchToolResultBlockParam = <NODE:27>(BetaWebFetchToolResultBlockParam, 'BetaWebFetchToolResultBlockParam', TypedDict, total = False)

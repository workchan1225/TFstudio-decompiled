# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_tool_search_tool_result_block_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict
from beta_cache_control_ephemeral_param import BetaCacheControlEphemeralParam
from beta_tool_search_tool_result_error_param import BetaToolSearchToolResultErrorParam
from beta_tool_search_tool_search_result_block_param import BetaToolSearchToolSearchResultBlockParam
__all__ = [
    'BetaToolSearchToolResultBlockParam',
    'Content']
Content: 'TypeAlias' = Union[(BetaToolSearchToolResultErrorParam, BetaToolSearchToolSearchResultBlockParam)]

def BetaToolSearchToolResultBlockParam():
    '''BetaToolSearchToolResultBlockParam'''
    cache_control: 'Optional[BetaCacheControlEphemeralParam]' = 'BetaToolSearchToolResultBlockParam'

BetaToolSearchToolResultBlockParam = <NODE:27>(BetaToolSearchToolResultBlockParam, 'BetaToolSearchToolResultBlockParam', TypedDict, total = False)

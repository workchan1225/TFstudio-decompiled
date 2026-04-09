# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_tool_use_block_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Dict, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict
from beta_direct_caller_param import BetaDirectCallerParam
from beta_server_tool_caller_param import BetaServerToolCallerParam
from beta_cache_control_ephemeral_param import BetaCacheControlEphemeralParam
__all__ = [
    'BetaToolUseBlockParam',
    'Caller']
Caller: 'TypeAlias' = Union[(BetaDirectCallerParam, BetaServerToolCallerParam)]

def BetaToolUseBlockParam():
    '''BetaToolUseBlockParam'''
    caller: 'Caller' = 'BetaToolUseBlockParam'

BetaToolUseBlockParam = <NODE:27>(BetaToolUseBlockParam, 'BetaToolUseBlockParam', TypedDict, total = False)

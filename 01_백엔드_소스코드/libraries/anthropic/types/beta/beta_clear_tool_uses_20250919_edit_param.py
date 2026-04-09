# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_clear_tool_uses_20250919_edit_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict
from _types import SequenceNotStr
from beta_tool_uses_keep_param import BetaToolUsesKeepParam
from beta_tool_uses_trigger_param import BetaToolUsesTriggerParam
from beta_input_tokens_trigger_param import BetaInputTokensTriggerParam
from beta_input_tokens_clear_at_least_param import BetaInputTokensClearAtLeastParam
__all__ = [
    'BetaClearToolUses20250919EditParam',
    'Trigger']
Trigger: 'TypeAlias' = Union[(BetaInputTokensTriggerParam, BetaToolUsesTriggerParam)]

def BetaClearToolUses20250919EditParam():
    '''BetaClearToolUses20250919EditParam'''
    trigger: 'Trigger' = 'BetaClearToolUses20250919EditParam'

BetaClearToolUses20250919EditParam = <NODE:27>(BetaClearToolUses20250919EditParam, 'BetaClearToolUses20250919EditParam', TypedDict, total = False)

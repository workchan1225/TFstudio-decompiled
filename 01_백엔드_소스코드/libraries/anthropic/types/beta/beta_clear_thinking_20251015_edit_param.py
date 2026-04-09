# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_clear_thinking_20251015_edit_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict
from beta_thinking_turns_param import BetaThinkingTurnsParam
from beta_all_thinking_turns_param import BetaAllThinkingTurnsParam
__all__ = [
    'BetaClearThinking20251015EditParam',
    'Keep']
Keep: 'TypeAlias' = Union[(BetaThinkingTurnsParam, BetaAllThinkingTurnsParam, Literal['all'])]

def BetaClearThinking20251015EditParam():
    '''BetaClearThinking20251015EditParam'''
    keep: 'Keep' = 'BetaClearThinking20251015EditParam'

BetaClearThinking20251015EditParam = <NODE:27>(BetaClearThinking20251015EditParam, 'BetaClearThinking20251015EditParam', TypedDict, total = False)

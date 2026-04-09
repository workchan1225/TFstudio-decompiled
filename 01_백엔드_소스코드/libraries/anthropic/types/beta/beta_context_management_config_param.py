# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_context_management_config_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Union, Iterable
from typing_extensions import TypeAlias, TypedDict
from beta_clear_thinking_20251015_edit_param import BetaClearThinking20251015EditParam
from beta_clear_tool_uses_20250919_edit_param import BetaClearToolUses20250919EditParam
__all__ = [
    'BetaContextManagementConfigParam',
    'Edit']
Edit: 'TypeAlias' = Union[(BetaClearToolUses20250919EditParam, BetaClearThinking20251015EditParam)]

def BetaContextManagementConfigParam():
    '''BetaContextManagementConfigParam'''
    edits: 'Iterable[Edit]' = 'BetaContextManagementConfigParam'

BetaContextManagementConfigParam = <NODE:27>(BetaContextManagementConfigParam, 'BetaContextManagementConfigParam', TypedDict, total = False)

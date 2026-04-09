# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: realtime_truncation_retention_ratio_param.pyc (Python 3.11)

from __future__ import annotations
from typing_extensions import Literal, Required, TypedDict
__all__ = [
    'RealtimeTruncationRetentionRatioParam',
    'TokenLimits']

def TokenLimits():
    '''TokenLimits'''
    post_instructions: 'int' = "Optional custom token limits for this truncation strategy.\n\n    If not provided, the model's default token limits will be used.\n    "

TokenLimits = <NODE:27>(TokenLimits, 'TokenLimits', TypedDict, total = False)

def RealtimeTruncationRetentionRatioParam():
    '''RealtimeTruncationRetentionRatioParam'''
    token_limits: 'TokenLimits' = '\n    Retain a fraction of the conversation tokens when the conversation exceeds the input token limit. This allows you to amortize truncations across multiple turns, which can help improve cached token usage.\n    '

RealtimeTruncationRetentionRatioParam = <NODE:27>(RealtimeTruncationRetentionRatioParam, 'RealtimeTruncationRetentionRatioParam', TypedDict, total = False)

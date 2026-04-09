# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_message_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Union, Iterable
from typing_extensions import Literal, Required, TypedDict
from beta_content_block_param import BetaContentBlockParam
__all__ = [
    'BetaMessageParam']

def BetaMessageParam():
    '''BetaMessageParam'''
    role: "Required[Literal['user', 'assistant']]" = 'BetaMessageParam'

BetaMessageParam = <NODE:27>(BetaMessageParam, 'BetaMessageParam', TypedDict, total = False)

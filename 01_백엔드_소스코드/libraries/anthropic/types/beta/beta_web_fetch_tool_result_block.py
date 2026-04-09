# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_web_fetch_tool_result_block.pyc (Python 3.11)

from typing import Union
from typing_extensions import Literal, TypeAlias
from _models import BaseModel
from beta_web_fetch_block import BetaWebFetchBlock
from beta_web_fetch_tool_result_error_block import BetaWebFetchToolResultErrorBlock
__all__ = [
    'BetaWebFetchToolResultBlock',
    'Content']
Content: TypeAlias = Union[(BetaWebFetchToolResultErrorBlock, BetaWebFetchBlock)]

class BetaWebFetchToolResultBlock(BaseModel):
    type: Literal['web_fetch_tool_result'] = 'BetaWebFetchToolResultBlock'

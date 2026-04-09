# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_tool_search_tool_result_block.pyc (Python 3.11)

from typing import Union
from typing_extensions import Literal, TypeAlias
from _models import BaseModel
from beta_tool_search_tool_result_error import BetaToolSearchToolResultError
from beta_tool_search_tool_search_result_block import BetaToolSearchToolSearchResultBlock
__all__ = [
    'BetaToolSearchToolResultBlock',
    'Content']
Content: TypeAlias = Union[(BetaToolSearchToolResultError, BetaToolSearchToolSearchResultBlock)]

class BetaToolSearchToolResultBlock(BaseModel):
    type: Literal['tool_search_tool_result'] = 'BetaToolSearchToolResultBlock'

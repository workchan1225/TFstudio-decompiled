# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_web_search_tool_result_block_content.pyc (Python 3.11)

from typing import List, Union
from typing_extensions import TypeAlias
from beta_web_search_result_block import BetaWebSearchResultBlock
from beta_web_search_tool_result_error import BetaWebSearchToolResultError
__all__ = [
    'BetaWebSearchToolResultBlockContent']
BetaWebSearchToolResultBlockContent: TypeAlias = Union[(BetaWebSearchToolResultError, List[BetaWebSearchResultBlock])]

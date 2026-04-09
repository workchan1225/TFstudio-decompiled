# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: web_search_tool_result_block_content.pyc (Python 3.11)

from typing import List, Union
from typing_extensions import TypeAlias
from web_search_result_block import WebSearchResultBlock
from web_search_tool_result_error import WebSearchToolResultError
__all__ = [
    'WebSearchToolResultBlockContent']
WebSearchToolResultBlockContent: TypeAlias = Union[(WebSearchToolResultError, List[WebSearchResultBlock])]

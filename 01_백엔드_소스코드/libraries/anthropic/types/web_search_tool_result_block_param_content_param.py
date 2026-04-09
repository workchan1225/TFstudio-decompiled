# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: web_search_tool_result_block_param_content_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Union, Iterable
from typing_extensions import TypeAlias
from web_search_result_block_param import WebSearchResultBlockParam
from web_search_tool_request_error_param import WebSearchToolRequestErrorParam
__all__ = [
    'WebSearchToolResultBlockParamContentParam']
WebSearchToolResultBlockParamContentParam: 'TypeAlias' = Union[(Iterable[WebSearchResultBlockParam], WebSearchToolRequestErrorParam)]

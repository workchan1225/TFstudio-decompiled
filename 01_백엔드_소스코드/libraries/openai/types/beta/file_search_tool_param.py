# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: file_search_tool_param.pyc (Python 3.11)

from __future__ import annotations
from typing_extensions import Literal, Required, TypedDict
__all__ = [
    'FileSearchToolParam',
    'FileSearch',
    'FileSearchRankingOptions']

def FileSearchRankingOptions():
    '''FileSearchRankingOptions'''
    ranker: "Literal['auto', 'default_2024_08_21']" = 'The ranking options for the file search.\n\n    If not specified, the file search tool will use the `auto` ranker and a score_threshold of 0.\n\n    See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.\n    '

FileSearchRankingOptions = <NODE:27>(FileSearchRankingOptions, 'FileSearchRankingOptions', TypedDict, total = False)

def FileSearch():
    '''FileSearch'''
    ranking_options: 'FileSearchRankingOptions' = 'Overrides for the file search tool.'

FileSearch = <NODE:27>(FileSearch, 'FileSearch', TypedDict, total = False)

def FileSearchToolParam():
    '''FileSearchToolParam'''
    file_search: 'FileSearch' = 'FileSearchToolParam'

FileSearchToolParam = <NODE:27>(FileSearchToolParam, 'FileSearchToolParam', TypedDict, total = False)

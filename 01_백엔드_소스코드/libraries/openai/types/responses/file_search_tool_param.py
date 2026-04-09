# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: file_search_tool_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict
from _types import SequenceNotStr
from shared_params.compound_filter import CompoundFilter
from shared_params.comparison_filter import ComparisonFilter
__all__ = [
    'FileSearchToolParam',
    'Filters',
    'RankingOptions',
    'RankingOptionsHybridSearch']
Filters: 'TypeAlias' = Union[(ComparisonFilter, CompoundFilter)]

def RankingOptionsHybridSearch():
    '''RankingOptionsHybridSearch'''
    text_weight: 'Required[float]' = '\n    Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.\n    '

RankingOptionsHybridSearch = <NODE:27>(RankingOptionsHybridSearch, 'RankingOptionsHybridSearch', TypedDict, total = False)

def RankingOptions():
    '''RankingOptions'''
    score_threshold: 'float' = 'Ranking options for search.'

RankingOptions = <NODE:27>(RankingOptions, 'RankingOptions', TypedDict, total = False)

def FileSearchToolParam():
    '''FileSearchToolParam'''
    ranking_options: 'RankingOptions' = 'A tool that searches for relevant content from uploaded files.\n\n    Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).\n    '

FileSearchToolParam = <NODE:27>(FileSearchToolParam, 'FileSearchToolParam', TypedDict, total = False)

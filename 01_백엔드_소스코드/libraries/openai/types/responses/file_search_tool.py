# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: file_search_tool.pyc (Python 3.11)

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias
from _models import BaseModel
from shared.compound_filter import CompoundFilter
from shared.comparison_filter import ComparisonFilter
__all__ = [
    'FileSearchTool',
    'Filters',
    'RankingOptions',
    'RankingOptionsHybridSearch']
Filters: TypeAlias = Union[(ComparisonFilter, CompoundFilter, None)]

class RankingOptionsHybridSearch(BaseModel):
    text_weight: float = '\n    Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.\n    '


class RankingOptions(BaseModel):
    '''Ranking options for search.'''
    hybrid_search: Optional[RankingOptionsHybridSearch] = None
    ranker: Optional[Literal[('auto', 'default-2024-11-15')]] = None
    score_threshold: Optional[float] = None


class FileSearchTool(BaseModel):
    vector_store_ids: List[str] = 'A tool that searches for relevant content from uploaded files.\n\n    Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).\n    '
    filters: Optional[Filters] = None
    max_num_results: Optional[int] = None
    ranking_options: Optional[RankingOptions] = None

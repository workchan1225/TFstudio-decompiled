# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: vector_store_search_params.pyc (Python 3.11)

from __future__ import annotations
from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict
from _types import SequenceNotStr
from shared_params.compound_filter import CompoundFilter
from shared_params.comparison_filter import ComparisonFilter
__all__ = [
    'VectorStoreSearchParams',
    'Filters',
    'RankingOptions']

def VectorStoreSearchParams():
    '''VectorStoreSearchParams'''
    rewrite_query: 'bool' = 'VectorStoreSearchParams'

VectorStoreSearchParams = <NODE:27>(VectorStoreSearchParams, 'VectorStoreSearchParams', TypedDict, total = False)
Filters: 'TypeAlias' = Union[(ComparisonFilter, CompoundFilter)]

def RankingOptions():
    '''RankingOptions'''
    score_threshold: 'float' = 'Ranking options for search.'

RankingOptions = <NODE:27>(RankingOptions, 'RankingOptions', TypedDict, total = False)

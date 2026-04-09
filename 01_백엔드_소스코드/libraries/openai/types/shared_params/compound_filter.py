# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: compound_filter.pyc (Python 3.11)

from __future__ import annotations
from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict
from comparison_filter import ComparisonFilter
__all__ = [
    'CompoundFilter',
    'Filter']
Filter: 'TypeAlias' = Union[(ComparisonFilter, object)]

def CompoundFilter():
    '''CompoundFilter'''
    type: "Required[Literal['and', 'or']]" = 'Combine multiple filters using `and` or `or`.'

CompoundFilter = <NODE:27>(CompoundFilter, 'CompoundFilter', TypedDict, total = False)

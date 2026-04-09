# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: compound_filter.pyc (Python 3.11)

from typing import List, Union
from typing_extensions import Literal, TypeAlias
from _models import BaseModel
from comparison_filter import ComparisonFilter
__all__ = [
    'CompoundFilter',
    'Filter']
Filter: TypeAlias = Union[(ComparisonFilter, object)]

class CompoundFilter(BaseModel):
    type: Literal[('and', 'or')] = 'Combine multiple filters using `and` or `or`.'

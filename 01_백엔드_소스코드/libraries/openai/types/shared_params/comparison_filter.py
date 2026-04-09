# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: comparison_filter.pyc (Python 3.11)

from __future__ import annotations
from typing import Union
from typing_extensions import Literal, Required, TypedDict
from _types import SequenceNotStr
__all__ = [
    'ComparisonFilter']

def ComparisonFilter():
    '''ComparisonFilter'''
    value: 'Required[Union[str, float, bool, SequenceNotStr[Union[str, float]]]]' = '\n    A filter used to compare a specified attribute key to a given value using a defined comparison operation.\n    '

ComparisonFilter = <NODE:27>(ComparisonFilter, 'ComparisonFilter', TypedDict, total = False)

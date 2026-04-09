# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: comparison_filter.pyc (Python 3.11)

from typing import List, Union
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ComparisonFilter']

class ComparisonFilter(BaseModel):
    value: Union[(str, float, bool, List[Union[(str, float)]])] = '\n    A filter used to compare a specified attribute key to a given value using a defined comparison operation.\n    '

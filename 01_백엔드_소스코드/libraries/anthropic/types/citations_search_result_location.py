# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: citations_search_result_location.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'CitationsSearchResultLocation']

class CitationsSearchResultLocation(BaseModel):
    start_block_index: int = 'CitationsSearchResultLocation'
    type: Literal['search_result_location'] = None

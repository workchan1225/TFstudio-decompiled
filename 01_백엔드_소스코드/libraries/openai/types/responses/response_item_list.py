# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_item_list.pyc (Python 3.11)

from typing import List
from typing_extensions import Literal
from _models import BaseModel
from response_item import ResponseItem
__all__ = [
    'ResponseItemList']

class ResponseItemList(BaseModel):
    object: Literal['list'] = 'A list of Response items.'

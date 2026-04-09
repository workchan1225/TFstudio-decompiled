# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_output_item_done_event.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
from response_output_item import ResponseOutputItem
__all__ = [
    'ResponseOutputItemDoneEvent']

class ResponseOutputItemDoneEvent(BaseModel):
    type: Literal['response.output_item.done'] = 'Emitted when an output item is marked done.'

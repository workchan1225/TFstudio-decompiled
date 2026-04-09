# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: compacted_response.pyc (Python 3.11)

from typing import List
from typing_extensions import Literal
from _models import BaseModel
from response_usage import ResponseUsage
from response_output_item import ResponseOutputItem
__all__ = [
    'CompactedResponse']

class CompactedResponse(BaseModel):
    usage: ResponseUsage = 'CompactedResponse'

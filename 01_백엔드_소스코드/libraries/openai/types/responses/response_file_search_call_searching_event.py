# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_file_search_call_searching_event.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseFileSearchCallSearchingEvent']

class ResponseFileSearchCallSearchingEvent(BaseModel):
    type: Literal['response.file_search_call.searching'] = 'Emitted when a file search is currently searching.'

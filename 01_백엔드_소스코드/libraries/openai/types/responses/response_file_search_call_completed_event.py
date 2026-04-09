# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_file_search_call_completed_event.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseFileSearchCallCompletedEvent']

class ResponseFileSearchCallCompletedEvent(BaseModel):
    type: Literal['response.file_search_call.completed'] = 'Emitted when a file search call is completed (results found).'

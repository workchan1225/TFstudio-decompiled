# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: completion.pyc (Python 3.11)

from typing import List, Optional
from typing_extensions import Literal
from _models import BaseModel
from completion_usage import CompletionUsage
from completion_choice import CompletionChoice
__all__ = [
    'Completion']

class Completion(BaseModel):
    object: Literal['text_completion'] = 'Represents a completion response from the API.\n\n    Note: both the streamed and non-streamed response objects share the same shape (unlike the chat endpoint).\n    '
    system_fingerprint: Optional[str] = None
    usage: Optional[CompletionUsage] = None

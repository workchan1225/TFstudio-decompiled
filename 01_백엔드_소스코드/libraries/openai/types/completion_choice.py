# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: completion_choice.pyc (Python 3.11)

from typing import Dict, List, Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'CompletionChoice',
    'Logprobs']

class Logprobs(BaseModel):
    text_offset: Optional[List[int]] = None
    token_logprobs: Optional[List[float]] = None
    tokens: Optional[List[str]] = None
    top_logprobs: Optional[List[Dict[(str, float)]]] = None


class CompletionChoice(BaseModel):
    index: int = 'CompletionChoice'
    text: str = None

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: realtime_response_usage.pyc (Python 3.11)

from typing import Optional
from _models import BaseModel
__all__ = [
    'RealtimeResponseUsage',
    'InputTokenDetails',
    'OutputTokenDetails']

class InputTokenDetails(BaseModel):
    audio_tokens: Optional[int] = None
    cached_tokens: Optional[int] = None
    text_tokens: Optional[int] = None


class OutputTokenDetails(BaseModel):
    audio_tokens: Optional[int] = None
    text_tokens: Optional[int] = None


class RealtimeResponseUsage(BaseModel):
    input_token_details: Optional[InputTokenDetails] = None
    input_tokens: Optional[int] = None
    output_token_details: Optional[OutputTokenDetails] = None
    output_tokens: Optional[int] = None
    total_tokens: Optional[int] = None

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: realtime_response_usage.pyc (Python 3.11)

from typing import Optional
from _models import BaseModel
from realtime_response_usage_input_token_details import RealtimeResponseUsageInputTokenDetails
from realtime_response_usage_output_token_details import RealtimeResponseUsageOutputTokenDetails
__all__ = [
    'RealtimeResponseUsage']

class RealtimeResponseUsage(BaseModel):
    '''Usage statistics for the Response, this will correspond to billing.

    A
    Realtime API session will maintain a conversation context and append new
    Items to the Conversation, thus output from previous turns (text and
    audio tokens) will become the input for later turns.
    '''
    input_token_details: Optional[RealtimeResponseUsageInputTokenDetails] = None
    input_tokens: Optional[int] = None
    output_token_details: Optional[RealtimeResponseUsageOutputTokenDetails] = None
    output_tokens: Optional[int] = None
    total_tokens: Optional[int] = None

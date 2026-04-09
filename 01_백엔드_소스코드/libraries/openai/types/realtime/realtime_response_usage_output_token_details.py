# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: realtime_response_usage_output_token_details.pyc (Python 3.11)

from typing import Optional
from _models import BaseModel
__all__ = [
    'RealtimeResponseUsageOutputTokenDetails']

class RealtimeResponseUsageOutputTokenDetails(BaseModel):
    '''Details about the output tokens used in the Response.'''
    audio_tokens: Optional[int] = None
    text_tokens: Optional[int] = None

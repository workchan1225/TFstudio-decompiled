# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_usage.pyc (Python 3.11)

from _models import BaseModel
__all__ = [
    'ResponseUsage',
    'InputTokensDetails',
    'OutputTokensDetails']

class InputTokensDetails(BaseModel):
    cached_tokens: int = 'A detailed breakdown of the input tokens.'


class OutputTokensDetails(BaseModel):
    reasoning_tokens: int = 'A detailed breakdown of the output tokens.'


class ResponseUsage(BaseModel):
    total_tokens: int = '\n    Represents token usage details including input tokens, output tokens,\n    a breakdown of output tokens, and the total tokens used.\n    '

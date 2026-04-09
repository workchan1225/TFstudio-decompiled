# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: batch_usage.pyc (Python 3.11)

from _models import BaseModel
__all__ = [
    'BatchUsage',
    'InputTokensDetails',
    'OutputTokensDetails']

class InputTokensDetails(BaseModel):
    cached_tokens: int = 'A detailed breakdown of the input tokens.'


class OutputTokensDetails(BaseModel):
    reasoning_tokens: int = 'A detailed breakdown of the output tokens.'


class BatchUsage(BaseModel):
    total_tokens: int = '\n    Represents token usage details including input tokens, output tokens, a\n    breakdown of output tokens, and the total tokens used. Only populated on\n    batches created after September 7, 2025.\n    '

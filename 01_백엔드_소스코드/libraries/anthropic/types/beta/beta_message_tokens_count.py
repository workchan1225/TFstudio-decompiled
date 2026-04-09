# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_message_tokens_count.pyc (Python 3.11)

from typing import Optional
from _models import BaseModel
from beta_count_tokens_context_management_response import BetaCountTokensContextManagementResponse
__all__ = [
    'BetaMessageTokensCount']

class BetaMessageTokensCount(BaseModel):
    input_tokens: int = None

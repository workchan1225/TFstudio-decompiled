# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_message_batch_errored_result.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
from beta_error_response import BetaErrorResponse
__all__ = [
    'BetaMessageBatchErroredResult']

class BetaMessageBatchErroredResult(BaseModel):
    type: Literal['errored'] = 'BetaMessageBatchErroredResult'

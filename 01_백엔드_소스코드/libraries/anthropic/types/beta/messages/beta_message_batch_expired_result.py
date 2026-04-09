# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_message_batch_expired_result.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'BetaMessageBatchExpiredResult']

class BetaMessageBatchExpiredResult(BaseModel):
    type: Literal['expired'] = 'BetaMessageBatchExpiredResult'

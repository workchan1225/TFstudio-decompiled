# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_message_batch_canceled_result.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'BetaMessageBatchCanceledResult']

class BetaMessageBatchCanceledResult(BaseModel):
    type: Literal['canceled'] = 'BetaMessageBatchCanceledResult'

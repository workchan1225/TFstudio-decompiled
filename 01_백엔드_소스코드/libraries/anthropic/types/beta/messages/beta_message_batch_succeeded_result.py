# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_message_batch_succeeded_result.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
from beta_message import BetaMessage
__all__ = [
    'BetaMessageBatchSucceededResult']

class BetaMessageBatchSucceededResult(BaseModel):
    type: Literal['succeeded'] = 'BetaMessageBatchSucceededResult'

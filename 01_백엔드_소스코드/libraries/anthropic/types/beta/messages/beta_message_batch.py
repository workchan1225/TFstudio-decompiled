# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_message_batch.pyc (Python 3.11)

from typing import Optional
from datetime import datetime
from typing_extensions import Literal
from _models import BaseModel
from beta_message_batch_request_counts import BetaMessageBatchRequestCounts
__all__ = [
    'BetaMessageBatch']

class BetaMessageBatch(BaseModel):
    id: str = 'BetaMessageBatch'
    archived_at: Optional[datetime] = None
    created_at: datetime = None
    request_counts: BetaMessageBatchRequestCounts = None
    type: Literal['message_batch'] = None

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: message_batch.pyc (Python 3.11)

from typing import Optional
from datetime import datetime
from typing_extensions import Literal
from _models import BaseModel
from message_batch_request_counts import MessageBatchRequestCounts
__all__ = [
    'MessageBatch']

class MessageBatch(BaseModel):
    id: str = 'MessageBatch'
    archived_at: Optional[datetime] = None
    created_at: datetime = None
    request_counts: MessageBatchRequestCounts = None
    type: Literal['message_batch'] = None

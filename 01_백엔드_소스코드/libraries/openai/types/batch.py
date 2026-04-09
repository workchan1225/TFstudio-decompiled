# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: batch.pyc (Python 3.11)

from typing import List, Optional
from typing_extensions import Literal
from _models import BaseModel
from batch_error import BatchError
from batch_usage import BatchUsage
from shared.metadata import Metadata
from batch_request_counts import BatchRequestCounts
__all__ = [
    'Batch',
    'Errors']

class Errors(BaseModel):
    data: Optional[List[BatchError]] = None
    object: Optional[str] = None


class Batch(BaseModel):
    status: Literal[('validating', 'failed', 'in_progress', 'finalizing', 'completed', 'expired', 'cancelling', 'cancelled')] = 'Batch'
    cancelled_at: Optional[int] = None
    cancelling_at: Optional[int] = None
    completed_at: Optional[int] = None
    error_file_id: Optional[str] = None
    errors: Optional[Errors] = None
    expired_at: Optional[int] = None
    expires_at: Optional[int] = None
    failed_at: Optional[int] = None
    finalizing_at: Optional[int] = None
    in_progress_at: Optional[int] = None
    metadata: Optional[Metadata] = None
    model: Optional[str] = None
    output_file_id: Optional[str] = None
    request_counts: Optional[BatchRequestCounts] = None
    usage: Optional[BatchUsage] = None

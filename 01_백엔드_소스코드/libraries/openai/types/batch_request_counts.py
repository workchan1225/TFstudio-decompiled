# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: batch_request_counts.pyc (Python 3.11)

from _models import BaseModel
__all__ = [
    'BatchRequestCounts']

class BatchRequestCounts(BaseModel):
    total: int = 'The request counts for different statuses within the batch.'

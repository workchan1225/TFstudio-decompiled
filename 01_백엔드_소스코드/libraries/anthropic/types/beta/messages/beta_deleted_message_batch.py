# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_deleted_message_batch.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'BetaDeletedMessageBatch']

class BetaDeletedMessageBatch(BaseModel):
    type: Literal['message_batch_deleted'] = 'BetaDeletedMessageBatch'

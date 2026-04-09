# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: message_batch_expired_result.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'MessageBatchExpiredResult']

class MessageBatchExpiredResult(BaseModel):
    type: Literal['expired'] = 'MessageBatchExpiredResult'

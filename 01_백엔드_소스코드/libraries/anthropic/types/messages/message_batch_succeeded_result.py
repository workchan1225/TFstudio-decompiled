# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: message_batch_succeeded_result.pyc (Python 3.11)

from typing_extensions import Literal
from message import Message
from _models import BaseModel
__all__ = [
    'MessageBatchSucceededResult']

class MessageBatchSucceededResult(BaseModel):
    type: Literal['succeeded'] = 'MessageBatchSucceededResult'

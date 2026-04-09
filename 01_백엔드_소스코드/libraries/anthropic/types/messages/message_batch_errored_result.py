# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: message_batch_errored_result.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
from shared.error_response import ErrorResponse
__all__ = [
    'MessageBatchErroredResult']

class MessageBatchErroredResult(BaseModel):
    type: Literal['errored'] = 'MessageBatchErroredResult'

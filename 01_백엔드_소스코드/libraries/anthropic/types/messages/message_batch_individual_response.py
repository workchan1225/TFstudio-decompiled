# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: message_batch_individual_response.pyc (Python 3.11)

from _models import BaseModel
from message_batch_result import MessageBatchResult
__all__ = [
    'MessageBatchIndividualResponse']

class MessageBatchIndividualResponse(BaseModel):
    result: MessageBatchResult = 'MessageBatchIndividualResponse'

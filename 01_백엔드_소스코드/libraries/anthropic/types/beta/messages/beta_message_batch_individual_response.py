# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_message_batch_individual_response.pyc (Python 3.11)

from _models import BaseModel
from beta_message_batch_result import BetaMessageBatchResult
__all__ = [
    'BetaMessageBatchIndividualResponse']

class BetaMessageBatchIndividualResponse(BaseModel):
    result: BetaMessageBatchResult = 'BetaMessageBatchIndividualResponse'

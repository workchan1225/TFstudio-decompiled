# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: message_creation_step_details.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'MessageCreationStepDetails',
    'MessageCreation']

class MessageCreation(BaseModel):
    message_id: str = 'MessageCreation'


class MessageCreationStepDetails(BaseModel):
    type: Literal['message_creation'] = 'Details of the message creation by the run step.'

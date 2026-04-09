# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_refusal_delta_event.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseRefusalDeltaEvent']

class ResponseRefusalDeltaEvent(BaseModel):
    type: Literal['response.refusal.delta'] = 'Emitted when there is a partial refusal text.'

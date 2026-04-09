# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: moderation_create_response.pyc (Python 3.11)

from typing import List
from _models import BaseModel
from moderation import Moderation
__all__ = [
    'ModerationCreateResponse']

class ModerationCreateResponse(BaseModel):
    results: List[Moderation] = 'Represents if a given text input is potentially harmful.'

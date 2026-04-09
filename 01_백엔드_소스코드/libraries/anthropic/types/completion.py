# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: completion.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from model import Model
from _models import BaseModel
__all__ = [
    'Completion']

class Completion(BaseModel):
    model: Model = 'Completion'
    type: Literal['completion'] = None

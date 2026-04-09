# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_output_refusal.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseOutputRefusal']

class ResponseOutputRefusal(BaseModel):
    type: Literal['refusal'] = 'A refusal from the model.'

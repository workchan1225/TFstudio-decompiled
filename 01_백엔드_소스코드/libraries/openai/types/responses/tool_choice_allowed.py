# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tool_choice_allowed.pyc (Python 3.11)

from typing import Dict, List
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ToolChoiceAllowed']

class ToolChoiceAllowed(BaseModel):
    type: Literal['allowed_tools'] = 'Constrains the tools available to the model to a pre-defined set.'

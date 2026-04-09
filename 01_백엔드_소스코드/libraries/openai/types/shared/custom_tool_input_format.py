# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: custom_tool_input_format.pyc (Python 3.11)

from typing import Union
from typing_extensions import Literal, Annotated, TypeAlias
from _utils import PropertyInfo
from _models import BaseModel
__all__ = [
    'CustomToolInputFormat',
    'Text',
    'Grammar']

class Text(BaseModel):
    type: Literal['text'] = 'Unconstrained free-form text.'


class Grammar(BaseModel):
    type: Literal['grammar'] = 'A grammar defined by the user.'

CustomToolInputFormat: TypeAlias = Annotated[(Union[(Text, Grammar)], PropertyInfo(discriminator = 'type'))]

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: moderation.pyc (Python 3.11)

from typing import List, Optional
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from _models import BaseModel
__all__ = [
    'Moderation',
    'Categories',
    'CategoryAppliedInputTypes',
    'CategoryScores']

class Categories(BaseModel):
    harassment: bool = 'A list of the categories, and whether they are flagged or not.'
    hate: bool = FieldInfo(alias = 'harassment/threatening')
    hate_threatening: bool = FieldInfo(alias = 'hate/threatening')
    illicit: Optional[bool] = None
    illicit_violent: Optional[bool] = FieldInfo(alias = 'illicit/violent', default = None)
    self_harm: bool = FieldInfo(alias = 'self-harm')
    self_harm_instructions: bool = FieldInfo(alias = 'self-harm/instructions')
    sexual: bool = FieldInfo(alias = 'self-harm/intent')
    violence: bool = FieldInfo(alias = 'sexual/minors')
    violence_graphic: bool = FieldInfo(alias = 'violence/graphic')


class CategoryAppliedInputTypes(BaseModel):
    harassment: List[Literal['text']] = '\n    A list of the categories along with the input type(s) that the score applies to.\n    '
    hate: List[Literal['text']] = FieldInfo(alias = 'harassment/threatening')
    illicit: List[Literal['text']] = FieldInfo(alias = 'hate/threatening')
    illicit_violent: List[Literal['text']] = FieldInfo(alias = 'illicit/violent')
    self_harm: List[Literal[('text', 'image')]] = FieldInfo(alias = 'self-harm')
    self_harm_instructions: List[Literal[('text', 'image')]] = FieldInfo(alias = 'self-harm/instructions')
    sexual: List[Literal[('text', 'image')]] = FieldInfo(alias = 'self-harm/intent')
    violence: List[Literal[('text', 'image')]] = FieldInfo(alias = 'sexual/minors')
    violence_graphic: List[Literal[('text', 'image')]] = FieldInfo(alias = 'violence/graphic')


class CategoryScores(BaseModel):
    harassment: float = 'A list of the categories along with their scores as predicted by model.'
    hate: float = FieldInfo(alias = 'harassment/threatening')
    illicit: float = FieldInfo(alias = 'hate/threatening')
    illicit_violent: float = FieldInfo(alias = 'illicit/violent')
    self_harm: float = FieldInfo(alias = 'self-harm')
    self_harm_instructions: float = FieldInfo(alias = 'self-harm/instructions')
    sexual: float = FieldInfo(alias = 'self-harm/intent')
    violence: float = FieldInfo(alias = 'sexual/minors')
    violence_graphic: float = FieldInfo(alias = 'violence/graphic')


class Moderation(BaseModel):
    flagged: bool = 'Moderation'

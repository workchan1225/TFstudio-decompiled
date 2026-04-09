# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: multi_grader.pyc (Python 3.11)

from typing import Union
from typing_extensions import Literal, TypeAlias
from _models import BaseModel
from python_grader import PythonGrader
from label_model_grader import LabelModelGrader
from score_model_grader import ScoreModelGrader
from string_check_grader import StringCheckGrader
from text_similarity_grader import TextSimilarityGrader
__all__ = [
    'MultiGrader',
    'Graders']
Graders: TypeAlias = Union[(StringCheckGrader, TextSimilarityGrader, PythonGrader, ScoreModelGrader, LabelModelGrader)]

class MultiGrader(BaseModel):
    type: Literal['multi'] = '\n    A MultiGrader object combines the output of multiple graders to produce a single score.\n    '

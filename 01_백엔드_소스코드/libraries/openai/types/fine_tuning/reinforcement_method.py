# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: reinforcement_method.pyc (Python 3.11)

from typing import Union, Optional
from typing_extensions import TypeAlias
from _models import BaseModel
from graders.multi_grader import MultiGrader
from graders.python_grader import PythonGrader
from graders.score_model_grader import ScoreModelGrader
from graders.string_check_grader import StringCheckGrader
from reinforcement_hyperparameters import ReinforcementHyperparameters
from graders.text_similarity_grader import TextSimilarityGrader
__all__ = [
    'ReinforcementMethod',
    'Grader']
Grader: TypeAlias = Union[(StringCheckGrader, TextSimilarityGrader, PythonGrader, ScoreModelGrader, MultiGrader)]

class ReinforcementMethod(BaseModel):
    grader: Grader = 'Configuration for the reinforcement fine-tuning method.'
    hyperparameters: Optional[ReinforcementHyperparameters] = None

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: reinforcement_method_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Union
from typing_extensions import Required, TypeAlias, TypedDict
from graders.multi_grader_param import MultiGraderParam
from graders.python_grader_param import PythonGraderParam
from graders.score_model_grader_param import ScoreModelGraderParam
from graders.string_check_grader_param import StringCheckGraderParam
from reinforcement_hyperparameters_param import ReinforcementHyperparametersParam
from graders.text_similarity_grader_param import TextSimilarityGraderParam
__all__ = [
    'ReinforcementMethodParam',
    'Grader']
Grader: 'TypeAlias' = Union[(StringCheckGraderParam, TextSimilarityGraderParam, PythonGraderParam, ScoreModelGraderParam, MultiGraderParam)]

def ReinforcementMethodParam():
    '''ReinforcementMethodParam'''
    hyperparameters: 'ReinforcementHyperparametersParam' = 'Configuration for the reinforcement fine-tuning method.'

ReinforcementMethodParam = <NODE:27>(ReinforcementMethodParam, 'ReinforcementMethodParam', TypedDict, total = False)

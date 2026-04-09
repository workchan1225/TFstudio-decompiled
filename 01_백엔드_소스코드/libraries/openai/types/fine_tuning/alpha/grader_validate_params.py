# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: grader_validate_params.pyc (Python 3.11)

from __future__ import annotations
from typing import Union
from typing_extensions import Required, TypeAlias, TypedDict
from graders.multi_grader_param import MultiGraderParam
from graders.python_grader_param import PythonGraderParam
from graders.score_model_grader_param import ScoreModelGraderParam
from graders.string_check_grader_param import StringCheckGraderParam
from graders.text_similarity_grader_param import TextSimilarityGraderParam
__all__ = [
    'GraderValidateParams',
    'Grader']

def GraderValidateParams():
    '''GraderValidateParams'''
    grader: 'Required[Grader]' = 'GraderValidateParams'

GraderValidateParams = <NODE:27>(GraderValidateParams, 'GraderValidateParams', TypedDict, total = False)
Grader: 'TypeAlias' = Union[(StringCheckGraderParam, TextSimilarityGraderParam, PythonGraderParam, ScoreModelGraderParam, MultiGraderParam)]

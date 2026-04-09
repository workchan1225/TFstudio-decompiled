# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: multi_grader_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict
from python_grader_param import PythonGraderParam
from label_model_grader_param import LabelModelGraderParam
from score_model_grader_param import ScoreModelGraderParam
from string_check_grader_param import StringCheckGraderParam
from text_similarity_grader_param import TextSimilarityGraderParam
__all__ = [
    'MultiGraderParam',
    'Graders']
Graders: 'TypeAlias' = Union[(StringCheckGraderParam, TextSimilarityGraderParam, PythonGraderParam, ScoreModelGraderParam, LabelModelGraderParam)]

def MultiGraderParam():
    '''MultiGraderParam'''
    type: "Required[Literal['multi']]" = '\n    A MultiGrader object combines the output of multiple graders to produce a single score.\n    '

MultiGraderParam = <NODE:27>(MultiGraderParam, 'MultiGraderParam', TypedDict, total = False)

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: skill_create_params.pyc (Python 3.11)

from __future__ import annotations
from typing import List, Optional
from typing_extensions import Annotated, TypedDict
from _types import FileTypes, SequenceNotStr
from _utils import PropertyInfo
from anthropic_beta_param import AnthropicBetaParam
__all__ = [
    'SkillCreateParams']

def SkillCreateParams():
    '''SkillCreateParams'''
    betas: "Annotated[List[AnthropicBetaParam], PropertyInfo(alias='anthropic-beta')]" = 'SkillCreateParams'

SkillCreateParams = <NODE:27>(SkillCreateParams, 'SkillCreateParams', TypedDict, total = False)

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: skill_list_params.pyc (Python 3.11)

from __future__ import annotations
from typing import List, Optional
from typing_extensions import Annotated, TypedDict
from _utils import PropertyInfo
from anthropic_beta_param import AnthropicBetaParam
__all__ = [
    'SkillListParams']

def SkillListParams():
    '''SkillListParams'''
    betas: "Annotated[List[AnthropicBetaParam], PropertyInfo(alias='anthropic-beta')]" = 'SkillListParams'

SkillListParams = <NODE:27>(SkillListParams, 'SkillListParams', TypedDict, total = False)

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: assistant_tool_choice_option_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Union
from typing_extensions import Literal, TypeAlias
from assistant_tool_choice_param import AssistantToolChoiceParam
__all__ = [
    'AssistantToolChoiceOptionParam']
AssistantToolChoiceOptionParam: 'TypeAlias' = Union[(Literal[('none', 'auto', 'required')], AssistantToolChoiceParam)]

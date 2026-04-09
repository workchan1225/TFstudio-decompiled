# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: assistant_tool_choice_option.pyc (Python 3.11)

from typing import Union
from typing_extensions import Literal, TypeAlias
from assistant_tool_choice import AssistantToolChoice
__all__ = [
    'AssistantToolChoiceOption']
AssistantToolChoiceOption: TypeAlias = Union[(Literal[('none', 'auto', 'required')], AssistantToolChoice)]

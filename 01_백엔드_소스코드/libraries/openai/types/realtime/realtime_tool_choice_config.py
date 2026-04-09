# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: realtime_tool_choice_config.pyc (Python 3.11)

from typing import Union
from typing_extensions import TypeAlias
from responses.tool_choice_mcp import ToolChoiceMcp
from responses.tool_choice_options import ToolChoiceOptions
from responses.tool_choice_function import ToolChoiceFunction
__all__ = [
    'RealtimeToolChoiceConfig']
RealtimeToolChoiceConfig: TypeAlias = Union[(ToolChoiceOptions, ToolChoiceFunction, ToolChoiceMcp)]

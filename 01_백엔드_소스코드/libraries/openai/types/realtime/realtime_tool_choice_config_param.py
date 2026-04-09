# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: realtime_tool_choice_config_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Union
from typing_extensions import TypeAlias
from responses.tool_choice_options import ToolChoiceOptions
from responses.tool_choice_mcp_param import ToolChoiceMcpParam
from responses.tool_choice_function_param import ToolChoiceFunctionParam
__all__ = [
    'RealtimeToolChoiceConfigParam']
RealtimeToolChoiceConfigParam: 'TypeAlias' = Union[(ToolChoiceOptions, ToolChoiceFunctionParam, ToolChoiceMcpParam)]

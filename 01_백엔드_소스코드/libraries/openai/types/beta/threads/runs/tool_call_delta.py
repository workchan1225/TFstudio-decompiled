# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tool_call_delta.pyc (Python 3.11)

from typing import Union
from typing_extensions import Annotated, TypeAlias
from _utils import PropertyInfo
from function_tool_call_delta import FunctionToolCallDelta
from file_search_tool_call_delta import FileSearchToolCallDelta
from code_interpreter_tool_call_delta import CodeInterpreterToolCallDelta
__all__ = [
    'ToolCallDelta']
ToolCallDelta: TypeAlias = Annotated[(Union[(CodeInterpreterToolCallDelta, FileSearchToolCallDelta, FunctionToolCallDelta)], PropertyInfo(discriminator = 'type'))]

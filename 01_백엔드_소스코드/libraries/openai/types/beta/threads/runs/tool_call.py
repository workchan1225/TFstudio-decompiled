# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tool_call.pyc (Python 3.11)

from typing import Union
from typing_extensions import Annotated, TypeAlias
from _utils import PropertyInfo
from function_tool_call import FunctionToolCall
from file_search_tool_call import FileSearchToolCall
from code_interpreter_tool_call import CodeInterpreterToolCall
__all__ = [
    'ToolCall']
ToolCall: TypeAlias = Annotated[(Union[(CodeInterpreterToolCall, FileSearchToolCall, FunctionToolCall)], PropertyInfo(discriminator = 'type'))]

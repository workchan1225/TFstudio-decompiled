# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: assistant_tool.pyc (Python 3.11)

from typing import Union
from typing_extensions import Annotated, TypeAlias
from _utils import PropertyInfo
from function_tool import FunctionTool
from file_search_tool import FileSearchTool
from code_interpreter_tool import CodeInterpreterTool
__all__ = [
    'AssistantTool']
AssistantTool: TypeAlias = Annotated[(Union[(CodeInterpreterTool, FileSearchTool, FunctionTool)], PropertyInfo(discriminator = 'type'))]

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: custom_tool.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
from shared.custom_tool_input_format import CustomToolInputFormat
__all__ = [
    'CustomTool']

class CustomTool(BaseModel):
    type: Literal['custom'] = 'A custom tool that processes input using a specified format.\n\n    Learn more about   [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)\n    '
    description: Optional[str] = None
    format: Optional[CustomToolInputFormat] = None

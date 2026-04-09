# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: computer_tool.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ComputerTool']

class ComputerTool(BaseModel):
    type: Literal['computer_use_preview'] = 'A tool that controls a virtual computer.\n\n    Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).\n    '

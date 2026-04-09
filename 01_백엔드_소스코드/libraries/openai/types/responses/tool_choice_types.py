# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tool_choice_types.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ToolChoiceTypes']

class ToolChoiceTypes(BaseModel):
    type: Literal[('file_search', 'web_search_preview', 'computer_use_preview', 'web_search_preview_2025_03_11', 'image_generation', 'code_interpreter')] = '\n    Indicates that the model should use a built-in tool to generate a response.\n    [Learn more about built-in tools](https://platform.openai.com/docs/guides/tools).\n    '

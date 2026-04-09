# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_prompt.pyc (Python 3.11)

from typing import Dict, Union, Optional
from typing_extensions import TypeAlias
from _models import BaseModel
from response_input_file import ResponseInputFile
from response_input_text import ResponseInputText
from response_input_image import ResponseInputImage
__all__ = [
    'ResponsePrompt',
    'Variables']
Variables: TypeAlias = Union[(str, ResponseInputText, ResponseInputImage, ResponseInputFile)]

class ResponsePrompt(BaseModel):
    id: str = '\n    Reference to a prompt template and its variables.\n    [Learn more](https://platform.openai.com/docs/guides/text?api-mode=responses#reusable-prompts).\n    '
    variables: Optional[Dict[(str, Variables)]] = None
    version: Optional[str] = None

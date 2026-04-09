# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_format_text_python.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseFormatTextPython']

class ResponseFormatTextPython(BaseModel):
    type: Literal['python'] = 'Configure the model to generate valid Python code.\n\n    See the\n    [custom grammars guide](https://platform.openai.com/docs/guides/custom-grammars) for more details.\n    '

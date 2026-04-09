# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_format_text_grammar.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseFormatTextGrammar']

class ResponseFormatTextGrammar(BaseModel):
    type: Literal['grammar'] = '\n    A custom grammar for the model to follow when generating text.\n    Learn more in the [custom grammars guide](https://platform.openai.com/docs/guides/custom-grammars).\n    '

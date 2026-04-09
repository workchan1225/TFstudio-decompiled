# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: chat_completion_content_part_text.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ChatCompletionContentPartText']

class ChatCompletionContentPartText(BaseModel):
    type: Literal['text'] = '\n    Learn about [text inputs](https://platform.openai.com/docs/guides/text-generation).\n    '

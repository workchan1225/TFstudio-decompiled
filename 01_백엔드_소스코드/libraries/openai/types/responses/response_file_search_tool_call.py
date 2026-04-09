# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_file_search_tool_call.pyc (Python 3.11)

from typing import Dict, List, Union, Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseFileSearchToolCall',
    'Result']

class Result(BaseModel):
    attributes: Optional[Dict[(str, Union[(str, float, bool)])]] = None
    file_id: Optional[str] = None
    filename: Optional[str] = None
    score: Optional[float] = None
    text: Optional[str] = None


class ResponseFileSearchToolCall(BaseModel):
    type: Literal['file_search_call'] = 'The results of a file search tool call.\n\n    See the\n    [file search guide](https://platform.openai.com/docs/guides/tools-file-search) for more information.\n    '
    results: Optional[List[Result]] = None

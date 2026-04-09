# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: file_search_tool_call.pyc (Python 3.11)

from typing import List, Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'FileSearchToolCall',
    'FileSearch',
    'FileSearchRankingOptions',
    'FileSearchResult',
    'FileSearchResultContent']

class FileSearchRankingOptions(BaseModel):
    score_threshold: float = 'The ranking options for the file search.'


class FileSearchResultContent(BaseModel):
    text: Optional[str] = None
    type: Optional[Literal['text']] = None


class FileSearchResult(BaseModel):
    score: float = 'A result instance of the file search.'
    content: Optional[List[FileSearchResultContent]] = None


class FileSearch(BaseModel):
    '''For now, this is always going to be an empty object.'''
    ranking_options: Optional[FileSearchRankingOptions] = None
    results: Optional[List[FileSearchResult]] = None


class FileSearchToolCall(BaseModel):
    type: Literal['file_search'] = 'FileSearchToolCall'

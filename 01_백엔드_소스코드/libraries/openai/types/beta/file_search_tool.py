# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: file_search_tool.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'FileSearchTool',
    'FileSearch',
    'FileSearchRankingOptions']

class FileSearchRankingOptions(BaseModel):
    score_threshold: float = 'The ranking options for the file search.\n\n    If not specified, the file search tool will use the `auto` ranker and a score_threshold of 0.\n\n    See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.\n    '
    ranker: Optional[Literal[('auto', 'default_2024_08_21')]] = None


class FileSearch(BaseModel):
    '''Overrides for the file search tool.'''
    max_num_results: Optional[int] = None
    ranking_options: Optional[FileSearchRankingOptions] = None


class FileSearchTool(BaseModel):
    type: Literal['file_search'] = 'FileSearchTool'
    file_search: Optional[FileSearch] = None

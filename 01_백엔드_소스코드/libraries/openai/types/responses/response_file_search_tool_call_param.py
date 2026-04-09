# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_file_search_tool_call_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict
from _types import SequenceNotStr
__all__ = [
    'ResponseFileSearchToolCallParam',
    'Result']

def Result():
    '''Result'''
    text: 'str' = 'Result'

Result = <NODE:27>(Result, 'Result', TypedDict, total = False)

def ResponseFileSearchToolCallParam():
    '''ResponseFileSearchToolCallParam'''
    results: 'Optional[Iterable[Result]]' = 'The results of a file search tool call.\n\n    See the\n    [file search guide](https://platform.openai.com/docs/guides/tools-file-search) for more information.\n    '

ResponseFileSearchToolCallParam = <NODE:27>(ResponseFileSearchToolCallParam, 'ResponseFileSearchToolCallParam', TypedDict, total = False)

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_function_web_search.pyc (Python 3.11)

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias
from _utils import PropertyInfo
from _models import BaseModel
__all__ = [
    'ResponseFunctionWebSearch',
    'Action',
    'ActionSearch',
    'ActionSearchSource',
    'ActionOpenPage',
    'ActionFind']

class ActionSearchSource(BaseModel):
    url: str = 'A source used in the search.'


class ActionSearch(BaseModel):
    type: Literal['search'] = 'Action type "search" - Performs a web search query.'
    sources: Optional[List[ActionSearchSource]] = None


class ActionOpenPage(BaseModel):
    url: str = 'Action type "open_page" - Opens a specific URL from search results.'


class ActionFind(BaseModel):
    url: str = 'Action type "find": Searches for a pattern within a loaded page.'

Action: TypeAlias = Annotated[(Union[(ActionSearch, ActionOpenPage, ActionFind)], PropertyInfo(discriminator = 'type'))]

class ResponseFunctionWebSearch(BaseModel):
    type: Literal['web_search_call'] = 'The results of a web search tool call.\n\n    See the\n    [web search guide](https://platform.openai.com/docs/guides/tools-web-search) for more information.\n    '

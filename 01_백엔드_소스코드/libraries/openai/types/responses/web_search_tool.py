# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: web_search_tool.pyc (Python 3.11)

from typing import List, Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'WebSearchTool',
    'Filters',
    'UserLocation']

class Filters(BaseModel):
    '''Filters for the search.'''
    allowed_domains: Optional[List[str]] = None


class UserLocation(BaseModel):
    '''The approximate location of the user.'''
    city: Optional[str] = None
    country: Optional[str] = None
    region: Optional[str] = None
    timezone: Optional[str] = None
    type: Optional[Literal['approximate']] = None


class WebSearchTool(BaseModel):
    type: Literal[('web_search', 'web_search_2025_08_26')] = 'Search the Internet for sources related to the prompt.\n\n    Learn more about the\n    [web search tool](https://platform.openai.com/docs/guides/tools-web-search).\n    '
    filters: Optional[Filters] = None
    search_context_size: Optional[Literal[('low', 'medium', 'high')]] = None
    user_location: Optional[UserLocation] = None

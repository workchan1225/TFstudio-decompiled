# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: web_search_tool_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Optional
from typing_extensions import Literal, Required, TypedDict
from _types import SequenceNotStr
__all__ = [
    'WebSearchToolParam',
    'Filters',
    'UserLocation']

def Filters():
    '''Filters'''
    allowed_domains: 'Optional[SequenceNotStr[str]]' = 'Filters for the search.'

Filters = <NODE:27>(Filters, 'Filters', TypedDict, total = False)

def UserLocation():
    '''UserLocation'''
    type: "Literal['approximate']" = 'The approximate location of the user.'

UserLocation = <NODE:27>(UserLocation, 'UserLocation', TypedDict, total = False)

def WebSearchToolParam():
    '''WebSearchToolParam'''
    user_location: 'Optional[UserLocation]' = 'Search the Internet for sources related to the prompt.\n\n    Learn more about the\n    [web search tool](https://platform.openai.com/docs/guides/tools-web-search).\n    '

WebSearchToolParam = <NODE:27>(WebSearchToolParam, 'WebSearchToolParam', TypedDict, total = False)

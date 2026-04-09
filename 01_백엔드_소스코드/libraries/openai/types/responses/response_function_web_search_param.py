# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_function_web_search_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict
__all__ = [
    'ResponseFunctionWebSearchParam',
    'Action',
    'ActionSearch',
    'ActionSearchSource',
    'ActionOpenPage',
    'ActionFind']

def ActionSearchSource():
    '''ActionSearchSource'''
    url: 'Required[str]' = 'A source used in the search.'

ActionSearchSource = <NODE:27>(ActionSearchSource, 'ActionSearchSource', TypedDict, total = False)

def ActionSearch():
    '''ActionSearch'''
    sources: 'Iterable[ActionSearchSource]' = 'Action type "search" - Performs a web search query.'

ActionSearch = <NODE:27>(ActionSearch, 'ActionSearch', TypedDict, total = False)

def ActionOpenPage():
    '''ActionOpenPage'''
    url: 'Required[str]' = 'Action type "open_page" - Opens a specific URL from search results.'

ActionOpenPage = <NODE:27>(ActionOpenPage, 'ActionOpenPage', TypedDict, total = False)

def ActionFind():
    '''ActionFind'''
    url: 'Required[str]' = 'Action type "find": Searches for a pattern within a loaded page.'

ActionFind = <NODE:27>(ActionFind, 'ActionFind', TypedDict, total = False)
Action: 'TypeAlias' = Union[(ActionSearch, ActionOpenPage, ActionFind)]

def ResponseFunctionWebSearchParam():
    '''ResponseFunctionWebSearchParam'''
    type: "Required[Literal['web_search_call']]" = 'The results of a web search tool call.\n\n    See the\n    [web search guide](https://platform.openai.com/docs/guides/tools-web-search) for more information.\n    '

ResponseFunctionWebSearchParam = <NODE:27>(ResponseFunctionWebSearchParam, 'ResponseFunctionWebSearchParam', TypedDict, total = False)

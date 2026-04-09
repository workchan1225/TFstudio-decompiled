# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: web_search_preview_tool_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Optional
from typing_extensions import Literal, Required, TypedDict
__all__ = [
    'WebSearchPreviewToolParam',
    'UserLocation']

def UserLocation():
    '''UserLocation'''
    timezone: 'Optional[str]' = "The user's location."

UserLocation = <NODE:27>(UserLocation, 'UserLocation', TypedDict, total = False)

def WebSearchPreviewToolParam():
    '''WebSearchPreviewToolParam'''
    user_location: 'Optional[UserLocation]' = 'This tool searches the web for relevant results to use in a response.\n\n    Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).\n    '

WebSearchPreviewToolParam = <NODE:27>(WebSearchPreviewToolParam, 'WebSearchPreviewToolParam', TypedDict, total = False)

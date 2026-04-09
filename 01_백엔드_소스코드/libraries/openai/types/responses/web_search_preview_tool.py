# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: web_search_preview_tool.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'WebSearchPreviewTool',
    'UserLocation']

class UserLocation(BaseModel):
    type: Literal['approximate'] = "The user's location."
    city: Optional[str] = None
    country: Optional[str] = None
    region: Optional[str] = None
    timezone: Optional[str] = None


class WebSearchPreviewTool(BaseModel):
    type: Literal[('web_search_preview', 'web_search_preview_2025_03_11')] = 'This tool searches the web for relevant results to use in a response.\n\n    Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).\n    '
    search_context_size: Optional[Literal[('low', 'medium', 'high')]] = None
    user_location: Optional[UserLocation] = None

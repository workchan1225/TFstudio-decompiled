# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: citations_delta.pyc (Python 3.11)

from typing import Union
from typing_extensions import Literal, Annotated, TypeAlias
from _utils import PropertyInfo
from _models import BaseModel
from citation_char_location import CitationCharLocation
from citation_page_location import CitationPageLocation
from citation_content_block_location import CitationContentBlockLocation
from citations_search_result_location import CitationsSearchResultLocation
from citations_web_search_result_location import CitationsWebSearchResultLocation
__all__ = [
    'CitationsDelta',
    'Citation']
Citation: TypeAlias = Annotated[(Union[(CitationCharLocation, CitationPageLocation, CitationContentBlockLocation, CitationsWebSearchResultLocation, CitationsSearchResultLocation)], PropertyInfo(discriminator = 'type'))]

class CitationsDelta(BaseModel):
    type: Literal['citations_delta'] = 'CitationsDelta'

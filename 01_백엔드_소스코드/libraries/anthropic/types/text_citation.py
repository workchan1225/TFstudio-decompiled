# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: text_citation.pyc (Python 3.11)

from typing import Union
from typing_extensions import Annotated, TypeAlias
from _utils import PropertyInfo
from citation_char_location import CitationCharLocation
from citation_page_location import CitationPageLocation
from citation_content_block_location import CitationContentBlockLocation
from citations_search_result_location import CitationsSearchResultLocation
from citations_web_search_result_location import CitationsWebSearchResultLocation
__all__ = [
    'TextCitation']
TextCitation: TypeAlias = Annotated[(Union[(CitationCharLocation, CitationPageLocation, CitationContentBlockLocation, CitationsWebSearchResultLocation, CitationsSearchResultLocation)], PropertyInfo(discriminator = 'type'))]

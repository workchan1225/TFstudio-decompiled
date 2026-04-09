# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_text_citation.pyc (Python 3.11)

from typing import Union
from typing_extensions import Annotated, TypeAlias
from _utils import PropertyInfo
from beta_citation_char_location import BetaCitationCharLocation
from beta_citation_page_location import BetaCitationPageLocation
from beta_citation_content_block_location import BetaCitationContentBlockLocation
from beta_citation_search_result_location import BetaCitationSearchResultLocation
from beta_citations_web_search_result_location import BetaCitationsWebSearchResultLocation
__all__ = [
    'BetaTextCitation']
BetaTextCitation: TypeAlias = Annotated[(Union[(BetaCitationCharLocation, BetaCitationPageLocation, BetaCitationContentBlockLocation, BetaCitationsWebSearchResultLocation, BetaCitationSearchResultLocation)], PropertyInfo(discriminator = 'type'))]

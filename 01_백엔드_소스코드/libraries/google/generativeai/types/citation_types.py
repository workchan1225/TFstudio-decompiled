# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: citation_types.pyc (Python 3.11)

from __future__ import annotations
from typing import List
from typing_extensions import TypedDict
from google.generativeai import protos
from google.generativeai import string_utils
__all__ = [
    'CitationMetadataDict',
    'CitationSourceDict']

class CitationSourceDict(TypedDict):
    license: 'str | None' = 'CitationSourceDict'
    __doc__ = string_utils.strip_oneof(protos.CitationSource.__doc__)


class CitationMetadataDict(TypedDict):
    citation_sources: 'List[CitationSourceDict | None]' = 'CitationMetadataDict'
    __doc__ = string_utils.strip_oneof(protos.CitationMetadata.__doc__)

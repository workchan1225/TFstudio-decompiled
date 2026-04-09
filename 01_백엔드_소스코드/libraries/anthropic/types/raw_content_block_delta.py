# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: raw_content_block_delta.pyc (Python 3.11)

from typing import Union
from typing_extensions import Annotated, TypeAlias
from _utils import PropertyInfo
from text_delta import TextDelta
from thinking_delta import ThinkingDelta
from citations_delta import CitationsDelta
from signature_delta import SignatureDelta
from input_json_delta import InputJSONDelta
__all__ = [
    'RawContentBlockDelta']
RawContentBlockDelta: TypeAlias = Annotated[(Union[(TextDelta, InputJSONDelta, CitationsDelta, ThinkingDelta, SignatureDelta)], PropertyInfo(discriminator = 'type'))]

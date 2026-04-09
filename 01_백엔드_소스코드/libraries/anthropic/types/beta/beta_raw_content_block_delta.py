# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_raw_content_block_delta.pyc (Python 3.11)

from typing import Union
from typing_extensions import Annotated, TypeAlias
from _utils import PropertyInfo
from beta_text_delta import BetaTextDelta
from beta_thinking_delta import BetaThinkingDelta
from beta_citations_delta import BetaCitationsDelta
from beta_signature_delta import BetaSignatureDelta
from beta_input_json_delta import BetaInputJSONDelta
__all__ = [
    'BetaRawContentBlockDelta']
BetaRawContentBlockDelta: TypeAlias = Annotated[(Union[(BetaTextDelta, BetaInputJSONDelta, BetaCitationsDelta, BetaThinkingDelta, BetaSignatureDelta)], PropertyInfo(discriminator = 'type'))]

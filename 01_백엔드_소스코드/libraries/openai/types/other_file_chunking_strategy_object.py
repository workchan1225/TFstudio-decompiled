# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: other_file_chunking_strategy_object.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'OtherFileChunkingStrategyObject']

class OtherFileChunkingStrategyObject(BaseModel):
    type: Literal['other'] = 'This is returned when the chunking strategy is unknown.\n\n    Typically, this is because the file was indexed before the `chunking_strategy` concept was introduced in the API.\n    '

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: static_file_chunking_strategy_object.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
from static_file_chunking_strategy import StaticFileChunkingStrategy
__all__ = [
    'StaticFileChunkingStrategyObject']

class StaticFileChunkingStrategyObject(BaseModel):
    type: Literal['static'] = 'StaticFileChunkingStrategyObject'

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: file_chunking_strategy.pyc (Python 3.11)

from typing import Union
from typing_extensions import Annotated, TypeAlias
from _utils import PropertyInfo
from other_file_chunking_strategy_object import OtherFileChunkingStrategyObject
from static_file_chunking_strategy_object import StaticFileChunkingStrategyObject
__all__ = [
    'FileChunkingStrategy']
FileChunkingStrategy: TypeAlias = Annotated[(Union[(StaticFileChunkingStrategyObject, OtherFileChunkingStrategyObject)], PropertyInfo(discriminator = 'type'))]

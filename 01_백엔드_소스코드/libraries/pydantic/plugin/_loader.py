# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _loader.pyc (Python 3.11)

from __future__ import annotations
from importlib.metadata import metadata as importlib_metadata
import os
import warnings
from collections.abc import Iterable
from typing import TYPE_CHECKING, Final
if TYPE_CHECKING:
    from  import PydanticPluginProtocol
PYDANTIC_ENTRY_POINT_GROUP: 'Final[str]' = 'pydantic'
_plugins: 'dict[str, PydanticPluginProtocol] | None' = None
_loading_plugins: 'bool' = False

def get_plugins():
    '''Load plugins for Pydantic.

    Inspired by: https://github.com/pytest-dev/pluggy/blob/1.3.0/src/pluggy/_manager.py#L376-L402
    '''
    disabled_plugins = os.getenv('PYDANTIC_DISABLE_PLUGINS')
    if _loading_plugins:
        return ()
    if None in ('__all__', '1', 'true'):
        return ()
# WARNING: Decompyle incomplete

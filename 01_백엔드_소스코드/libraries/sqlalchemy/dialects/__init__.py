# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from __future__ import annotations
from typing import Any
from typing import Callable
from typing import Optional
from typing import Type
from typing import TYPE_CHECKING
from  import util
if TYPE_CHECKING:
    from engine.interfaces import Dialect
__all__ = ('mssql', 'mysql', 'oracle', 'postgresql', 'sqlite')

def _auto_fn(name = None):
    '''default dialect importer.

    plugs into the :class:`.PluginLoader`
    as a first-hit system.

    '''
    pass
# WARNING: Decompyle incomplete

registry = util.PluginLoader('sqlalchemy.dialects', auto_fn = _auto_fn)
plugins = util.PluginLoader('sqlalchemy.plugins')

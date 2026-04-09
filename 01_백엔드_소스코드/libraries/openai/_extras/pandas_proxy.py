# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: pandas_proxy.pyc (Python 3.11)

from __future__ import annotations
from typing import TYPE_CHECKING, Any
from typing_extensions import override
from _utils import LazyProxy
from _common import MissingDependencyError, format_instructions
if TYPE_CHECKING:
    import pandas
PANDAS_INSTRUCTIONS = format_instructions(library = 'pandas', extra = 'datalib')

def PandasProxy():
    '''PandasProxy'''
    __load__ = (lambda self = None: try:
import pandasexcept ImportError:
err = Noneraise MissingDependencyError(PANDAS_INSTRUCTIONS), errerr = Nonedel errpandas)()

PandasProxy = <NODE:27>(PandasProxy, 'PandasProxy', LazyProxy[Any])
if not TYPE_CHECKING:
    pandas = PandasProxy()
    return None

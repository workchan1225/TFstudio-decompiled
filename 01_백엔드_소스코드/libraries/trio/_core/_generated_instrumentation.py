# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _generated_instrumentation.pyc (Python 3.11)

from __future__ import annotations
from typing import TYPE_CHECKING
from _ki import enable_ki_protection
from _run import GLOBAL_RUN_CONTEXT
if TYPE_CHECKING:
    from _instrumentation import Instrument
__all__ = [
    'add_instrument',
    'remove_instrument']
add_instrument = (lambda instrument = None: try:
GLOBAL_RUN_CONTEXT.runner.instruments.add_instrument(instrument)except AttributeError:
raise RuntimeError('must be called from async context'), None)()
remove_instrument = (lambda instrument = None: try:
GLOBAL_RUN_CONTEXT.runner.instruments.remove_instrument(instrument)except AttributeError:
raise RuntimeError('must be called from async context'), None)()

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: contexts.pyc (Python 3.11)

from __future__ import annotations
from contextlib import contextmanager
import os
import sys
from typing import IO, TYPE_CHECKING
from pandas.compat import CHAINED_WARNING_DISABLED
from pandas.errors import ChainedAssignmentError
from pandas.io.common import get_handle
if TYPE_CHECKING:
    from collections.abc import Generator
    from pandas._typing import BaseBuffer, CompressionOptions, FilePath
decompress_file = (lambda path = None, compression = None: pass# WARNING: Decompyle incomplete
)()
set_timezone = (lambda tz = None: pass# WARNING: Decompyle incomplete
)()
with_csv_dialect = (lambda name = None: pass# WARNING: Decompyle incomplete
)()

def raises_chained_assignment_error(extra_warnings, extra_match = ((), ())):
    assert_produces_warning = assert_produces_warning
    import pandas._testing
    if CHAINED_WARNING_DISABLED:
        if not extra_warnings:
            nullcontext = nullcontext
            import contextlib
            return nullcontext()
        return assert_produces_warning(extra_warnings, match = extra_match)
    warning = None
    match = 'A value is being set on a copy of a DataFrame or Series through chained assignment'
# WARNING: Decompyle incomplete

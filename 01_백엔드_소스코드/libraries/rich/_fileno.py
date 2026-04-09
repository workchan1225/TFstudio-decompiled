# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _fileno.pyc (Python 3.11)

from __future__ import annotations
from typing import IO, Callable

def get_fileno(file_like = None):
    '''Get fileno() from a file, accounting for poorly implemented file-like objects.

    Args:
        file_like (IO): A file-like object.

    Returns:
        int | None: The result of fileno if available, or None if operation failed.
    '''
    fileno = getattr(file_like, 'fileno', None)
# WARNING: Decompyle incomplete

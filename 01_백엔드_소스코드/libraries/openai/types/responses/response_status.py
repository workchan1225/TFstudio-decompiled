# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_status.pyc (Python 3.11)

from typing_extensions import Literal, TypeAlias
__all__ = [
    'ResponseStatus']
ResponseStatus: TypeAlias = Literal[('completed', 'failed', 'in_progress', 'cancelled', 'queued', 'incomplete')]

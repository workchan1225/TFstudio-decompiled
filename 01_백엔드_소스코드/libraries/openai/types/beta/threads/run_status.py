# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: run_status.pyc (Python 3.11)

from typing_extensions import Literal, TypeAlias
__all__ = [
    'RunStatus']
RunStatus: TypeAlias = Literal[('queued', 'in_progress', 'requires_action', 'cancelling', 'cancelled', 'failed', 'completed', 'incomplete', 'expired')]

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: utils.pyc (Python 3.11)

from __future__ import annotations
import time
__all__ = [
    'Deadline']

class Deadline:
    '''
    Manage timeouts across multiple steps.

    Args:
        timeout: Time available in seconds or :obj:`None` if there is no limit.

    '''
    
    def __init__(self = None, timeout = None):
        self
    # WARNING: Decompyle incomplete

    
    def timeout(self = None, *, raise_if_elapsed):
        '''
        Calculate a timeout from a deadline.

        Args:
            raise_if_elapsed: Whether to raise :exc:`TimeoutError`
                if the deadline lapsed.

        Raises:
            TimeoutError: If the deadline lapsed.

        Returns:
            Time left in seconds or :obj:`None` if there is no limit.

        '''
        pass
    # WARNING: Decompyle incomplete

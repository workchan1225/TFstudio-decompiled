# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: before_sleep.pyc (Python 3.11)

import typing
from tenacity import _utils
if typing.TYPE_CHECKING:
    import logging
    from tenacity import RetryCallState

def before_sleep_nothing(retry_state = None):
    '''Before sleep strategy that does nothing.'''
    pass


def before_sleep_log(logger = None, log_level = None, exc_info = None):
    '''Before sleep strategy that logs to some logger the attempt.'''
    pass
# WARNING: Decompyle incomplete

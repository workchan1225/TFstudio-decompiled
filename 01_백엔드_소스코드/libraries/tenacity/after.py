# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: after.pyc (Python 3.11)

import typing
from tenacity import _utils
if typing.TYPE_CHECKING:
    import logging
    from tenacity import RetryCallState

def after_nothing(retry_state = None):
    '''After call strategy that does nothing.'''
    pass


def after_log(logger = None, log_level = None, sec_format = None):
    '''After call strategy that logs to some logger the finished attempt.'''
    pass
# WARNING: Decompyle incomplete

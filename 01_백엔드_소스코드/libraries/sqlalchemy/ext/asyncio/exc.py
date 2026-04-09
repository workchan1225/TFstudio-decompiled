# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: exc.pyc (Python 3.11)

from  import exc

class AsyncMethodRequired(exc.InvalidRequestError):
    """an API can't be used because its result would not be
    compatible with async"""
    pass


class AsyncContextNotStarted(exc.InvalidRequestError):
    '''a startable context manager has not been started.'''
    pass


class AsyncContextAlreadyStarted(exc.InvalidRequestError):
    '''a startable context manager is already started.'''
    pass

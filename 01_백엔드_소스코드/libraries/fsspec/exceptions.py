# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: exceptions.pyc (Python 3.11)

'''
fsspec user-defined exception classes
'''
import asyncio

class BlocksizeMismatchError(ValueError):
    '''
    Raised when a cached file is opened with a different blocksize than it was
    written with
    '''
    pass


class FSTimeoutError(asyncio.TimeoutError):
    '''
    Raised when a fsspec function timed out occurs
    '''
    pass

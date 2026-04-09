# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''Top-level package for sniffio.'''
__all__ = [
    'current_async_library',
    'AsyncLibraryNotFoundError',
    'current_async_library_cvar',
    'thread_local']
from _version import __version__
from _impl import current_async_library, AsyncLibraryNotFoundError, current_async_library_cvar, thread_local

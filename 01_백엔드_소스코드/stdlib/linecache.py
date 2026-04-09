# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: linecache.pyc (Python 3.11)

'''Cache lines from Python source files.

This is intended to read lines from modules imported -- hence if a filename
is not found, it will look down the module search path for a file by
that name.
'''
import functools
import sys
import os
import tokenize
__all__ = [
    'getline',
    'clearcache',
    'checkcache',
    'lazycache']
cache = { }

def clearcache():
    '''Clear the cache entirely.'''
    cache.clear()


def getline(filename, lineno, module_globals = (None,)):
    """Get a line for a Python source file from the cache.
    Update the cache if it doesn't contain an entry for this file already."""
    lines = getlines(filename, module_globals)
    if  <= 1, lineno or 1, lineno <= len(lines):
        pass
    
    return lines[lineno - 1]
    return ''


def getlines(filename, module_globals = (None,)):
    """Get the lines for a Python source file from the cache.
    Update the cache if it doesn't contain an entry for this file already."""
    if filename in cache:
        entry = cache[filename]
        if len(entry) != 1:
            return cache[filename][2]
        
        try:
            return updatecache(filename, module_globals)
        except MemoryError:
            clearcache()
            return 



def checkcache(filename = (None,)):
    '''Discard cache entries that are out of date.
    (This is not checked upon each call!)'''
    pass
# WARNING: Decompyle incomplete


def updatecache(filename, module_globals = (None,)):
    """Update a cache entry and return its list of lines.
    If something's wrong, print a message, discard the cache entry,
    and return an empty list."""
    if filename in cache and len(cache[filename]) != 1:
        cache.pop(filename, None)
    if (filename or filename.startswith('<')) and filename.endswith('>'):
        return []
    fullname = None
# WARNING: Decompyle incomplete


def lazycache(filename, module_globals):
    '''Seed the cache for filename with module_globals.

    The module loader will be asked for the source only when getlines is
    called, not immediately.

    If there is an entry in the cache already, it is not altered.

    :return: True if a lazy load is registered in the cache,
        otherwise False. To register such a load a module loader with a
        get_source method must be found, the filename must be a cacheable
        filename, and the filename must not be already cached.
    '''
    if filename in cache:
        if len(cache[filename]) == 1:
            return True
        return None
    if (None or filename.startswith('<')) and filename.endswith('>'):
        return False
# WARNING: Decompyle incomplete

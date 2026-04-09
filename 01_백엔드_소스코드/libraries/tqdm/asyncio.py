# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: asyncio.pyc (Python 3.11)

'''
Asynchronous progressbar decorator for iterators.
Includes a default `range` iterator printing to `stderr`.

Usage:
>>> from tqdm.asyncio import trange, tqdm
>>> async for i in trange(10):
...     ...
'''
import asyncio
from sys import version_info
from std import tqdm as std_tqdm
__author__ = {
    'github.com/': [
        'casperdcl'] }
__all__ = [
    'tqdm_asyncio',
    'tarange',
    'tqdm',
    'trange']

class tqdm_asyncio(std_tqdm):
    pass
# WARNING: Decompyle incomplete


def tarange(*args, **kwargs):
    '''
    A shortcut for `tqdm.asyncio.tqdm(range(*args), **kwargs)`.
    '''
    pass
# WARNING: Decompyle incomplete

tqdm = tqdm_asyncio
trange = tarange

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: gui.pyc (Python 3.11)

'''
Matplotlib GUI progressbar decorator for iterators.

Usage:
>>> from tqdm.gui import trange, tqdm
>>> for i in trange(10):
...     ...
'''
import re
from warnings import warn
from std import TqdmExperimentalWarning
from std import tqdm as std_tqdm
__author__ = {
    'github.com/': [
        'casperdcl',
        'lrq3000'] }
__all__ = [
    'tqdm_gui',
    'tgrange',
    'tqdm',
    'trange']

class tqdm_gui(std_tqdm):
    pass
# WARNING: Decompyle incomplete


def tgrange(*args, **kwargs):
    '''Shortcut for `tqdm.gui.tqdm(range(*args), **kwargs)`.'''
    pass
# WARNING: Decompyle incomplete

tqdm = tqdm_gui
trange = tgrange

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ordered_set.pyc (Python 3.11)

'''
An OrderedSet is a custom MutableSet that remembers its order, so that every
entry has an index that can be looked up.

Based on a recipe originally posted to ActiveState Recipes by Raymond Hettiger,
and released under the MIT license.
'''
import itertools as it
from collections import deque

try:
    from collections.abc import MutableSet, Sequence
except ImportError:
    from collections import MutableSet, Sequence

SLICE_ALL = slice(None)
__version__ = '3.1'

def is_iterable(obj):

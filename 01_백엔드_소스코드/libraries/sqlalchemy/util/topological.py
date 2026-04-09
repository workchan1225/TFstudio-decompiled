# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: topological.pyc (Python 3.11)

'''Topological sorting algorithms.'''
from __future__ import annotations
from typing import Any
from typing import Collection
from typing import DefaultDict
from typing import Iterable
from typing import Iterator
from typing import Sequence
from typing import Set
from typing import Tuple
from typing import TypeVar
from  import util
from exc import CircularDependencyError
_T = TypeVar('_T', bound = Any)
__all__ = [
    'sort',
    'sort_as_subsets',
    'find_cycles']

def sort_as_subsets(tuples = None, allitems = None):
    pass
# WARNING: Decompyle incomplete


def sort(tuples = None, allitems = None, deterministic_order = None):
    '''sort the given list of items by dependency.

    \'tuples\' is a list of tuples representing a partial ordering.

    deterministic_order is no longer used, the order is now always
    deterministic given the order of "allitems".    the flag is there
    for backwards compatibility with Alembic.

    '''
    pass
# WARNING: Decompyle incomplete


def find_cycles(tuples = None, allitems = None):
    edges = util.defaultdict(set)
# WARNING: Decompyle incomplete


def _gen_edges(edges = None):
    pass
# WARNING: Decompyle incomplete

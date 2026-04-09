# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: utils.pyc (Python 3.11)

import bisect
from collections import defaultdict
from sympy.combinatorics import Permutation
from sympy.core.containers import Tuple
from sympy.core.numbers import Integer

def _get_mapping_from_subranks(subranks):
    mapping = { }
    counter = 0
    for i, rank in enumerate(subranks):
        for j in range(rank):
            mapping[counter] = (i, j)
            counter += 1
            return mapping


def _get_contraction_links(args, subranks, *contraction_indices):
    pass
# WARNING: Decompyle incomplete


def _sort_contraction_indices(pairing_indices):
    pairing_indices = pairing_indices()
    pairing_indices.sort(key = (lambda x: min(x)))
    return pairing_indices


def _get_diagonal_indices(flattened_indices):
    pass
# WARNING: Decompyle incomplete


def _get_argindex(subindices, ind):
    for i, sind in enumerate(subindices):
        if ind == sind:
            
            return None, i
        if None(sind, (set, frozenset)) and ind in sind:
            
            return None, i
        raise IndexError(f'''{ind!s} not found in {subindices!s}''')


def _apply_recursively_over_nested_lists(func, arr):
    pass
# WARNING: Decompyle incomplete


def _build_push_indices_up_func_transformation(flattened_contraction_indices):
    pass
# WARNING: Decompyle incomplete


def _build_push_indices_down_func_transformation(flattened_contraction_indices):
    pass
# WARNING: Decompyle incomplete


def _apply_permutation_to_list(perm = None, target_list = None):
    '''
    Permute a list according to the given permutation.
    '''
    new_list = range(perm.size)()
    for i, e in enumerate(target_list):
        new_list[perm(i)] = e
        return new_list

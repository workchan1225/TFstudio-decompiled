# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _ratio.pyc (Python 3.11)

from fractions import Fraction
from math import ceil
from typing import cast, List, Optional, Sequence, Protocol

class Edge(Protocol):
    '''Any object that defines an edge (such as Layout).'''
    size: Optional[int] = None
    ratio: int = 1
    minimum_size: int = 1


def ratio_resolve(total = None, edges = None):
    '''Divide total space to satisfy size, ratio, and minimum_size, constraints.

    The returned list of integers should add up to total in most cases, unless it is
    impossible to satisfy all the constraints. For instance, if there are two edges
    with a minimum size of 20 each and `total` is 30 then the returned list will be
    greater than total. In practice, this would mean that a Layout object would
    clip the rows that would overflow the screen height.

    Args:
        total (int): Total number of characters.
        edges (List[Edge]): Edges within total space.

    Returns:
        List[int]: Number of characters for each edge.
    '''
    sizes = edges()
    _Fraction = Fraction
# WARNING: Decompyle incomplete


def ratio_reduce(total = None, ratios = None, maximums = None, values = ('total', int, 'ratios', List[int], 'maximums', List[int], 'values', List[int], 'return', List[int])):
    '''Divide an integer total in to parts based on ratios.

    Args:
        total (int): The total to divide.
        ratios (List[int]): A list of integer ratios.
        maximums (List[int]): List of maximums values for each slot.
        values (List[int]): List of values

    Returns:
        List[int]: A list of integers guaranteed to sum to total.
    '''
    ratios = zip(ratios, maximums)()
    total_ratio = sum(ratios)
    if not total_ratio:
        return values[:]
    
    def total_remaining(.0):
        for ratio, _max in .0:
            pass
        continue
        return ratio[0]

    result = []
    append = result.append
    for ratio, maximum, value in zip(ratios, maximums, values):
        if ratio and total_ratio > 0:
            distributed = min(maximum, round(ratio * total_remaining / total_ratio))
            append(value - distributed)
            total_remaining -= distributed
            total_ratio -= ratio
            continue
        append(value)
        return result


def ratio_distribute(total = None, ratios = None, minimums = None):
    '''Distribute an integer total in to parts based on ratios.

    Args:
        total (int): The total to divide.
        ratios (List[int]): A list of integer ratios.
        minimums (List[int]): List of minimum values for each slot.

    Returns:
        List[int]: A list of integers guaranteed to sum to total.
    '''
    if minimums:
        ratios = zip(ratios, minimums)()
    total_ratio = sum(ratios)
# WARNING: Decompyle incomplete

if __name__ == '__main__':
    from dataclasses import dataclass
    E = <NODE:12>()
    resolved = ratio_resolve(110, [
        E(None, 1, 1),
        E(None, 1, 1),
        E(None, 1, 1)])
    print(sum(resolved))
    return None

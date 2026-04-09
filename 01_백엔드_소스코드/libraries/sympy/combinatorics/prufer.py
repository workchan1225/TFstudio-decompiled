# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: prufer.pyc (Python 3.11)

from sympy.core import Basic
from sympy.core.containers import Tuple
from sympy.tensor.array import Array
from sympy.core.sympify import _sympify
from sympy.utilities.iterables import flatten, iterable
from sympy.utilities.misc import as_int
from collections import defaultdict

class Prufer(Basic):
    """
    The Prufer correspondence is an algorithm that describes the
    bijection between labeled trees and the Prufer code. A Prufer
    code of a labeled tree is unique up to isomorphism and has
    a length of n - 2.

    Prufer sequences were first used by Heinz Prufer to give a
    proof of Cayley's formula.

    References
    ==========

    .. [1] https://mathworld.wolfram.com/LabeledTree.html

    """
    _prufer_repr = None
    _tree_repr = None
    _nodes = None
    _rank = None
    prufer_repr = (lambda self: pass# WARNING: Decompyle incomplete
)()
    tree_repr = (lambda self: pass# WARNING: Decompyle incomplete
)()
    nodes = (lambda self: self._nodes)()
    rank = (lambda self: pass# WARNING: Decompyle incomplete
)()
    size = (lambda self: self.prev(self.rank).prev().rank + 1)()
    to_prufer = (lambda tree, n: d = defaultdict(int)L = []# WARNING: Decompyle incomplete
)()
    to_tree = (lambda prufer: pass# WARNING: Decompyle incomplete
)()
    edges = (lambda : pass# WARNING: Decompyle incomplete
)()
    
    def prufer_rank(self):
        '''Computes the rank of a Prufer sequence.

        Examples
        ========

        >>> from sympy.combinatorics.prufer import Prufer
        >>> a = Prufer([[0, 1], [0, 2], [0, 3]])
        >>> a.prufer_rank()
        0

        See Also
        ========

        rank, next, prev, size

        '''
        r = 0
        p = 1
        for i in range(self.nodes - 3, -1, -1):
            r += p * self.prufer_repr[i]
            p *= self.nodes
            return r

    unrank = (lambda self, rank, n: pass# WARNING: Decompyle incomplete
)()
    
    def __new__(cls, *args, **kw_args):
        '''The constructor for the Prufer object.

        Examples
        ========

        >>> from sympy.combinatorics.prufer import Prufer

        A Prufer object can be constructed from a list of edges:

        >>> a = Prufer([[0, 1], [0, 2], [0, 3]])
        >>> a.prufer_repr
        [0, 0]

        If the number of nodes is given, no checking of the nodes will
        be performed; it will be assumed that nodes 0 through n - 1 are
        present:

        >>> Prufer([[0, 1], [0, 2], [0, 3]], 4)
        Prufer([[0, 1], [0, 2], [0, 3]], 4)

        A Prufer object can be constructed from a Prufer sequence:

        >>> b = Prufer([1, 3])
        >>> b.tree_repr
        [[0, 1], [1, 3], [2, 3]]

        '''
        arg0 = Array(args[0]) if args[0] else Tuple()
        args = tuple + (lambda .0: pass# WARNING: Decompyle incomplete
)(args[1:]())
    # WARNING: Decompyle incomplete

    
    def next(self, delta = (1,)):
        '''Generates the Prufer sequence that is delta beyond the current one.

        Examples
        ========

        >>> from sympy.combinatorics.prufer import Prufer
        >>> a = Prufer([[0, 1], [0, 2], [0, 3]])
        >>> b = a.next(1) # == a.next()
        >>> b.tree_repr
        [[0, 2], [0, 1], [1, 3]]
        >>> b.rank
        1

        See Also
        ========

        prufer_rank, rank, prev, size

        '''
        return Prufer.unrank(self.rank + delta, self.nodes)

    
    def prev(self, delta = (1,)):
        '''Generates the Prufer sequence that is -delta before the current one.

        Examples
        ========

        >>> from sympy.combinatorics.prufer import Prufer
        >>> a = Prufer([[0, 1], [1, 2], [2, 3], [1, 4]])
        >>> a.rank
        36
        >>> b = a.prev()
        >>> b
        Prufer([1, 2, 0])
        >>> b.rank
        35

        See Also
        ========

        prufer_rank, rank, next, size

        '''
        return Prufer.unrank(self.rank - delta, self.nodes)

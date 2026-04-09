# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: graycode.pyc (Python 3.11)

from sympy.core import Basic, Integer
import random

class GrayCode(Basic):
    """
    A Gray code is essentially a Hamiltonian walk on
    a n-dimensional cube with edge length of one.
    The vertices of the cube are represented by vectors
    whose values are binary. The Hamilton walk visits
    each vertex exactly once. The Gray code for a 3d
    cube is ['000','100','110','010','011','111','101',
    '001'].

    A Gray code solves the problem of sequentially
    generating all possible subsets of n objects in such
    a way that each subset is obtained from the previous
    one by either deleting or adding a single object.
    In the above example, 1 indicates that the object is
    present, and 0 indicates that its absent.

    Gray codes have applications in statistics as well when
    we want to compute various statistics related to subsets
    in an efficient manner.

    Examples
    ========

    >>> from sympy.combinatorics import GrayCode
    >>> a = GrayCode(3)
    >>> list(a.generate_gray())
    ['000', '001', '011', '010', '110', '111', '101', '100']
    >>> a = GrayCode(4)
    >>> list(a.generate_gray())
    ['0000', '0001', '0011', '0010', '0110', '0111', '0101', '0100',     '1100', '1101', '1111', '1110', '1010', '1011', '1001', '1000']

    References
    ==========

    .. [1] Nijenhuis,A. and Wilf,H.S.(1978).
           Combinatorial Algorithms. Academic Press.
    .. [2] Knuth, D. (2011). The Art of Computer Programming, Vol 4
           Addison Wesley


    """
    _skip = False
    _current = 0
    _rank = None
    
    def __new__(cls, n, *args, **kw_args):
        """
        Default constructor.

        It takes a single argument ``n`` which gives the dimension of the Gray
        code. The starting Gray code string (``start``) or the starting ``rank``
        may also be given; the default is to start at rank = 0 ('0...0').

        Examples
        ========

        >>> from sympy.combinatorics import GrayCode
        >>> a = GrayCode(3)
        >>> a
        GrayCode(3)
        >>> a.n
        3

        >>> a = GrayCode(3, start='100')
        >>> a.current
        '100'

        >>> a = GrayCode(4, rank=4)
        >>> a.current
        '0110'
        >>> a.rank
        4

        """
        if n < 1 or int(n) != n:
            raise ValueError('Gray code dimension must be a positive integer, not %i' % n)
        n = Integer(n)
        args = (n,) + args
    # WARNING: Decompyle incomplete

    
    def next(self, delta = (1,)):
        """
        Returns the Gray code a distance ``delta`` (default = 1) from the
        current value in canonical order.


        Examples
        ========

        >>> from sympy.combinatorics import GrayCode
        >>> a = GrayCode(3, start='110')
        >>> a.next().current
        '111'
        >>> a.next(-1).current
        '010'
        """
        return GrayCode(self.n, rank = (self.rank + delta) % self.selections)

    selections = (lambda self: 2 ** self.n)()
    n = (lambda self: self.args[0])()
    
    def generate_gray(self, **hints):
        """
        Generates the sequence of bit vectors of a Gray Code.

        Examples
        ========

        >>> from sympy.combinatorics import GrayCode
        >>> a = GrayCode(3)
        >>> list(a.generate_gray())
        ['000', '001', '011', '010', '110', '111', '101', '100']
        >>> list(a.generate_gray(start='011'))
        ['011', '010', '110', '111', '101', '100']
        >>> list(a.generate_gray(rank=4))
        ['110', '111', '101', '100']

        See Also
        ========

        skip

        References
        ==========

        .. [1] Knuth, D. (2011). The Art of Computer Programming,
               Vol 4, Addison Wesley

        """
        pass
    # WARNING: Decompyle incomplete

    
    def skip(self):
        """
        Skips the bit generation.

        Examples
        ========

        >>> from sympy.combinatorics import GrayCode
        >>> a = GrayCode(3)
        >>> for i in a.generate_gray():
        ...     if i == '010':
        ...         a.skip()
        ...     print(i)
        ...
        000
        001
        011
        010
        111
        101
        100

        See Also
        ========

        generate_gray
        """
        self._skip = True

    rank = (lambda self: pass# WARNING: Decompyle incomplete
)()
    current = (lambda self: if not self._current:
rv = '0'if not isinstance(rv, str):
rv = bin(rv)[2:]rv.rjust(self.n, '0'))()
    unrank = (lambda self, n, rank: pass# WARNING: Decompyle incomplete
)()


def random_bitstring(n):
    '''
    Generates a random bitlist of length n.

    Examples
    ========

    >>> from sympy.combinatorics.graycode import random_bitstring
    >>> random_bitstring(3) # doctest: +SKIP
    100
    '''
    return (lambda .0: [ random.choice('01') for i in .0 ])(range(n)())


def gray_to_bin(bin_list):
    """
    Convert from Gray coding to binary coding.

    We assume big endian encoding.

    Examples
    ========

    >>> from sympy.combinatorics.graycode import gray_to_bin
    >>> gray_to_bin('100')
    '111'

    See Also
    ========

    bin_to_gray
    """
    b = [
        bin_list[0]]
    for i in range(1, len(bin_list)):
        b += str(int(b[i - 1] != bin_list[i]))
        return ''.join(b)


def bin_to_gray(bin_list):
    """
    Convert from binary coding to gray coding.

    We assume big endian encoding.

    Examples
    ========

    >>> from sympy.combinatorics.graycode import bin_to_gray
    >>> bin_to_gray('111')
    '100'

    See Also
    ========

    gray_to_bin
    """
    b = [
        bin_list[0]]
    for i in range(1, len(bin_list)):
        b += str(int(bin_list[i]) ^ int(bin_list[i - 1]))
        return ''.join(b)


def get_subset_from_bitstring(super_set, bitstring):
    """
    Gets the subset defined by the bitstring.

    Examples
    ========

    >>> from sympy.combinatorics.graycode import get_subset_from_bitstring
    >>> get_subset_from_bitstring(['a', 'b', 'c', 'd'], '0011')
    ['c', 'd']
    >>> get_subset_from_bitstring(['c', 'a', 'c', 'c'], '1100')
    ['c', 'a']

    See Also
    ========

    graycode_subsets
    """
    pass
# WARNING: Decompyle incomplete


def graycode_subsets(gray_code_set):
    """
    Generates the subsets as enumerated by a Gray code.

    Examples
    ========

    >>> from sympy.combinatorics.graycode import graycode_subsets
    >>> list(graycode_subsets(['a', 'b', 'c']))
    [[], ['c'], ['b', 'c'], ['b'], ['a', 'b'], ['a', 'b', 'c'],     ['a', 'c'], ['a']]
    >>> list(graycode_subsets(['a', 'b', 'c', 'c']))
    [[], ['c'], ['c', 'c'], ['c'], ['b', 'c'], ['b', 'c', 'c'],     ['b', 'c'], ['b'], ['a', 'b'], ['a', 'b', 'c'], ['a', 'b', 'c', 'c'],     ['a', 'b', 'c'], ['a', 'c'], ['a', 'c', 'c'], ['a', 'c'], ['a']]

    See Also
    ========

    get_subset_from_bitstring
    """
    pass
# WARNING: Decompyle incomplete

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: enumerative.pyc (Python 3.11)

"""
Algorithms and classes to support enumerative combinatorics.

Currently just multiset partitions, but more could be added.

Terminology (following Knuth, algorithm 7.1.2.5M TAOCP)
*multiset* aaabbcccc has a *partition* aaabc | bccc

The submultisets, aaabc and bccc of the partition are called
*parts*, or sometimes *vectors*.  (Knuth notes that multiset
partitions can be thought of as partitions of vectors of integers,
where the ith element of the vector gives the multiplicity of
element i.)

The values a, b and c are *components* of the multiset.  These
correspond to elements of a set, but in a multiset can be present
with a multiplicity greater than 1.

The algorithm deserves some explanation.

Think of the part aaabc from the multiset above.  If we impose an
ordering on the components of the multiset, we can represent a part
with a vector, in which the value of the first element of the vector
corresponds to the multiplicity of the first component in that
part. Thus, aaabc can be represented by the vector [3, 1, 1].  We
can also define an ordering on parts, based on the lexicographic
ordering of the vector (leftmost vector element, i.e., the element
with the smallest component number, is the most significant), so
that [3, 1, 1] > [3, 1, 0] and [3, 1, 1] > [2, 1, 4].  The ordering
on parts can be extended to an ordering on partitions: First, sort
the parts in each partition, left-to-right in decreasing order. Then
partition A is greater than partition B if A's leftmost/greatest
part is greater than B's leftmost part.  If the leftmost parts are
equal, compare the second parts, and so on.

In this ordering, the greatest partition of a given multiset has only
one part.  The least partition is the one in which the components
are spread out, one per part.

The enumeration algorithms in this file yield the partitions of the
argument multiset in decreasing order.  The main data structure is a
stack of parts, corresponding to the current partition.  An
important invariant is that the parts on the stack are themselves in
decreasing order.  This data structure is decremented to find the
next smaller partition.  Most often, decrementing the partition will
only involve adjustments to the smallest parts at the top of the
stack, much as adjacent integers *usually* differ only in their last
few digits.

Knuth's algorithm uses two main operations on parts:

Decrement - change the part so that it is smaller in the
  (vector) lexicographic order, but reduced by the smallest amount possible.
  For example, if the multiset has vector [5,
  3, 1], and the bottom/greatest part is [4, 2, 1], this part would
  decrement to [4, 2, 0], while [4, 0, 0] would decrement to [3, 3,
  1].  A singleton part is never decremented -- [1, 0, 0] is not
  decremented to [0, 3, 1].  Instead, the decrement operator needs
  to fail for this case.  In Knuth's pseudocode, the decrement
  operator is step m5.

Spread unallocated multiplicity - Once a part has been decremented,
  it cannot be the rightmost part in the partition.  There is some
  multiplicity that has not been allocated, and new parts must be
  created above it in the stack to use up this multiplicity.  To
  maintain the invariant that the parts on the stack are in
  decreasing order, these new parts must be less than or equal to
  the decremented part.
  For example, if the multiset is [5, 3, 1], and its most
  significant part has just been decremented to [5, 3, 0], the
  spread operation will add a new part so that the stack becomes
  [[5, 3, 0], [0, 0, 1]].  If the most significant part (for the
  same multiset) has been decremented to [2, 0, 0] the stack becomes
  [[2, 0, 0], [2, 0, 0], [1, 3, 1]].  In the pseudocode, the spread
  operation for one part is step m2.  The complete spread operation
  is a loop of steps m2 and m3.

In order to facilitate the spread operation, Knuth stores, for each
component of each part, not just the multiplicity of that component
in the part, but also the total multiplicity available for this
component in this part or any lesser part above it on the stack.

One added twist is that Knuth does not represent the part vectors as
arrays. Instead, he uses a sparse representation, in which a
component of a part is represented as a component number (c), plus
the multiplicity of the component in that part (v) as well as the
total multiplicity available for that component (u).  This saves
time that would be spent skipping over zeros.

"""

class PartComponent:
    """Internal class used in support of the multiset partitions
    enumerators and the associated visitor functions.

    Represents one component of one part of the current partition.

    A stack of these, plus an auxiliary frame array, f, represents a
    partition of the multiset.

    Knuth's pseudocode makes c, u, and v separate arrays.
    """
    __slots__ = ('c', 'u', 'v')
    
    def __init__(self):
        self.c = 0
        self.u = 0
        self.v = 0

    
    def __repr__(self):
        '''for debug/algorithm animation purposes'''
        return 'c:%d u:%d v:%d' % (self.c, self.u, self.v)

    
    def __eq__(self, other):

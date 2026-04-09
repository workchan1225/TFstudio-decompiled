# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: interval_arithmetic.pyc (Python 3.11)

"""
Interval Arithmetic for plotting.
This module does not implement interval arithmetic accurately and
hence cannot be used for purposes other than plotting. If you want
to use interval arithmetic, use mpmath's interval arithmetic.

The module implements interval arithmetic using numpy and
python floating points. The rounding up and down is not handled
and hence this is not an accurate implementation of interval
arithmetic.

The module uses numpy for speed which cannot be achieved with mpmath.
"""
from sympy.core.numbers import int_valued
from sympy.core.logic import fuzzy_and
from sympy.simplify.simplify import nsimplify
from interval_membership import intervalMembership

class interval:
    """ Represents an interval containing floating points as start and
    end of the interval
    The is_valid variable tracks whether the interval obtained as the
    result of the function is in the domain and is continuous.
    - True: Represents the interval result of a function is continuous and
            in the domain of the function.
    - False: The interval argument of the function was not in the domain of
             the function, hence the is_valid of the result interval is False
    - None: The function was not continuous over the interval or
            the function's argument interval is partly in the domain of the
            function

    A comparison between an interval and a real number, or a
    comparison between two intervals may return ``intervalMembership``
    of two 3-valued logic values.
    """
    
    def __init__(self = None, *, is_valid, *args, **kwargs):
        self.is_valid = is_valid
        if len(args) == 1:
            if isinstance(args[0], interval):
                self.start, self.end = args[0].start, args[0].end
                return None
            self.start = None(args[0])
            self.end = float(args[0])
            return None
        if None(args) == 2:
            if args[0] < args[1]:
                self.start = float(args[0])
                self.end = float(args[1])
                return None
            self.start = None(args[1])
            self.end = float(args[0])
            return None
        raise None('interval takes a maximum of two float values as arguments')

    mid = (lambda self: (self.start + self.end) / 2)()
    width = (lambda self: self.end - self.start)()
    
    def __repr__(self):
        return 'interval(%f, %f)' % (self.start, self.end)

    
    def __str__(self):
        return '[%f, %f]' % (self.start, self.end)

    
    def __lt__(self, other):
        if isinstance(other, (int, float)):
            if self.end < other:
                return intervalMembership(True, self.is_valid)
            if None.start > other:
                return intervalMembership(False, self.is_valid)
            return None(None, self.is_valid)
        if None(other, interval):
            valid = fuzzy_and([
                self.is_valid,
                other.is_valid])
            if self.end < other.start:
                return intervalMembership(True, valid)
            if None.start > other.end:
                return intervalMembership(False, valid)
            return None(None, valid)

    
    def __gt__(self, other):
        if isinstance(other, (int, float)):
            if self.start > other:
                return intervalMembership(True, self.is_valid)
            if None.end < other:
                return intervalMembership(False, self.is_valid)
            return None(None, self.is_valid)
        if None(other, interval):
            return other.__lt__(self)

    
    def __eq__(self, other):
        if isinstance(other, (int, float)):
            if self.start == other and self.end == other:
                return intervalMembership(True, self.is_valid)
            if None in self:
                return intervalMembership(None, self.is_valid)
            return None(False, self.is_valid)
    # WARNING: Decompyle incomplete

    
    def __ne__(self, other):
        if isinstance(other, (int, float)):
            if self.start == other and self.end == other:
                return intervalMembership(False, self.is_valid)
            if None in self:
                return intervalMembership(None, self.is_valid)
            return None(True, self.is_valid)
    # WARNING: Decompyle incomplete

    
    def __le__(self, other):
        if isinstance(other, (int, float)):
            if self.end <= other:
                return intervalMembership(True, self.is_valid)
            if None.start > other:
                return intervalMembership(False, self.is_valid)
            return None(None, self.is_valid)
        if None(other, interval):
            valid = fuzzy_and([
                self.is_valid,
                other.is_valid])
            if self.end <= other.start:
                return intervalMembership(True, valid)
            if None.start > other.end:
                return intervalMembership(False, valid)
            return None(None, valid)

    
    def __ge__(self, other):
        if isinstance(other, (int, float)):
            if self.start >= other:
                return intervalMembership(True, self.is_valid)
            if None.end < other:
                return intervalMembership(False, self.is_valid)
            return None(None, self.is_valid)
        if None(other, interval):
            return other.__le__(self)

    
    def __add__(self, other):
        if isinstance(other, (int, float)):
            if self.is_valid:
                return interval(self.start + other, self.end + other)
            start = None.start + other
            end = self.end + other
            return interval(start, end, is_valid = self.is_valid)
        if None(other, interval):
            start = self.start + other.start
            end = self.end + other.end
            valid = fuzzy_and([
                self.is_valid,
                other.is_valid])
            return interval(start, end, is_valid = valid)

    __radd__ = __add__
    
    def __sub__(self, other):
        if isinstance(other, (int, float)):
            start = self.start - other
            end = self.end - other
            return interval(start, end, is_valid = self.is_valid)
        if None(other, interval):
            start = self.start - other.end
            end = self.end - other.start
            valid = fuzzy_and([
                self.is_valid,
                other.is_valid])
            return interval(start, end, is_valid = valid)

    
    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            start = other - self.end
            end = other - self.start
            return interval(start, end, is_valid = self.is_valid)
        if None(other, interval):
            return other.__sub__(self)

    
    def __neg__(self):
        if self.is_valid:
            return interval(-(self.end), -(self.start))
        return None(-(self.end), -(self.start), is_valid = self.is_valid)

    
    def __mul__(self, other):
        pass
    # WARNING: Decompyle incomplete

    __rmul__ = __mul__
    
    def __contains__(self, other):

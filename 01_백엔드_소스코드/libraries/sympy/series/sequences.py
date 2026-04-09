# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: sequences.pyc (Python 3.11)

from sympy.core.basic import Basic
from sympy.core.cache import cacheit
from sympy.core.containers import Tuple
from sympy.core.decorators import call_highest_priority
from sympy.core.parameters import global_parameters
from sympy.core.function import AppliedUndef, expand
from sympy.core.mul import Mul
from sympy.core.numbers import Integer
from sympy.core.relational import Eq
from sympy.core.singleton import S, Singleton
from sympy.core.sorting import ordered
from sympy.core.symbol import Dummy, Symbol, Wild
from sympy.core.sympify import sympify
from sympy.matrices import Matrix
from sympy.polys import lcm, factor
from sympy.sets.sets import Interval, Intersection
from sympy.tensor.indexed import Idx
from sympy.utilities.iterables import flatten, is_sequence, iterable

class SeqBase(Basic):
    '''Base class for sequences'''
    is_commutative = True
    _op_priority = 15
    _start_key = (lambda expr: try:
start = expr.startexcept NotImplementedError:
start = S.Infinitystart)()
    
    def _intersect_interval(self, other):
        '''Returns start and stop.

        Takes intersection over the two intervals.
        '''
        interval = Intersection(self.interval, other.interval)
        return (interval.inf, interval.sup)

    gen = (lambda self: raise NotImplementedError('(%s).gen' % self))()
    interval = (lambda self: raise NotImplementedError('(%s).interval' % self))()
    start = (lambda self: raise NotImplementedError('(%s).start' % self))()
    stop = (lambda self: raise NotImplementedError('(%s).stop' % self))()
    length = (lambda self: raise NotImplementedError('(%s).length' % self))()
    variables = (lambda self: ())()
    free_symbols = (lambda self: pass# WARNING: Decompyle incomplete
)()
    coeff = (lambda self, pt: if pt < self.start or pt > self.stop:
raise IndexError(f'''Index {pt!s} out of bounds {self.interval!s}''')self._eval_coeff(pt))()
    
    def _eval_coeff(self, pt):
        raise NotImplementedError('The _eval_coeff method should be added to%s to return coefficient so it is availablewhen coeff calls it.' % self.func)

    
    def _ith_point(self, i):
        """Returns the i'th point of a sequence.

        Explanation
        ===========

        If start point is negative infinity, point is returned from the end.
        Assumes the first point to be indexed zero.

        Examples
        =========

        >>> from sympy import oo
        >>> from sympy.series.sequences import SeqPer

        bounded

        >>> SeqPer((1, 2, 3), (-10, 10))._ith_point(0)
        -10
        >>> SeqPer((1, 2, 3), (-10, 10))._ith_point(5)
        -5

        End is at infinity

        >>> SeqPer((1, 2, 3), (0, oo))._ith_point(5)
        5

        Starts at negative infinity

        >>> SeqPer((1, 2, 3), (-oo, 0))._ith_point(5)
        -5
        """
        if self.start is S.NegativeInfinity:
            initial = self.stop
        else:
            initial = self.start
        if self.start is S.NegativeInfinity:
            step = -1
        else:
            step = 1
        return initial + i * step

    
    def _add(self, other):
        '''
        Should only be used internally.

        Explanation
        ===========

        self._add(other) returns a new, term-wise added sequence if self
        knows how to add with other, otherwise it returns ``None``.

        ``other`` should only be a sequence object.

        Used within :class:`SeqAdd` class.
        '''
        pass

    
    def _mul(self, other):
        '''
        Should only be used internally.

        Explanation
        ===========

        self._mul(other) returns a new, term-wise multiplied sequence if self
        knows how to multiply with other, otherwise it returns ``None``.

        ``other`` should only be a sequence object.

        Used within :class:`SeqMul` class.
        '''
        pass

    
    def coeff_mul(self, other):
        """
        Should be used when ``other`` is not a sequence. Should be
        defined to define custom behaviour.

        Examples
        ========

        >>> from sympy import SeqFormula
        >>> from sympy.abc import n
        >>> SeqFormula(n**2).coeff_mul(2)
        SeqFormula(2*n**2, (n, 0, oo))

        Notes
        =====

        '*' defines multiplication of sequences with sequences only.
        """
        return Mul(self, other)

    
    def __add__(self, other):
        """Returns the term-wise addition of 'self' and 'other'.

        ``other`` should be a sequence.

        Examples
        ========

        >>> from sympy import SeqFormula
        >>> from sympy.abc import n
        >>> SeqFormula(n**2) + SeqFormula(n**3)
        SeqFormula(n**3 + n**2, (n, 0, oo))
        """
        if not isinstance(other, SeqBase):
            raise TypeError('cannot add sequence and %s' % type(other))
        return SeqAdd(self, other)

    __radd__ = (lambda self, other: self + other)()
    
    def __sub__(self, other):
        '''Returns the term-wise subtraction of ``self`` and ``other``.

        ``other`` should be a sequence.

        Examples
        ========

        >>> from sympy import SeqFormula
        >>> from sympy.abc import n
        >>> SeqFormula(n**2) - (SeqFormula(n))
        SeqFormula(n**2 - n, (n, 0, oo))
        '''
        if not isinstance(other, SeqBase):
            raise TypeError('cannot subtract sequence and %s' % type(other))
        return SeqAdd(self, -other)

    __rsub__ = (lambda self, other: -self + other)()
    
    def __neg__(self):
        '''Negates the sequence.

        Examples
        ========

        >>> from sympy import SeqFormula
        >>> from sympy.abc import n
        >>> -SeqFormula(n**2)
        SeqFormula(-n**2, (n, 0, oo))
        '''
        return self.coeff_mul(-1)

    
    def __mul__(self, other):
        """Returns the term-wise multiplication of 'self' and 'other'.

        ``other`` should be a sequence. For ``other`` not being a
        sequence see :func:`coeff_mul` method.

        Examples
        ========

        >>> from sympy import SeqFormula
        >>> from sympy.abc import n
        >>> SeqFormula(n**2) * (SeqFormula(n))
        SeqFormula(n**3, (n, 0, oo))
        """
        if not isinstance(other, SeqBase):
            raise TypeError('cannot multiply sequence and %s' % type(other))
        return SeqMul(self, other)

    __rmul__ = (lambda self, other: self * other)()
    
    def __iter__(self):
        pass
    # WARNING: Decompyle incomplete

    
    def __getitem__(self, index):
        pass
    # WARNING: Decompyle incomplete

    
    def find_linear_recurrence(self, n, d, gfvar = (None, None)):
        '''
        Finds the shortest linear recurrence that satisfies the first n
        terms of sequence of order `\\leq` ``n/2`` if possible.
        If ``d`` is specified, find shortest linear recurrence of order
        `\\leq` min(d, n/2) if possible.
        Returns list of coefficients ``[b(1), b(2), ...]`` corresponding to the
        recurrence relation ``x(n) = b(1)*x(n-1) + b(2)*x(n-2) + ...``
        Returns ``[]`` if no recurrence is found.
        If gfvar is specified, also returns ordinary generating function as a
        function of gfvar.

        Examples
        ========

        >>> from sympy import sequence, sqrt, oo, lucas
        >>> from sympy.abc import n, x, y
        >>> sequence(n**2).find_linear_recurrence(10, 2)
        []
        >>> sequence(n**2).find_linear_recurrence(10)
        [3, -3, 1]
        >>> sequence(2**n).find_linear_recurrence(10)
        [2]
        >>> sequence(23*n**4+91*n**2).find_linear_recurrence(10)
        [5, -10, 10, -5, 1]
        >>> sequence(sqrt(5)*(((1 + sqrt(5))/2)**n - (-(1 + sqrt(5))/2)**(-n))/5).find_linear_recurrence(10)
        [1, 1]
        >>> sequence(x+y*(-2)**(-n), (n, 0, oo)).find_linear_recurrence(30)
        [1/2, 1/2]
        >>> sequence(3*5**n + 12).find_linear_recurrence(20,gfvar=x)
        ([6, -5], 3*(5 - 21*x)/((x - 1)*(5*x - 1)))
        >>> sequence(lucas(n)).find_linear_recurrence(15,gfvar=x)
        ([1, 1], (x - 2)/(x**2 + x - 1))
        '''
        pass
    # WARNING: Decompyle incomplete



def EmptySequence():
    '''EmptySequence'''
    __doc__ = 'Represents an empty sequence.\n\n    The empty sequence is also available as a singleton as\n    ``S.EmptySequence``.\n\n    Examples\n    ========\n\n    >>> from sympy import EmptySequence, SeqPer\n    >>> from sympy.abc import x\n    >>> EmptySequence\n    EmptySequence\n    >>> SeqPer((1, 2), (x, 0, 10)) + EmptySequence\n    SeqPer((1, 2), (x, 0, 10))\n    >>> SeqPer((1, 2)) * EmptySequence\n    EmptySequence\n    >>> EmptySequence.coeff_mul(-1)\n    EmptySequence\n    '
    interval = (lambda self: S.EmptySet)()
    length = (lambda self: S.Zero)()
    
    def coeff_mul(self, coeff):
        '''See docstring of SeqBase.coeff_mul'''
        return self

    
    def __iter__(self):
        return iter([])


EmptySequence = <NODE:27>(EmptySequence, 'EmptySequence', SeqBase, metaclass = Singleton)

class SeqExpr(SeqBase):
    '''Sequence expression class.

    Various sequences should inherit from this class.

    Examples
    ========

    >>> from sympy.series.sequences import SeqExpr
    >>> from sympy.abc import x
    >>> from sympy import Tuple
    >>> s = SeqExpr(Tuple(1, 2, 3), Tuple(x, 0, 10))
    >>> s.gen
    (1, 2, 3)
    >>> s.interval
    Interval(0, 10)
    >>> s.length
    11

    See Also
    ========

    sympy.series.sequences.SeqPer
    sympy.series.sequences.SeqFormula
    '''
    gen = (lambda self: self.args[0])()
    interval = (lambda self: Interval(self.args[1][1], self.args[1][2]))()
    start = (lambda self: self.interval.inf)()
    stop = (lambda self: self.interval.sup)()
    length = (lambda self: (self.stop - self.start) + 1)()
    variables = (lambda self: (self.args[1][0],))()


class SeqPer(SeqExpr):
    '''
    Represents a periodic sequence.

    The elements are repeated after a given period.

    Examples
    ========

    >>> from sympy import SeqPer, oo
    >>> from sympy.abc import k

    >>> s = SeqPer((1, 2, 3), (0, 5))
    >>> s.periodical
    (1, 2, 3)
    >>> s.period
    3

    For value at a particular point

    >>> s.coeff(3)
    1

    supports slicing

    >>> s[:]
    [1, 2, 3, 1, 2, 3]

    iterable

    >>> list(s)
    [1, 2, 3, 1, 2, 3]

    sequence starts from negative infinity

    >>> SeqPer((1, 2, 3), (-oo, 0))[0:6]
    [1, 2, 3, 1, 2, 3]

    Periodic formulas

    >>> SeqPer((k, k**2, k**3), (k, 0, oo))[0:6]
    [0, 1, 8, 3, 16, 125]

    See Also
    ========

    sympy.series.sequences.SeqFormula
    '''
    
    def __new__(cls, periodical, limits = (None,)):
        periodical = sympify(periodical)
        
        def _find_x(periodical):
            free = periodical.free_symbols
            if len(periodical.free_symbols) == 1:
                return free.pop()
            return None('k')

        (x, start, stop) = (None, None, None)
    # WARNING: Decompyle incomplete

    period = (lambda self: len(self.gen))()
    periodical = (lambda self: self.gen)()
    
    def _eval_coeff(self, pt):
        if self.start is S.NegativeInfinity:
            idx = (self.stop - pt) % self.period
        else:
            idx = (pt - self.start) % self.period
        return self.periodical[idx].subs(self.variables[0], pt)

    
    def _add(self, other):
        '''See docstring of SeqBase._add'''
        if isinstance(other, SeqPer):
            lper1 = self.period
            per1 = self.periodical
            lper2 = other.period
            per2 = other.periodical
            per_length = lcm(lper1, lper2)
            new_per = []
            for x in range(per_length):
                ele1 = per1[x % lper1]
                ele2 = per2[x % lper2]
                new_per.append(ele1 + ele2)
                (start, stop) = self._intersect_interval(other)
                return SeqPer(new_per, (self.variables[0], start, stop))
                return None

    
    def _mul(self, other):
        '''See docstring of SeqBase._mul'''
        if isinstance(other, SeqPer):
            lper1 = self.period
            per1 = self.periodical
            lper2 = other.period
            per2 = other.periodical
            per_length = lcm(lper1, lper2)
            new_per = []
            for x in range(per_length):
                ele1 = per1[x % lper1]
                ele2 = per2[x % lper2]
                new_per.append(ele1 * ele2)
                (start, stop) = self._intersect_interval(other)
                return SeqPer(new_per, (self.variables[0], start, stop))
                return None

    
    def coeff_mul(self, coeff):
        '''See docstring of SeqBase.coeff_mul'''
        pass
    # WARNING: Decompyle incomplete



class SeqFormula(SeqExpr):
    """
    Represents sequence based on a formula.

    Elements are generated using a formula.

    Examples
    ========

    >>> from sympy import SeqFormula, oo, Symbol
    >>> n = Symbol('n')
    >>> s = SeqFormula(n**2, (n, 0, 5))
    >>> s.formula
    n**2

    For value at a particular point

    >>> s.coeff(3)
    9

    supports slicing

    >>> s[:]
    [0, 1, 4, 9, 16, 25]

    iterable

    >>> list(s)
    [0, 1, 4, 9, 16, 25]

    sequence starts from negative infinity

    >>> SeqFormula(n**2, (-oo, 0))[0:6]
    [0, 1, 4, 9, 16, 25]

    See Also
    ========

    sympy.series.sequences.SeqPer
    """
    
    def __new__(cls, formula, limits = (None,)):
        formula = sympify(formula)
        
        def _find_x(formula):
            free = formula.free_symbols
            if len(free) == 1:
                return free.pop()
            if not None:
                return Dummy('k')
            raise None(' specify dummy variables for %s. If the formula contains more than one free symbol, a dummy variable should be supplied explicitly e.g., SeqFormula(m*n**2, (n, 0, 5))' % formula)

        (x, start, stop) = (None, None, None)
    # WARNING: Decompyle incomplete

    formula = (lambda self: self.gen)()
    
    def _eval_coeff(self, pt):
        d = self.variables[0]
        return self.formula.subs(d, pt)

    
    def _add(self, other):
        '''See docstring of SeqBase._add'''
        if isinstance(other, SeqFormula):
            v1 = self.variables[0]
            form1 = self.formula
            v2 = other.variables[0]
            form2 = other.formula
            formula = form1 + form2.subs(v2, v1)
            (start, stop) = self._intersect_interval(other)
            return SeqFormula(formula, (v1, start, stop))

    
    def _mul(self, other):
        '''See docstring of SeqBase._mul'''
        if isinstance(other, SeqFormula):
            v1 = self.variables[0]
            form1 = self.formula
            v2 = other.variables[0]
            form2 = other.formula
            formula = form1 * form2.subs(v2, v1)
            (start, stop) = self._intersect_interval(other)
            return SeqFormula(formula, (v1, start, stop))

    
    def coeff_mul(self, coeff):
        '''See docstring of SeqBase.coeff_mul'''
        coeff = sympify(coeff)
        formula = self.formula * coeff
        return SeqFormula(formula, self.args[1])

    
    def expand(self, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete



class RecursiveSeq(SeqBase):
    '''
    A finite degree recursive sequence.

    Explanation
    ===========

    That is, a sequence a(n) that depends on a fixed, finite number of its
    previous values. The general form is

        a(n) = f(a(n - 1), a(n - 2), ..., a(n - d))

    for some fixed, positive integer d, where f is some function defined by a
    SymPy expression.

    Parameters
    ==========

    recurrence : SymPy expression defining recurrence
        This is *not* an equality, only the expression that the nth term is
        equal to. For example, if :code:`a(n) = f(a(n - 1), ..., a(n - d))`,
        then the expression should be :code:`f(a(n - 1), ..., a(n - d))`.

    yn : applied undefined function
        Represents the nth term of the sequence as e.g. :code:`y(n)` where
        :code:`y` is an undefined function and `n` is the sequence index.

    n : symbolic argument
        The name of the variable that the recurrence is in, e.g., :code:`n` if
        the recurrence function is :code:`y(n)`.

    initial : iterable with length equal to the degree of the recurrence
        The initial values of the recurrence.

    start : start value of sequence (inclusive)

    Examples
    ========

    >>> from sympy import Function, symbols
    >>> from sympy.series.sequences import RecursiveSeq
    >>> y = Function("y")
    >>> n = symbols("n")
    >>> fib = RecursiveSeq(y(n - 1) + y(n - 2), y(n), n, [0, 1])

    >>> fib.coeff(3) # Value at a particular point
    2

    >>> fib[:6] # supports slicing
    [0, 1, 1, 2, 3, 5]

    >>> fib.recurrence # inspect recurrence
    Eq(y(n), y(n - 2) + y(n - 1))

    >>> fib.degree # automatically determine degree
    2

    >>> for x in zip(range(10), fib): # supports iteration
    ...     print(x)
    (0, 0)
    (1, 1)
    (2, 1)
    (3, 2)
    (4, 3)
    (5, 5)
    (6, 8)
    (7, 13)
    (8, 21)
    (9, 34)

    See Also
    ========

    sympy.series.sequences.SeqFormula

    '''
    
    def __new__(cls, recurrence, yn, n, initial, start = (None, 0)):
        pass
    # WARNING: Decompyle incomplete

    _recurrence = (lambda self: self.args[0])()
    recurrence = (lambda self: Eq(self.yn, self.args[0]))()
    yn = (lambda self: self.args[1])()
    y = (lambda self: self.yn.func)()
    n = (lambda self: self.args[2])()
    initial = (lambda self: self.args[3])()
    start = (lambda self: self.args[4])()
    stop = (lambda self: S.Infinity)()
    interval = (lambda self: (self.start, S.Infinity))()
    
    def _eval_coeff(self, index):
        if index - self.start < len(self.cache):
            return self.cache[self.y(index)]
        for current in None(len(self.cache), index + 1):
            seq_index = self.start + current
            current_recurrence = self._recurrence.xreplace({
                self.n: seq_index })
            new_term = current_recurrence.xreplace(self.cache)
            self.cache[self.y(seq_index)] = new_term
            return self.cache[self.y(self.start + current)]

    
    def __iter__(self):
        pass
    # WARNING: Decompyle incomplete



def sequence(seq, limits = (None,)):
    '''
    Returns appropriate sequence object.

    Explanation
    ===========

    If ``seq`` is a SymPy sequence, returns :class:`SeqPer` object
    otherwise returns :class:`SeqFormula` object.

    Examples
    ========

    >>> from sympy import sequence
    >>> from sympy.abc import n
    >>> sequence(n**2, (n, 0, 5))
    SeqFormula(n**2, (n, 0, 5))
    >>> sequence((1, 2, 3), (n, 0, 5))
    SeqPer((1, 2, 3), (n, 0, 5))

    See Also
    ========

    sympy.series.sequences.SeqPer
    sympy.series.sequences.SeqFormula
    '''
    seq = sympify(seq)
    if is_sequence(seq, Tuple):
        return SeqPer(seq, limits)
    return None(seq, limits)


class SeqExprOp(SeqBase):
    '''
    Base class for operations on sequences.

    Examples
    ========

    >>> from sympy.series.sequences import SeqExprOp, sequence
    >>> from sympy.abc import n
    >>> s1 = sequence(n**2, (n, 0, 10))
    >>> s2 = sequence((1, 2, 3), (n, 5, 10))
    >>> s = SeqExprOp(s1, s2)
    >>> s.gen
    (n**2, (1, 2, 3))
    >>> s.interval
    Interval(5, 10)
    >>> s.length
    6

    See Also
    ========

    sympy.series.sequences.SeqAdd
    sympy.series.sequences.SeqMul
    '''
    gen = (lambda self: (lambda .0: pass# WARNING: Decompyle incomplete
)(self.args())
)()
    interval = (lambda self: pass# WARNING: Decompyle incomplete
)()
    start = (lambda self: self.interval.inf)()
    stop = (lambda self: self.interval.sup)()
    variables = (lambda self: flatten((lambda .0: [ a.variables for a in .0 ])(self.args()))
)()
    length = (lambda self: (self.stop - self.start) + 1)()


class SeqAdd(SeqExprOp):
    '''Represents term-wise addition of sequences.

    Rules:
        * The interval on which sequence is defined is the intersection
          of respective intervals of sequences.
        * Anything + :class:`EmptySequence` remains unchanged.
        * Other rules are defined in ``_add`` methods of sequence classes.

    Examples
    ========

    >>> from sympy import EmptySequence, oo, SeqAdd, SeqPer, SeqFormula
    >>> from sympy.abc import n
    >>> SeqAdd(SeqPer((1, 2), (n, 0, oo)), EmptySequence)
    SeqPer((1, 2), (n, 0, oo))
    >>> SeqAdd(SeqPer((1, 2), (n, 0, 5)), SeqPer((1, 2), (n, 6, 10)))
    EmptySequence
    >>> SeqAdd(SeqPer((1, 2), (n, 0, oo)), SeqFormula(n**2, (n, 0, oo)))
    SeqAdd(SeqFormula(n**2, (n, 0, oo)), SeqPer((1, 2), (n, 0, oo)))
    >>> SeqAdd(SeqFormula(n**3), SeqFormula(n**2))
    SeqFormula(n**3 + n**2, (n, 0, oo))

    See Also
    ========

    sympy.series.sequences.SeqMul
    '''
    
    def __new__(cls, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    reduce = (lambda args: pass# WARNING: Decompyle incomplete
)()
    
    def _eval_coeff(self, pt):
        '''adds up the coefficients of all the sequences at point pt'''
        pass
    # WARNING: Decompyle incomplete



class SeqMul(SeqExprOp):
    '''Represents term-wise multiplication of sequences.

    Explanation
    ===========

    Handles multiplication of sequences only. For multiplication
    with other objects see :func:`SeqBase.coeff_mul`.

    Rules:
        * The interval on which sequence is defined is the intersection
          of respective intervals of sequences.
        * Anything \\* :class:`EmptySequence` returns :class:`EmptySequence`.
        * Other rules are defined in ``_mul`` methods of sequence classes.

    Examples
    ========

    >>> from sympy import EmptySequence, oo, SeqMul, SeqPer, SeqFormula
    >>> from sympy.abc import n
    >>> SeqMul(SeqPer((1, 2), (n, 0, oo)), EmptySequence)
    EmptySequence
    >>> SeqMul(SeqPer((1, 2), (n, 0, 5)), SeqPer((1, 2), (n, 6, 10)))
    EmptySequence
    >>> SeqMul(SeqPer((1, 2), (n, 0, oo)), SeqFormula(n**2))
    SeqMul(SeqFormula(n**2, (n, 0, oo)), SeqPer((1, 2), (n, 0, oo)))
    >>> SeqMul(SeqFormula(n**3), SeqFormula(n**2))
    SeqFormula(n**5, (n, 0, oo))

    See Also
    ========

    sympy.series.sequences.SeqAdd
    '''
    
    def __new__(cls, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    reduce = (lambda args: pass# WARNING: Decompyle incomplete
)()
    
    def _eval_coeff(self, pt):
        '''multiplies the coefficients of all the sequences at point pt'''
        val = 1
        for a in self.args:
            val *= a.coeff(pt)
            return val

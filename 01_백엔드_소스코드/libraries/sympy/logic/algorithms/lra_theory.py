# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: lra_theory.pyc (Python 3.11)

'''Implements "A Fast Linear-Arithmetic Solver for DPLL(T)"

The LRASolver class defined in this file can be used
in conjunction with a SAT solver to check the
satisfiability of formulas involving inequalities.

Here\'s an example of how that would work:

    Suppose you want to check the satisfiability of
    the following formula:

    >>> from sympy.core.relational import Eq
    >>> from sympy.abc import x, y
    >>> f = ((x > 0) | (x < 0)) & (Eq(x, 0) | Eq(y, 1)) & (~Eq(y, 1) | Eq(1, 2))

    First a preprocessing step should be done on f. During preprocessing,
    f should be checked for any predicates such as `Q.prime` that can\'t be
    handled. Also unequality like `~Eq(y, 1)` should be split.

    I should mention that the paper says to split both equalities and
    unequality, but this implementation only requires that unequality
    be split.

    >>> f = ((x > 0) | (x < 0)) & (Eq(x, 0) | Eq(y, 1)) & ((y < 1) | (y > 1) | Eq(1, 2))

    Then an LRASolver instance needs to be initialized with this formula.

    >>> from sympy.assumptions.cnf import CNF, EncodedCNF
    >>> from sympy.assumptions.ask import Q
    >>> from sympy.logic.algorithms.lra_theory import LRASolver
    >>> cnf = CNF.from_prop(f)
    >>> enc = EncodedCNF()
    >>> enc.add_from_cnf(cnf)
    >>> lra, conflicts = LRASolver.from_encoded_cnf(enc)

    Any immediate one-lital conflicts clauses will be detected here.
    In this example, `~Eq(1, 2)` is one such conflict clause. We\'ll
    want to add it to `f` so that the SAT solver is forced to
    assign Eq(1, 2) to False.

    >>> f = f & ~Eq(1, 2)

    Now that the one-literal conflict clauses have been added
    and an lra object has been initialized, we can pass `f`
    to a SAT solver. The SAT solver will give us a satisfying
    assignment such as:

    (1 = 2): False
    (y = 1): True
    (y < 1): True
    (y > 1): True
    (x = 0): True
    (x < 0): True
    (x > 0): True

    Next you would pass this assignment to the LRASolver
    which will be able to determine that this particular
    assignment is satisfiable or not.

    Note that since EncodedCNF is inherently non-deterministic,
    the int each predicate is encoded as is not consistent. As a
    result, the code bellow likely does not reflect the assignment
    given above.

    >>> lra.assert_lit(-1) #doctest: +SKIP
    >>> lra.assert_lit(2) #doctest: +SKIP
    >>> lra.assert_lit(3) #doctest: +SKIP
    >>> lra.assert_lit(4) #doctest: +SKIP
    >>> lra.assert_lit(5) #doctest: +SKIP
    >>> lra.assert_lit(6) #doctest: +SKIP
    >>> lra.assert_lit(7) #doctest: +SKIP
    >>> is_sat, conflict_or_assignment = lra.check()

    As the particular assignment suggested is not satisfiable,
    the LRASolver will return unsat and a conflict clause when
    given that assignment. The conflict clause will always be
    minimal, but there can be multiple minimal conflict clauses.
    One possible conflict clause could be `~(x < 0) | ~(x > 0)`.

    We would then add whatever conflict clause is given to
    `f` to prevent the SAT solver from coming up with an
    assignment with the same conflicting literals. In this case,
    the conflict clause `~(x < 0) | ~(x > 0)` would prevent
    any assignment where both (x < 0) and (x > 0) were both
    true.

    The SAT solver would then find another assignment
    and we would check that assignment with the LRASolver
    and so on. Eventually either a satisfying assignment
    that the SAT solver and LRASolver agreed on would be found
    or enough conflict clauses would be added so that the
    boolean formula was unsatisfiable.


This implementation is based on [1]_, which includes a
detailed explanation of the algorithm and pseudocode
for the most important functions.

[1]_ also explains how backtracking and theory propagation
could be implemented to speed up the current implementation,
but these are not currently implemented.

TODO:
 - Handle non-rational real numbers
 - Handle positive and negative infinity
 - Implement backtracking and theory proposition
 - Simplify matrix by removing unused variables using Gaussian elimination

References
==========

.. [1] Dutertre, B., de Moura, L.:
       A Fast Linear-Arithmetic Solver for DPLL(T)
       https://link.springer.com/chapter/10.1007/11817963_11
'''
from sympy.solvers.solveset import linear_eq_to_matrix
from sympy.matrices.dense import eye
from sympy.assumptions import Predicate
from sympy.assumptions.assume import AppliedPredicate
from sympy.assumptions.ask import Q
from sympy.core import Dummy
from sympy.core.mul import Mul
from sympy.core.add import Add
from sympy.core.relational import Eq, Ne
from sympy.core.sympify import sympify
from sympy.core.singleton import S
from sympy.core.numbers import Rational, oo
from sympy.matrices.dense import Matrix

class UnhandledInput(Exception):
    '''
    Raised while creating an LRASolver if non-linearity
    or non-rational numbers are present.
    '''
    pass

ALLOWED_PRED = {
    Q.eq,
    Q.gt,
    Q.lt,
    Q.le,
    Q.ge}
HANDLE_NEGATION = True

class LRASolver:
    """
    Linear Arithmetic Solver for DPLL(T) implemented with an algorithm based on
    the Dual Simplex method. Uses Bland's pivoting rule to avoid cycling.

    References
    ==========

    .. [1] Dutertre, B., de Moura, L.:
           A Fast Linear-Arithmetic Solver for DPLL(T)
           https://link.springer.com/chapter/10.1007/11817963_11
    """
    
    def __init__(self, A, slack_variables, nonslack_variables, enc_to_boundary, s_subs, testing_mode):
        '''
        Use the "from_encoded_cnf" method to create a new LRASolver.
        '''
        self.run_checks = testing_mode
        self.s_subs = s_subs
        if (lambda .0: pass# WARNING: Decompyle incomplete
)(A()):
            raise UnhandledInput('Non-rational numbers are not handled')
        if (lambda .0: pass# WARNING: Decompyle incomplete
)(enc_to_boundary.values()()):
            raise UnhandledInput('Non-rational numbers are not handled')
        n = len(slack_variables) + len(nonslack_variables)
        m = len(slack_variables)
    # WARNING: Decompyle incomplete

    from_encoded_cnf = (lambda encoded_cnf, testing_mode = (False,): pass# WARNING: Decompyle incomplete
)()
    
    def reset_bounds(self):
        '''
        Resets the state of the LRASolver to before
        anything was asserted.
        '''
        self.result = None
        for var in self.all_var:
            var.lower = LRARational(-float('inf'), 0)
            var.lower_from_eq = False
            var.lower_from_neg = False
            var.upper = LRARational(float('inf'), 0)
            var.upper_from_eq = False
            var.lower_from_neg = False
            var.assign = LRARational(0, 0)
            return None

    
    def assert_lit(self, enc_constraint):
        '''
        Assert a literal representing a constraint
        and update the internal state accordingly.

        Note that due to peculiarities of this implementation
        asserting ~(x > 0) will assert (x <= 0) but asserting
        ~Eq(x, 0) will not do anything.

        Parameters
        ==========

        enc_constraint : int
            A mapping of encodings to constraints
            can be found in `self.enc_to_boundary`.

        Returns
        =======

        None or (False, explanation)

        explanation : set of ints
            A conflict clause that "explains" why
            the literals asserted so far are unsatisfiable.
        '''
        if abs(enc_constraint) not in self.enc_to_boundary:
            return None
        if None and enc_constraint < 0:
            return None
        boundary = None.enc_to_boundary[abs(enc_constraint)]
        negated = enc_constraint < 0
        c = boundary.bound
        sym = boundary.var
        if boundary.equality and negated:
            return None
        upper = None.upper != negated
        if boundary.strict != negated:
            delta = -1 if upper else 1
            c = LRARational(c, delta)
        else:
            c = LRARational(c, 0)
        if boundary.equality:
            res1 = self._assert_lower(sym, c, from_equality = True, from_neg = negated)
            if res1 and res1[0] == False:
                res = res1
            else:
                res2 = self._assert_upper(sym, c, from_equality = True, from_neg = negated)
                res = res2
        elif upper:
            res = self._assert_upper(sym, c, from_neg = negated)
        else:
            res = self._assert_lower(sym, c, from_neg = negated)
        if self.is_sat and sym not in self.slack_set:
            self.is_sat = res is None
        else:
            self.is_sat = False
        return res

    
    def _assert_upper(self, xi, ci, from_equality, from_neg = (False, False)):
        '''
        Adjusts the upper bound on variable xi if the new upper bound is
        more limiting. The assignment of variable xi is adjusted to be
        within the new bound if needed.

        Also calls `self._update` to update the assignment for slack variables
        to keep all equalities satisfied.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _assert_lower(self, xi, ci, from_equality, from_neg = (False, False)):
        '''
        Adjusts the lower bound on variable xi if the new lower bound is
        more limiting. The assignment of variable xi is adjusted to be
        within the new bound if needed.

        Also calls `self._update` to update the assignment for slack variables
        to keep all equalities satisfied.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _update(self, xi, v):
        '''
        Updates all slack variables that have equations that contain
        variable xi so that they stay satisfied given xi is equal to v.
        '''
        i = xi.col_idx
        for j, b in enumerate(self.slack):
            aji = self.A[(j, i)]
            b.assign = b.assign + (v - xi.assign) * aji
            xi.assign = v
            return None

    
    def check(self):
        '''
        Searches for an assignment that satisfies all constraints
        or determines that no such assignment exists and gives
        a minimal conflict clause that "explains" why the
        constraints are unsatisfiable.

        Returns
        =======

        (True, assignment) or (False, explanation)

        assignment : dict of LRAVariables to values
            Assigned values are tuples that represent a rational number
            plus some infinatesimal delta.

        explanation : set of ints
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _pivot_and_update(self, M, basic, nonbasic, xi, xj, v):
        '''
        Pivots basic variable xi with nonbasic variable xj,
        and sets value of xi to v and adjusts the values of all basic variables
        to keep equations satisfied.
        '''
        j = xj.col_idx
        i = basic[xi]
    # WARNING: Decompyle incomplete

    _pivot = (lambda M, i, j: _, _, Mij = M[(i, :)], M[(:, j)], M[(i, j)]if Mij == 0:
raise ZeroDivisionError('Tried to pivot about zero-valued entry.')A = M.copy()A[(i, :)] = -A[(i, :)] / Mijfor row in range(M.shape[0]):
if row != i:
A[(row, :)] = A[(row, :)] + A[(row, j)] * A[(i, :)]A)()


def _sep_const_coeff(expr):
    '''
    Example
    =======

    >>> from sympy.logic.algorithms.lra_theory import _sep_const_coeff
    >>> from sympy.abc import x, y
    >>> _sep_const_coeff(2*x)
    (x, 2)
    >>> _sep_const_coeff(2*x + 3*y)
    (2*x + 3*y, 1)
    '''
    if isinstance(expr, Add):
        return (expr, sympify(1))
    if None(expr, Mul):
        coeffs = expr.args
    else:
        coeffs = [
            expr]
    const = []
    var = []
# WARNING: Decompyle incomplete


def _list_terms(expr):
    if not isinstance(expr, Add):
        return [
            expr]
    return None.args


def _sep_const_terms(expr):
    '''
    Example
    =======

    >>> from sympy.logic.algorithms.lra_theory import _sep_const_terms
    >>> from sympy.abc import x, y
    >>> _sep_const_terms(2*x + 3*y + 2)
    (2*x + 3*y, 2)
    '''
    if isinstance(expr, Add):
        terms = expr.args
    else:
        terms = [
            expr]
    const = []
    var = []
    for t in terms:
        if len(t.free_symbols) == 0:
            const.append(t)
            continue
        var.append(t)
        return (sum(var), sum(const))


def _eval_binrel(binrel):
    '''
    Simplify binary relation to True / False if possible.
    '''
    if not len(binrel.lhs.free_symbols) == 0 or len(binrel.rhs.free_symbols) == 0:
        return binrel
    if None.function == Q.lt:
        res = binrel.lhs < binrel.rhs
    elif binrel.function == Q.gt:
        res = binrel.lhs > binrel.rhs
    elif binrel.function == Q.le:
        res = binrel.lhs <= binrel.rhs
    elif binrel.function == Q.ge:
        res = binrel.lhs >= binrel.rhs
    elif binrel.function == Q.eq:
        res = Eq(binrel.lhs, binrel.rhs)
    elif binrel.function == Q.ne:
        res = Ne(binrel.lhs, binrel.rhs)
    if res == True or res == False:
        return res


class Boundary:
    '''
    Represents an upper or lower bound or an equality between a symbol
    and some constant.
    '''
    
    def __init__(self, var, const, upper, equality, strict = (None,)):
        pass
    # WARNING: Decompyle incomplete

    from_upper = (lambda var: neg = -1 if var.upper_from_neg else 1b = Boundary(var, var.upper[0], True, var.upper_from_eq, var.upper[1] != 0)if neg < 0:
b = b.get_negated()(b, neg))()
    from_lower = (lambda var: neg = -1 if var.lower_from_neg else 1b = Boundary(var, var.lower[0], False, var.lower_from_eq, var.lower[1] != 0)if neg < 0:
b = b.get_negated()(b, neg))()
    
    def get_negated(self):
        return Boundary(self.var, self.bound, not (self.upper), self.equality, not (self.strict))

    
    def get_inequality(self):
        if self.equality:
            return Eq(self.var.var, self.bound)
        if None.upper and self.strict:
            return self.var.var < self.bound
        if None.upper and self.strict:
            return self.var.var > self.bound
        if None.upper:
            return self.var.var <= self.bound
        return None.var.var >= self.bound

    
    def __repr__(self):
        return repr('Boundry(' + repr(self.get_inequality()) + ')')

    
    def __eq__(self, other):
        other = (other.var, other.bound, other.strict, other.upper, other.equality)
        return (self.var, self.bound, self.strict, self.upper, self.equality) == other

    
    def __hash__(self):
        return hash((self.var, self.bound, self.strict, self.upper, self.equality))



class LRARational:
    '''
    Represents a rational plus or minus some amount
    of arbitrary small deltas.
    '''
    
    def __init__(self, rational, delta):
        self.value = (rational, delta)

    
    def __lt__(self, other):
        return self.value < other.value

    
    def __le__(self, other):
        return self.value <= other.value

    
    def __eq__(self, other):
        return self.value == other.value

    
    def __add__(self, other):
        return LRARational(self.value[0] + other.value[0], self.value[1] + other.value[1])

    
    def __sub__(self, other):
        return LRARational(self.value[0] - other.value[0], self.value[1] - other.value[1])

    
    def __mul__(self, other):
        pass
    # WARNING: Decompyle incomplete

    
    def __getitem__(self, index):
        return self.value[index]

    
    def __repr__(self):
        return repr(self.value)



class LRAVariable:
    '''
    Object to keep track of upper and lower bounds
    on `self.var`.
    '''
    
    def __init__(self, var):
        self.upper = LRARational(float('inf'), 0)
        self.upper_from_eq = False
        self.upper_from_neg = False
        self.lower = LRARational(-float('inf'), 0)
        self.lower_from_eq = False
        self.lower_from_neg = False
        self.assign = LRARational(0, 0)
        self.var = var
        self.col_idx = None

    
    def __repr__(self):
        return repr(self.var)

    
    def __eq__(self, other):
        if not isinstance(other, LRAVariable):
            return False
        return None.var == self.var

    
    def __hash__(self):
        return hash(self.var)

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ask.pyc (Python 3.11)

'''Module for querying SymPy objects about assumptions.'''
from sympy.assumptions.assume import global_assumptions, Predicate, AppliedPredicate
from sympy.assumptions.cnf import CNF, EncodedCNF, Literal
from sympy.core import sympify
from sympy.core.kind import BooleanKind
from sympy.core.relational import Eq, Ne, Gt, Lt, Ge, Le
from sympy.logic.inference import satisfiable
from sympy.utilities.decorator import memoize_property
from sympy.utilities.exceptions import sympy_deprecation_warning, SymPyDeprecationWarning, ignore_warnings

class AssumptionKeys:
    '''
    This class contains all the supported keys by ``ask``.
    It should be accessed via the instance ``sympy.Q``.

    '''
    hermitian = (lambda self: HermitianPredicate = HermitianPredicateimport handlers.setsHermitianPredicate())()
    antihermitian = (lambda self: AntihermitianPredicate = AntihermitianPredicateimport handlers.setsAntihermitianPredicate())()
    real = (lambda self: RealPredicate = RealPredicateimport handlers.setsRealPredicate())()
    extended_real = (lambda self: ExtendedRealPredicate = ExtendedRealPredicateimport handlers.setsExtendedRealPredicate())()
    imaginary = (lambda self: ImaginaryPredicate = ImaginaryPredicateimport handlers.setsImaginaryPredicate())()
    complex = (lambda self: ComplexPredicate = ComplexPredicateimport handlers.setsComplexPredicate())()
    algebraic = (lambda self: AlgebraicPredicate = AlgebraicPredicateimport handlers.setsAlgebraicPredicate())()
    transcendental = (lambda self: TranscendentalPredicate = TranscendentalPredicateimport predicates.setsTranscendentalPredicate())()
    integer = (lambda self: IntegerPredicate = IntegerPredicateimport handlers.setsIntegerPredicate())()
    noninteger = (lambda self: NonIntegerPredicate = NonIntegerPredicateimport predicates.setsNonIntegerPredicate())()
    rational = (lambda self: RationalPredicate = RationalPredicateimport handlers.setsRationalPredicate())()
    irrational = (lambda self: IrrationalPredicate = IrrationalPredicateimport handlers.setsIrrationalPredicate())()
    finite = (lambda self: FinitePredicate = FinitePredicateimport handlers.calculusFinitePredicate())()
    infinite = (lambda self: InfinitePredicate = InfinitePredicateimport handlers.calculusInfinitePredicate())()
    positive_infinite = (lambda self: PositiveInfinitePredicate = PositiveInfinitePredicateimport handlers.calculusPositiveInfinitePredicate())()
    negative_infinite = (lambda self: NegativeInfinitePredicate = NegativeInfinitePredicateimport handlers.calculusNegativeInfinitePredicate())()
    positive = (lambda self: PositivePredicate = PositivePredicateimport handlers.orderPositivePredicate())()
    negative = (lambda self: NegativePredicate = NegativePredicateimport handlers.orderNegativePredicate())()
    zero = (lambda self: ZeroPredicate = ZeroPredicateimport handlers.orderZeroPredicate())()
    extended_positive = (lambda self: ExtendedPositivePredicate = ExtendedPositivePredicateimport handlers.orderExtendedPositivePredicate())()
    extended_negative = (lambda self: ExtendedNegativePredicate = ExtendedNegativePredicateimport handlers.orderExtendedNegativePredicate())()
    nonzero = (lambda self: NonZeroPredicate = NonZeroPredicateimport handlers.orderNonZeroPredicate())()
    nonpositive = (lambda self: NonPositivePredicate = NonPositivePredicateimport handlers.orderNonPositivePredicate())()
    nonnegative = (lambda self: NonNegativePredicate = NonNegativePredicateimport handlers.orderNonNegativePredicate())()
    extended_nonzero = (lambda self: ExtendedNonZeroPredicate = ExtendedNonZeroPredicateimport handlers.orderExtendedNonZeroPredicate())()
    extended_nonpositive = (lambda self: ExtendedNonPositivePredicate = ExtendedNonPositivePredicateimport handlers.orderExtendedNonPositivePredicate())()
    extended_nonnegative = (lambda self: ExtendedNonNegativePredicate = ExtendedNonNegativePredicateimport handlers.orderExtendedNonNegativePredicate())()
    even = (lambda self: EvenPredicate = EvenPredicateimport handlers.ntheoryEvenPredicate())()
    odd = (lambda self: OddPredicate = OddPredicateimport handlers.ntheoryOddPredicate())()
    prime = (lambda self: PrimePredicate = PrimePredicateimport handlers.ntheoryPrimePredicate())()
    composite = (lambda self: CompositePredicate = CompositePredicateimport handlers.ntheoryCompositePredicate())()
    commutative = (lambda self: CommutativePredicate = CommutativePredicateimport handlers.commonCommutativePredicate())()
    is_true = (lambda self: IsTruePredicate = IsTruePredicateimport handlers.commonIsTruePredicate())()
    symmetric = (lambda self: SymmetricPredicate = SymmetricPredicateimport handlers.matricesSymmetricPredicate())()
    invertible = (lambda self: InvertiblePredicate = InvertiblePredicateimport handlers.matricesInvertiblePredicate())()
    orthogonal = (lambda self: OrthogonalPredicate = OrthogonalPredicateimport handlers.matricesOrthogonalPredicate())()
    unitary = (lambda self: UnitaryPredicate = UnitaryPredicateimport handlers.matricesUnitaryPredicate())()
    positive_definite = (lambda self: PositiveDefinitePredicate = PositiveDefinitePredicateimport handlers.matricesPositiveDefinitePredicate())()
    upper_triangular = (lambda self: UpperTriangularPredicate = UpperTriangularPredicateimport handlers.matricesUpperTriangularPredicate())()
    lower_triangular = (lambda self: LowerTriangularPredicate = LowerTriangularPredicateimport handlers.matricesLowerTriangularPredicate())()
    diagonal = (lambda self: DiagonalPredicate = DiagonalPredicateimport handlers.matricesDiagonalPredicate())()
    fullrank = (lambda self: FullRankPredicate = FullRankPredicateimport handlers.matricesFullRankPredicate())()
    square = (lambda self: SquarePredicate = SquarePredicateimport handlers.matricesSquarePredicate())()
    integer_elements = (lambda self: IntegerElementsPredicate = IntegerElementsPredicateimport handlers.matricesIntegerElementsPredicate())()
    real_elements = (lambda self: RealElementsPredicate = RealElementsPredicateimport handlers.matricesRealElementsPredicate())()
    complex_elements = (lambda self: ComplexElementsPredicate = ComplexElementsPredicateimport handlers.matricesComplexElementsPredicate())()
    singular = (lambda self: SingularPredicate = SingularPredicateimport predicates.matricesSingularPredicate())()
    normal = (lambda self: NormalPredicate = NormalPredicateimport predicates.matricesNormalPredicate())()
    triangular = (lambda self: TriangularPredicate = TriangularPredicateimport predicates.matricesTriangularPredicate())()
    unit_triangular = (lambda self: UnitTriangularPredicate = UnitTriangularPredicateimport predicates.matricesUnitTriangularPredicate())()
    eq = (lambda self: EqualityPredicate = EqualityPredicateimport relation.equalityEqualityPredicate())()
    ne = (lambda self: UnequalityPredicate = UnequalityPredicateimport relation.equalityUnequalityPredicate())()
    gt = (lambda self: StrictGreaterThanPredicate = StrictGreaterThanPredicateimport relation.equalityStrictGreaterThanPredicate())()
    ge = (lambda self: GreaterThanPredicate = GreaterThanPredicateimport relation.equalityGreaterThanPredicate())()
    lt = (lambda self: StrictLessThanPredicate = StrictLessThanPredicateimport relation.equalityStrictLessThanPredicate())()
    le = (lambda self: LessThanPredicate = LessThanPredicateimport relation.equalityLessThanPredicate())()

Q = AssumptionKeys()

def _extract_all_facts(assump, exprs):
    '''
    Extract all relevant assumptions from *assump* with respect to given *exprs*.

    Parameters
    ==========

    assump : sympy.assumptions.cnf.CNF

    exprs : tuple of expressions

    Returns
    =======

    sympy.assumptions.cnf.CNF

    Examples
    ========

    >>> from sympy import Q
    >>> from sympy.assumptions.cnf import CNF
    >>> from sympy.assumptions.ask import _extract_all_facts
    >>> from sympy.abc import x, y
    >>> assump = CNF.from_prop(Q.positive(x) & Q.integer(y))
    >>> exprs = (x,)
    >>> cnf = _extract_all_facts(assump, exprs)
    >>> cnf.clauses
    {frozenset({Literal(Q.positive, False)})}

    '''
    facts = set()
    for clause in assump.clauses:
        args = []
        for literal in clause:
            if isinstance(literal.lit, AppliedPredicate) and len(literal.lit.arguments) == 1:
                if literal.lit.arg in exprs:
                    args.append(Literal(literal.lit.function, literal.is_Not))
                    continue
            
        if args:
            facts.add(frozenset(args))
        return CNF(facts)


def ask(proposition, assumptions, context = (True, global_assumptions)):
    '''
    Function to evaluate the proposition with assumptions.

    Explanation
    ===========

    This function evaluates the proposition to ``True`` or ``False`` if
    the truth value can be determined. If not, it returns ``None``.

    It should be discerned from :func:`~.refine()` which, when applied to a
    proposition, simplifies the argument to symbolic ``Boolean`` instead of
    Python built-in ``True``, ``False`` or ``None``.

    **Syntax**

        * ask(proposition)
            Evaluate the *proposition* in global assumption context.

        * ask(proposition, assumptions)
            Evaluate the *proposition* with respect to *assumptions* in
            global assumption context.

    Parameters
    ==========

    proposition : Boolean
        Proposition which will be evaluated to boolean value. If this is
        not ``AppliedPredicate``, it will be wrapped by ``Q.is_true``.

    assumptions : Boolean, optional
        Local assumptions to evaluate the *proposition*.

    context : AssumptionsContext, optional
        Default assumptions to evaluate the *proposition*. By default,
        this is ``sympy.assumptions.global_assumptions`` variable.

    Returns
    =======

    ``True``, ``False``, or ``None``

    Raises
    ======

    TypeError : *proposition* or *assumptions* is not valid logical expression.

    ValueError : assumptions are inconsistent.

    Examples
    ========

    >>> from sympy import ask, Q, pi
    >>> from sympy.abc import x, y
    >>> ask(Q.rational(pi))
    False
    >>> ask(Q.even(x*y), Q.even(x) & Q.integer(y))
    True
    >>> ask(Q.prime(4*x), Q.integer(x))
    False

    If the truth value cannot be determined, ``None`` will be returned.

    >>> print(ask(Q.odd(3*x))) # cannot determine unless we know x
    None

    ``ValueError`` is raised if assumptions are inconsistent.

    >>> ask(Q.integer(x), Q.even(x) & Q.odd(x))
    Traceback (most recent call last):
      ...
    ValueError: inconsistent assumptions Q.even(x) & Q.odd(x)

    Notes
    =====

    Relations in assumptions are not implemented (yet), so the following
    will not give a meaningful result.

    >>> ask(Q.positive(x), x > 0)

    It is however a work in progress.

    See Also
    ========

    sympy.assumptions.refine.refine : Simplification using assumptions.
        Proposition is not reduced to ``None`` if the truth value cannot
        be determined.
    '''
    satask = satask
    import sympy.assumptions.satask
    lra_satask = lra_satask
    import sympy.assumptions.lra_satask
    UnhandledInput = UnhandledInput
    import sympy.logic.algorithms.lra_theory
    proposition = sympify(proposition)
    assumptions = sympify(assumptions)
    if isinstance(proposition, Predicate) or proposition.kind is not BooleanKind:
        raise TypeError('proposition must be a valid logical expression')
    if isinstance(assumptions, Predicate) or assumptions.kind is not BooleanKind:
        raise TypeError('assumptions must be a valid logical expression')
    binrelpreds = {
        Le: Q.le,
        Ge: Q.ge,
        Lt: Q.lt,
        Gt: Q.gt,
        Ne: Q.ne,
        Eq: Q.eq }
    if isinstance(proposition, AppliedPredicate):
        args = proposition.arguments
        key = proposition.function
    elif proposition.func in binrelpreds:
        args = proposition.args
        key = binrelpreds[type(proposition)]
    else:
        args = (proposition,)
        key = Q.is_true
    assump_cnf = CNF.from_prop(assumptions)
    assump_cnf.extend(context)
    local_facts = _extract_all_facts(assump_cnf, args)
    known_facts_cnf = get_all_known_facts()
    enc_cnf = EncodedCNF()
    enc_cnf.from_cnf(CNF(known_facts_cnf))
    enc_cnf.add_from_cnf(local_facts)
    if local_facts.clauses and satisfiable(enc_cnf) is False:
        raise ValueError('inconsistent assumptions %s' % assumptions)
    res = _ask_single_fact(key, local_facts)
# WARNING: Decompyle incomplete


def _ask_single_fact(key, local_facts):
    '''
    Compute the truth value of single predicate using assumptions.

    Parameters
    ==========

    key : sympy.assumptions.assume.Predicate
        Proposition predicate.

    local_facts : sympy.assumptions.cnf.CNF
        Local assumption in CNF form.

    Returns
    =======

    ``True``, ``False`` or ``None``

    Examples
    ========

    >>> from sympy import Q
    >>> from sympy.assumptions.cnf import CNF
    >>> from sympy.assumptions.ask import _ask_single_fact

    If prerequisite of proposition is rejected by the assumption,
    return ``False``.

    >>> key, assump = Q.zero, ~Q.zero
    >>> local_facts = CNF.from_prop(assump)
    >>> _ask_single_fact(key, local_facts)
    False
    >>> key, assump = Q.zero, ~Q.even
    >>> local_facts = CNF.from_prop(assump)
    >>> _ask_single_fact(key, local_facts)
    False

    If assumption implies the proposition, return ``True``.

    >>> key, assump = Q.even, Q.zero
    >>> local_facts = CNF.from_prop(assump)
    >>> _ask_single_fact(key, local_facts)
    True

    If proposition rejects the assumption, return ``False``.

    >>> key, assump = Q.even, Q.odd
    >>> local_facts = CNF.from_prop(assump)
    >>> _ask_single_fact(key, local_facts)
    False
    '''
    pass
# WARNING: Decompyle incomplete


def register_handler(key, handler):
    '''
    Register a handler in the ask system. key must be a string and handler a
    class inheriting from AskHandler.

    .. deprecated:: 1.8.
        Use multipledispatch handler instead. See :obj:`~.Predicate`.

    '''
    sympy_deprecation_warning('\n        The AskHandler system is deprecated. The register_handler() function\n        should be replaced with the multipledispatch handler of Predicate.\n        ', deprecated_since_version = '1.8', active_deprecations_target = 'deprecated-askhandler')
    if isinstance(key, Predicate):
        key = key.name.name
    Qkey = getattr(Q, key, None)
# WARNING: Decompyle incomplete


def remove_handler(key, handler):
    '''
    Removes a handler from the ask system.

    .. deprecated:: 1.8.
        Use multipledispatch handler instead. See :obj:`~.Predicate`.

    '''
    sympy_deprecation_warning('\n        The AskHandler system is deprecated. The remove_handler() function\n        should be replaced with the multipledispatch handler of Predicate.\n        ', deprecated_since_version = '1.8', active_deprecations_target = 'deprecated-askhandler')
    if isinstance(key, Predicate):
        key = key.name.name
    ignore_warnings(SymPyDeprecationWarning)
    getattr(Q, key).remove_handler(handler)
    None(None, None)
    return None
    with None:
        if not None:
            pass

from sympy.assumptions.ask_generated import get_all_known_facts, get_known_facts_dict

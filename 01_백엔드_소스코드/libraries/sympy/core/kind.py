# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: kind.pyc (Python 3.11)

'''
Module to efficiently partition SymPy objects.

This system is introduced because class of SymPy object does not always
represent the mathematical classification of the entity. For example,
``Integral(1, x)`` and ``Integral(Matrix([1,2]), x)`` are both instance
of ``Integral`` class. However the former is number and the latter is
matrix.

One way to resolve this is defining subclass for each mathematical type,
such as ``MatAdd`` for the addition between matrices. Basic algebraic
operation such as addition or multiplication take this approach, but
defining every class for every mathematical object is not scalable.

Therefore, we define the "kind" of the object and let the expression
infer the kind of itself from its arguments. Function and class can
filter the arguments by their kind, and behave differently according to
the type of itself.

This module defines basic kinds for core objects. Other kinds such as
``ArrayKind`` or ``MatrixKind`` can be found in corresponding modules.

.. notes::
       This approach is experimental, and can be replaced or deleted in the future.
       See https://github.com/sympy/sympy/pull/20549.
'''
from collections import defaultdict
from cache import cacheit
from sympy.multipledispatch.dispatcher import Dispatcher, ambiguity_warn, ambiguity_register_error_ignore_dup, str_signature, RaiseNotImplementedError

class KindMeta(type):
    pass
# WARNING: Decompyle incomplete


def Kind():
    '''Kind'''
    pass
# WARNING: Decompyle incomplete

Kind = <NODE:27>(Kind, 'Kind', object, metaclass = KindMeta)

class _UndefinedKind(Kind):
    pass
# WARNING: Decompyle incomplete

UndefinedKind = _UndefinedKind()

class _NumberKind(Kind):
    pass
# WARNING: Decompyle incomplete

NumberKind = _NumberKind()

class _BooleanKind(Kind):
    pass
# WARNING: Decompyle incomplete

BooleanKind = _BooleanKind()

class KindDispatcher:
    """
    Dispatcher to select a kind from multiple kinds by binary dispatching.

    .. notes::
       This approach is experimental, and can be replaced or deleted in
       the future.

    Explanation
    ===========

    SymPy object's :obj:`sympy.core.kind.Kind()` vaguely represents the
    algebraic structure where the object belongs to. Therefore, with
    given operation, we can always find a dominating kind among the
    different kinds. This class selects the kind by recursive binary
    dispatching. If the result cannot be determined, ``UndefinedKind``
    is returned.

    Examples
    ========

    Multiplication between numbers return number.

    >>> from sympy import NumberKind, Mul
    >>> Mul._kind_dispatcher(NumberKind, NumberKind)
    NumberKind

    Multiplication between number and unknown-kind object returns unknown kind.

    >>> from sympy import UndefinedKind
    >>> Mul._kind_dispatcher(NumberKind, UndefinedKind)
    UndefinedKind

    Any number and order of kinds is allowed.

    >>> Mul._kind_dispatcher(UndefinedKind, NumberKind)
    UndefinedKind
    >>> Mul._kind_dispatcher(NumberKind, UndefinedKind, NumberKind)
    UndefinedKind

    Since matrix forms a vector space over scalar field, multiplication
    between matrix with numeric element and number returns matrix with
    numeric element.

    >>> from sympy.matrices import MatrixKind
    >>> Mul._kind_dispatcher(MatrixKind(NumberKind), NumberKind)
    MatrixKind(NumberKind)

    If a matrix with number element and another matrix with unknown-kind
    element are multiplied, we know that the result is matrix but the
    kind of its elements is unknown.

    >>> Mul._kind_dispatcher(MatrixKind(NumberKind), MatrixKind(UndefinedKind))
    MatrixKind(UndefinedKind)

    Parameters
    ==========

    name : str

    commutative : bool, optional
        If True, binary dispatch will be automatically registered in
        reversed order as well.

    doc : str, optional

    """
    
    def __init__(self, name, commutative, doc = (False, None)):
        self.name = name
        self.doc = doc
        self.commutative = commutative
        self._dispatcher = Dispatcher(name)

    
    def __repr__(self):
        return '<dispatched %s>' % self.name

    
    def register(self, *types, **kwargs):
        '''
        Register the binary dispatcher for two kind classes.

        If *self.commutative* is ``True``, signature in reversed order is
        automatically registered as well.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def __call__(self, *args, **kwargs):
        if self.commutative:
            kinds = frozenset(args)
        else:
            kinds = []
            prev = None
            for a in args:
                if prev is not a:
                    kinds.append(a)
                    prev = a
    # WARNING: Decompyle incomplete

    dispatch_kinds = (lambda self, kinds: if len(kinds) == 1:
(result,) = kindsif not isinstance(result, Kind):
raise RuntimeError('%s is not a kind.' % result)result# WARNING: Decompyle incomplete
)()
    __doc__ = (lambda self: docs = [
'Kind dispatcher : %s' % self.name,
'Note that support for this is experimental. See the docs for :class:`KindDispatcher` for details']if self.doc:
docs.append(self.doc)s = 'Registered kind classes\n's += '=' * len(s)docs.append(s)amb_sigs = []typ_sigs = defaultdict(list)for sigs in self._dispatcher.ordering[::-1]:
key = self._dispatcher.funcs[sigs]typ_sigs[key].append(sigs)for func, sigs in typ_sigs.items():
sigs_str = (lambda .0: pass# WARNING: Decompyle incomplete
)(sigs())
                if isinstance(func, RaiseNotImplementedError):
                    amb_sigs.append(sigs_str)
                    continue
                s = 'Inputs: %s\n' % sigs_str
                s += '-' * len(s) + '\n'
                docs.append(s)
                if amb_sigs:
                    s = 'Ambiguous kind classes\n'
                    s += '=' * len(s)
                    docs.append(s)
                    s = '\n'.join(amb_sigs)
                    docs.append(s)
        return '\n\n'.join(docs)
)()

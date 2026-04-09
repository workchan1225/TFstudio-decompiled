# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: assume.pyc (Python 3.11)

'''A module which implements predicates and assumption context.'''
from contextlib import contextmanager
import inspect
from sympy.core.symbol import Str
from sympy.core.sympify import _sympify
from sympy.logic.boolalg import Boolean, false, true
from sympy.multipledispatch.dispatcher import Dispatcher, str_signature
from sympy.utilities.exceptions import sympy_deprecation_warning
from sympy.utilities.iterables import is_sequence
from sympy.utilities.source import get_class

class AssumptionsContext(set):
    pass
# WARNING: Decompyle incomplete

global_assumptions = AssumptionsContext()

class AppliedPredicate(Boolean):
    pass
# WARNING: Decompyle incomplete


class PredicateMeta(type):
    pass
# WARNING: Decompyle incomplete


def Predicate():
    '''Predicate'''
    pass
# WARNING: Decompyle incomplete

Predicate = <NODE:27>(Predicate, 'Predicate', Boolean, metaclass = PredicateMeta)

class UndefinedPredicate(Predicate):
    pass
# WARNING: Decompyle incomplete

assuming = (lambda : pass# WARNING: Decompyle incomplete
)()

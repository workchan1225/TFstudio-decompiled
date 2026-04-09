# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: engines.pyc (Python 3.11)

'''
Engine classes for :func:`~pandas.eval`
'''
from __future__ import annotations
import abc
from typing import TYPE_CHECKING
from pandas.errors import NumExprClobberingError
from pandas.core.computation.align import align_terms, reconstruct_object
from pandas.core.computation.ops import MATHOPS, REDUCTIONS
from pandas.io.formats import printing
if TYPE_CHECKING:
    from pandas.core.computation.expr import Expr
_ne_builtins = frozenset(MATHOPS + REDUCTIONS)

def _check_ne_builtin_clash(expr = None):
    '''
    Attempt to prevent foot-shooting in a helpful way.

    Parameters
    ----------
    expr : Expr
        Terms can contain
    '''
    names = expr.names
    overlap = names & _ne_builtins
    if overlap:
        s = (lambda .0: [ repr(x) for x in .0 ])(overlap())
        raise NumExprClobberingError(f'''Variables in expression "{expr}" overlap with builtins: ({s})''')


def AbstractEngine():
    '''AbstractEngine'''
    __doc__ = 'Object serving as a base class for all engines.'
    has_neg_frac = False
    
    def __init__(self = None, expr = None):
        self.expr = expr
        self.aligned_axes = None
        self.result_type = None
        self.result_name = None

    
    def convert(self = None):
        '''
        Convert an expression for evaluation.

        Defaults to return the expression as a string.
        '''
        return printing.pprint_thing(self.expr)

    
    def evaluate(self = None):
        '''
        Run the engine on the expression.

        This method performs alignment which is necessary no matter what engine
        is being used, thus its implementation is in the base class.

        Returns
        -------
        object
            The result of the passed expression.
        '''
        if not self._is_aligned:
            (self.result_type, self.aligned_axes, self.result_name) = align_terms(self.expr.terms)
        res = self._evaluate()
        return reconstruct_object(self.result_type, res, self.aligned_axes, self.expr.terms.return_type, self.result_name)

    _is_aligned = (lambda self = None:

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: consts.pyc (Python 3.11)

from types import ModuleType
import weakref
from numba.core.errors import ConstantInferenceError, NumbaError
from numba.core import ir

class ConstantInference(object):
    """
    A constant inference engine for a given interpreter.
    Inference inspects the IR to try and compute a compile-time constant for
    a variable.

    This shouldn't be used directly, instead call Interpreter.infer_constant().
    """
    
    def __init__(self, func_ir):
        self._func_ir = weakref.proxy(func_ir)
        self._cache = { }

    
    def infer_constant(self, name, loc = (None,)):
        '''
        Infer a constant value for the given variable *name*.
        If no value can be inferred, numba.errors.ConstantInferenceError
        is raised.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _fail(self, val):
        raise ConstantInferenceError(f'''Constant inference not possible for: {val!s}''', loc = None)

    
    def _do_infer(self, name):
        if not isinstance(name, str):
            raise TypeError(f'''infer_constant() called with non-str {name!r}''')
        
        try:
            defn = self._func_ir.get_definition(name)
        except KeyError:
            raise ConstantInferenceError(f'''no single definition for {name!r}''')

        
        try:
            const = defn.infer_constant()
        except ConstantInferenceError:
            if isinstance(defn, ir.Expr):
                return 
            None._fail(defn)

        return const

    
    def _infer_expr(self, expr):
        pass
    # WARNING: Decompyle incomplete

    
    def _infer_call(self, func, expr):
        pass
    # WARNING: Decompyle incomplete

    
    def _infer_getattr(self, value, expr):

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: setdecl.pyc (Python 3.11)

import operator
from numba.core import types
from templates import ConcreteTemplate, AbstractTemplate, AttributeTemplate, CallableTemplate, Registry, signature, bound_function, make_callable_template
from numba.core.typing import collections
registry = Registry()
infer = registry.register
infer_global = registry.register_global
infer_getattr = registry.register_attr
SetBuiltin = <NODE:12>()
SetAttribute = <NODE:12>()

class SetOperator(AbstractTemplate):
    
    def generic(self, args, kws):
        if len(args) != 2:
            return None
        (a, b) = None
    # WARNING: Decompyle incomplete



class SetComparison(AbstractTemplate):
    
    def generic(self, args, kws):
        if len(args) != 2:
            return None
        (a, b) = None
    # WARNING: Decompyle incomplete


for op_key in (operator.add, operator.invert):
    ConcreteSetOperator = <NODE:12>()
    for op_key in (operator.iadd,):
        ConcreteInplaceSetOperator = <NODE:12>()
        return None

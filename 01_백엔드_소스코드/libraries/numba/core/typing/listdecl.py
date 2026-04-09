# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: listdecl.pyc (Python 3.11)

import operator
from numba.core import types
from templates import ConcreteTemplate, AbstractTemplate, AttributeTemplate, CallableTemplate, Registry, signature, bound_function, make_callable_template
from numba.core.typing import collections
registry = Registry()
infer = registry.register
infer_global = registry.register_global
infer_getattr = registry.register_attr
ListBuiltin = <NODE:12>()
ListAttribute = <NODE:12>()
AddList = <NODE:12>()
InplaceAddList = <NODE:12>()
MulList = <NODE:12>()
InplaceMulList = <NODE:12>()

class ListCompare(AbstractTemplate):
    
    def generic(self, args, kws):
        (lhs, rhs) = args
    # WARNING: Decompyle incomplete


ListEq = <NODE:12>()

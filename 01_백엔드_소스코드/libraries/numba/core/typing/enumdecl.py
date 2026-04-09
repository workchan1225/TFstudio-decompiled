# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: enumdecl.pyc (Python 3.11)

'''
Typing for enums.
'''
import operator
from numba.core import types
from numba.core.typing.templates import AbstractTemplate, AttributeTemplate, signature, Registry
registry = Registry()
infer = registry.register
infer_global = registry.register_global
infer_getattr = registry.register_attr
EnumAttribute = <NODE:12>()
EnumClassAttribute = <NODE:12>()
EnumClassStaticGetItem = <NODE:12>()

class EnumCompare(AbstractTemplate):
    
    def generic(self, args, kws):
        (lhs, rhs) = args
        if isinstance(lhs, types.EnumMember) or isinstance(rhs, types.EnumMember) or lhs == rhs:
            return signature(types.boolean, lhs, rhs)
        return None
        return None


EnumEq = <NODE:12>()
EnumNe = <NODE:12>()

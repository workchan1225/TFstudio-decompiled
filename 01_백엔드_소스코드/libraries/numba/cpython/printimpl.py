# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: printimpl.pyc (Python 3.11)

'''
This file implements print functionality for the CPU.
'''
from numba.core import types, typing, cgutils
from numba.core.imputils import Registry, impl_ret_untracked
registry = Registry('printimpl')
lower = registry.lower
print_item_impl = (lambda context, builder, sig, args: (ty,) = sig.argsval = ty.literal_valuepyapi = context.get_python_api(builder)strobj = pyapi.unserialize(pyapi.serialize_object(val))pyapi.print_object(strobj)pyapi.decref(strobj)res = context.get_dummy_value()impl_ret_untracked(context, builder, sig.return_type, res))()
print_item_impl = (lambda context, builder, sig, args:

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: eh.pyc (Python 3.11)

'''
Exception handling intrinsics.
'''
from numba.core import types, errors, cgutils
from numba.core.extending import intrinsic
exception_check = (lambda typingctx: 
def codegen(context, builder, signature, args):
nrt = context.nrtnrt.eh_check(builder)restype = types.boolean(restype(), codegen))()
mark_try_block = (lambda typingctx: 
def codegen(context, builder, signature, args):
nrt = context.nrtnrt.eh_try(builder)context.get_dummy_value()restype = types.none(restype(), codegen))()
end_try_block = (lambda typingctx: 
def codegen(context, builder, signature, args):
nrt = context.nrtnrt.eh_end_try(builder)context.get_dummy_value()restype = types.none(restype(), codegen))()
exception_match = (lambda typingctx, exc_value, exc_class: if exc_class.exc_class is not Exception:
msg = 'Exception matching is limited to {}'raise errors.UnsupportedError(msg.format(Exception))
def codegen(context, builder, signature, args):
cgutils.true_bitrestype = types.boolean(restype(exc_value, exc_class), codegen))()

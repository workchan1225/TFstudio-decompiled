# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: npdatetime.pyc (Python 3.11)

'''
Typing declarations for np.timedelta64.
'''
from itertools import product
import operator
from numba.core import types, errors
from numba.core.typing.templates import AttributeTemplate, ConcreteTemplate, AbstractTemplate, infer_global, infer, infer_getattr, signature
from numba.np import npdatetime_helpers
from numba.np.numpy_support import numpy_version

class TimedeltaUnaryOp(AbstractTemplate):
    
    def generic(self, args, kws):
        if len(args) == 2:
            return None
        (op,) = None
        if not isinstance(op, types.NPTimedelta):
            return None
        return None(op, op)



class TimedeltaBinOp(AbstractTemplate):
    
    def generic(self, args, kws):
        if len(args) == 1:
            return None
        (left, right) = None
        if not (lambda .0: pass# WARNING: Decompyle incomplete
)(args()):
            return None
        if all.can_cast_timedelta_units(left.unit, right.unit):
            return signature(right, left, right)
        if None.can_cast_timedelta_units(right.unit, left.unit):
            return signature(left, left, right)



class TimedeltaCmpOp(AbstractTemplate):
    
    def generic(self, args, kws):
        (left, right) = args
        if not (lambda .0: pass# WARNING: Decompyle incomplete
)(args()):
            return None
        return all(types.boolean, left, right)



class TimedeltaOrderedCmpOp(AbstractTemplate):
    
    def generic(self, args, kws):
        (left, right) = args
        if not (lambda .0: pass# WARNING: Decompyle incomplete
)(args()):
            return None
        if all.can_cast_timedelta_units(left.unit, right.unit) or npdatetime_helpers.can_cast_timedelta_units(right.unit, left.unit):
            return signature(types.boolean, left, right)



class TimedeltaMixOp(AbstractTemplate):
    
    def generic(self, args, kws):
        '''
        (timedelta64, {int, float}) -> timedelta64
        ({int, float}, timedelta64) -> timedelta64
        '''
        pass
    # WARNING: Decompyle incomplete



class TimedeltaDivOp(AbstractTemplate):
    
    def generic(self, args, kws):
        '''
        (timedelta64, {int, float}) -> timedelta64
        (timedelta64, timedelta64) -> float
        '''
        (left, right) = args
        if not isinstance(left, types.NPTimedelta):
            return None
        if None(right, types.NPTimedelta):
            if npdatetime_helpers.can_cast_timedelta_units(left.unit, right.unit) or npdatetime_helpers.can_cast_timedelta_units(right.unit, left.unit):
                return signature(types.float64, left, right)
            return None
        if None(right, types.Float):
            return signature(left, left, right)
        if None(right, types.Integer):
            return signature(left, left, types.int64)


TimedeltaUnaryPos = <NODE:12>()
TimedeltaUnaryNeg = <NODE:12>()
TimedeltaBinAdd = <NODE:12>()()
TimedeltaBinSub = <NODE:12>()()
TimedeltaBinMult = <NODE:12>()()
TimedeltaTrueDiv = <NODE:12>()()
TimedeltaFloorDiv = <NODE:12>()()
TimedeltaCmpLt = <NODE:12>()
TimedeltaCmpLE = <NODE:12>()
TimedeltaCmpGt = <NODE:12>()
TimedeltaCmpGE = <NODE:12>()
TimedeltaAbs = <NODE:12>()
DatetimePlusTimedelta = <NODE:12>()()
DatetimeMinusTimedelta = <NODE:12>()()
DatetimeMinusDatetime = <NODE:12>()

class DatetimeCmpOp(AbstractTemplate):
    
    def generic(self, args, kws):
        (left, right) = args
        if not (lambda .0: pass# WARNING: Decompyle incomplete
)(args()):
            return None
        return all(types.boolean, left, right)


DatetimeCmpEq = <NODE:12>()
DatetimeCmpNe = <NODE:12>()
DatetimeCmpLt = <NODE:12>()
DatetimeCmpLE = <NODE:12>()
DatetimeCmpGt = <NODE:12>()
DatetimeCmpGE = <NODE:12>()
DatetimeMinMax = <NODE:12>()()

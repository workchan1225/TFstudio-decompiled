# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''Private counterpart of ``numpy.typing``.'''
from __future__ import annotations
from  import ufunc
from _utils import set_module
from typing import TYPE_CHECKING, final
NBitBase = <NODE:12>()()

class _256Bit(NBitBase):
    pass


class _128Bit(_256Bit):
    pass


class _96Bit(_128Bit):
    pass


class _80Bit(_96Bit):
    pass


class _64Bit(_80Bit):
    pass


class _32Bit(_64Bit):
    pass


class _16Bit(_32Bit):
    pass


class _8Bit(_16Bit):
    pass

from _nested_sequence import _NestedSequence
from _nbit import _NBitByte, _NBitShort, _NBitIntC, _NBitIntP, _NBitInt, _NBitLongLong, _NBitHalf, _NBitSingle, _NBitDouble, _NBitLongDouble
from _char_codes import _BoolCodes, _UInt8Codes, _UInt16Codes, _UInt32Codes, _UInt64Codes, _Int8Codes, _Int16Codes, _Int32Codes, _Int64Codes, _Float16Codes, _Float32Codes, _Float64Codes, _Complex64Codes, _Complex128Codes, _ByteCodes, _ShortCodes, _IntCCodes, _IntPCodes, _IntCodes, _LongLongCodes, _UByteCodes, _UShortCodes, _UIntCCodes, _UIntPCodes, _UIntCodes, _ULongLongCodes, _HalfCodes, _SingleCodes, _DoubleCodes, _LongDoubleCodes, _CSingleCodes, _CDoubleCodes, _CLongDoubleCodes, _DT64Codes, _TD64Codes, _StrCodes, _BytesCodes, _VoidCodes, _ObjectCodes
from _scalars import _CharLike_co, _BoolLike_co, _UIntLike_co, _IntLike_co, _FloatLike_co, _ComplexLike_co, _TD64Like_co, _NumberLike_co, _ScalarLike_co, _VoidLike_co
from _shape import _Shape, _ShapeLike
from _dtype_like import DTypeLike, _DTypeLike, _SupportsDType, _VoidDTypeLike, _DTypeLikeBool, _DTypeLikeUInt, _DTypeLikeInt, _DTypeLikeFloat, _DTypeLikeComplex, _DTypeLikeTD64, _DTypeLikeDT64, _DTypeLikeObject, _DTypeLikeVoid, _DTypeLikeStr, _DTypeLikeBytes, _DTypeLikeComplex_co
from _array_like import NDArray, ArrayLike, _ArrayLike, _FiniteNestedSequence, _SupportsArray, _SupportsArrayFunc, _ArrayLikeInt, _ArrayLikeBool_co, _ArrayLikeUInt_co, _ArrayLikeInt_co, _ArrayLikeFloat_co, _ArrayLikeComplex_co, _ArrayLikeNumber_co, _ArrayLikeTD64_co, _ArrayLikeDT64_co, _ArrayLikeObject_co, _ArrayLikeVoid_co, _ArrayLikeStr_co, _ArrayLikeBytes_co, _ArrayLikeUnknown, _UnknownType
if TYPE_CHECKING:
    from _ufunc import _UFunc_Nin1_Nout1, _UFunc_Nin2_Nout1, _UFunc_Nin1_Nout2, _UFunc_Nin2_Nout2, _GUFunc_Nin2_Nout1
    return None
_UFunc_Nin1_Nout1 = None
_UFunc_Nin2_Nout1 = ufunc
_UFunc_Nin1_Nout2 = ufunc
_UFunc_Nin2_Nout2 = ufunc
_GUFunc_Nin2_Nout1 = ufunc

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: numerictypes.pyc (Python 3.11)

'''
numerictypes: Define the numeric type objects

This module is designed so "from numerictypes import \\*" is safe.
Exported symbols include:

  Dictionary with all registered number types (including aliases):
    sctypeDict

  Type objects (not all will be available, depends on platform):
      see variable sctypes for which ones you have

    Bit-width names

    int8 int16 int32 int64 int128
    uint8 uint16 uint32 uint64 uint128
    float16 float32 float64 float96 float128 float256
    complex32 complex64 complex128 complex192 complex256 complex512
    datetime64 timedelta64

    c-based names

    bool_

    object_

    void, str_, unicode_

    byte, ubyte,
    short, ushort
    intc, uintc,
    intp, uintp,
    int_, uint,
    longlong, ulonglong,

    single, csingle,
    float_, complex_,
    longfloat, clongfloat,

   As part of the type-hierarchy:    xx -- is bit-width

   generic
     +-> bool_                                  (kind=b)
     +-> number
     |   +-> integer
     |   |   +-> signedinteger     (intxx)      (kind=i)
     |   |   |     byte
     |   |   |     short
     |   |   |     intc
     |   |   |     intp
     |   |   |     int_
     |   |   |     longlong
     |   |   \\-> unsignedinteger  (uintxx)     (kind=u)
     |   |         ubyte
     |   |         ushort
     |   |         uintc
     |   |         uintp
     |   |         uint_
     |   |         ulonglong
     |   +-> inexact
     |       +-> floating          (floatxx)    (kind=f)
     |       |     half
     |       |     single
     |       |     float_          (double)
     |       |     longfloat
     |       \\-> complexfloating  (complexxx)  (kind=c)
     |             csingle         (singlecomplex)
     |             complex_        (cfloat, cdouble)
     |             clongfloat      (longcomplex)
     +-> flexible
     |   +-> character
     |   |     str_     (string_, bytes_)       (kind=S)    [Python 2]
     |   |     unicode_                         (kind=U)    [Python 2]
     |   |
     |   |     bytes_   (string_)               (kind=S)    [Python 3]
     |   |     str_     (unicode_)              (kind=U)    [Python 3]
     |   |
     |   \\-> void                              (kind=V)
     \\-> object_ (not used much)               (kind=O)

'''
import numbers
import warnings
from multiarray import ndarray, array, dtype, datetime_data, datetime_as_string, busday_offset, busday_count, is_busday, busdaycalendar
from _utils import set_module
__all__ = [
    'sctypeDict',
    'sctypes',
    'ScalarType',
    'obj2sctype',
    'cast',
    'nbytes',
    'sctype2char',
    'maximum_sctype',
    'issctype',
    'typecodes',
    'find_common_type',
    'issubdtype',
    'datetime_data',
    'datetime_as_string',
    'busday_offset',
    'busday_count',
    'is_busday',
    'busdaycalendar']
from _string_helpers import english_lower, english_upper, english_capitalize, LOWER_TABLE, UPPER_TABLE
from _type_aliases import sctypeDict, allTypes, bitname, sctypes, _concrete_types, _concrete_typeinfo, _bits_of
from _dtype import _kind_name
from builtins import bool, int, float, complex, object, str, bytes
from numpy.compat import long, unicode
generic = allTypes['generic']
genericTypeRank = [
    'bool',
    'int8',
    'uint8',
    'int16',
    'uint16',
    'int32',
    'uint32',
    'int64',
    'uint64',
    'int128',
    'uint128',
    'float16',
    'float32',
    'float64',
    'float80',
    'float96',
    'float128',
    'float256',
    'complex32',
    'complex64',
    'complex128',
    'complex160',
    'complex192',
    'complex256',
    'complex512',
    'object']
maximum_sctype = (lambda t: g = obj2sctype(t)# WARNING: Decompyle incomplete
)()
issctype = (lambda rep: if not isinstance(rep, (type, dtype)):
Falsetry:
res = obj2sctype(rep)if res and res != object_:
TrueNoneexcept Exception:
False)()
obj2sctype = (lambda rep, default = (None,): if isinstance(rep, type) and issubclass(rep, generic):
repif None(rep, ndarray):
rep.dtype.typetry:
res = dtype(rep)res.typeexcept Exception:
)()
issubclass_ = (lambda arg1, arg2: try:
issubclass(arg1, arg2)except TypeError:
False)()
issubsctype = (lambda arg1, arg2: issubclass(obj2sctype(arg1), obj2sctype(arg2)))()
issubdtype = (lambda arg1, arg2: if not issubclass_(arg1, generic):
arg1 = dtype(arg1).typeif not issubclass_(arg2, generic):
arg2 = dtype(arg2).typeissubclass(arg1, arg2))()

class _typedict(dict):
    '''
    Base object for a dictionary for look-up with any alias for an array dtype.

    Instances of `_typedict` can not be used as dictionaries directly,
    first they have to be populated.

    '''
    
    def __getitem__(self, obj):
        return dict.__getitem__(self, obj2sctype(obj))


nbytes = _typedict()
_alignment = _typedict()
_maxvals = _typedict()
_minvals = _typedict()

def _construct_lookups():
    for name, info in _concrete_typeinfo.items():
        obj = info.type
        nbytes[obj] = info.bits // 8
        _alignment[obj] = info.alignment
        if len(info) > 5:
            _maxvals[obj] = info.max
            _minvals[obj] = info.min
            continue
        _maxvals[obj] = None
        _minvals[obj] = None
        return None

_construct_lookups()
sctype2char = (lambda sctype: sctype = obj2sctype(sctype)# WARNING: Decompyle incomplete
)()
cast = _typedict()
for key in _concrete_types:
    
    cast[key] = lambda x, k = (key,): array(x, copy = False).astype(k)
    
    def _scalar_type_key(typ):
        '''A ``key`` function for `sorted`.'''
        dt = dtype(typ)
        return (dt.kind.lower(), dt.itemsize)

    ScalarType = [
        int,
        float,
        complex,
        bool,
        bytes,
        str,
        memoryview]
    ScalarType += sorted(_concrete_types, key = _scalar_type_key)
    ScalarType = tuple(ScalarType)
    for key in allTypes:
        globals()[key] = allTypes[key]
        __all__.append(key)
        del key
        typecodes = {
            'Character': 'c',
            'Integer': 'bhilqp',
            'UnsignedInteger': 'BHILQP',
            'Float': 'efdg',
            'Complex': 'FDG',
            'AllInteger': 'bBhHiIlLqQpP',
            'AllFloat': 'efdgFDG',
            'Datetime': 'Mm',
            'All': '?bhilqpBHILQPefdgFDGSUVOMm' }
        typeDict = sctypeDict
        _kind_list = [
            'b',
            'u',
            'i',
            'f',
            'c',
            'S',
            'U',
            'V',
            'O',
            'M',
            'm']
        __test_types = '?' + typecodes['AllInteger'][:-2] + typecodes['AllFloat'] + 'O'
        __len_test_types = len(__test_types)
        
        def _find_common_coerce(a, b):
            if a > b:
                return a
            
            try:
                thisind = __test_types.index(a.char)
            except ValueError:
                return None

            return _can_coerce_all([
                a,
                b], start = thisind)

        
        def _can_coerce_all(dtypelist, start = (0,)):
            pass
        # WARNING: Decompyle incomplete

        
        def _register_types():
            numbers.Integral.register(integer)
            numbers.Complex.register(inexact)
            numbers.Real.register(floating)
            numbers.Number.register(number)

        _register_types()
        find_common_type = (lambda array_types, scalar_types: warnings.warn('np.find_common_type is deprecated.  Please use `np.result_type` or `np.promote_types`.\nSee https://numpy.org/devdocs/release/1.25.0-notes.html and the docs for more information.  (Deprecated NumPy 1.25)', DeprecationWarning, stacklevel = 2)array_types = array_types()scalar_types = scalar_types()maxa = _can_coerce_all(array_types)maxsc = _can_coerce_all(scalar_types)# WARNING: Decompyle incomplete
)()
        return None

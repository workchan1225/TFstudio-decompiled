# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: getlimits.pyc (Python 3.11)

'''Machine limits for Float32 and Float64 and (long double) if available...

'''
__all__ = [
    'finfo',
    'iinfo']
import warnings
from _utils import set_module
from _machar import MachAr
from  import numeric
from  import numerictypes as ntypes
from numeric import array, inf, NaN
from umath import log10, exp2, nextafter, isnan

def _fr0(a):
    '''fix rank-0 --> rank-1'''
    if a.ndim == 0:
        a = a.copy()
        a.shape = (1,)
    return a


def _fr1(a):
    '''fix rank > 0 --> rank-0'''
    if a.size == 1:
        a = a.copy()
        a.shape = ()
    return a


class MachArLike:
    ''' Object to simulate MachAr instance '''
    
    def __init__(self = None, ftype = {
        'smallest_subnormal': None }, *, eps, epsneg, huge, tiny, ibeta, smallest_subnormal, **kwargs):
        self.params = _MACHAR_PARAMS[ftype]
        self.ftype = ftype
        self.title = self.params['title']
        if not smallest_subnormal:
            self._smallest_subnormal = nextafter(self.ftype(0), self.ftype(1), dtype = self.ftype)
        else:
            self._smallest_subnormal = smallest_subnormal
        self.epsilon = self._float_to_float(eps)
        self.eps = self._float_to_float(eps)
        self.epsneg = self._float_to_float(epsneg)
        self.xmax = self._float_to_float(huge)
        self.huge = self._float_to_float(huge)
        self.xmin = self._float_to_float(tiny)
        self.smallest_normal = self._float_to_float(tiny)
        self.tiny = self._float_to_float(tiny)
        self.ibeta = self.params['itype'](ibeta)
        self.__dict__.update(kwargs)
        self.precision = int(-log10(self.eps))
        self.resolution = self._float_to_float(self._float_conv(10) ** (-(self.precision)))
        self._str_eps = self._float_to_str(self.eps)
        self._str_epsneg = self._float_to_str(self.epsneg)
        self._str_xmin = self._float_to_str(self.xmin)
        self._str_xmax = self._float_to_str(self.xmax)
        self._str_resolution = self._float_to_str(self.resolution)
        self._str_smallest_normal = self._float_to_str(self.xmin)

    smallest_subnormal = (lambda self: value = self._smallest_subnormalif self.ftype(0) == value:
warnings.warn('The value of the smallest subnormal for {} type is zero.'.format(self.ftype), UserWarning, stacklevel = 2)self._float_to_float(value))()
    _str_smallest_subnormal = (lambda self: self._float_to_str(self.smallest_subnormal))()
    
    def _float_to_float(self, value):
        '''Converts float to float.

        Parameters
        ----------
        value : float
            value to be converted.
        '''
        return _fr1(self._float_conv(value))

    
    def _float_conv(self, value):
        '''Converts float to conv.

        Parameters
        ----------
        value : float
            value to be converted.
        '''
        return array([
            value], self.ftype)

    
    def _float_to_str(self, value):
        '''Converts float to str.

        Parameters
        ----------
        value : float
            value to be converted.
        '''
        return self.params['fmt'] % array(_fr0(value)[0], self.ftype)


_convert_to_float = {
    ntypes.clongfloat: ntypes.longfloat,
    ntypes.complex_: ntypes.float_,
    ntypes.csingle: ntypes.single }
_title_fmt = 'numpy {} precision floating point number'
_MACHAR_PARAMS = {
    ntypes.half: dict(itype = ntypes.int16, fmt = '%12.5e', title = _title_fmt.format('half')),
    ntypes.longdouble: dict(itype = ntypes.longlong, fmt = '%s', title = _title_fmt.format('long double')),
    ntypes.single: dict(itype = ntypes.int32, fmt = '%15.7e', title = _title_fmt.format('single')),
    ntypes.double: dict(itype = ntypes.int64, fmt = '%24.16e', title = _title_fmt.format('double')) }
_KNOWN_TYPES = { }

def _register_type(machar, bytepat):
    _KNOWN_TYPES[bytepat] = machar

_float_ma = { }

def _register_known_types():

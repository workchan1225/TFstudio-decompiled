# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _ufunc_config.pyc (Python 3.11)

'''
Functions for changing global ufunc configuration

This provides helpers which wrap `umath.geterrobj` and `umath.seterrobj`
'''
import collections.abc as collections
import contextlib
import contextvars
from _utils import set_module
from umath import UFUNC_BUFSIZE_DEFAULT, ERR_IGNORE, ERR_WARN, ERR_RAISE, ERR_CALL, ERR_PRINT, ERR_LOG, ERR_DEFAULT, SHIFT_DIVIDEBYZERO, SHIFT_OVERFLOW, SHIFT_UNDERFLOW, SHIFT_INVALID
from  import umath
__all__ = [
    'seterr',
    'geterr',
    'setbufsize',
    'getbufsize',
    'seterrcall',
    'geterrcall',
    'errstate',
    '_no_nep50_warning']
_errdict = {
    'ignore': ERR_IGNORE,
    'warn': ERR_WARN,
    'raise': ERR_RAISE,
    'call': ERR_CALL,
    'print': ERR_PRINT,
    'log': ERR_LOG }
_errdict_rev = _errdict.items()()
seterr = (lambda all, divide, over, under, invalid = (None, None, None, None, None): pyvals = umath.geterrobj()old = geterr()# WARNING: Decompyle incomplete
)()
geterr = (lambda : maskvalue = umath.geterrobj()[1]mask = 7res = { }val = maskvalue >> SHIFT_DIVIDEBYZERO & maskres['divide'] = _errdict_rev[val]val = maskvalue >> SHIFT_OVERFLOW & maskres['over'] = _errdict_rev[val]val = maskvalue >> SHIFT_UNDERFLOW & maskres['under'] = _errdict_rev[val]val = maskvalue >> SHIFT_INVALID & maskres['invalid'] = _errdict_rev[val]res)()
setbufsize = (lambda size: if size > 1e+07:
raise ValueError('Buffer size, %s, is too big.' % size)if size < 5:
raise ValueError('Buffer size, %s, is too small.' % size)if size % 16 != 0:
raise ValueError('Buffer size, %s, is not a multiple of 16.' % size)pyvals = umath.geterrobj()old = getbufsize()pyvals[0] = sizeumath.seterrobj(pyvals)old)()
getbufsize = (lambda : umath.geterrobj()[0])()
seterrcall = (lambda func: pass# WARNING: Decompyle incomplete
)()
geterrcall = (lambda : umath.geterrobj()[2])()

class _unspecified:
    pass

_Unspecified = _unspecified()
errstate = <NODE:12>()

def _setdef():
    defval = [
        UFUNC_BUFSIZE_DEFAULT,
        ERR_DEFAULT,
        None]
    umath.seterrobj(defval)

_setdef()
NO_NEP50_WARNING = contextvars.ContextVar('_no_nep50_warning', default = False)
_no_nep50_warning = (lambda : pass# WARNING: Decompyle incomplete
)()()

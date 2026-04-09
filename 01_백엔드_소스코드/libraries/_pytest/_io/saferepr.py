# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: saferepr.pyc (Python 3.11)

from __future__ import annotations
import pprint
import reprlib

def _try_repr_or_str(obj = None):
    
    try:
        return repr(obj)
    except (KeyboardInterrupt, SystemExit):
        raise 
        except BaseException:
            return 



def _format_repr_exception(exc = None, obj = None):
    
    try:
        exc_info = _try_repr_or_str(exc)
    except (KeyboardInterrupt, SystemExit):
        raise 
        except BaseException:
            inner_exc = None
            exc_info = f'''unpresentable exception ({_try_repr_or_str(inner_exc)})'''
            inner_exc = None
            del inner_exc
        except:
            inner_exc = None
            del inner_exc
        return f'''<[{exc_info} raised in repr()] {type(obj).__name__} object at 0x{id(obj):x}>'''



def _ellipsize(s = None, maxsize = None):
    if len(s) > maxsize:
        i = max(0, (maxsize - 3) // 2)
        j = max(0, maxsize - 3 - i)
        return s[:i] + '...' + s[len(s) - j:]


class SafeRepr(reprlib.Repr):
    pass
# WARNING: Decompyle incomplete


def safeformat(obj = None):
    '''Return a pretty printed string for the given object.

    Failing __repr__ functions of user instances will be represented
    with a short exception info.
    '''
    
    try:
        return pprint.pformat(obj)
    except Exception:
        exc = None
        del exc
        return None
        None = 
        del exc


DEFAULT_REPR_MAX_SIZE = 240

def saferepr(obj = None, maxsize = None, use_ascii = None):
    """Return a size-limited safe repr-string for the given object.

    Failing __repr__ functions of user instances will be represented
    with a short exception info and 'saferepr' generally takes
    care to never raise exceptions itself.

    This function is a wrapper around the Repr/reprlib functionality of the
    stdlib.
    """
    return SafeRepr(maxsize, use_ascii).repr(obj)


def saferepr_unlimited(obj = None, use_ascii = None):
    '''Return an unlimited-size safe repr-string for the given object.

    As with saferepr, failing __repr__ functions of user instances
    will be represented with a short exception info.

    This function is a wrapper around simple repr.

    Note: a cleaner solution would be to alter ``saferepr``this way
    when maxsize=None, but that might affect some other code.
    '''
    
    try:
        if use_ascii:
            return ascii(obj)
        return None(obj)
    except Exception:
        exc = None
        del exc
        return None
        None = 
        del exc

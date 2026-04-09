# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: function_base.pyc (Python 3.11)

import functools
import warnings
import operator
import types
import numpy as np
from  import numeric as _nx
from numeric import result_type, NaN, asanyarray, ndim
from numpy.core.multiarray import add_docstring
from numpy.core import overrides
__all__ = [
    'logspace',
    'linspace',
    'geomspace']
array_function_dispatch = functools.partial(overrides.array_function_dispatch, module = 'numpy')

def _linspace_dispatcher(start, stop, num, endpoint, retstep, dtype, axis = (None, None, None, None, None)):
    return (start, stop)

linspace = (lambda start, stop, num, endpoint, retstep, dtype, axis = (50, True, False, None, 0): num = operator.index(num)if num < 0:
raise ValueError('Number of samples, %s, must be non-negative.' % num)div = num - 1 if endpoint else numstart = asanyarray(start) * 1stop = asanyarray(stop) * 1dt = result_type(start, stop, float(num))# WARNING: Decompyle incomplete
)()

def _logspace_dispatcher(start, stop, num, endpoint, base, dtype, axis = (None, None, None, None, None)):
    return (start, stop, base)

logspace = (lambda start, stop, num, endpoint, base, dtype, axis = (50, True, 10, None, 0): pass# WARNING: Decompyle incomplete
)()

def _geomspace_dispatcher(start, stop, num, endpoint, dtype, axis = (None, None, None, None)):
    return (start, stop)

geomspace = (lambda start, stop, num, endpoint, dtype, axis = (50, True, None, 0): start = asanyarray(start)stop = asanyarray(stop)if _nx.any(start == 0) or _nx.any(stop == 0):
raise ValueError('Geometric sequence cannot include zero')dt = result_type(start, stop, float(num), _nx.zeros((), dtype))# WARNING: Decompyle incomplete
)()

def _needs_add_docstring(obj):
    '''
    Returns true if the only way to set the docstring of `obj` from python is
    via add_docstring.

    This function errs on the side of being overly conservative.
    '''
    Py_TPFLAGS_HEAPTYPE = 512
    if isinstance(obj, (types.FunctionType, types.MethodType, property)):
        return False
    if None(obj, type) and obj.__flags__ & Py_TPFLAGS_HEAPTYPE:
        return False


def _add_docstring(obj, doc, warn_on_python):
    if not warn_on_python and _needs_add_docstring(obj):
        warnings.warn('add_newdoc was used on a pure-python object {}. Prefer to attach it directly to the source.'.format(obj), UserWarning, stacklevel = 3)
    
    try:
        add_docstring(obj, doc)
        return None
    except Exception:
        return None



def add_newdoc(place, obj, doc, warn_on_python = (True,)):
    """
    Add documentation to an existing object, typically one defined in C

    The purpose is to allow easier editing of the docstrings without requiring
    a re-compile. This exists primarily for internal use within numpy itself.

    Parameters
    ----------
    place : str
        The absolute name of the module to import from
    obj : str
        The name of the object to add documentation to, typically a class or
        function name
    doc : {str, Tuple[str, str], List[Tuple[str, str]]}
        If a string, the documentation to apply to `obj`

        If a tuple, then the first element is interpreted as an attribute of
        `obj` and the second as the docstring to apply - ``(method, docstring)``

        If a list, then each element of the list should be a tuple of length
        two - ``[(method1, docstring1), (method2, docstring2), ...]``
    warn_on_python : bool
        If True, the default, emit `UserWarning` if this is used to attach
        documentation to a pure-python object.

    Notes
    -----
    This routine never raises an error if the docstring can't be written, but
    will raise an error if the object being documented does not exist.

    This routine cannot modify read-only docstrings, as appear
    in new-style classes or built-in functions. Because this
    routine never raises an error the caller must check manually
    that the docstrings were changed.

    Since this function grabs the ``char *`` from a c-level str object and puts
    it into the ``tp_doc`` slot of the type of `obj`, it violates a number of
    C-API best-practices, by:

    - modifying a `PyTypeObject` after calling `PyType_Ready`
    - calling `Py_INCREF` on the str and losing the reference, so the str
      will never be released

    If possible it should be avoided.
    """
    new = getattr(__import__(place, globals(), { }, [
        obj]), obj)
    if isinstance(doc, str):
        _add_docstring(new, doc.strip(), warn_on_python)
        return None
    if None(doc, tuple):
        (attr, docstring) = doc
        _add_docstring(getattr(new, attr), docstring.strip(), warn_on_python)
        return None
    if None(doc, list):
        for attr, docstring in doc:
            _add_docstring(getattr(new, attr), docstring.strip(), warn_on_python)
            return None
            return None

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: utils.pyc (Python 3.11)

import os
import sys
import textwrap
import types
import re
import warnings
import functools
import platform
from _utils import set_module
from numpy.core.numerictypes import issubclass_, issubsctype, issubdtype
from numpy.core import ndarray, ufunc, asarray
import numpy as np
__all__ = [
    'issubclass_',
    'issubsctype',
    'issubdtype',
    'deprecate',
    'deprecate_with_doc',
    'get_include',
    'info',
    'source',
    'who',
    'lookfor',
    'byte_bounds',
    'safe_eval',
    'show_runtime']

def show_runtime():
    '''
    Print information about various resources in the system
    including available intrinsic support and BLAS/LAPACK library
    in use

    .. versionadded:: 1.24.0

    See Also
    --------
    show_config : Show libraries in the system on which NumPy was built.

    Notes
    -----
    1. Information is derived with the help of `threadpoolctl <https://pypi.org/project/threadpoolctl/>`_
       library if available.
    2. SIMD related information is derived from ``__cpu_features__``,
       ``__cpu_baseline__`` and ``__cpu_dispatch__``

    '''
    __cpu_features__ = __cpu_features__
    __cpu_baseline__ = __cpu_baseline__
    __cpu_dispatch__ = __cpu_dispatch__
    import numpy.core._multiarray_umath
    pprint = pprint
    import pprint
    config_found = [
        {
            'numpy_version': np.__version__,
            'python': sys.version,
            'uname': platform.uname() }]
    features_not_found = []
    features_found = []
    for feature in __cpu_dispatch__:
        if __cpu_features__[feature]:
            features_found.append(feature)
            continue
        features_not_found.append(feature)
        config_found.append({
            'simd_extensions': {
                'baseline': __cpu_baseline__,
                'found': features_found,
                'not_found': features_not_found } })
        
        try:
            threadpool_info = threadpool_info
            import threadpoolctl
            config_found.extend(threadpool_info())
        except ImportError:
            print('WARNING: `threadpoolctl` not found in system! Install it by `pip install threadpoolctl`. Once installed, try `np.show_runtime` again for more detailed build information')

        pprint(config_found)
        return None


def get_include():
    """
    Return the directory that contains the NumPy \\*.h header files.

    Extension modules that need to compile against NumPy should use this
    function to locate the appropriate include directory.

    Notes
    -----
    When using ``distutils``, for example in ``setup.py``::

        import numpy as np
        ...
        Extension('extension_name', ...
                include_dirs=[np.get_include()])
        ...

    """
    import numpy
# WARNING: Decompyle incomplete


class _Deprecate:
    '''
    Decorator class to deprecate old functions.

    Refer to `deprecate` for details.

    See Also
    --------
    deprecate

    '''
    
    def __init__(self, old_name, new_name, message = (None, None, None)):
        self.old_name = old_name
        self.new_name = new_name
        self.message = message

    
    def __call__(self, func, *args, **kwargs):
        '''
        Decorator call.  Refer to ``decorate``.

        '''
        pass
    # WARNING: Decompyle incomplete



def _get_indent(lines):
    '''
    Determines the leading whitespace that could be removed from all the lines.
    '''
    indent = sys.maxsize
    for line in lines:
        content = len(line.lstrip())
        if content:
            indent = min(indent, len(line) - content)
        if indent == sys.maxsize:
            indent = 0
    return indent


def deprecate(*args, **kwargs):
    """
    Issues a DeprecationWarning, adds warning to `old_name`'s
    docstring, rebinds ``old_name.__name__`` and returns the new
    function object.

    This function may also be used as a decorator.

    Parameters
    ----------
    func : function
        The function to be deprecated.
    old_name : str, optional
        The name of the function to be deprecated. Default is None, in
        which case the name of `func` is used.
    new_name : str, optional
        The new name for the function. Default is None, in which case the
        deprecation message is that `old_name` is deprecated. If given, the
        deprecation message is that `old_name` is deprecated and `new_name`
        should be used instead.
    message : str, optional
        Additional explanation of the deprecation.  Displayed in the
        docstring after the warning.

    Returns
    -------
    old_func : function
        The deprecated function.

    Examples
    --------
    Note that ``olduint`` returns a value after printing Deprecation
    Warning:

    >>> olduint = np.deprecate(np.uint)
    DeprecationWarning: `uint64` is deprecated! # may vary
    >>> olduint(6)
    6

    """
    pass
# WARNING: Decompyle incomplete


def deprecate_with_doc(msg):
    """
    Deprecates a function and includes the deprecation in its docstring.

    This function is used as a decorator. It returns an object that can be
    used to issue a DeprecationWarning, by passing the to-be decorated
    function as argument, this adds warning to the to-be decorated function's
    docstring and returns the new function object.

    See Also
    --------
    deprecate : Decorate a function such that it issues a `DeprecationWarning`

    Parameters
    ----------
    msg : str
        Additional explanation of the deprecation. Displayed in the
        docstring after the warning.

    Returns
    -------
    obj : object

    """
    return _Deprecate(message = msg)


def byte_bounds(a):
    """
    Returns pointers to the end-points of an array.

    Parameters
    ----------
    a : ndarray
        Input array. It must conform to the Python-side of the array
        interface.

    Returns
    -------
    (low, high) : tuple of 2 integers
        The first integer is the first byte of the array, the second
        integer is just past the last byte of the array.  If `a` is not
        contiguous it will not use every byte between the (`low`, `high`)
        values.

    Examples
    --------
    >>> I = np.eye(2, dtype='f'); I.dtype
    dtype('float32')
    >>> low, high = np.byte_bounds(I)
    >>> high - low == I.size*I.itemsize
    True
    >>> I = np.eye(2); I.dtype
    dtype('float64')
    >>> low, high = np.byte_bounds(I)
    >>> high - low == I.size*I.itemsize
    True

    """
    ai = a.__array_interface__
    a_data = ai['data'][0]
    astrides = ai['strides']
    ashape = ai['shape']
    bytes_a = asarray(a).dtype.itemsize
    a_low = a_data
    a_high = a_data
# WARNING: Decompyle incomplete


def who(vardict = (None,)):
    """
    Print the NumPy arrays in the given dictionary.

    If there is no dictionary passed in or `vardict` is None then returns
    NumPy arrays in the globals() dictionary (all NumPy arrays in the
    namespace).

    Parameters
    ----------
    vardict : dict, optional
        A dictionary possibly containing ndarrays.  Default is globals().

    Returns
    -------
    out : None
        Returns 'None'.

    Notes
    -----
    Prints out the name, shape, bytes and type of all of the ndarrays
    present in `vardict`.

    Examples
    --------
    >>> a = np.arange(10)
    >>> b = np.ones(20)
    >>> np.who()
    Name            Shape            Bytes            Type
    ===========================================================
    a               10               80               int64
    b               20               160              float64
    Upper bound on total bytes  =       240

    >>> d = {'x': np.arange(2.0), 'y': np.arange(3.0), 'txt': 'Some str',
    ... 'idx':5}
    >>> np.who(d)
    Name            Shape            Bytes            Type
    ===========================================================
    x               2                16               float64
    y               3                24               float64
    Upper bound on total bytes  =       40

    """
    pass
# WARNING: Decompyle incomplete


def _split_line(name, arguments, width):
    firstwidth = len(name)
    k = firstwidth
    newstr = name
    sepstr = ', '
    arglist = arguments.split(sepstr)
    for argument in arglist:
        if k == firstwidth:
            addstr = ''
        else:
            addstr = sepstr
        k = k + len(argument) + len(addstr)
        if k > width:
            k = firstwidth + 1 + len(argument)
            newstr = newstr + ',\n' + ' ' * (firstwidth + 2) + argument
            continue
        newstr = newstr + addstr + argument
        return newstr

_namedict = None
_dictlist = None

def _makenamedict(module = ('numpy',)):
    module = __import__(module, globals(), locals(), [])
    thedict = {
        module.__name__: module.__dict__ }
    dictlist = [
        module.__name__]
    totraverse = [
        module.__dict__]
    if len(totraverse) == 0:
        pass
    else:
        thisdict = totraverse.pop(0)
        for x in thisdict.keys():
            if isinstance(thisdict[x], types.ModuleType):
                modname = thisdict[x].__name__
                if modname not in dictlist:
                    moddict = thisdict[x].__dict__
                    dictlist.append(modname)
                    totraverse.append(moddict)
                    thedict[modname] = moddict
            return (thedict, dictlist)


def _info(obj, output = (None,)):
    '''Provide information about ndarray obj.

    Parameters
    ----------
    obj : ndarray
        Must be ndarray, not checked.
    output
        Where printed output goes.

    Notes
    -----
    Copied over from the numarray module prior to its removal.
    Adapted somewhat as only numpy is an option now.

    Called by info.

    '''
    extra = ''
    tic = ''
    
    bp = lambda x: x
    cls = getattr(obj, '__class__', type(obj))
    nm = getattr(cls, '__name__', cls)
    strides = obj.strides
    endian = obj.dtype.byteorder
# WARNING: Decompyle incomplete

info = (lambda object, maxwidth, output, toplevel = (None, 76, None, 'numpy'): import pydocimport inspectif hasattr(object, '_ppimport_importer') or hasattr(object, '_ppimport_module'):
object = object._ppimport_moduleelif hasattr(object, '_ppimport_attr'):
object = object._ppimport_attr# WARNING: Decompyle incomplete
)()
source = (lambda object, output = (sys.stdout,): import inspecttry:
print('In file: %s\n' % inspect.getsourcefile(object), file = output)print(inspect.getsource(object), file = output)Noneexcept Exception:
print('Not available for this object.', file = output)None)()
_lookfor_caches = { }
_function_signature_re = re.compile('[a-z0-9_]+\\(.*[,=].*\\)', re.I)
lookfor = (lambda what, module, import_modules, regenerate, output = (None, True, False, None): pass# WARNING: Decompyle incomplete
)()

def _lookfor_generate_cache(module, import_modules, regenerate):
    '''
    Generate docstring cache for given module.

    Parameters
    ----------
    module : str, None, module
        Module for which to generate docstring cache
    import_modules : bool
        Whether to import sub-modules in packages.
    regenerate : bool
        Re-generate the docstring cache

    Returns
    -------
    cache : dict {obj_full_name: (docstring, kind, index), ...}
        Docstring cache for the module, either cached one (regenerate=False)
        or newly generated.

    '''
    import inspect
    StringIO = StringIO
    import io
# WARNING: Decompyle incomplete


def _getmembers(item):
    pass
# WARNING: Decompyle incomplete


def safe_eval(source):
    '''
    Protected string evaluation.

    Evaluate a string containing a Python literal expression without
    allowing the execution of arbitrary non-literal code.

    .. warning::

        This function is identical to :py:meth:`ast.literal_eval` and
        has the same security implications.  It may not always be safe
        to evaluate large input strings.

    Parameters
    ----------
    source : str
        The string to evaluate.

    Returns
    -------
    obj : object
       The result of evaluating `source`.

    Raises
    ------
    SyntaxError
        If the code has invalid Python syntax, or if it contains
        non-literal code.

    Examples
    --------
    >>> np.safe_eval(\'1\')
    1
    >>> np.safe_eval(\'[1, 2, 3]\')
    [1, 2, 3]
    >>> np.safe_eval(\'{"foo": ("bar", 10.0)}\')
    {\'foo\': (\'bar\', 10.0)}

    >>> np.safe_eval(\'import os\')
    Traceback (most recent call last):
      ...
    SyntaxError: invalid syntax

    >>> np.safe_eval(\'open("/home/user/.ssh/id_dsa").read()\')
    Traceback (most recent call last):
      ...
    ValueError: malformed node or string: <_ast.Call object at 0x...>

    '''
    import ast
    return ast.literal_eval(source)


def _median_nancheck(data, result, axis):
    '''
    Utility function to check median result from data for NaN values at the end
    and return NaN in that case. Input result can also be a MaskedArray.

    Parameters
    ----------
    data : array
        Sorted input data to median function
    result : Array or MaskedArray
        Result of median function.
    axis : int
        Axis along which the median was computed.

    Returns
    -------
    result : scalar or ndarray
        Median or NaN in axes which contained NaN in the input.  If the input
        was an array, NaN will be inserted in-place.  If a scalar, either the
        input itself or a scalar NaN.
    '''
    if data.size == 0:
        return result
    potential_nans = None.take(-1, axis = axis)
    n = np.isnan(potential_nans)
    if np.ma.isMaskedArray(n):
        n = n.filled(False)
    if not n.any():
        return result
    if None(result, np.generic):
        return potential_nans
    None.copyto(result, potential_nans, where = n)
    return result


def _opt_info():
    '''
    Returns a string contains the supported CPU features by the current build.

    The string format can be explained as follows:
        - dispatched features that are supported by the running machine
          end with `*`.
        - dispatched features that are "not" supported by the running machine
          end with `?`.
        - remained features are representing the baseline.
    '''
    __cpu_features__ = __cpu_features__
    __cpu_baseline__ = __cpu_baseline__
    __cpu_dispatch__ = __cpu_dispatch__
    import numpy.core._multiarray_umath
    if len(__cpu_baseline__) == 0 and len(__cpu_dispatch__) == 0:
        return ''
    enabled_features = None.join(__cpu_baseline__)
    for feature in __cpu_dispatch__:
        if __cpu_features__[feature]:
            enabled_features += f''' {feature}*'''
            continue
        enabled_features += f''' {feature}?'''
        return enabled_features


def drop_metadata(dtype):
    '''
    Returns the dtype unchanged if it contained no metadata or a copy of the
    dtype if it (or any of its structure dtypes) contained metadata.

    This utility is used by `np.save` and `np.savez` to drop metadata before
    saving.

    .. note::

        Due to its limitation this function may move to a more appropriate
        home or change in the future and is considered semi-public API only.

    .. warning::

        This function does not preserve more strange things like record dtypes
        and user dtypes may simply return the wrong thing.  If you need to be
        sure about the latter, check the result with:
        ``np.can_cast(new_dtype, dtype, casting="no")``.

    '''
    pass
# WARNING: Decompyle incomplete

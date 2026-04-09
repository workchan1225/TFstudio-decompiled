# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: stride_tricks.pyc (Python 3.11)

'''
Utilities that manipulate strides to achieve desirable effects.

An explanation of strides can be found in the "ndarray.rst" file in the
NumPy reference guide.

'''
import numpy as np
from numpy.core.numeric import normalize_axis_tuple
from numpy.core.overrides import array_function_dispatch, set_module
__all__ = [
    'broadcast_to',
    'broadcast_arrays',
    'broadcast_shapes']

class DummyArray:
    '''Dummy object that just exists to hang __array_interface__ dictionaries
    and possibly keep alive a reference to a base array.
    '''
    
    def __init__(self, interface, base = (None,)):
        self.__array_interface__ = interface
        self.base = base



def _maybe_view_as_subclass(original_array, new_array):
    if type(original_array) is not type(new_array):
        new_array = new_array.view(type = type(original_array))
        if new_array.__array_finalize__:
            new_array.__array_finalize__(original_array)
    return new_array


def as_strided(x, shape, strides, subok, writeable = (None, None, False, True)):
    '''
    Create a view into the array with the given shape and strides.

    .. warning:: This function has to be used with extreme care, see notes.

    Parameters
    ----------
    x : ndarray
        Array to create a new.
    shape : sequence of int, optional
        The shape of the new array. Defaults to ``x.shape``.
    strides : sequence of int, optional
        The strides of the new array. Defaults to ``x.strides``.
    subok : bool, optional
        .. versionadded:: 1.10

        If True, subclasses are preserved.
    writeable : bool, optional
        .. versionadded:: 1.12

        If set to False, the returned array will always be readonly.
        Otherwise it will be writable if the original array was. It
        is advisable to set this to False if possible (see Notes).

    Returns
    -------
    view : ndarray

    See also
    --------
    broadcast_to : broadcast an array to a given shape.
    reshape : reshape an array.
    lib.stride_tricks.sliding_window_view :
        userfriendly and safe function for the creation of sliding window views.

    Notes
    -----
    ``as_strided`` creates a view into the array given the exact strides
    and shape. This means it manipulates the internal data structure of
    ndarray and, if done incorrectly, the array elements can point to
    invalid memory and can corrupt results or crash your program.
    It is advisable to always use the original ``x.strides`` when
    calculating new strides to avoid reliance on a contiguous memory
    layout.

    Furthermore, arrays created with this function often contain self
    overlapping memory, so that two elements are identical.
    Vectorized write operations on such arrays will typically be
    unpredictable. They may even give different results for small, large,
    or transposed arrays.

    Since writing to these arrays has to be tested and done with great
    care, you may want to use ``writeable=False`` to avoid accidental write
    operations.

    For these reasons it is advisable to avoid ``as_strided`` when
    possible.
    '''
    x = np.array(x, copy = False, subok = subok)
    interface = dict(x.__array_interface__)
# WARNING: Decompyle incomplete


def _sliding_window_view_dispatcher(x = None, window_shape = (None,), axis = {
    'subok': None,
    'writeable': None }, *, subok, writeable):
    return (x,)

sliding_window_view = (lambda x = array_function_dispatch(_sliding_window_view_dispatcher), window_shape = (None,), axis = {
    'subok': False,
    'writeable': False }, *, subok, writeable, window_shape_array = None: pass# WARNING: Decompyle incomplete
)()

def _broadcast_to(array, shape, subok, readonly):
    shape = tuple(shape) if np.iterable(shape) else (shape,)
    array = np.array(array, copy = False, subok = subok)
    if shape and array.shape:
        raise ValueError('cannot broadcast a non-scalar to a scalar array')
    if (lambda .0: pass# WARNING: Decompyle incomplete
)(shape()):
        raise ValueError('all elements of broadcast shape must be non-negative')
    extras = []
    it = np.nditer((array,), flags = [
        'multi_index',
        'refs_ok',
        'zerosize_ok'] + extras, op_flags = [
        'readonly'], itershape = shape, order = 'C')
    it
    broadcast = it.itviews[0]
    None(None, None)


def _broadcast_to_dispatcher(array, shape, subok = (None,)):
    return (array,)

broadcast_to = (lambda array, shape, subok = (False,): _broadcast_to(array, shape, subok = subok, readonly = True))()

def _broadcast_shape(*args):
    '''Returns the shape of the arrays that would result from broadcasting the
    supplied arrays against each other.
    '''
    pass
# WARNING: Decompyle incomplete

broadcast_shapes = (lambda : arrays = args()# WARNING: Decompyle incomplete
)()

def _broadcast_arrays_dispatcher(*, subok, *args):
    return args

broadcast_arrays = (lambda *: pass# WARNING: Decompyle incomplete
)()

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _at.pyc (Python 3.11)

'''Update operations for read-only arrays.'''
from __future__ import annotations
import operator
from collections.abc import Callable
from enum import Enum
from types import ModuleType
from typing import TYPE_CHECKING, ClassVar, cast
from _utils import _compat
from _utils._compat import array_namespace, is_dask_array, is_jax_array, is_torch_array, is_writeable_array
from _utils._helpers import meta_namespace
from _utils._typing import Array, SetIndex
if TYPE_CHECKING:
    from typing_extensions import Self

class _AtOp(Enum):
    '''Operations for use in `xpx.at`.'''
    SET = 'set'
    ADD = 'add'
    SUBTRACT = 'subtract'
    MULTIPLY = 'multiply'
    DIVIDE = 'divide'
    POWER = 'power'
    MIN = 'min'
    MAX = 'max'
    
    def __str__(self = None):
        """
        Return string representation (useful for pytest logs).

        Returns
        -------
        str
            The operation's name.
        """
        return self.value



class Undef(Enum):
    '''Sentinel for undefined values.'''
    UNDEF = 0

_undef = Undef.UNDEF

class at:
    _idx: 'SetIndex | Undef' = "\n    Update operations for read-only arrays.\n\n    This implements ``jax.numpy.ndarray.at`` for all writeable\n    backends (those that support ``__setitem__``) and routes\n    to the ``.at[]`` method for JAX arrays.\n\n    Parameters\n    ----------\n    x : array\n        Input array.\n    idx : index, optional\n        Only `array API standard compliant indices\n        <https://data-apis.org/array-api/latest/API_specification/indexing.html>`_\n        are supported.\n\n        You may use two alternate syntaxes::\n\n          >>> import array_api_extra as xpx\n          >>> xpx.at(x, idx).set(value)  # or add(value), etc.\n          >>> xpx.at(x)[idx].set(value)\n\n    copy : bool, optional\n        None (default)\n            The array parameter *may* be modified in place if it is\n            possible and beneficial for performance.\n            You should not reuse it after calling this function.\n        True\n            Ensure that the inputs are not modified.\n        False\n            Ensure that the update operation writes back to the input.\n            Raise ``ValueError`` if a copy cannot be avoided.\n\n    xp : array_namespace, optional\n        The standard-compatible namespace for `x`. Default: infer.\n\n    Returns\n    -------\n    Updated input array.\n\n    Warnings\n    --------\n    (a) When you omit the ``copy`` parameter, you should never reuse the parameter\n    array later on; ideally, you should reassign it immediately::\n\n        >>> import array_api_extra as xpx\n        >>> x = xpx.at(x, 0).set(2)\n\n    The above best practice pattern ensures that the behaviour won't change depending\n    on whether ``x`` is writeable or not, as the original ``x`` object is dereferenced\n    as soon as ``xpx.at`` returns; this way there is no risk to accidentally update it\n    twice.\n\n    On the reverse, the anti-pattern below must be avoided, as it will result in\n    different behaviour on read-only versus writeable arrays::\n\n        >>> x = xp.asarray([0, 0, 0])\n        >>> y = xpx.at(x, 0).set(2)\n        >>> z = xpx.at(x, 1).set(3)\n\n    In the above example, both calls to ``xpx.at`` update ``x`` in place *if possible*.\n    This causes the behaviour to diverge depending on whether ``x`` is writeable or not:\n\n    - If ``x`` is writeable, then after the snippet above you'll have\n      ``x == y == z == [2, 3, 0]``\n    - If ``x`` is read-only, then you'll end up with\n      ``x == [0, 0, 0]``, ``y == [2, 0, 0]`` and ``z == [0, 3, 0]``.\n\n    The correct pattern to use if you want diverging outputs from the same input is\n    to enforce copies::\n\n        >>> x = xp.asarray([0, 0, 0])\n        >>> y = xpx.at(x, 0).set(2, copy=True)  # Never updates x\n        >>> z = xpx.at(x, 1).set(3)  # May or may not update x in place\n        >>> del x  # avoid accidental reuse of x as we don't know its state anymore\n\n    (b) The array API standard does not support integer array indices.\n    The behaviour of update methods when the index is an array of integers is\n    undefined and will vary between backends; this is particularly true when the\n    index contains multiple occurrences of the same index, e.g.::\n\n        >>> import numpy as np\n        >>> import jax.numpy as jnp\n        >>> import array_api_extra as xpx\n        >>> xpx.at(np.asarray([123]), np.asarray([0, 0])).add(1)\n        array([124])\n        >>> xpx.at(jnp.asarray([123]), jnp.asarray([0, 0])).add(1)\n        Array([125], dtype=int32)\n\n    See Also\n    --------\n    jax.numpy.ndarray.at : Equivalent array method in JAX.\n\n    Notes\n    -----\n    `sparse <https://sparse.pydata.org/>`_, as well as read-only arrays from libraries\n    not explicitly covered by ``array-api-compat``, are not supported by update\n    methods.\n\n    Boolean masks are supported on Dask and jitted JAX arrays exclusively\n    when `idx` has the same shape as `x` and `y` is 0-dimensional.\n    Note that this support is not available in JAX's native\n    ``x.at[mask].set(y)``.\n\n    This pattern::\n\n        >>> mask = m(x)\n        >>> x[mask] = f(x[mask])\n\n    Can't be replaced by `at`, as it won't work on Dask and JAX inside jax.jit::\n\n        >>> mask = m(x)\n        >>> x = xpx.at(x, mask).set(f(x[mask])  # Crash on Dask and jax.jit\n\n    You should instead use::\n\n        >>> x = xp.where(m(x), f(x), x)\n\n    Examples\n    --------\n    Given either of these equivalent expressions::\n\n      >>> import array_api_extra as xpx\n      >>> x = xpx.at(x)[1].add(2)\n      >>> x = xpx.at(x, 1).add(2)\n\n    If x is a JAX array, they are the same as::\n\n      >>> x = x.at[1].add(2)\n\n    If x is a read-only NumPy array, they are the same as::\n\n      >>> x = x.copy()\n      >>> x[1] += 2\n\n    For other known backends, they are the same as::\n\n      >>> x[1] += 2\n    "
    __slots__: 'ClassVar[tuple[str, ...]]' = ('_idx', '_x')
    
    def __init__(self = None, x = None, idx = None):
        self._x = x
        self._idx = idx

    
    def __getitem__(self = None, idx = None):
        '''
        Allow for the alternate syntax ``at(x)[start:stop:step]``.

        It looks prettier than ``at(x, slice(start, stop, step))``
        and feels more intuitive coming from the JAX documentation.
        '''
        if self._idx is not _undef:
            msg = 'Index has already been set'
            raise ValueError(msg)
        return type(self)(self._x, idx)

    
    def _op(self, at_op, in_place_op, out_of_place_op = None, y = None, copy = None, xp = ('copy', 'bool | None', 'xp', 'ModuleType | None', 'at_op', '_AtOp', 'in_place_op', 'Callable[[Array, Array | complex], Array] | None', 'out_of_place_op', 'Callable[[Array, Array], Array] | None', 'y', 'Array | complex', 'return', 'Array')):
        """
        Implement all update operations.

        Parameters
        ----------
        at_op : _AtOp
            Method of JAX's Array.at[].
        in_place_op : Callable[[Array, Array | complex], Array] | None
            In-place operation to apply on mutable backends::

                x[idx] = in_place_op(x[idx], y)

            If None::

                x[idx] = y

        out_of_place_op : Callable[[Array, Array], Array] | None
            Out-of-place operation to apply when idx is a boolean mask and the backend
            doesn't support in-place updates::

                x = xp.where(idx, out_of_place_op(x, y), x)

            If None::

                x = xp.where(idx, y, x)

        y : array or complex
            Right-hand side of the operation.
        copy : bool or None
            Whether to copy the input array. See the class docstring for details.
        xp : array_namespace, optional
            The array namespace for the input array. Default: infer.

        Returns
        -------
        Array
            Updated `x`.
        """
        apply_where = apply_where
        import _funcs
        idx = self._idx
        x = self._x
    # WARNING: Decompyle incomplete

    
    def set(self = None, y = None, copy = None, xp = (None, None)):
        '''Apply ``x[idx] = y`` and return the update array.'''
        return self._op(_AtOp.SET, None, None, y, copy = copy, xp = xp)

    
    def add(self = None, y = None, copy = None, xp = (None, None)):
        '''Apply ``x[idx] += y`` and return the updated array.'''
        return self._op(_AtOp.ADD, operator.iadd, operator.add, y, copy = copy, xp = xp)

    
    def subtract(self = None, y = None, copy = None, xp = (None, None)):
        '''Apply ``x[idx] -= y`` and return the updated array.'''
        return self._op(_AtOp.SUBTRACT, operator.isub, operator.sub, y, copy = copy, xp = xp)

    
    def multiply(self = None, y = None, copy = None, xp = (None, None)):
        '''Apply ``x[idx] *= y`` and return the updated array.'''
        return self._op(_AtOp.MULTIPLY, operator.imul, operator.mul, y, copy = copy, xp = xp)

    
    def divide(self = None, y = None, copy = None, xp = (None, None)):
        '''Apply ``x[idx] /= y`` and return the updated array.'''
        return self._op(_AtOp.DIVIDE, operator.itruediv, operator.truediv, y, copy = copy, xp = xp)

    
    def power(self = None, y = None, copy = None, xp = (None, None)):
        '''Apply ``x[idx] **= y`` and return the updated array.'''
        return self._op(_AtOp.POWER, operator.ipow, operator.pow, y, copy = copy, xp = xp)

    
    def min(self = None, y = None, copy = None, xp = (None, None)):
        '''Apply ``x[idx] = minimum(x[idx], y)`` and return the updated array.'''
        pass
    # WARNING: Decompyle incomplete

    
    def max(self = None, y = None, copy = None, xp = (None, None)):
        '''Apply ``x[idx] = maximum(x[idx], y)`` and return the updated array.'''
        pass
    # WARNING: Decompyle incomplete

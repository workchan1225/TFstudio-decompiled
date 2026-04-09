# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: blocks.pyc (Python 3.11)

from __future__ import annotations
import inspect
import re
from typing import TYPE_CHECKING, Any, Literal, Self, cast, final
import warnings
import numpy as np
from pandas._libs import NaT, internals as libinternals, lib
from pandas._libs.internals import BlockPlacement, BlockValuesRefs
from pandas._libs.missing import NA
from pandas.errors import AbstractMethodError, OutOfBoundsDatetime, Pandas4Warning
from pandas.util._decorators import cache_readonly
from pandas.util._exceptions import find_stack_level
from pandas.util._validators import validate_bool_kwarg
from pandas.core.dtypes.astype import astype_array_safe, astype_is_view
from pandas.core.dtypes.cast import LossySetitemError, can_hold_element, convert_dtypes, find_result_type, np_can_hold_element
from pandas.core.dtypes.common import is_1d_only_ea_dtype, is_float_dtype, is_integer_dtype, is_list_like, is_scalar, is_string_dtype
from pandas.core.dtypes.dtypes import DatetimeTZDtype, ExtensionDtype, IntervalDtype, NumpyEADtype, PeriodDtype
from pandas.core.dtypes.generic import ABCDataFrame, ABCIndex, ABCNumpyExtensionArray, ABCSeries
from pandas.core.dtypes.inference import is_re
from pandas.core.dtypes.missing import is_valid_na_for_dtype, isna, na_value_for_dtype
from pandas.core import missing

algorithms
from pandas.core.array_algos.putmask import extract_bool_array, putmask_inplace, putmask_without_repeat, setitem_datetimelike_compat, validate_putmask
putmask_inplace = putmask_inplace
putmask_without_repeat = putmask_without_repeat
setitem_datetimelike_compat = setitem_datetimelike_compat
validate_putmask = validate_putmask
import pandas.core.algorithms, core
from pandas.core.array_algos.quantile import quantile_compat
from pandas.core.array_algos.replace import compare_or_regex_search, replace_regex, should_use_regex
from pandas.core.array_algos.transforms import shift
from pandas.core.arrays import DatetimeArray, ExtensionArray, IntervalArray, NumpyExtensionArray, PeriodArray, TimedeltaArray
from pandas.core.arrays.string_ import StringDtype
from pandas.core.base import PandasObject

common
from pandas.core.computation import expressions
import pandas.core.common, core
from pandas.core.construction import ensure_wrapped_if_datetimelike, extract_array
from pandas.core.indexers import check_setitem_lengths
from pandas.core.indexes.base import get_values_for_csv
if TYPE_CHECKING:
    from collections.abc import Callable, Generator, Iterable, Sequence
    from pandas._typing import ArrayLike, AxisInt, DtypeBackend, DtypeObj, FillnaOptions, IgnoreRaise, InterpolateOptions, QuantileInterpolation, Shape, npt
    from pandas.core.api import Index
    from pandas.core.arrays._mixins import NDArrayBackedExtensionArray
_dtype_obj = np.dtype('object')

class Block(libinternals.Block, PandasObject):
    __init__: 'Callable' = '\n    Canonical n-dimensional unit of homogeneous dtype contained in a pandas\n    data structure\n\n    Index-ignorant; let the container take care of that\n    '
    __slots__ = ()
    is_numeric = False
    _validate_ndim = (lambda self = None: not is_1d_only_ea_dtype(self.dtype))()()
    is_object = (lambda self = None: self.values.dtype == _dtype_obj)()()
    is_extension = (lambda self = None: not lib.is_np_dtype(self.values.dtype))()()
    _can_consolidate = (lambda self = None: not (self.is_extension))()()
    _consolidate_key = (lambda self: (self._can_consolidate, self.dtype.name))()()
    _can_hold_na = (lambda self = cache_readonly: dtype = self.dtypeif isinstance(dtype, np.dtype):
dtype.kind not in 'iub'None._can_hold_na)()()
    is_bool = (lambda self = final: self.values.dtype == np.dtype(bool))()()
    external_values = (lambda self: external_values(self.values))()
    fill_value = (lambda self: na_value_for_dtype(self.dtype, compat = False))()()
    _standardize_fill_value = (lambda self, value: if self.dtype != _dtype_obj and is_valid_na_for_dtype(value, self.dtype):
value = self.fill_valuevalue)()
    mgr_locs = (lambda self = cache_readonly: self._mgr_locs)()
    mgr_locs = (lambda self = final, new_mgr_locs = final: self._mgr_locs = new_mgr_locs)()
    make_block = (lambda self = None, values = None, placement = final, refs = (None, None): pass# WARNING: Decompyle incomplete
)()
    make_block_same_class = (lambda self = None, values = None, placement = final, refs = (None, None): pass# WARNING: Decompyle incomplete
)()
    __repr__ = (lambda self = None: name = type(self).__name__result)()
    __len__ = (lambda self = None: len(self.values))()
    slice_block_columns = (lambda self = None, slc = None: new_mgr_locs = self._mgr_locs[slc]new_values = self._slice(slc)refs = self.refstype(self)(new_values, new_mgr_locs, self.ndim, refs = refs))()
    take_block_columns = (lambda self = None, indices = None: new_mgr_locs = self._mgr_locs[indices]new_values = self._slice(indices)type(self)(new_values, new_mgr_locs, self.ndim, refs = None))()
    getitem_block_columns = (lambda self = None, slicer = None, new_mgr_locs = final, ref_inplace_op = (False,): new_values = self._slice(slicer)refs = self.refs if ref_inplace_op or self.refs.has_reference() else Nonetype(self)(new_values, new_mgr_locs, self.ndim, refs = refs))()
    _can_hold_element = (lambda self = None, element = None: element = extract_array(element, extract_numpy = True)can_hold_element(self.values, element))()
    should_store = (lambda self = None, value = None: value.dtype == self.dtype)()
    apply = (lambda self = None, func = None: pass# WARNING: Decompyle incomplete
)()
    reduce = (lambda self = None, func = None: pass# WARNING: Decompyle incomplete
)()
    _split_op_result = (lambda self = None, result = None: if result.ndim > 1 and isinstance(result.dtype, ExtensionDtype):
nbs = []for i, loc in enumerate(self._mgr_locs):
if not is_1d_only_ea_dtype(result.dtype):
vals = result[i:i + 1]else:
vals = result[i]bp = BlockPlacement(loc)block = self.make_block(values = vals, placement = bp)nbs.append(block)nbsnb = self.make_block(result)[
nb])()
    _split = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    split_and_operate = (lambda self = None, func = None: pass# WARNING: Decompyle incomplete
)()
    coerce_to_target_dtype = (lambda self = None, other = None, raise_on_upcast = final: new_dtype = find_result_type(self.values.dtype, other)if new_dtype == self.dtype:
raise AssertionError('Something has gone wrong, please report a bug at https://github.com/pandas-dev/pandas/issues')if is_scalar(other) and is_integer_dtype(self.values.dtype) and isna(other) and other is not NaT:
if not isinstance(other, (np.datetime64, np.timedelta64)) or np.isnat(other):
raise_on_upcast = Falseelif isinstance(other, np.ndarray) and other.ndim == 1 and is_integer_dtype(self.values.dtype) and is_float_dtype(other.dtype) and lib.has_only_ints_or_nan(other):
raise_on_upcast = Falseif raise_on_upcast:
raise TypeError(f'''Invalid value \'{other}\' for dtype \'{self.values.dtype}\'''')if self.values.dtype == new_dtype:
raise AssertionError(f'''Did not expect new dtype {new_dtype} to equal self.dtype {self.values.dtype}. Please report a bug at https://github.com/pandas-dev/pandas/issues.''')try:
self.astype(new_dtype)except OutOfBoundsDatetime:
err = Noneraise OutOfBoundsDatetime(f'''Incompatible (high-resolution) value for dtype=\'{self.dtype}\'. Explicitly cast before operating.'''), errerr = Nonedel err)()
    convert = (lambda self = None: if not self.is_object:
[
self.copy(deep = False)]if None.ndim != 1 and self.shape[0] != 1:
blocks = self.split_and_operate(Block.convert)if (lambda .0: pass# WARNING: Decompyle incomplete
)(blocks()):
                return [
                    self.copy(deep = False)]
            return all
        values = None.values
        if values.ndim == 2:
            values = values[0]
        res_values = lib.maybe_convert_objects(values, convert_non_numeric = True)
        refs = None
        if (res_values is values or isinstance(res_values, NumpyExtensionArray)) and res_values._ndarray is values:
            refs = self.refs
        res_values = ensure_block_shape(res_values, self.ndim)
        res_values = maybe_coerce_values(res_values)
        return [
            self.make_block(res_values, refs = refs)]
)()
    
    def convert_dtypes(self, infer_objects, convert_string = None, convert_integer = None, convert_boolean = None, convert_floating = (True, True, True, True, True, 'numpy_nullable'), dtype_backend = ('infer_objects', 'bool', 'convert_string', 'bool', 'convert_integer', 'bool', 'convert_boolean', 'bool', 'convert_floating', 'bool', 'dtype_backend', 'DtypeBackend', 'return', 'list[Block]')):
        pass
    # WARNING: Decompyle incomplete

    dtype = (lambda self = None: self.values.dtype)()()
    astype = (lambda self = None, dtype = None, errors = final, squeeze = ('raise', False): values = self.valuesif squeeze and values.ndim == 2 and is_1d_only_ea_dtype(dtype):
if values.shape[0] != 1:
raise ValueError('Can not squeeze with more than one column.')values = values[(0, :)]new_values = astype_array_safe(values, dtype, errors = errors)new_values = maybe_coerce_values(new_values)refs = Noneif astype_is_view(values.dtype, new_values.dtype):
refs = self.refsnewb = self.make_block(new_values, refs = refs)if newb.shape != self.shape:
raise TypeError(f'''cannot set astype for dtype ({self.dtype.name} [{self.shape}]) to different shape ({newb.dtype.name} [{newb.shape}])''')newb)()
    get_values_for_csv = (lambda self = None, *, float_format: result = get_values_for_csv(self.values, na_rep = na_rep, quoting = quoting, float_format = float_format, date_format = date_format, decimal = decimal)self.make_block(result))()
    copy = (lambda self = None, *, deep: values = self.valuesif deep:
values = values.copy()refs = Noneelse:
values = values.view()refs = self.refstype(self)(values, placement = self._mgr_locs, ndim = self.ndim, refs = refs))()
    
    def _maybe_copy(self = None, inplace = None, deep = None):
        if not inplace and self.refs.has_reference():
            return self
        return None.copy(deep = deep)

    _get_refs_and_copy = (lambda self = None, inplace = None: refs = Nonecopy = not inplaceif inplace:
if self.refs.has_reference():
copy = Trueelse:
refs = self.refs(copy, refs))()
    replace = (lambda self = None, to_replace = None, value = final, inplace = (False, None), mask = ('inplace', 'bool', 'mask', 'npt.NDArray[np.bool_] | None', 'return', 'list[Block]'): values = self.valuesif not self._can_hold_element(to_replace):
[
self._maybe_copy(inplace, deep = False)]# WARNING: Decompyle incomplete
)()
    _replace_regex = (lambda self = None, to_replace = None, value = final, inplace = (False, None), mask = ('inplace', 'bool', 'return', 'list[Block]'): if not is_re(to_replace) and self._can_hold_element(to_replace):
[
self.copy(deep = False)]if None(to_replace) and self.dtype not in (object, 'string'):
[
self.copy(deep = False)]if not None._can_hold_element(value):
if not self.dtype == 'string' or is_re(value):
block = self.astype(np.dtype(object))else:
block = self._maybe_copy(inplace)rx = re.compile(to_replace)replace_regex(block.values, rx, value, mask)[
block])()
    replace_list = (lambda self = None, src_list = None, dest_list = final, inplace = (False, False), regex = ('src_list', 'Iterable[Any]', 'dest_list', 'Sequence[Any]', 'inplace', 'bool', 'regex', 'bool', 'return', 'list[Block]'): pass# WARNING: Decompyle incomplete
)()
    _replace_coerce = (lambda self, to_replace = None, value = None, mask = final, inplace = (True, False), regex = ('mask', 'npt.NDArray[np.bool_]', 'inplace', 'bool', 'regex', 'bool', 'return', 'list[Block]'): if should_use_regex(regex, to_replace):
self._replace_regex(to_replace, value, inplace = inplace, mask = mask)# WARNING: Decompyle incomplete
)()
    
    def _maybe_squeeze_arg(self = None, arg = None):
        '''
        For compatibility with 1D-only ExtensionArrays.
        '''
        return arg

    
    def _unwrap_setitem_indexer(self, indexer):
        '''
        For compatibility with 1D-only ExtensionArrays.
        '''
        return indexer

    shape = (lambda self = None: self.values.shape)()
    
    def iget(self = None, i = None):
        return self.values[i]

    
    def _slice(self = None, slicer = None):
        '''return a slice of my values'''
        return self.values[slicer]

    
    def set_inplace(self = None, locs = None, values = None, copy = (False,)):
        '''
        Modify block values in-place with new item value.

        If copy=True, first copy the underlying values in place before modifying
        (for Copy-on-Write).

        Notes
        -----
        `set_inplace` never creates a new array or new Block, whereas `setitem`
        _may_ create a new array and always creates a new Block.

        Caller is responsible for checking values.dtype == self.dtype.
        '''
        if copy:
            self.values = self.values.copy()
        self.values[locs] = values

    take_nd = (lambda self = None, indexer = None, axis = final, new_mgr_locs = (None, lib.no_default), fill_value = ('indexer', 'npt.NDArray[np.intp]', 'axis', 'AxisInt', 'new_mgr_locs', 'BlockPlacement | None', 'return', 'Block'): values = self.valuesif fill_value is lib.no_default:
fill_value = self.fill_valueallow_fill = Falseelse:
allow_fill = Truenew_values = algos.take_nd(values, indexer, axis = axis, allow_fill = allow_fill, fill_value = fill_value)# WARNING: Decompyle incomplete
)()
    
    def _unstack(self, unstacker = None, fill_value = None, new_placement = None, needs_masking = ('new_placement', 'npt.NDArray[np.intp]', 'needs_masking', 'npt.NDArray[np.bool_]')):
        '''
        Return a list of unstacked blocks of self

        Parameters
        ----------
        unstacker : reshape._Unstacker
        fill_value : int
            Only used in ExtensionBlock._unstack
        new_placement : np.ndarray[np.intp]
        allow_fill : bool
        needs_masking : np.ndarray[bool]

        Returns
        -------
        blocks : list of Block
            New blocks of unstacked values.
        mask : array-like of bool
            The mask of columns of `blocks` we should keep.
        '''
        (new_values, mask) = unstacker.get_new_values(self.values.T, fill_value = fill_value)
        mask = mask.any(0)
        new_values = new_values.T[mask]
        new_placement = new_placement[mask]
        bp = BlockPlacement(new_placement)
        blocks = [
            new_block_2d(new_values, placement = bp)]
        return (blocks, mask)

    
    def setitem(self = None, indexer = None, value = None):
        '''
        Attempt self.values[indexer] = value, possibly creating a new array.

        Parameters
        ----------
        indexer : tuple, list-like, array-like, slice, int
            The subset of self.values to set
        value : object
            The value being set

        Returns
        -------
        Block

        Notes
        -----
        `indexer` is a direct slice/positional indexer. `value` must
        be a compatible shape.
        '''
        value = self._standardize_fill_value(value)
        values = cast(np.ndarray, self.values)
        if self.ndim == 2:
            values = values.T
        check_setitem_lengths(indexer, value, values)
        if self.dtype != _dtype_obj:
            value = extract_array(value, extract_numpy = True)
        
        try:
            casted = np_can_hold_element(values.dtype, value)
            if self.dtype == _dtype_obj:
                vi = values[indexer]
                if lib.is_list_like(vi):
                    casted = setitem_datetimelike_compat(values, len(vi), casted)
            self = self._maybe_copy(inplace = True)
            values = cast(np.ndarray, self.values.T)
            if isinstance(casted, np.ndarray) and casted.ndim == 1 and len(casted) == 1:
                casted = casted[(0, ...)]
            
            try:
                values[indexer] = casted
            except (TypeError, ValueError):
                err = None
                if is_list_like(casted):
                    raise ValueError('setting an array element with a sequence.'), err
                raise 
                err = None
                del err
                except LossySetitemError:
                    nb = self.coerce_to_target_dtype(value, raise_on_upcast = True)
                    return 

            return self


    
    def putmask(self = None, mask = None, new = None):
        '''
        putmask the data to the block; it is possible that we may create a
        new dtype of block

        Return the resulting block(s).

        Parameters
        ----------
        mask : np.ndarray[bool], SparseArray[bool], or BooleanArray
        new : an ndarray/object

        Returns
        -------
        List[Block]
        '''
        orig_mask = mask
        values = cast(np.ndarray, self.values)
        (mask, noop) = validate_putmask(values.T, mask)
    # WARNING: Decompyle incomplete

    
    def where(self = None, other = None, cond = None):
        '''
        evaluate the block; return result block(s) from the result

        Parameters
        ----------
        other : an ndarray/object
        cond : np.ndarray[bool], SparseArray[bool], or BooleanArray

        Returns
        -------
        List[Block]
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def fillna(self = None, value = None, limit = None, inplace = (None, False)):
        '''
        fillna on the block with the value. If we fail, then convert to
        block to hold objects instead and try again
        '''
        inplace = validate_bool_kwarg(inplace, 'inplace')
        if not self._can_hold_na:
            noop = True
        else:
            mask = isna(self.values)
            (mask, noop) = validate_putmask(self.values, mask)
        if noop:
            return [
                self.copy(deep = False)]
    # WARNING: Decompyle incomplete

    
    def pad_or_backfill(self = None, *, method, inplace, limit, limit_area):
        if not self._can_hold_na:
            return [
                self.copy(deep = False)]
        (copy, refs) = None._get_refs_and_copy(inplace)
        vals = cast(NumpyExtensionArray, self.array_values)
        new_values = vals.T._pad_or_backfill(method = method, limit = limit, limit_area = limit_area, copy = copy).T
        data = extract_array(new_values, extract_numpy = True)
        return [
            self.make_block_same_class(data, refs = refs)]

    interpolate = (lambda self = None, *, method: inplace = validate_bool_kwarg(inplace, 'inplace')if method == 'asfreq':
missing.clean_fill_method(method)if not self._can_hold_na:
[
self.copy(deep = False)]if None.dtype == _dtype_obj:
name = {
1: 'Series',
2: 'DataFrame' }[self.ndim]raise TypeError(f'''{name} cannot interpolate with object dtype.''')(copy, refs) = self._get_refs_and_copy(inplace)# WARNING: Decompyle incomplete
)()
    diff = (lambda self = None, n = None: new_values = algos.diff(self.values.T, n, axis = 0).T[
self.make_block(values = new_values)])()
    
    def shift(self = None, periods = None, fill_value = None):
        '''shift the block by periods, possibly upcast'''
        axis = self.ndim - 1
        if lib.is_scalar(fill_value) and self.dtype != _dtype_obj:
            raise ValueError('fill_value must be a scalar')
        fill_value = self._standardize_fill_value(fill_value)
        
        try:
            casted = np_can_hold_element(self.dtype, fill_value)
            values = cast(np.ndarray, self.values)
            new_values = shift(values, periods, axis, casted)
            return [
                self.make_block_same_class(new_values)]
        except LossySetitemError:
            if not self.dtype.kind not in 'iub' or is_valid_na_for_dtype(fill_value, self.dtype):
                warnings.warn('shifting with a fill value that cannot be held by original dtype is deprecated and will raise in a future version. Explicitly cast to the desired dtype before shifting instead.', Pandas4Warning, stacklevel = find_stack_level())
            nb = self.coerce_to_target_dtype(fill_value, raise_on_upcast = False)
            return 


    quantile = (lambda self = None, qs = None, interpolation = final: pass# WARNING: Decompyle incomplete
)()
    round = (lambda self = None, decimals = None: if self.is_numeric or self.is_bool:
if isinstance(self.values, (DatetimeArray, TimedeltaArray, PeriodArray)):
warnings.warn('obj.round has no effect with datetime, timedelta, or period dtypes. Use obj.dt.round(...) instead.', UserWarning, stacklevel = find_stack_level())self.copy(deep = False)values = None.values.round(decimals)refs = Noneif values is self.values:
refs = self.refsself.make_block_same_class(values, refs = refs))()
    
    def delete(self = None, loc = None):
        '''Deletes the locs from the block.

        We split the block to avoid copying the underlying data. We create new
        blocks for every connected segment of the initial block that is not deleted.
        The new blocks point to the initial array.
        '''
        if not is_list_like(loc):
            loc = [
                loc]
        if self.ndim == 1:
            values = cast(np.ndarray, self.values)
            values = np.delete(values, loc)
            mgr_locs = self._mgr_locs.delete(loc)
            return [
                type(self)(values, placement = mgr_locs, ndim = self.ndim)]
        if None.max(loc) >= self.values.shape[0]:
            raise IndexError
        loc = np.concatenate([
            loc,
            [
                self.values.shape[0]]])
        mgr_locs_arr = self._mgr_locs.as_array
        new_blocks = []
        previous_loc = -1
        refs = self.refs if self.refs.has_reference() else None
        for idx in loc:
            if idx == previous_loc + 1:
                pass
            else:
                values = self.values[(previous_loc + 1:idx, :)]
                locs = mgr_locs_arr[previous_loc + 1:idx]
                nb = type(self)(values, placement = BlockPlacement(locs), ndim = self.ndim, refs = refs)
                new_blocks.append(nb)
            previous_loc = idx
            return new_blocks

    is_view = (lambda self = None: raise AbstractMethodError(self))()
    array_values = (lambda self = None: raise AbstractMethodError(self))()
    
    def get_values(self = None, dtype = None):
        '''
        return an internal format, currently just the ndarray
        this is often overridden to handle to_dense like operations
        '''
        raise AbstractMethodError(self)



class EABackedBlock(Block):
    pass
# WARNING: Decompyle incomplete


class ExtensionBlock(EABackedBlock):
    pass
# WARNING: Decompyle incomplete


class NumpyBlock(Block):
    values: 'np.ndarray' = 'NumpyBlock'
    __slots__ = ()
    is_view = (lambda self = None: self.values.base is not None)()
    array_values = (lambda self = None: NumpyExtensionArray(self.values))()
    
    def get_values(self = None, dtype = None):
        if dtype == _dtype_obj:
            return self.values.astype(_dtype_obj)
        return None.values

    is_numeric = (lambda self = None: dtype = self.values.dtypekind = dtype.kindkind in 'fciub')()


class NDArrayBackedExtensionBlock(EABackedBlock):
    values: 'NDArrayBackedExtensionArray' = '\n    Block backed by an NDArrayBackedExtensionArray\n    '
    is_view = (lambda self = None: self.values._ndarray.base is not None)()


class DatetimeLikeBlock(NDArrayBackedExtensionBlock):
    '''Block for datetime64[ns], timedelta64[ns].'''
    __slots__ = ()
    values: 'DatetimeArray | TimedeltaArray' = False


def maybe_coerce_values(values = None):
    '''
    Input validation for values passed to __init__. Ensure that
    any datetime64/timedelta64 dtypes are in nanoseconds.  Ensure
    that we do not have string dtypes.

    Parameters
    ----------
    values : np.ndarray or ExtensionArray

    Returns
    -------
    values : np.ndarray or ExtensionArray
    '''
    if isinstance(values, np.ndarray):
        values = ensure_wrapped_if_datetimelike(values)
        if issubclass(values.dtype.type, str):
            values = np.array(values, dtype = object)
# WARNING: Decompyle incomplete


def get_block_type(dtype = None):
    '''
    Find the appropriate Block subclass to use for the given values and dtype.

    Parameters
    ----------
    dtype : numpy or pandas dtype

    Returns
    -------
    cls : class, subclass of Block
    '''
    if isinstance(dtype, DatetimeTZDtype):
        return DatetimeLikeBlock
    if None(dtype, PeriodDtype):
        return NDArrayBackedExtensionBlock
    if None(dtype, ExtensionDtype):
        return ExtensionBlock
    kind = None.kind
    if kind in 'Mm':
        return DatetimeLikeBlock


def new_block_2d(values = None, placement = None, refs = None):
    klass = get_block_type(values.dtype)
    values = maybe_coerce_values(values)
    return klass(values, ndim = 2, placement = placement, refs = refs)


def new_block(values = None, placement = None, *, ndim, refs):
    klass = get_block_type(values.dtype)
    return klass(values, ndim = ndim, placement = placement, refs = refs)


def check_ndim(values = None, placement = None, ndim = None):
    '''
    ndim inference and validation.

    Validates that values.ndim and ndim are consistent.
    Validates that len(values) and len(placement) are consistent.

    Parameters
    ----------
    values : array-like
    placement : BlockPlacement
    ndim : int

    Raises
    ------
    ValueError : the number of dimensions do not match
    '''
    if values.ndim > ndim:
        raise ValueError(f'''Wrong number of dimensions. values.ndim > ndim [{values.ndim} > {ndim}]''')
    if not is_1d_only_ea_dtype(values.dtype):
        if values.ndim != ndim:
            raise ValueError(f'''Wrong number of dimensions. values.ndim != ndim [{values.ndim} != {ndim}]''')
        if len(placement) != len(values):
            raise ValueError(f'''Wrong number of items passed {len(values)}, placement implies {len(placement)}''')
        return None
    if None == 2 or len(placement) != 1:
        raise ValueError('need to split')
    return None


def extract_pandas_array(values = None, dtype = None, ndim = None):
    """
    Ensure that we don't allow NumpyExtensionArray / NumpyEADtype in internals.
    """
    if isinstance(values, ABCNumpyExtensionArray):
        values = values.to_numpy()
        if ndim and ndim > 1:
            values = np.atleast_2d(values)
    if isinstance(dtype, NumpyEADtype):
        dtype = dtype.numpy_dtype
    return (values, dtype)


def extend_blocks(result = None, blocks = None):
    '''return a new extended blocks, given the result'''
    pass
# WARNING: Decompyle incomplete


def ensure_block_shape(values = None, ndim = None):
    '''
    Reshape if possible to have values.ndim == ndim.
    '''
    if not values.ndim < ndim and is_1d_only_ea_dtype(values.dtype):
        values = cast('np.ndarray | DatetimeArray | TimedeltaArray', values)
        values = values.reshape(1, -1)
    return values


def external_values(values = None):
    '''
    The array that Series.values returns (public attribute).

    This has some historical constraints, and is overridden in block
    subclasses to return the correct array (e.g. period returns
    object ndarray and datetimetz a datetime64[ns] ndarray instead of
    proper extension array).
    '''
    if isinstance(values, (PeriodArray, IntervalArray)):
        return values.astype(object)
    if None(values, (DatetimeArray, TimedeltaArray)):
        values = values._ndarray
    if isinstance(values, np.ndarray):
        values = values.view()
        values.flags.writeable = False
    
    return values

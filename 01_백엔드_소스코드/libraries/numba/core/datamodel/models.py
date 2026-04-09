# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: models.pyc (Python 3.11)

from functools import partial
from collections import deque
from llvmlite import ir
from numba.core.datamodel.registry import register_default
from numba.core import types, cgutils
from numba.np import numpy_support

class DataModel(object):
    '''
    DataModel describe how a FE type is represented in the LLVM IR at
    different contexts.

    Contexts are:

    - value: representation inside function body.  Maybe stored in stack.
    The representation here are flexible.

    - data: representation used when storing into containers (e.g. arrays).

    - argument: representation used for function argument.  All composite
    types are unflattened into multiple primitive types.

    - return: representation used for return argument.

    Throughput the compiler pipeline, a LLVM value is usually passed around
    in the "value" representation.  All "as_" prefix function converts from
    "value" representation.  All "from_" prefix function converts to the
    "value"  representation.

    '''
    
    def __init__(self, dmm, fe_type):
        self._dmm = dmm
        self._fe_type = fe_type

    fe_type = (lambda self: self._fe_type)()
    
    def get_value_type(self):
        raise NotImplementedError(self)

    
    def get_data_type(self):
        return self.get_value_type()

    
    def get_argument_type(self):
        '''Return a LLVM type or nested tuple of LLVM type
        '''
        return self.get_value_type()

    
    def get_return_type(self):
        return self.get_value_type()

    
    def as_data(self, builder, value):
        raise NotImplementedError(self)

    
    def as_argument(self, builder, value):
        '''
        Takes one LLVM value
        Return a LLVM value or nested tuple of LLVM value
        '''
        raise NotImplementedError(self)

    
    def as_return(self, builder, value):
        raise NotImplementedError(self)

    
    def from_data(self, builder, value):
        raise NotImplementedError(self)

    
    def from_argument(self, builder, value):
        '''
        Takes a LLVM value or nested tuple of LLVM value
        Returns one LLVM value
        '''
        raise NotImplementedError(self)

    
    def from_return(self, builder, value):
        raise NotImplementedError(self)

    
    def load_from_data_pointer(self, builder, ptr, align = (None,)):
        '''
        Load value from a pointer to data.
        This is the default implementation, sufficient for most purposes.
        '''
        return self.from_data(builder, builder.load(ptr, align = align))

    
    def traverse(self, builder):
        '''
        Traverse contained members.
        Returns a iterable of contained (types, getters).
        Each getter is a one-argument function accepting a LLVM value.
        '''
        return []

    
    def traverse_models(self):
        '''
        Recursively list all models involved in this model.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def traverse_types(self):
        '''
        Recursively list all frontend types involved in this model.
        '''
        types = [
            self._fe_type]
        queue = deque([
            self])
    # WARNING: Decompyle incomplete

    
    def inner_models(self):
        '''
        List all *inner* models.
        '''
        return []

    
    def get_nrt_meminfo(self, builder, value):
        '''
        Returns the MemInfo object or None if it is not tracked.
        It is only defined for types.meminfo_pointer
        '''
        pass

    
    def has_nrt_meminfo(self):
        return False

    
    def contains_nrt_meminfo(self):
        '''
        Recursively check all contained types for need for NRT meminfo.
        '''
        return (lambda .0: pass# WARNING: Decompyle incomplete
)(self.traverse_models()())

    
    def _compared_fields(self):
        return (type(self), self._fe_type)

    
    def __hash__(self):
        return hash(tuple(self._compared_fields()))

    
    def __eq__(self, other):
        if type(self) is type(other):
            return self._compared_fields() == other._compared_fields()

    
    def __ne__(self, other):
        return not self.__eq__(other)


OmittedArgDataModel = <NODE:12>()
BooleanModel = <NODE:12>()()

class PrimitiveModel(DataModel):
    pass
# WARNING: Decompyle incomplete


class ProxyModel(DataModel):
    '''
    Helper class for models which delegate to another model.
    '''
    
    def get_value_type(self):
        return self._proxied_model.get_value_type()

    
    def get_data_type(self):
        return self._proxied_model.get_data_type()

    
    def get_return_type(self):
        return self._proxied_model.get_return_type()

    
    def get_argument_type(self):
        return self._proxied_model.get_argument_type()

    
    def as_data(self, builder, value):
        return self._proxied_model.as_data(builder, value)

    
    def as_argument(self, builder, value):
        return self._proxied_model.as_argument(builder, value)

    
    def as_return(self, builder, value):
        return self._proxied_model.as_return(builder, value)

    
    def from_data(self, builder, value):
        return self._proxied_model.from_data(builder, value)

    
    def from_argument(self, builder, value):
        return self._proxied_model.from_argument(builder, value)

    
    def from_return(self, builder, value):
        return self._proxied_model.from_return(builder, value)


EnumModel = <NODE:12>()()
OpaqueModel = <NODE:12>()()()()()()()()()()()()()()()()()()()()()()()()()()()()
MemInfoModel = <NODE:12>()
IntegerModel = <NODE:12>()()
FloatModel = <NODE:12>()
PointerModel = <NODE:12>()
EphemeralPointerModel = <NODE:12>()
EphemeralArrayModel = <NODE:12>()
ExternalFuncPointerModel = <NODE:12>()
UniTupleModel = <NODE:12>()()()

class CompositeModel(DataModel):
    '''Any model that is composed of multiple other models should subclass from
    this.
    '''
    pass


class StructModel(CompositeModel):
    pass
# WARNING: Decompyle incomplete

ComplexModel = <NODE:12>()
TupleModel = <NODE:12>()()()()()
UnionModel = <NODE:12>()
PairModel = <NODE:12>()
ListPayloadModel = <NODE:12>()
ListModel = <NODE:12>()
ListIterModel = <NODE:12>()
SetEntryModel = <NODE:12>()
SetPayloadModel = <NODE:12>()
SetModel = <NODE:12>()
SetIterModel = <NODE:12>()
ArrayModel = <NODE:12>()()()()()()
ArrayFlagsModel = <NODE:12>()
NestedArrayModel = <NODE:12>()
OptionalModel = <NODE:12>()
RecordModel = <NODE:12>()
UnicodeCharSeq = <NODE:12>()
CharSeq = <NODE:12>()

class CContiguousFlatIter(StructModel):
    pass
# WARNING: Decompyle incomplete


class FlatIter(StructModel):
    pass
# WARNING: Decompyle incomplete

UniTupleIter = <NODE:12>()
SliceModel = <NODE:12>()()
NPDatetimeModel = <NODE:12>()()
ArrayIterator = <NODE:12>()
EnumerateType = <NODE:12>()
ZipType = <NODE:12>()
RangeIteratorType = <NODE:12>()
GeneratorModel = <NODE:12>()
ArrayCTypesModel = <NODE:12>()
RangeModel = <NODE:12>()
NdIndexModel = <NODE:12>()
handle_numpy_flat_type = (lambda dmm, ty: if ty.array_type.layout == 'C':
CContiguousFlatIter(dmm, ty, need_indices = False)None(dmm, ty))()
handle_numpy_ndenumerate_type = (lambda dmm, ty: if ty.array_type.layout == 'C':
CContiguousFlatIter(dmm, ty, need_indices = True)None(dmm, ty))()
handle_bound_function = (lambda dmm, ty: dmm[ty.this])()
NdIter = <NODE:12>()
DeferredStructModel = <NODE:12>()
StructPayloadModel = <NODE:12>()

class StructRefModel(StructModel):
    pass
# WARNING: Decompyle incomplete

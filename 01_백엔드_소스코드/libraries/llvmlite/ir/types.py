# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: types.pyc (Python 3.11)

'''
Classes that are LLVM types
'''
import struct
from llvmlite import ir_layer_typed_pointers_enabled
from llvmlite.ir._utils import _StrCaching

def _wrapname(x):
    return '"{0}"'.format(x.replace('\\', '\\5c').replace('"', '\\22'))


class Type(_StrCaching):
    '''
    The base class for all LLVM types.
    '''
    is_pointer = False
    null = 'zeroinitializer'
    
    def __repr__(self):
        return f'''<{type(self)!s} {str(self)!s}>'''

    
    def _to_string(self):
        raise NotImplementedError

    
    def as_pointer(self, addrspace = (0,)):
        return PointerType(self, addrspace)

    
    def __ne__(self, other):
        return not (self == other)

    
    def _get_ll_global_value_type(self, target_data, context = (None,)):
        '''
        Convert this type object to an LLVM type.
        '''
        Module = Module
        GlobalVariable = GlobalVariable
        import llvmlite.ir
        parse_assembly = parse_assembly
        import llvmlite.binding
    # WARNING: Decompyle incomplete

    
    def get_abi_size(self, target_data, context = (None,)):
        '''
        Get the ABI size of this type according to data layout *target_data*.
        '''
        llty = self._get_ll_global_value_type(target_data, context)
        return target_data.get_abi_size(llty)

    
    def get_element_offset(self, target_data, ndx, context = (None,)):
        llty = self._get_ll_global_value_type(target_data, context)
        return target_data.get_element_offset(llty, ndx)

    
    def get_abi_alignment(self, target_data, context = (None,)):
        '''
        Get the minimum ABI alignment of this type according to data layout
        *target_data*.
        '''
        llty = self._get_ll_global_value_type(target_data, context)
        return target_data.get_abi_alignment(llty)

    
    def format_constant(self, value):
        '''
        Format constant *value* of this type.  This method may be overriden
        by subclasses.
        '''
        return str(value)

    
    def wrap_constant_value(self, value):
        '''
        Wrap constant *value* if necessary.  This method may be overriden
        by subclasses (especially aggregate types).
        '''
        return value

    
    def __call__(self, value):
        '''
        Create a LLVM constant of this type with the given Python value.
        '''
        Constant = Constant
        import llvmlite.ir
        return Constant(self, value)



class MetaDataType(Type):
    
    def _to_string(self):
        return 'metadata'

    
    def as_pointer(self):
        raise TypeError

    
    def __eq__(self, other):
        return isinstance(other, MetaDataType)

    
    def __hash__(self):
        return hash(MetaDataType)



class LabelType(Type):
    '''
    The label type is the type of e.g. basic blocks.
    '''
    
    def _to_string(self):
        return 'label'



class PointerType(Type):
    pass
# WARNING: Decompyle incomplete


class _TypedPointerType(PointerType):
    pass
# WARNING: Decompyle incomplete


class VoidType(Type):
    '''
    The type for empty values (e.g. a function returning no value).
    '''
    
    def _to_string(self):
        return 'void'

    
    def __eq__(self, other):
        return isinstance(other, VoidType)

    
    def __hash__(self):
        return hash(VoidType)

    from_llvm = (lambda cls, typeref, ir_ctx: cls())()


class FunctionType(Type):
    '''
    The type for functions.
    '''
    
    def __init__(self, return_type, args, var_arg = (False,)):
        self.return_type = return_type
        self.args = tuple(args)
        self.var_arg = var_arg

    
    def _to_string(self):
        if self.args:
            strargs = (lambda .0: [ str(a) for a in .0 ])(self.args())
            if self.var_arg:
                return '{0} ({1}, ...)'.format(self.return_type, strargs)
            return ', '.join.format(self.return_type, strargs)
        if None.var_arg:
            return '{0} (...)'.format(self.return_type)
        return None.format(self.return_type)

    
    def __eq__(self, other):

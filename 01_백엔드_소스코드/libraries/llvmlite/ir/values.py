# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: values.pyc (Python 3.11)

'''
Classes that are LLVM values: Value, Constant...
Instructions are in the instructions module.
'''
import functools
import string
import re
from types import MappingProxyType
from llvmlite.ir import values, types, _utils
from llvmlite.ir._utils import _StrCaching, _StringReferenceCaching, _HasMetadata
_VALID_CHARS = frozenset(map(ord, string.ascii_letters)) | frozenset(map(ord, string.digits)) | frozenset(map(ord, " !#$%&'()*+,-./:;<=>?@[]^_`{|}~"))
_SIMPLE_IDENTIFIER_RE = re.compile('[-a-zA-Z$._][-a-zA-Z$._0-9]*$')
_CMP_MAP = {
    '>': 'gt',
    '<': 'lt',
    '==': 'eq',
    '!=': 'ne',
    '>=': 'ge',
    '<=': 'le' }

def _escape_string(text, _map = ({ },)):
    '''
    Escape the given bytestring for safe use as a LLVM array constant.
    Any unicode string input is first encoded with utf8 into bytes.
    '''
    pass
# WARNING: Decompyle incomplete


def _binop(opname):
    pass
# WARNING: Decompyle incomplete


def _castop(opname):
    pass
# WARNING: Decompyle incomplete


class _ConstOpMixin(object):
    '''
    A mixin defining constant operations, for use in constant-like classes.
    '''
    shl = (lambda self, other: pass)()
    lshr = (lambda self, other: pass)()
    ashr = (lambda self, other: pass)()
    add = (lambda self, other: pass)()
    fadd = (lambda self, other: pass)()
    sub = (lambda self, other: pass)()
    fsub = (lambda self, other: pass)()
    mul = (lambda self, other: pass)()
    fmul = (lambda self, other: pass)()
    udiv = (lambda self, other: pass)()
    sdiv = (lambda self, other: pass)()
    fdiv = (lambda self, other: pass)()
    urem = (lambda self, other: pass)()
    srem = (lambda self, other: pass)()
    frem = (lambda self, other: pass)()
    or_ = (lambda self, other: pass)()
    and_ = (lambda self, other: pass)()
    xor = (lambda self, other: pass)()
    
    def _cmp(self, prefix, sign, cmpop, other):
        ins = prefix + 'cmp'
        
        try:
            op = _CMP_MAP[cmpop]
        except KeyError:
            raise ValueError(f'''invalid comparison {cmpop!r} for {ins!s}''')

        if not prefix == 'i' or cmpop in ('==', '!='):
            op = sign + op
        if self.type != other.type:
            raise ValueError(f'''Operands must be the same type, got ({self.type!s}, {other.type!s})''')
        fmt = '{0} {1} ({2} {3}, {4} {5})'.format(ins, op, self.type, self.get_reference(), other.type, other.get_reference())
        return FormattedConstant(types.IntType(1), fmt)

    
    def icmp_signed(self, cmpop, other):
        """
        Signed integer comparison:
            lhs <cmpop> rhs

        where cmpop can be '==', '!=', '<', '<=', '>', '>='
        """
        return self._cmp('i', 's', cmpop, other)

    
    def icmp_unsigned(self, cmpop, other):
        """
        Unsigned integer (or pointer) comparison:
            lhs <cmpop> rhs

        where cmpop can be '==', '!=', '<', '<=', '>', '>='
        """
        return self._cmp('i', 'u', cmpop, other)

    
    def fcmp_ordered(self, cmpop, other):
        """
        Floating-point ordered comparison:
            lhs <cmpop> rhs

        where cmpop can be '==', '!=', '<', '<=', '>', '>=', 'ord', 'uno'
        """
        return self._cmp('f', 'o', cmpop, other)

    
    def fcmp_unordered(self, cmpop, other):
        """
        Floating-point unordered comparison:
            lhs <cmpop> rhs

        where cmpop can be '==', '!=', '<', '<=', '>', '>=', 'ord', 'uno'
        """
        return self._cmp('f', 'u', cmpop, other)

    
    def not_(self):
        '''
        Bitwise integer complement:
            ~value
        '''
        if isinstance(self.type, types.VectorType):
            rhs = values.Constant(self.type, (-1,) * self.type.count)
        else:
            rhs = values.Constant(self.type, -1)
        return self.xor(rhs)

    
    def neg(self):
        '''
        Integer negative:
            -value
        '''
        zero = values.Constant(self.type, 0)
        return zero.sub(self)

    
    def fneg(self):
        '''
        Floating-point negative:
            -value
        '''
        fmt = 'fneg ({0} {1})'.format(self.type, self.get_reference())
        return FormattedConstant(self.type, fmt)

    trunc = (lambda self, typ: pass)()
    zext = (lambda self, typ: pass)()
    sext = (lambda self, typ: pass)()
    fptrunc = (lambda self, typ: pass)()
    fpext = (lambda self, typ: pass)()
    bitcast = (lambda self, typ: pass)()
    fptoui = (lambda self, typ: pass)()
    uitofp = (lambda self, typ: pass)()
    fptosi = (lambda self, typ: pass)()
    sitofp = (lambda self, typ: pass)()
    ptrtoint = (lambda self, typ: if not isinstance(self.type, types.PointerType):
msg = "can only call ptrtoint() on pointer type, not '%s'"raise TypeError(msg % (self.type,))if not isinstance(typ, types.IntType):
raise TypeError(f'''can only ptrtoint() to integer type, not \'{typ!s}\''''))()
    inttoptr = (lambda self, typ: if not isinstance(self.type, types.IntType):
msg = "can only call inttoptr() on integer constants, not '%s'"raise TypeError(msg % (self.type,))if not isinstance(typ, types.PointerType):
raise TypeError(f'''can only inttoptr() to pointer type, not \'{typ!s}\''''))()
    
    def gep(self, indices):
        '''
        Call getelementptr on this pointer constant.
        '''
        if not isinstance(self.type, types.PointerType):
            raise TypeError(f'''can only call gep() on pointer constants, not \'{self.type!s}\'''')
        outtype = self.type
        for i in indices:
            outtype = outtype.gep(i)
            strindices = indices()
            op = 'getelementptr ({0}, {1} {2}, {3})'.format(self.type.pointee, self.type, self.get_reference(), ', '.join(strindices))
            return FormattedConstant(outtype.as_pointer(self.addrspace), op)



class Value(object):
    '''
    The base class for all values.
    '''
    
    def __repr__(self):
        return f'''<ir.{self.__class__.__name__!s} type=\'{self.type!s}\' ...>'''



class _Undefined(object):
    """
    'undef': a value for undefined values.
    """
    
    def __new__(cls):
        
        try:
            return Undefined
        except NameError:
            return 



Undefined = _Undefined()

class Constant(Value, _ConstOpMixin, _StringReferenceCaching, _StrCaching):
    '''
    A constant LLVM value.
    '''
    
    def __init__(self, typ, constant):
        pass
    # WARNING: Decompyle incomplete

    
    def _to_string(self):
        return '{0} {1}'.format(self.type, self.get_reference())

    
    def _get_reference(self):
        pass
    # WARNING: Decompyle incomplete

    literal_array = (lambda cls, elems: tys = elems()if len(tys) == 0:
raise ValueError('need at least one element')ty = tys[0]for other in tys:
if ty != other:
raise TypeError('all elements must have the same type')cls(types.ArrayType(ty, len(elems)), elems))()
    literal_struct = (lambda cls, elems, packed = (False,): tys = elems()cls(types.LiteralStructType(tys, packed), elems))()
    addrspace = (lambda self: if not isinstance(self.type, types.PointerType):
raise TypeError('Only pointer constant have address spaces')self.type.addrspace)()
    
    def __eq__(self, other):
        if isinstance(other, Constant):
            return str(self) == str(other)

    
    def __ne__(self, other):
        return not self.__eq__(other)

    
    def __hash__(self):
        return hash(str(self))

    
    def __repr__(self):
        return f'''<ir.Constant type=\'{self.type!s}\' value={self.constant!r}>'''



class FormattedConstant(Constant):
    '''
    A constant with an already formatted IR representation.
    '''
    
    def __init__(self, typ, constant):
        pass
    # WARNING: Decompyle incomplete

    
    def _to_string(self):
        return self.constant

    
    def _get_reference(self):
        return self.constant



class NamedValue(Value, _StringReferenceCaching, _StrCaching):
    '''
    The base class for named values.
    '''
    name_prefix = '%'
    deduplicate_name = True
    
    def __init__(self, parent, type, name):
        pass
    # WARNING: Decompyle incomplete

    
    def _to_string(self):
        buf = []
        if not isinstance(self.type, types.VoidType):
            buf.append('{0} = '.format(self.get_reference()))
        self.descr(buf)
        return ''.join(buf).rstrip()

    
    def descr(self, buf):
        raise NotImplementedError

    
    def _get_name(self):
        return self._name

    
    def _set_name(self, name):
        name = self.parent.scope.register(name, deduplicate = self.deduplicate_name)
        self._name = name

    name = property(_get_name, _set_name)
    
    def _get_reference(self):
        name = self.name
        if '\\' in name or '"' in name:
            name = name.replace('\\', '\\5c').replace('"', '\\22')
        return '{0}"{1}"'.format(self.name_prefix, name)

    
    def __repr__(self):
        return f'''<ir.{self.__class__.__name__!s} {self.name!r} of type \'{self.type!s}\'>'''

    function_type = (lambda self: ty = self.typeif isinstance(ty, types.PointerType):
ty = self.type.pointeeif isinstance(ty, types.FunctionType):
tyraise None('Not a function: {0}'.format(self.type)))()


class MetaDataString(NamedValue):
    pass
# WARNING: Decompyle incomplete


class MetaDataArgument(Value, _StringReferenceCaching, _StrCaching):
    '''
    An argument value to a function taking metadata arguments.
    This can wrap any other kind of LLVM value.

    Do not instantiate directly, Builder.call() will create these
    automatically.
    '''
    
    def __init__(self, value):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_reference(self):
        return '{0} {1}'.format(self.wrapped_value.type, self.wrapped_value.get_reference())

    _to_string = _get_reference


class NamedMetaData(object):
    '''
    A named metadata node.

    Do not instantiate directly, use Module.add_named_metadata() instead.
    '''
    
    def __init__(self, parent):
        self.parent = parent
        self.operands = []

    
    def add(self, md):
        self.operands.append(md)



class MDValue(NamedValue):
    pass
# WARNING: Decompyle incomplete


class DIToken:
    '''
    A debug information enumeration value that should appear bare in
    the emitted metadata.

    Use this to wrap known constants, e.g. the DW_* enumerations.
    '''
    
    def __init__(self, value):
        self.value = value



class DIValue(NamedValue):
    pass
# WARNING: Decompyle incomplete


class GlobalValue(_HasMetadata, _ConstOpMixin, NamedValue):
    pass
# WARNING: Decompyle incomplete


class GlobalVariable(GlobalValue):
    pass
# WARNING: Decompyle incomplete


class AttributeSet(set):
    pass
# WARNING: Decompyle incomplete


class FunctionAttributes(AttributeSet):
    pass
# WARNING: Decompyle incomplete


class Function(GlobalValue):
    pass
# WARNING: Decompyle incomplete


class ArgumentAttributes(AttributeSet):
    pass
# WARNING: Decompyle incomplete


class _BaseArgument(NamedValue):
    pass
# WARNING: Decompyle incomplete


class Argument(_BaseArgument):
    '''
    The specification of a function argument.
    '''
    
    def __str__(self):
        attrs = self.attributes._to_list(self.type)
        if attrs:
            return '{0} {1} {2}'.format(self.type, ' '.join(attrs), self.get_reference())
        return None.format(self.type, self.get_reference())



class ReturnValue(_BaseArgument):
    """
    The specification of a function's return value.
    """
    
    def __str__(self):
        attrs = self.attributes._to_list(self.type)
        if attrs:
            return '{0} {1}'.format(' '.join(attrs), self.type)
        return None(self.type)



class Block(NamedValue):
    pass
# WARNING: Decompyle incomplete


class BlockAddress(Value):
    '''
    The address of a basic block.
    '''
    
    def __init__(self, function, basic_block):
        pass
    # WARNING: Decompyle incomplete

    
    def __str__(self):
        return '{0} {1}'.format(self.type, self.get_reference())

    
    def get_reference(self):
        return 'blockaddress({0}, {1})'.format(self.function.get_reference(), self.basic_block.get_reference())

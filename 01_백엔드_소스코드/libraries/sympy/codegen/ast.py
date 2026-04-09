# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ast.pyc (Python 3.11)

__doc__ = '\nTypes used to represent a full function/module as an Abstract Syntax Tree.\n\nMost types are small, and are merely used as tokens in the AST. A tree diagram\nhas been included below to illustrate the relationships between the AST types.\n\n\nAST Type Tree\n-------------\n::\n\n  *Basic*\n       |\n       |\n   CodegenAST\n       |\n       |--->AssignmentBase\n       |             |--->Assignment\n       |             |--->AugmentedAssignment\n       |                                    |--->AddAugmentedAssignment\n       |                                    |--->SubAugmentedAssignment\n       |                                    |--->MulAugmentedAssignment\n       |                                    |--->DivAugmentedAssignment\n       |                                    |--->ModAugmentedAssignment\n       |\n       |--->CodeBlock\n       |\n       |\n       |--->Token\n                |--->Attribute\n                |--->For\n                |--->String\n                |       |--->QuotedString\n                |       |--->Comment\n                |--->Type\n                |       |--->IntBaseType\n                |       |              |--->_SizedIntType\n                |       |                               |--->SignedIntType\n                |       |                               |--->UnsignedIntType\n                |       |--->FloatBaseType\n                |                        |--->FloatType\n                |                        |--->ComplexBaseType\n                |                                           |--->ComplexType\n                |--->Node\n                |       |--->Variable\n                |       |           |---> Pointer\n                |       |--->FunctionPrototype\n                |                            |--->FunctionDefinition\n                |--->Element\n                |--->Declaration\n                |--->While\n                |--->Scope\n                |--->Stream\n                |--->Print\n                |--->FunctionCall\n                |--->BreakToken\n                |--->ContinueToken\n                |--->NoneToken\n                |--->Return\n\n\nPredefined types\n----------------\n\nA number of ``Type`` instances are provided in the ``sympy.codegen.ast`` module\nfor convenience. Perhaps the two most common ones for code-generation (of numeric\ncodes) are ``float32`` and ``float64`` (known as single and double precision respectively).\nThere are also precision generic versions of Types (for which the codeprinters selects the\nunderlying data type at time of printing): ``real``, ``integer``, ``complex_``, ``bool_``.\n\nThe other ``Type`` instances defined are:\n\n- ``intc``: Integer type used by C\'s "int".\n- ``intp``: Integer type used by C\'s "unsigned".\n- ``int8``, ``int16``, ``int32``, ``int64``: n-bit integers.\n- ``uint8``, ``uint16``, ``uint32``, ``uint64``: n-bit unsigned integers.\n- ``float80``: known as "extended precision" on modern x86/amd64 hardware.\n- ``complex64``: Complex number represented by two ``float32`` numbers\n- ``complex128``: Complex number represented by two ``float64`` numbers\n\nUsing the nodes\n---------------\n\nIt is possible to construct simple algorithms using the AST nodes. Let\'s construct a loop applying\nNewton\'s method::\n\n    >>> from sympy import symbols, cos\n    >>> from sympy.codegen.ast import While, Assignment, aug_assign, Print, QuotedString\n    >>> t, dx, x = symbols(\'tol delta val\')\n    >>> expr = cos(x) - x**3\n    >>> whl = While(abs(dx) > t, [\n    ...     Assignment(dx, -expr/expr.diff(x)),\n    ...     aug_assign(x, \'+\', dx),\n    ...     Print([x])\n    ... ])\n    >>> from sympy import pycode\n    >>> py_str = pycode(whl)\n    >>> print(py_str)\n    while (abs(delta) > tol):\n        delta = (val**3 - math.cos(val))/(-3*val**2 - math.sin(val))\n        val += delta\n        print(val)\n    >>> import math\n    >>> tol, val, delta = 1e-5, 0.5, float(\'inf\')\n    >>> exec(py_str)\n    1.1121416371\n    0.909672693737\n    0.867263818209\n    0.865477135298\n    0.865474033111\n    >>> print(\'%3.1g\' % (math.cos(val) - val**3))\n    -3e-11\n\nIf we want to generate Fortran code for the same while loop we simple call ``fcode``::\n\n    >>> from sympy import fcode\n    >>> print(fcode(whl, standard=2003, source_format=\'free\'))\n    do while (abs(delta) > tol)\n       delta = (val**3 - cos(val))/(-3*val**2 - sin(val))\n       val = val + delta\n       print *, val\n    end do\n\nThere is a function constructing a loop (or a complete function) like this in\n:mod:`sympy.codegen.algorithms`.\n\n'
from __future__ import annotations
from typing import Any
from collections import defaultdict
from sympy.core.relational import Ge, Gt, Le, Lt
from sympy.core import Symbol, Tuple, Dummy
from sympy.core.basic import Basic
from sympy.core.expr import Expr, Atom
from sympy.core.numbers import Float, Integer, oo
from sympy.core.sympify import _sympify, sympify, SympifyError
from sympy.utilities.iterables import iterable, topological_sort, numbered_symbols, filter_symbols

def _mk_Tuple(args):
    '''
    Create a SymPy Tuple object from an iterable, converting Python strings to
    AST strings.

    Parameters
    ==========

    args: iterable
        Arguments to :class:`sympy.Tuple`.

    Returns
    =======

    sympy.Tuple
    '''
    args = args()
# WARNING: Decompyle incomplete


class CodegenAST(Basic):
    __slots__ = ()


class Token(CodegenAST):
    pass
# WARNING: Decompyle incomplete


class BreakToken(Token):
    """ Represents 'break' in C/Python ('exit' in Fortran).

    Use the premade instance ``break_`` or instantiate manually.

    Examples
    ========

    >>> from sympy import ccode, fcode
    >>> from sympy.codegen.ast import break_
    >>> ccode(break_)
    'break'
    >>> fcode(break_, source_format='free')
    'exit'
    """
    pass

break_ = BreakToken()

class ContinueToken(Token):
    """ Represents 'continue' in C/Python ('cycle' in Fortran)

    Use the premade instance ``continue_`` or instantiate manually.

    Examples
    ========

    >>> from sympy import ccode, fcode
    >>> from sympy.codegen.ast import continue_
    >>> ccode(continue_)
    'continue'
    >>> fcode(continue_, source_format='free')
    'cycle'
    """
    pass

continue_ = ContinueToken()

class NoneToken(Token):
    pass
# WARNING: Decompyle incomplete

none = NoneToken()

class AssignmentBase(CodegenAST):
    pass
# WARNING: Decompyle incomplete


class Assignment(AssignmentBase):
    """
    Represents variable assignment for code generation.

    Parameters
    ==========

    lhs : Expr
        SymPy object representing the lhs of the expression. These should be
        singular objects, such as one would use in writing code. Notable types
        include Symbol, MatrixSymbol, MatrixElement, and Indexed. Types that
        subclass these types are also supported.

    rhs : Expr
        SymPy object representing the rhs of the expression. This can be any
        type, provided its shape corresponds to that of the lhs. For example,
        a Matrix type can be assigned to MatrixSymbol, but not to Symbol, as
        the dimensions will not align.

    Examples
    ========

    >>> from sympy import symbols, MatrixSymbol, Matrix
    >>> from sympy.codegen.ast import Assignment
    >>> x, y, z = symbols('x, y, z')
    >>> Assignment(x, y)
    Assignment(x, y)
    >>> Assignment(x, 0)
    Assignment(x, 0)
    >>> A = MatrixSymbol('A', 1, 3)
    >>> mat = Matrix([x, y, z]).T
    >>> Assignment(A, mat)
    Assignment(A, Matrix([[x, y, z]]))
    >>> Assignment(A[0, 1], x)
    Assignment(A[0, 1], x)
    """
    op = ':='


class AugmentedAssignment(AssignmentBase):
    '''
    Base class for augmented assignments.

    Attributes:
    ===========

    binop : str
       Symbol for binary operation being applied in the assignment, such as "+",
       "*", etc.
    '''
    binop = None
    op = (lambda self: self.binop + '=')()


class AddAugmentedAssignment(AugmentedAssignment):
    binop = '+'


class SubAugmentedAssignment(AugmentedAssignment):
    binop = '-'


class MulAugmentedAssignment(AugmentedAssignment):
    binop = '*'


class DivAugmentedAssignment(AugmentedAssignment):
    binop = '/'


class ModAugmentedAssignment(AugmentedAssignment):
    binop = '%'

augassign_classes = (AddAugmentedAssignment, SubAugmentedAssignment, MulAugmentedAssignment, DivAugmentedAssignment, ModAugmentedAssignment)()

def aug_assign(lhs, op, rhs):
    """
    Create 'lhs op= rhs'.

    Explanation
    ===========

    Represents augmented variable assignment for code generation. This is a
    convenience function. You can also use the AugmentedAssignment classes
    directly, like AddAugmentedAssignment(x, y).

    Parameters
    ==========

    lhs : Expr
        SymPy object representing the lhs of the expression. These should be
        singular objects, such as one would use in writing code. Notable types
        include Symbol, MatrixSymbol, MatrixElement, and Indexed. Types that
        subclass these types are also supported.

    op : str
        Operator (+, -, /, \\*, %).

    rhs : Expr
        SymPy object representing the rhs of the expression. This can be any
        type, provided its shape corresponds to that of the lhs. For example,
        a Matrix type can be assigned to MatrixSymbol, but not to Symbol, as
        the dimensions will not align.

    Examples
    ========

    >>> from sympy import symbols
    >>> from sympy.codegen.ast import aug_assign
    >>> x, y = symbols('x, y')
    >>> aug_assign(x, '+', y)
    AddAugmentedAssignment(x, y)
    """
    if op not in augassign_classes:
        raise ValueError('Unrecognized operator %s' % op)
    return augassign_classes[op](lhs, rhs)


class CodeBlock(CodegenAST):
    pass
# WARNING: Decompyle incomplete


class For(Token):
    '''Represents a \'for-loop\' in the code.

    Expressions are of the form:
        "for target in iter:
            body..."

    Parameters
    ==========

    target : symbol
    iter : iterable
    body : CodeBlock or iterable
!        When passed an iterable it is used to instantiate a CodeBlock.

    Examples
    ========

    >>> from sympy import symbols, Range
    >>> from sympy.codegen.ast import aug_assign, For
    >>> x, i, j, k = symbols(\'x i j k\')
    >>> for_i = For(i, Range(10), [aug_assign(x, \'+\', i*j*k)])
    >>> for_i  # doctest: -NORMALIZE_WHITESPACE
    For(i, iterable=Range(0, 10, 1), body=CodeBlock(
        AddAugmentedAssignment(x, i*j*k)
    ))
    >>> for_ji = For(j, Range(7), [for_i])
    >>> for_ji  # doctest: -NORMALIZE_WHITESPACE
    For(j, iterable=Range(0, 7, 1), body=CodeBlock(
        For(i, iterable=Range(0, 10, 1), body=CodeBlock(
            AddAugmentedAssignment(x, i*j*k)
        ))
    ))
    >>> for_kji =For(k, Range(5), [for_ji])
    >>> for_kji  # doctest: -NORMALIZE_WHITESPACE
    For(k, iterable=Range(0, 5, 1), body=CodeBlock(
        For(j, iterable=Range(0, 7, 1), body=CodeBlock(
            For(i, iterable=Range(0, 10, 1), body=CodeBlock(
                AddAugmentedAssignment(x, i*j*k)
            ))
        ))
    ))
    '''
    __slots__ = ('target', 'iterable', 'body')
    _fields = ('target', 'iterable', 'body')
    _construct_target = staticmethod(_sympify)
    _construct_body = (lambda cls, itr: if isinstance(itr, CodeBlock):
itr# WARNING: Decompyle incomplete
)()
    _construct_iterable = (lambda cls, itr: if not iterable(itr):
raise TypeError('iterable must be an iterable')if isinstance(itr, list):
itr = tuple(itr)_sympify(itr))()


class String(Token, Atom):
    """ SymPy object representing a string.

    Atomic object which is not an expression (as opposed to Symbol).

    Parameters
    ==========

    text : str

    Examples
    ========

    >>> from sympy.codegen.ast import String
    >>> f = String('foo')
    >>> f
    foo
    >>> str(f)
    'foo'
    >>> f.text
    'foo'
    >>> print(repr(f))
    String('foo')

    """
    __slots__ = ('text',)
    _fields = ('text',)
    not_in_args = [
        'text']
    is_Atom = True
    _construct_text = (lambda cls, text: if not isinstance(text, str):
raise TypeError('Argument text is not a string type.')text)()
    
    def _sympystr(self, printer, *args, **kwargs):
        return self.text

    
    def kwargs(self, exclude, apply = ((), None)):
        return { }

    func = (lambda self: pass# WARNING: Decompyle incomplete
)()
    
    def _latex(self, printer):
        latex_escape = latex_escape
        import sympy.printing.latex
        return '\\texttt{{"{}"}}'.format(latex_escape(self.text))



class QuotedString(String):
    ''' Represents a string which should be printed with quotes. '''
    pass


class Comment(String):
    ''' Represents a comment. '''
    pass


class Node(Token):
    """ Subclass of Token, carrying the attribute 'attrs' (Tuple)

    Examples
    ========

    >>> from sympy.codegen.ast import Node, value_const, pointer_const
    >>> n1 = Node([value_const])
    >>> n1.attr_params('value_const')  # get the parameters of attribute (by name)
    ()
    >>> from sympy.codegen.fnodes import dimension
    >>> n2 = Node([value_const, dimension(5, 3)])
    >>> n2.attr_params(value_const)  # get the parameters of attribute (by Attribute instance)
    ()
    >>> n2.attr_params('dimension')  # get the parameters of attribute (by name)
    (5, 3)
    >>> n2.attr_params(pointer_const) is None
    True

    """
    __slots__: 'tuple[str, ...]' = ('attrs',)
    _fields = __slots__
    defaults: 'dict[str, Any]' = {
        'attrs': Tuple() }
    _construct_attrs = staticmethod(_mk_Tuple)
    
    def attr_params(self, looking_for):
        ''' Returns the parameters of the Attribute with name ``looking_for`` in self.attrs '''
        for attr in self.attrs:
            if str(attr.name) == str(looking_for):
                
                return None, attr.parameters
            return None



class Type(Token):
    """ Represents a type.

    Explanation
    ===========

    The naming is a super-set of NumPy naming. Type has a classmethod
    ``from_expr`` which offer type deduction. It also has a method
    ``cast_check`` which casts the argument to its type, possibly raising an
    exception if rounding error is not within tolerances, or if the value is not
    representable by the underlying data type (e.g. unsigned integers).

    Parameters
    ==========

    name : str
        Name of the type, e.g. ``object``, ``int16``, ``float16`` (where the latter two
        would use the ``Type`` sub-classes ``IntType`` and ``FloatType`` respectively).
        If a ``Type`` instance is given, the said instance is returned.

    Examples
    ========

    >>> from sympy.codegen.ast import Type
    >>> t = Type.from_expr(42)
    >>> t
    integer
    >>> print(repr(t))
    IntBaseType(String('integer'))
    >>> from sympy.codegen.ast import uint8
    >>> uint8.cast_check(-1)   # doctest: +ELLIPSIS
    Traceback (most recent call last):
      ...
    ValueError: Minimum value for data type bigger than new value.
    >>> from sympy.codegen.ast import float32
    >>> v6 = 0.123456
    >>> float32.cast_check(v6)
    0.123456
    >>> v10 = 12345.67894
    >>> float32.cast_check(v10)  # doctest: +ELLIPSIS
    Traceback (most recent call last):
      ...
    ValueError: Casting gives a significantly different value.
    >>> boost_mp50 = Type('boost::multiprecision::cpp_dec_float_50')
    >>> from sympy import cxxcode
    >>> from sympy.codegen.ast import Declaration, Variable
    >>> cxxcode(Declaration(Variable('x', type=boost_mp50)))
    'boost::multiprecision::cpp_dec_float_50 x'

    References
    ==========

    .. [1] https://numpy.org/doc/stable/user/basics.types.html

    """
    __slots__: 'tuple[str, ...]' = ('name',)
    _fields = __slots__
    _construct_name = String
    
    def _sympystr(self, printer, *args, **kwargs):
        return str(self.name)

    from_expr = (lambda cls, expr: if isinstance(expr, (float, Float)):
realif None(expr, (int, Integer)) or getattr(expr, 'is_integer', False):
integerif None(expr, 'is_real', False):
realif None(expr, complex) or getattr(expr, 'is_complex', False):
complex_if None(expr, bool) or getattr(expr, 'is_Relational', False):
bool_raise None('Could not deduce type from expr.'))()
    
    def _check(self, value):
        pass

    
    def cast_check(self, value, rtol, atol, precision_targets = (None, 0, None)):
        """ Casts a value to the data type of the instance.

        Parameters
        ==========

        value : number
        rtol : floating point number
            Relative tolerance. (will be deduced if not given).
        atol : floating point number
            Absolute tolerance (in addition to ``rtol``).
        type_aliases : dict
            Maps substitutions for Type, e.g. {integer: int64, real: float32}

        Examples
        ========

        >>> from sympy.codegen.ast import integer, float32, int8
        >>> integer.cast_check(3.0) == 3
        True
        >>> float32.cast_check(1e-40)  # doctest: +ELLIPSIS
        Traceback (most recent call last):
          ...
        ValueError: Minimum value for data type bigger than new value.
        >>> int8.cast_check(256)  # doctest: +ELLIPSIS
        Traceback (most recent call last):
          ...
        ValueError: Maximum value for data type smaller than new value.
        >>> v10 = 12345.67894
        >>> float32.cast_check(v10)  # doctest: +ELLIPSIS
        Traceback (most recent call last):
          ...
        ValueError: Casting gives a significantly different value.
        >>> from sympy.codegen.ast import float64
        >>> float64.cast_check(v10)
        12345.67894
        >>> from sympy import Float
        >>> v18 = Float('0.123456789012345646')
        >>> float64.cast_check(v18)
        Traceback (most recent call last):
          ...
        ValueError: Casting gives a significantly different value.
        >>> from sympy.codegen.ast import float80
        >>> float80.cast_check(v18)
        0.123456789012345649

        """
        pass
    # WARNING: Decompyle incomplete

    
    def _latex(self, printer):
        latex_escape = latex_escape
        import sympy.printing.latex
        type_name = latex_escape(self.__class__.__name__)
        name = latex_escape(self.name.text)
        return '\\text{{{}}}\\left(\\texttt{{{}}}\\right)'.format(type_name, name)



class IntBaseType(Type):
    ''' Integer base type, contains no size information. '''
    __slots__ = ()
    
    cast_nocheck = lambda self, i: Integer(int(i))


class _SizedIntType(IntBaseType):
    __slots__ = ('nbits',)
    _fields = Type._fields + __slots__
    _construct_nbits = Integer
    
    def _check(self, value):
        if value < self.min:
            raise ValueError('Value is too small: %d < %d' % (value, self.min))
        if value > self.max:
            raise ValueError('Value is too big: %d > %d' % (value, self.max))



class SignedIntType(_SizedIntType):
    ''' Represents a signed integer type. '''
    __slots__ = ()
    min = (lambda self: -2 ** (self.nbits - 1))()
    max = (lambda self: 2 ** (self.nbits - 1) - 1)()


class UnsignedIntType(_SizedIntType):
    ''' Represents an unsigned integer type. '''
    __slots__ = ()
    min = (lambda self: 0)()
    max = (lambda self: 2 ** self.nbits - 1)()

two = Integer(2)

class FloatBaseType(Type):
    ''' Represents a floating point number type. '''
    __slots__ = ()
    cast_nocheck = Float


class FloatType(FloatBaseType):
    """ Represents a floating point type with fixed bit width.

    Base 2 & one sign bit is assumed.

    Parameters
    ==========

    name : str
        Name of the type.
    nbits : integer
        Number of bits used (storage).
    nmant : integer
        Number of bits used to represent the mantissa.
    nexp : integer
        Number of bits used to represent the mantissa.

    Examples
    ========

    >>> from sympy import S
    >>> from sympy.codegen.ast import FloatType
    >>> half_precision = FloatType('f16', nbits=16, nmant=10, nexp=5)
    >>> half_precision.max
    65504
    >>> half_precision.tiny == S(2)**-14
    True
    >>> half_precision.eps == S(2)**-10
    True
    >>> half_precision.dig == 3
    True
    >>> half_precision.decimal_dig == 5
    True
    >>> half_precision.cast_check(1.0)
    1.0
    >>> half_precision.cast_check(1e5)  # doctest: +ELLIPSIS
    Traceback (most recent call last):
      ...
    ValueError: Maximum value for data type smaller than new value.
    """
    __slots__ = ('nbits', 'nmant', 'nexp')
    _fields = Type._fields + __slots__
    _construct_nbits = Integer
    _construct_nmant = Integer
    _construct_nexp = Integer
    max_exponent = (lambda self: two ** (self.nexp - 1))()
    min_exponent = (lambda self: 3 - self.max_exponent)()
    max = (lambda self: (1 - two ** (-(self.nmant + 1))) * two ** self.max_exponent)()
    tiny = (lambda self: two ** (self.min_exponent - 1))()
    eps = (lambda self: two ** (-(self.nmant)))()
    dig = (lambda self: floor = floorlog = logimport sympy.functionsfloor(self.nmant * log(2) / log(10)))()
    decimal_dig = (lambda self: ceiling = ceilinglog = logimport sympy.functionsceiling((self.nmant + 1) * log(2) / log(10) + 1))()
    
    def cast_nocheck(self, value):
        ''' Casts without checking if out of bounds or subnormal. '''
        if value == oo:
            return float(oo)
        if None == -oo:
            return float(-oo)
        return None(str(sympify(value).evalf(self.decimal_dig)), self.decimal_dig)

    
    def _check(self, value):
        if value < -(self.max):
            raise ValueError('Value is too small: %d < %d' % (value, -(self.max)))
        if value > self.max:
            raise ValueError('Value is too big: %d > %d' % (value, self.max))
        if abs(value) < self.tiny:
            raise ValueError('Smallest (absolute) value for data type bigger than new value.')



class ComplexBaseType(FloatBaseType):
    pass
# WARNING: Decompyle incomplete


class ComplexType(FloatType, ComplexBaseType):
    ''' Represents a complex floating point number. '''
    __slots__ = ()

intc = IntBaseType('intc')
intp = IntBaseType('intp')
int8 = SignedIntType('int8', 8)
int16 = SignedIntType('int16', 16)
int32 = SignedIntType('int32', 32)
int64 = SignedIntType('int64', 64)
uint8 = UnsignedIntType('uint8', 8)
uint16 = UnsignedIntType('uint16', 16)
uint32 = UnsignedIntType('uint32', 32)
uint64 = UnsignedIntType('uint64', 64)
float16 = FloatType('float16', 16, nexp = 5, nmant = 10)
float32 = FloatType('float32', 32, nexp = 8, nmant = 23)
float64 = FloatType('float64', 64, nexp = 11, nmant = 52)
float80 = FloatType('float80', 80, nexp = 15, nmant = 63)
float128 = FloatType('float128', 128, nexp = 15, nmant = 112)
float256 = FloatType('float256', 256, nexp = 19, nmant = 236)
# WARNING: Decompyle incomplete

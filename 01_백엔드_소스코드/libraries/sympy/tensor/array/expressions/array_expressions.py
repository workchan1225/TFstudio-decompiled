# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: array_expressions.pyc (Python 3.11)

import collections.abc as collections
import operator
from collections import defaultdict, Counter
from functools import reduce
import itertools
from itertools import accumulate
from typing import Optional, List, Tuple as tTuple
import typing
from sympy.core.numbers import Integer
from sympy.core.relational import Equality
from sympy.functions.special.tensor_functions import KroneckerDelta
from sympy.core.basic import Basic
from sympy.core.containers import Tuple
from sympy.core.expr import Expr
from sympy.core.function import Function, Lambda
from sympy.core.mul import Mul
from sympy.core.singleton import S
from sympy.core.sorting import default_sort_key
from sympy.core.symbol import Dummy, Symbol
from sympy.matrices.matrixbase import MatrixBase
from sympy.matrices.expressions.diagonal import diagonalize_vector
from sympy.matrices.expressions.matexpr import MatrixExpr
from sympy.matrices.expressions.special import ZeroMatrix
from sympy.tensor.array.arrayop import permutedims, tensorcontraction, tensordiagonal, tensorproduct
from sympy.tensor.array.dense_ndim_array import ImmutableDenseNDimArray
from sympy.tensor.array.ndim_array import NDimArray
from sympy.tensor.indexed import Indexed, IndexedBase
from sympy.matrices.expressions.matexpr import MatrixElement
from sympy.tensor.array.expressions.utils import _apply_recursively_over_nested_lists, _sort_contraction_indices, _get_mapping_from_subranks, _build_push_indices_up_func_transformation, _get_contraction_links, _build_push_indices_down_func_transformation
from sympy.combinatorics import Permutation
from sympy.combinatorics.permutations import _af_invert
from sympy.core.sympify import _sympify

class _ArrayExpr(Expr):
    shape: tTuple[(Expr, ...)] = '_ArrayExpr'
    
    def __getitem__(self, item):
        if not isinstance(item, collections.abc.Iterable):
            item = (item,)
        ArrayElement._check_shape(self, item)
        return self._get(item)

    
    def _get(self, item):
        return _get_array_element_or_slice(self, item)



class ArraySymbol(_ArrayExpr):
    '''
    Symbol representing an array expression
    '''
    
    def __new__(cls = None, symbol = None, shape = None):
        if isinstance(symbol, str):
            symbol = Symbol(symbol)
    # WARNING: Decompyle incomplete

    name = (lambda self: self._args[0])()
    shape = (lambda self: self._args[1])()
    
    def as_explicit(self):
        pass
    # WARNING: Decompyle incomplete



class ArrayElement(Expr):
    '''
    An element of an array.
    '''
    _diff_wrt = True
    is_symbol = True
    is_commutative = True
    
    def __new__(cls, name, indices):
        if isinstance(name, str):
            name = Symbol(name)
        name = _sympify(name)
        if not isinstance(indices, collections.abc.Iterable):
            indices = (indices,)
        indices = _sympify(tuple(indices))
        cls._check_shape(name, indices)
        obj = Expr.__new__(cls, name, indices)
        return obj

    _check_shape = (lambda cls, name, indices: indices = tuple(indices)if hasattr(name, 'shape'):
index_error = IndexError('number of indices does not match shape of the array')if len(indices) != len(name.shape):
raise index_errorif (lambda .0: pass# WARNING: Decompyle incomplete
)(zip(indices, name.shape)()):
                raise ValueError('shape is out of bounds')
        if (lambda .0: pass# WARNING: Decompyle incomplete
)(indices()):
            raise ValueError('shape contains negative values')
)()
    name = (lambda self: self._args[0])()
    indices = (lambda self: self._args[1])()
    
    def _eval_derivative(self, s):
        if not isinstance(s, ArrayElement):
            return S.Zero
        if None == self:
            return S.One
        if None.name != self.name:
            return S.Zero
        return (lambda .0: pass# WARNING: Decompyle incomplete
)(zip(self.indices, s.indices)())



class ZeroArray(_ArrayExpr):
    '''
    Symbolic array of zeros. Equivalent to ``ZeroMatrix`` for matrices.
    '''
    
    def __new__(cls, *shape):
        if len(shape) == 0:
            return S.Zero
        shape = None(_sympify, shape)
    # WARNING: Decompyle incomplete

    shape = (lambda self: self._args)()
    
    def as_explicit(self):
        if not (lambda .0: pass# WARNING: Decompyle incomplete
)(self.shape()):
            raise ValueError('Cannot return explicit form for symbolic shape.')
    # WARNING: Decompyle incomplete

    
    def _get(self, item):
        return S.Zero



class OneArray(_ArrayExpr):
    '''
    Symbolic array of ones.
    '''
    
    def __new__(cls, *shape):
        if len(shape) == 0:
            return S.One
        shape = None(_sympify, shape)
    # WARNING: Decompyle incomplete

    shape = (lambda self: self._args)()
    
    def as_explicit(self):
        if not (lambda .0: pass# WARNING: Decompyle incomplete
)(self.shape()):
            raise ValueError('Cannot return explicit form for symbolic shape.')
    # WARNING: Decompyle incomplete

    
    def _get(self, item):
        return S.One



class _CodegenArrayAbstract(Basic):
    subranks = (lambda self: self._subranks[:])()
    
    def subrank(self):
        '''
        The sum of ``subranks``.
        '''
        return sum(self.subranks)

    shape = (lambda self: self._shape)()
    
    def doit(self, **hints):
        pass
    # WARNING: Decompyle incomplete



class ArrayTensorProduct(_CodegenArrayAbstract):
    '''
    Class to represent the tensor product of array-like objects.
    '''
    
    def __new__(cls, *args, **kwargs):
        args = args()
        canonicalize = kwargs.pop('canonicalize', False)
        ranks = args()
    # WARNING: Decompyle incomplete

    
    def _canonicalize(self):
        pass
    # WARNING: Decompyle incomplete

    _flatten = (lambda cls, args: pass# WARNING: Decompyle incomplete
)()
    
    def as_explicit(self):
        pass
    # WARNING: Decompyle incomplete



class ArrayAdd(_CodegenArrayAbstract):
    '''
    Class for elementwise array additions.
    '''
    
    def __new__(cls, *args, **kwargs):
        args = args()
        ranks = args()
        ranks = list(set(ranks))
        if len(ranks) != 1:
            raise ValueError('summing arrays of different ranks')
        shapes = args()
        if (lambda .0: pass# WARNING: Decompyle incomplete
)(shapes()) > 1:
            raise ValueError('mismatching shapes in addition')
        canonicalize = kwargs.pop('canonicalize', False)
    # WARNING: Decompyle incomplete

    
    def _canonicalize(self):
        args = self.args
        args = self._flatten_args(args)
        shapes = args()
        args = args()
    # WARNING: Decompyle incomplete

    _flatten_args = (lambda cls, args: new_args = []for arg in args:
if isinstance(arg, ArrayAdd):
new_args.extend(arg.args)continuenew_args.append(arg)new_args)()
    
    def as_explicit(self):
        
        def <listcomp>(.0):
            '''as_explicit'''
            for arg in .0:
                pass
            continue
            return arg.as_explicit()[arg]

        return operator.add(<listcomp>, self.args())



class PermuteDims(_CodegenArrayAbstract):
    '''
    Class to represent permutation of axes of arrays.

    Examples
    ========

    >>> from sympy.tensor.array import permutedims
    >>> from sympy import MatrixSymbol
    >>> M = MatrixSymbol("M", 3, 3)
    >>> cg = permutedims(M, [1, 0])

    The object ``cg`` represents the transposition of ``M``, as the permutation
    ``[1, 0]`` will act on its indices by switching them:

    `M_{ij} \\Rightarrow M_{ji}`

    This is evident when transforming back to matrix form:

    >>> from sympy.tensor.array.expressions.from_array_to_matrix import convert_array_to_matrix
    >>> convert_array_to_matrix(cg)
    M.T

    >>> N = MatrixSymbol("N", 3, 2)
    >>> cg = permutedims(N, [1, 0])
    >>> cg.shape
    (2, 3)

    There are optional parameters that can be used as alternative to the permutation:

    >>> from sympy.tensor.array.expressions import ArraySymbol, PermuteDims
    >>> M = ArraySymbol("M", (1, 2, 3, 4, 5))
    >>> expr = PermuteDims(M, index_order_old="ijklm", index_order_new="kijml")
    >>> expr
    PermuteDims(M, (0 2 1)(3 4))
    >>> expr.shape
    (3, 1, 2, 5, 4)

    Permutations of tensor products are simplified in order to achieve a
    standard form:

    >>> from sympy.tensor.array import tensorproduct
    >>> M = MatrixSymbol("M", 4, 5)
    >>> tp = tensorproduct(M, N)
    >>> tp.shape
    (4, 5, 3, 2)
    >>> perm1 = permutedims(tp, [2, 3, 1, 0])

    The args ``(M, N)`` have been sorted and the permutation has been
    simplified, the expression is equivalent:

    >>> perm1.expr.args
    (N, M)
    >>> perm1.shape
    (3, 2, 5, 4)
    >>> perm1.permutation
    (2 3)

    The permutation in its array form has been simplified from
    ``[2, 3, 1, 0]`` to ``[0, 1, 3, 2]``, as the arguments of the tensor
    product `M` and `N` have been switched:

    >>> perm1.permutation.array_form
    [0, 1, 3, 2]

    We can nest a second permutation:

    >>> perm2 = permutedims(perm1, [1, 0, 2, 3])
    >>> perm2.shape
    (2, 3, 5, 4)
    >>> perm2.permutation.array_form
    [1, 0, 3, 2]
    '''
    
    def __new__(cls, expr, permutation, index_order_old, index_order_new = (None, None, None), **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def _canonicalize(self):
        pass
    # WARNING: Decompyle incomplete

    expr = (lambda self: self.args[0])()
    permutation = (lambda self: self.args[1])()
    _PermuteDims_denestarg_ArrayTensorProduct = (lambda cls, expr, permutation: pass# WARNING: Decompyle incomplete
)()
    _PermuteDims_denestarg_ArrayContraction = (lambda cls, expr, permutation: pass# WARNING: Decompyle incomplete
)()
    _check_permutation_mapping = (lambda cls, expr, permutation: pass# WARNING: Decompyle incomplete
)()
    _check_if_there_are_closed_cycles = (lambda cls, expr, permutation: pass# WARNING: Decompyle incomplete
)()
    
    def nest_permutation(self):
        '''
        DEPRECATED.
        '''
        ret = self._nest_permutation(self.expr, self.permutation)
    # WARNING: Decompyle incomplete

    _nest_permutation = (lambda cls, expr, permutation: pass# WARNING: Decompyle incomplete
)()
    
    def as_explicit(self):
        expr = self.expr
        if hasattr(expr, 'as_explicit'):
            expr = expr.as_explicit()
        return permutedims(expr, self.permutation)

    _get_permutation_from_arguments = (lambda cls, permutation, index_order_old, index_order_new, dim: pass# WARNING: Decompyle incomplete
)()
    _get_permutation_from_index_orders = (lambda cls, index_order_old, index_order_new, dim: pass# WARNING: Decompyle incomplete
)()


class ArrayDiagonal(_CodegenArrayAbstract):
    '''
    Class to represent the diagonal operator.

    Explanation
    ===========

    In a 2-dimensional array it returns the diagonal, this looks like the
    operation:

    `A_{ij} \\rightarrow A_{ii}`

    The diagonal over axes 1 and 2 (the second and third) of the tensor product
    of two 2-dimensional arrays `A \\otimes B` is

    `\\Big[ A_{ab} B_{cd} \\Big]_{abcd} \\rightarrow \\Big[ A_{ai} B_{id} \\Big]_{adi}`

    In this last example the array expression has been reduced from
    4-dimensional to 3-dimensional. Notice that no contraction has occurred,
    rather there is a new index `i` for the diagonal, contraction would have
    reduced the array to 2 dimensions.

    Notice that the diagonalized out dimensions are added as new dimensions at
    the end of the indices.
    '''
    
    def __new__(cls, expr, *diagonal_indices, **kwargs):
        expr = _sympify(expr)
        diagonal_indices = diagonal_indices()
        canonicalize = kwargs.get('canonicalize', False)
        shape = get_shape(expr)
    # WARNING: Decompyle incomplete

    
    def _canonicalize(self):
        expr = self.expr
        diagonal_indices = self.diagonal_indices
        trivial_diags = diagonal_indices()
    # WARNING: Decompyle incomplete

    _validate = (lambda expr: pass# WARNING: Decompyle incomplete
)()
    _remove_trivial_dimensions = (lambda shape: pass# WARNING: Decompyle incomplete
)()
    expr = (lambda self: self.args[0])()
    diagonal_indices = (lambda self: self.args[1:])()
    _flatten = (lambda expr: pass# WARNING: Decompyle incomplete
)()
    _ArrayDiagonal_denest_ArrayAdd = (lambda cls, expr: pass# WARNING: Decompyle incomplete
)()
    _ArrayDiagonal_denest_ArrayDiagonal = (lambda cls, expr: pass# WARNING: Decompyle incomplete
)()
    _ArrayDiagonal_denest_PermuteDims = (lambda cls = classmethod, expr = classmethod: pass# WARNING: Decompyle incomplete
)()
    
    def _push_indices_down_nonstatic(self, indices):
        pass
    # WARNING: Decompyle incomplete

    
    def _push_indices_up_nonstatic(self, indices):
        pass
    # WARNING: Decompyle incomplete

    _push_indices_down = (lambda cls, diagonal_indices, indices, rank: pass# WARNING: Decompyle incomplete
)()
    _push_indices_up = (lambda cls, diagonal_indices, indices, rank: pass# WARNING: Decompyle incomplete
)()
    _get_positions_shape = (lambda cls, shape, diagonal_indices: pass# WARNING: Decompyle incomplete
)()
    
    def as_explicit(self):
        expr = self.expr
        if hasattr(expr, 'as_explicit'):
            expr = expr.as_explicit()
    # WARNING: Decompyle incomplete



class ArrayElementwiseApplyFunc(_CodegenArrayAbstract):
    
    def __new__(cls, function, element):
        if not isinstance(function, Lambda):
            d = Dummy('d')
            function = Lambda(d, function(d))
        obj = _CodegenArrayAbstract.__new__(cls, function, element)
        obj._subranks = _get_subranks(element)
        return obj

    function = (lambda self: self.args[0])()
    expr = (lambda self: self.args[1])()
    shape = (lambda self: self.expr.shape)()
    
    def _get_function_fdiff(self):
        d = Dummy('d')
        function = self.function(d)
        fdiff = function.diff(d)
        if isinstance(fdiff, Function):
            fdiff = type(fdiff)
        else:
            fdiff = Lambda(d, fdiff)
        return fdiff

    
    def as_explicit(self):
        expr = self.expr
        if hasattr(expr, 'as_explicit'):
            expr = expr.as_explicit()
        return expr.applyfunc(self.function)



class ArrayContraction(_CodegenArrayAbstract):
    '''
    This class is meant to represent contractions of arrays in a form easily
    processable by the code printers.
    '''
    
    def __new__(cls, expr, *contraction_indices, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def _canonicalize(self):
        pass
    # WARNING: Decompyle incomplete

    
    def __mul__(self, other):
        if other == 1:
            return self
        raise None('Product of N-dim arrays is not uniquely defined. Use another method.')

    
    def __rmul__(self, other):
        if other == 1:
            return self
        raise None('Product of N-dim arrays is not uniquely defined. Use another method.')

    _validate = (lambda expr: pass# WARNING: Decompyle incomplete
)()
    _push_indices_down = (lambda cls, contraction_indices, indices: flattened_contraction_indices = contraction_indices()flattened_contraction_indices.sort()transform = _build_push_indices_down_func_transformation(flattened_contraction_indices)_apply_recursively_over_nested_lists(transform, indices))()
    _push_indices_up = (lambda cls, contraction_indices, indices: flattened_contraction_indices = contraction_indices()flattened_contraction_indices.sort()transform = _build_push_indices_up_func_transformation(flattened_contraction_indices)_apply_recursively_over_nested_lists(transform, indices))()
    _lower_contraction_to_addends = (lambda cls, expr, contraction_indices: pass# WARNING: Decompyle incomplete
)()
    
    def split_multiple_contractions(self):
        '''
        Recognize multiple contractions and attempt at rewriting them as paired-contractions.

        This allows some contractions involving more than two indices to be
        rewritten as multiple contractions involving two indices, thus allowing
        the expression to be rewritten as a matrix multiplication line.

        Examples:

        * `A_ij b_j0 C_jk` ===> `A*DiagMatrix(b)*C`

        Care for:
        - matrix being diagonalized (i.e. `A_ii`)
        - vectors being diagonalized (i.e. `a_i0`)

        Multiple contractions can be split into matrix multiplications if
        not more than two arguments are non-diagonals or non-vectors.
        Vectors get diagonalized while diagonal matrices remain diagonal.
        The non-diagonal matrices can be at the beginning or at the end
        of the final matrix multiplication line.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def flatten_contraction_of_diagonal(self):
        pass
    # WARNING: Decompyle incomplete

    _get_free_indices_to_position_map = (lambda free_indices, contraction_indices: free_indices_to_position = { }flattened_contraction_indices = contraction_indices()counter = 0# WARNING: Decompyle incomplete
)()
    _get_index_shifts = (lambda expr: inner_contraction_indices = expr.contraction_indicesall_inner = inner_contraction_indices()all_inner.sort()total_rank = _get_subrank(expr)inner_rank = len(all_inner)outer_rank = total_rank - inner_rankshifts = range(outer_rank)()counter = 0pointer = 0# WARNING: Decompyle incomplete
)()
    _convert_outer_indices_to_inner_indices = (lambda expr: pass# WARNING: Decompyle incomplete
)()
    _flatten = (lambda expr: inner_contraction_indices = expr.contraction_indices# WARNING: Decompyle incomplete
)()
    _ArrayContraction_denest_ArrayContraction = (lambda cls, expr: pass# WARNING: Decompyle incomplete
)()
    _ArrayContraction_denest_ZeroArray = (lambda cls, expr: pass# WARNING: Decompyle incomplete
)()
    _ArrayContraction_denest_ArrayAdd = (lambda cls, expr: pass# WARNING: Decompyle incomplete
)()
    _ArrayContraction_denest_PermuteDims = (lambda cls, expr: pass# WARNING: Decompyle incomplete
)()
    _ArrayContraction_denest_ArrayDiagonal = (lambda cls = classmethod, expr = classmethod: pass# WARNING: Decompyle incomplete
)()
    _sort_fully_contracted_args = (lambda cls, expr, contraction_indices: pass# WARNING: Decompyle incomplete
)()
    
    def _get_contraction_tuples(self):
        '''
        Return tuples containing the argument index and position within the
        argument of the index position.

        Examples
        ========

        >>> from sympy import MatrixSymbol
        >>> from sympy.abc import N
        >>> from sympy.tensor.array import tensorproduct, tensorcontraction
        >>> A = MatrixSymbol("A", N, N)
        >>> B = MatrixSymbol("B", N, N)

        >>> cg = tensorcontraction(tensorproduct(A, B), (1, 2))
        >>> cg._get_contraction_tuples()
        [[(0, 1), (1, 0)]]

        Notes
        =====

        Here the contraction pair `(1, 2)` meaning that the 2nd and 3rd indices
        of the tensor product `A\\otimes B` are contracted, has been transformed
        into `(0, 1)` and `(1, 0)`, identifying the same indices in a different
        notation. `(0, 1)` is the second index (1) of the first argument (i.e.
                0 or `A`). `(1, 0)` is the first index (i.e. 0) of the second
        argument (i.e. 1 or `B`).
        '''
        pass
    # WARNING: Decompyle incomplete

    _contraction_tuples_to_contraction_indices = (lambda expr, contraction_tuples: pass# WARNING: Decompyle incomplete
)()
    free_indices = (lambda self: self._free_indices[:])()
    free_indices_to_position = (lambda self: dict(self._free_indices_to_position))()
    expr = (lambda self: self.args[0])()
    contraction_indices = (lambda self: self.args[1:])()
    
    def _contraction_indices_to_components(self):
        expr = self.expr
        if not isinstance(expr, ArrayTensorProduct):
            raise NotImplementedError('only for contractions of tensor products')
        ranks = expr.subranks
        mapping = { }
        counter = 0
        for i, rank in enumerate(ranks):
            for j in range(rank):
                mapping[counter] = (i, j)
                counter += 1
                return mapping

    
    def sort_args_by_name(self):
        '''
        Sort arguments in the tensor product so that their order is lexicographical.

        Examples
        ========

        >>> from sympy.tensor.array.expressions.from_matrix_to_array import convert_matrix_to_array
        >>> from sympy import MatrixSymbol
        >>> from sympy.abc import N
        >>> A = MatrixSymbol("A", N, N)
        >>> B = MatrixSymbol("B", N, N)
        >>> C = MatrixSymbol("C", N, N)
        >>> D = MatrixSymbol("D", N, N)

        >>> cg = convert_matrix_to_array(C*D*A*B)
        >>> cg
        ArrayContraction(ArrayTensorProduct(A, D, C, B), (0, 3), (1, 6), (2, 5))
        >>> cg.sort_args_by_name()
        ArrayContraction(ArrayTensorProduct(A, D, B, C), (0, 3), (1, 4), (2, 7))
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _get_contraction_links(self):
        '''
        Returns a dictionary of links between arguments in the tensor product
        being contracted.

        See the example for an explanation of the values.

        Examples
        ========

        >>> from sympy import MatrixSymbol
        >>> from sympy.abc import N
        >>> from sympy.tensor.array.expressions.from_matrix_to_array import convert_matrix_to_array
        >>> A = MatrixSymbol("A", N, N)
        >>> B = MatrixSymbol("B", N, N)
        >>> C = MatrixSymbol("C", N, N)
        >>> D = MatrixSymbol("D", N, N)

        Matrix multiplications are pairwise contractions between neighboring
        matrices:

        `A_{ij} B_{jk} C_{kl} D_{lm}`

        >>> cg = convert_matrix_to_array(A*B*C*D)
        >>> cg
        ArrayContraction(ArrayTensorProduct(B, C, A, D), (0, 5), (1, 2), (3, 6))

        >>> cg._get_contraction_links()
        {0: {0: (2, 1), 1: (1, 0)}, 1: {0: (0, 1), 1: (3, 0)}, 2: {1: (0, 0)}, 3: {0: (1, 1)}}

        This dictionary is interpreted as follows: argument in position 0 (i.e.
        matrix `A`) has its second index (i.e. 1) contracted to `(1, 0)`, that
        is argument in position 1 (matrix `B`) on the first index slot of `B`,
        this is the contraction provided by the index `j` from `A`.

        The argument in position 1 (that is, matrix `B`) has two contractions,
        the ones provided by the indices `j` and `k`, respectively the first
        and second indices (0 and 1 in the sub-dict).  The link `(0, 1)` and
        `(2, 0)` respectively. `(0, 1)` is the index slot 1 (the 2nd) of
        argument in position 0 (that is, `A_{\\ldot j}`), and so on.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def as_explicit(self):
        expr = self.expr
        if hasattr(expr, 'as_explicit'):
            expr = expr.as_explicit()
    # WARNING: Decompyle incomplete



class Reshape(_CodegenArrayAbstract):
    '''
    Reshape the dimensions of an array expression.

    Examples
    ========

    >>> from sympy.tensor.array.expressions import ArraySymbol, Reshape
    >>> A = ArraySymbol("A", (6,))
    >>> A.shape
    (6,)
    >>> Reshape(A, (3, 2)).shape
    (3, 2)

    Check the component-explicit forms:

    >>> A.as_explicit()
    [A[0], A[1], A[2], A[3], A[4], A[5]]
    >>> Reshape(A, (3, 2)).as_explicit()
    [[A[0], A[1]], [A[2], A[3]], [A[4], A[5]]]

    '''
    
    def __new__(cls, expr, shape):
        expr = _sympify(expr)
    # WARNING: Decompyle incomplete

    shape = (lambda self: self._shape)()
    expr = (lambda self: self._expr)()
    
    def doit(self, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def as_explicit(self):
        ee = self.expr
        if hasattr(ee, 'as_explicit'):
            ee = ee.as_explicit()
        if isinstance(ee, MatrixBase):
            Array = Array
            import sympy
            ee = Array(ee)
        elif isinstance(ee, MatrixExpr):
            return self
    # WARNING: Decompyle incomplete



class _ArgE:
    indices: List[Optional[int]] = '\n    The ``_ArgE`` object contains references to the array expression\n    (``.element``) and a list containing the information about index\n    contractions (``.indices``).\n\n    Index contractions are numbered and contracted indices show the number of\n    the contraction. Uncontracted indices have ``None`` value.\n\n    For example:\n    ``_ArgE(M, [None, 3])``\n    This object means that expression ``M`` is part of an array contraction\n    and has two indices, the first is not contracted (value ``None``),\n    the second index is contracted to the 4th (i.e. number ``3``) group of the\n    array contraction object.\n    '
    
    def __init__(self = None, element = None, indices = None):
        self.element = element
    # WARNING: Decompyle incomplete

    
    def __str__(self):
        return f'''_ArgE({self.element!s}, {self.indices!s})'''

    __repr__ = __str__


class _IndPos:
    '''
    Index position, requiring two integers in the constructor:

    - arg: the position of the argument in the tensor product,
    - rel: the relative position of the index inside the argument.
    '''
    
    def __init__(self = None, arg = None, rel = None):
        self.arg = arg
        self.rel = rel

    
    def __str__(self):
        return '_IndPos(%i, %i)' % (self.arg, self.rel)

    __repr__ = __str__
    
    def __iter__(self):
        pass
    # WARNING: Decompyle incomplete



class _EditArrayContraction:
    '''
    Utility class to help manipulate array contraction objects.

    This class takes as input an ``ArrayContraction`` object and turns it into
    an editable object.

    The field ``args_with_ind`` of this class is a list of ``_ArgE`` objects
    which can be used to easily edit the contraction structure of the
    expression.

    Once editing is finished, the ``ArrayContraction`` object may be recreated
    by calling the ``.to_array_contraction()`` method.
    '''
    
    def __init__(self = None, base_array = None):
        if isinstance(base_array, ArrayContraction):
            mapping = _get_mapping_from_subranks(base_array.subranks)
            expr = base_array.expr
            contraction_indices = base_array.contraction_indices
            diagonalized = ()
        elif isinstance(base_array, ArrayDiagonal):
            if isinstance(base_array.expr, ArrayContraction):
                mapping = _get_mapping_from_subranks(base_array.expr.subranks)
                expr = base_array.expr.expr
                diagonalized = ArrayContraction._push_indices_down(base_array.expr.contraction_indices, base_array.diagonal_indices)
                contraction_indices = base_array.expr.contraction_indices
            elif isinstance(base_array.expr, ArrayTensorProduct):
                mapping = { }
                expr = base_array.expr
                diagonalized = base_array.diagonal_indices
                contraction_indices = []
            else:
                mapping = { }
                expr = base_array.expr
                diagonalized = base_array.diagonal_indices
                contraction_indices = []
        elif isinstance(base_array, ArrayTensorProduct):
            expr = base_array
            contraction_indices = []
            diagonalized = ()
        else:
            raise NotImplementedError()
        if isinstance(expr, ArrayTensorProduct):
            args = list(expr.args)
        else:
            args = [
                expr]
        args_with_ind = args()
        for i, contraction_tuple in enumerate(contraction_indices):
            for j in contraction_tuple:
                (arg_pos, rel_pos) = mapping[j]
                args_with_ind[arg_pos].indices[rel_pos] = i
                self.args_with_ind = args_with_ind
                self.number_of_contraction_indices = len(contraction_indices)
                self._track_permutation = None
                mapping = _get_mapping_from_subranks(base_array.subranks)
                for i, e in enumerate(diagonalized):
                    for j in e:
                        (arg_pos, rel_pos) = mapping[j]
                        self.args_with_ind[arg_pos].indices[rel_pos] = -1 - i
                        return None

    
    def insert_after(self = None, arg = None, new_arg = None):
        pos = self.args_with_ind.index(arg)
        self.args_with_ind.insert(pos + 1, new_arg)

    
    def get_new_contraction_index(self):
        return self.number_of_contraction_indices - 1

    
    def refresh_indices(self):
        pass
    # WARNING: Decompyle incomplete

    
    def merge_scalars(self):
        scalars = []
        for arg_with_ind in self.args_with_ind:
            if len(arg_with_ind.indices) == 0:
                scalars.append(arg_with_ind)
            for i in scalars:
                self.args_with_ind.remove(i)
                scalar = (lambda .0: [ i.element for i in .0 ])(scalars())
                if len(self.args_with_ind) == 0:
                    self.args_with_ind.append(_ArgE(scalar))
                    return None
                _a2m_tensor_product = _a2m_tensor_product
                import sympy.tensor.array.expressions.from_array_to_matrix
                self.args_with_ind[0].element = _a2m_tensor_product(scalar, self.args_with_ind[0].element)
                return None

    
    def to_array_contraction(self):
        counter = 0
        diag_indices = defaultdict(list)
        count_index_freq = Counter()
    # WARNING: Decompyle incomplete

    
    def get_contraction_indices(self = None):
        contraction_indices = range(self.number_of_contraction_indices)()
        current_position = 0
    # WARNING: Decompyle incomplete

    
    def get_mapping_for_index(self = None, ind = None):
        if ind >= self.number_of_contraction_indices:
            raise ValueError('index value exceeding the index range')
        positions = []
        for i, arg_with_ind in enumerate(self.args_with_ind):
            for j, arg_ind in enumerate(arg_with_ind.indices):
                if ind == arg_ind:
                    positions.append(_IndPos(i, j))
                return positions

    
    def get_contraction_indices_to_ind_rel_pos(self = None):
        contraction_indices = range(self.number_of_contraction_indices)()
    # WARNING: Decompyle incomplete

    
    def count_args_with_index(self = None, index = None):
        '''
        Count the number of arguments that have the given index.
        '''
        counter = 0
        for arg_with_ind in self.args_with_ind:
            if index in arg_with_ind.indices:
                counter += 1
            return counter

    
    def get_args_with_index(self = None, index = None):
        '''
        Get a list of arguments having the given index.
        '''
        pass
    # WARNING: Decompyle incomplete

    number_of_diagonal_indices = (lambda self: data = set()for arg in self.args_with_ind:
(lambda .0: pass# WARNING: Decompyle incomplete
)(arg.indices())
            return len(data)
)()
    
    def track_permutation_start(self):
        pass
    # WARNING: Decompyle incomplete

    
    def track_permutation_merge(self = None, destination = None, from_element = property):
        index_destination = self.args_with_ind.index(destination)
        index_element = self.args_with_ind.index(from_element)
        self._track_permutation[index_destination].extend(self._track_permutation[index_element])
        self._track_permutation.pop(index_element)

    
    def get_absolute_free_range(self = None, arg = None):
        '''
        Return the range of the free indices of the arg as absolute positions
        among all free indices.
        '''
        counter = 0
        for arg_with_ind in self.args_with_ind:
            number_free_indices = (lambda .0: pass# WARNING: Decompyle incomplete
)(arg_with_ind.indices())
            if arg_with_ind == arg:
                
                return len, (counter, counter + number_free_indices)
            raise IndexError('argument not found')

    
    def get_absolute_range(self = None, arg = None):
        '''
        Return the absolute range of indices for arg, disregarding dummy
        indices.
        '''
        counter = 0
        for arg_with_ind in self.args_with_ind:
            number_indices = len(arg_with_ind.indices)
            if arg_with_ind == arg:
                
                return None, (counter, counter + number_indices)
            raise IndexError('argument not found')



def get_rank(expr):
    if isinstance(expr, (MatrixExpr, MatrixElement)):
        return 2
    if None(expr, _CodegenArrayAbstract):
        return len(expr.shape)
    if None(expr, NDimArray):
        return expr.rank()
    if None(expr, Indexed):
        return expr.rank
# WARNING: Decompyle incomplete


def _get_subrank(expr):
    if isinstance(expr, _CodegenArrayAbstract):
        return expr.subrank()
    return None(expr)


def _get_subranks(expr):
    if isinstance(expr, _CodegenArrayAbstract):
        return expr.subranks
    return [
        None(expr)]


def get_shape(expr):
    if hasattr(expr, 'shape'):
        return expr.shape


def nest_permutation(expr):
    if isinstance(expr, PermuteDims):
        return expr.nest_permutation()


def _array_tensor_product(*args, **kwargs):
    pass
# WARNING: Decompyle incomplete


def _array_contraction(expr, *contraction_indices, **kwargs):
    pass
# WARNING: Decompyle incomplete


def _array_diagonal(expr, *diagonal_indices, **kwargs):
    pass
# WARNING: Decompyle incomplete


def _permute_dims(expr, permutation, **kwargs):
    pass
# WARNING: Decompyle incomplete


def _array_add(*args, **kwargs):
    pass
# WARNING: Decompyle incomplete


def _get_array_element_or_slice(expr, indices):
    return ArrayElement(expr, indices)

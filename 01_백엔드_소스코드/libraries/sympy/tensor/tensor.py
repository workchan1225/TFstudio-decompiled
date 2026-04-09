# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tensor.pyc (Python 3.11)

'''
This module defines tensors with abstract index notation.

The abstract index notation has been first formalized by Penrose.

Tensor indices are formal objects, with a tensor type; there is no
notion of index range, it is only possible to assign the dimension,
used to trace the Kronecker delta; the dimension can be a Symbol.

The Einstein summation convention is used.
The covariant indices are indicated with a minus sign in front of the index.

For instance the tensor ``t = p(a)*A(b,c)*q(-c)`` has the index ``c``
contracted.

A tensor expression ``t`` can be called; called with its
indices in sorted order it is equal to itself:
in the above example ``t(a, b) == t``;
one can call ``t`` with different indices; ``t(c, d) == p(c)*A(d,a)*q(-a)``.

The contracted indices are dummy indices, internally they have no name,
the indices being represented by a graph-like structure.

Tensors are put in canonical form using ``canon_bp``, which uses
the Butler-Portugal algorithm for canonicalization using the monoterm
symmetries of the tensors.

If there is a (anti)symmetric metric, the indices can be raised and
lowered when the tensor is put in canonical form.
'''
from __future__ import annotations
from typing import Any
from functools import reduce
from math import prod
from abc import abstractmethod, ABC
from collections import defaultdict
import operator
import itertools
from sympy.core.numbers import Integer, Rational
from sympy.combinatorics import Permutation
from sympy.combinatorics.tensor_can import get_symmetric_group_sgs, bsgs_direct_product, canonicalize, riemann_bsgs
from sympy.core import Basic, Expr, sympify, Add, Mul, S
from sympy.core.cache import clear_cache
from sympy.core.containers import Tuple, Dict
from sympy.core.sorting import default_sort_key
from sympy.core.symbol import Symbol, symbols
from sympy.core.sympify import CantSympify, _sympify
from sympy.core.operations import AssocOp
from sympy.external.gmpy import SYMPY_INTS
from sympy.matrices import eye
from sympy.utilities.exceptions import sympy_deprecation_warning, SymPyDeprecationWarning, ignore_warnings
from sympy.utilities.decorator import memoize_property, deprecated
from sympy.utilities.iterables import sift

def deprecate_data():
    sympy_deprecation_warning('\n        The data attribute of TensorIndexType is deprecated. Use The\n        replace_with_arrays() method instead.\n        ', deprecated_since_version = '1.4', active_deprecations_target = 'deprecated-tensorindextype-attrs', stacklevel = 4)


def deprecate_fun_eval():
    sympy_deprecation_warning('\n        The Tensor.fun_eval() method is deprecated. Use\n        Tensor.substitute_indices() instead.\n        ', deprecated_since_version = '1.5', active_deprecations_target = 'deprecated-tensor-fun-eval', stacklevel = 4)


def deprecate_call():
    sympy_deprecation_warning('\n        Calling a tensor like Tensor(*indices) is deprecated. Use\n        Tensor.substitute_indices() instead.\n        ', deprecated_since_version = '1.5', active_deprecations_target = 'deprecated-tensor-fun-eval', stacklevel = 4)


class _IndexStructure(CantSympify):
    '''
    This class handles the indices (free and dummy ones). It contains the
    algorithms to manage the dummy indices replacements and contractions of
    free indices under multiplications of tensor expressions, as well as stuff
    related to canonicalization sorting, getting the permutation of the
    expression and so on. It also includes tools to get the ``TensorIndex``
    objects corresponding to the given index structure.
    '''
    
    def __init__(self, free, dum, index_types, indices, canon_bp = (False,)):
        self.free = free
        self.dum = dum
        self.index_types = index_types
        self.indices = indices
        self._ext_rank = len(self.free) + 2 * len(self.dum)
        self.dum.sort(key = (lambda x: x[0]))

    from_indices = (lambda : pass# WARNING: Decompyle incomplete
)()
    from_components_free_dum = (lambda components, free, dum: index_types = []for component in components:
index_types.extend(component.index_types)indices = _IndexStructure.generate_indices_from_free_dum_index_types(free, dum, index_types)_IndexStructure(free, dum, index_types, indices))()
    _free_dum_from_indices = (lambda : pass# WARNING: Decompyle incomplete
)()
    
    def get_indices(self):
        '''
        Get a list of indices, creating new tensor indices to complete dummy indices.
        '''
        return self.indices[:]

    generate_indices_from_free_dum_index_types = (lambda free, dum, index_types: indices = [
None] * (len(free) + 2 * len(dum))for idx, pos in free:
indices[pos] = idxgenerate_dummy_name = _IndexStructure._get_generator_for_dummy_indices(free)for pos1, pos2 in dum:
typ1 = index_types[pos1]indname = generate_dummy_name(typ1)indices[pos1] = TensorIndex(indname, typ1, True)indices[pos2] = TensorIndex(indname, typ1, False)_IndexStructure._replace_dummy_names(indices, free, dum))()
    _get_generator_for_dummy_indices = (lambda free: pass# WARNING: Decompyle incomplete
)()
    _replace_dummy_names = (lambda indices, free, dum: dum.sort(key = (lambda x: x[0]))
        new_indices = list(indices)
    # WARNING: Decompyle incomplete
)()
    
    def get_free_indices(self = staticmethod):
        '''
        Get a list of free indices.
        '''
        free = sorted(self.free, key = (lambda x: x[1]))
        return free()

    
    def __str__(self):
        return '_IndexStructure({}, {}, {})'.format(self.free, self.dum, self.index_types)

    
    def __repr__(self):
        return self.__str__()

    
    def _get_sorted_free_indices_for_canon(self):
        sorted_free = self.free[:]
        sorted_free.sort(key = (lambda x: x[0]))
        return sorted_free

    
    def _get_sorted_dum_indices_for_canon(self):
        return sorted(self.dum, key = (lambda x: x[0]))

    
    def _get_lexicographically_sorted_index_types(self):
        permutation = self.indices_canon_args()[0]
        index_types = [
            None] * self._ext_rank
        for i, it in enumerate(self.index_types):
            index_types[permutation(i)] = it
            return index_types

    
    def _get_lexicographically_sorted_indices(self):
        permutation = self.indices_canon_args()[0]
        indices = [
            None] * self._ext_rank
        for i, it in enumerate(self.indices):
            indices[permutation(i)] = it
            return indices

    
    def perm2tensor(self, g, is_canon_bp = (False,)):
        '''
        Returns a ``_IndexStructure`` instance corresponding to the permutation ``g``.

        Explanation
        ===========

        ``g``  permutation corresponding to the tensor in the representation
        used in canonicalization

        ``is_canon_bp``   if True, then ``g`` is the permutation
        corresponding to the canonical form of the tensor
        '''
        sorted_free = self._get_sorted_free_indices_for_canon()()
        lex_index_types = self._get_lexicographically_sorted_index_types()
        lex_indices = self._get_lexicographically_sorted_indices()
        nfree = len(sorted_free)
        rank = self._ext_rank
        dum = range((rank - nfree) // 2)()
        free = []
        index_types = [
            None] * rank
        indices = [
            None] * rank
    # WARNING: Decompyle incomplete

    
    def indices_canon_args(self):
        '''
        Returns ``(g, dummies, msym, v)``, the entries of ``canonicalize``

        See ``canonicalize`` in ``tensor_can.py`` in combinatorics module.
        '''
        _af_new = _af_new
        import sympy.combinatorics.permutations
        n = self._ext_rank
        g = [
            None] * n + [
            n,
            n + 1]
        
        def metric_symmetry_to_msym(metric):
            pass
        # WARNING: Decompyle incomplete

        for indx, ipos in enumerate(self._get_sorted_free_indices_for_canon()):
            g[ipos] = i
            pos = len(self.free)
            j = len(self.free)
            dummies = []
            prev = None
            a = []
            msym = []
            for ipos1, ipos2 in self._get_sorted_dum_indices_for_canon():
                g[ipos1] = j
                g[ipos2] = j + 1
                j += 2
                typ = self.index_types[ipos1]
                if typ != prev:
                    if a:
                        dummies.append(a)
                    a = [
                        pos,
                        pos + 1]
                    prev = typ
                    msym.append(metric_symmetry_to_msym(typ.metric))
                else:
                    a.extend([
                        pos,
                        pos + 1])
                pos += 2
                if a:
                    dummies.append(a)
        return (_af_new(g), dummies, msym)



def components_canon_args(components):
    numtyp = []
    prev = None
    for t in components:
        if t == prev:
            continue
        t = None
        numtyp.append([
            prev,
            1])
        v = []
        for h, n in numtyp:
            if h.comm in (0, 1):
                comm = h.comm
            else:
                comm = TensorManager.get_comm(h.comm, h.comm)
            v.append((h.symmetry.base, h.symmetry.generators, n, comm))
            return v


class _TensorDataLazyEvaluator(CantSympify):
    '''
    EXPERIMENTAL: do not rely on this class, it may change without deprecation
    warnings in future versions of SymPy.

    Explanation
    ===========

    This object contains the logic to associate components data to a tensor
    expression. Components data are set via the ``.data`` property of tensor
    expressions, is stored inside this class as a mapping between the tensor
    expression and the ``ndarray``.

    Computations are executed lazily: whereas the tensor expressions can have
    contractions, tensor products, and additions, components data are not
    computed until they are accessed by reading the ``.data`` property
    associated to the tensor expression.
    '''
    _substitutions_dict: 'dict[Any, Any]' = { }
    _substitutions_dict_tensmul: 'dict[Any, Any]' = { }
    
    def __getitem__(self, key):
        dat = self._get(key)
    # WARNING: Decompyle incomplete

    
    def _get(self, key):
        '''
        Retrieve ``data`` associated with ``key``.

        Explanation
        ===========

        This algorithm looks into ``self._substitutions_dict`` for all
        ``TensorHead`` in the ``TensExpr`` (or just ``TensorHead`` if key is a
        TensorHead instance). It reconstructs the components data that the
        tensor expression should have by performing on components data the
        operations that correspond to the abstract tensor operations applied.

        Metric tensor is handled in a different manner: it is pre-computed in
        ``self._substitutions_dict_tensmul``.
        '''
        pass
    # WARNING: Decompyle incomplete

    data_contract_dum = (lambda ndarray_list, dum, ext_rank: tensorproduct = tensorproducttensorcontraction = tensorcontractionMutableDenseNDimArray = MutableDenseNDimArrayimport arrayarrays = list(map(MutableDenseNDimArray, ndarray_list))# WARNING: Decompyle incomplete
)()
    
    def data_tensorhead_from_tensmul(self, data, tensmul, tensorhead):
        '''
        This method is used when assigning components data to a ``TensMul``
        object, it converts components data to a fully contravariant ndarray,
        which is then stored according to the ``TensorHead`` key.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def data_from_tensor(self, tensor):
        '''
        This method corrects the components data to the right signature
        (covariant/contravariant) using the metric associated with each
        ``TensorIndexType``.
        '''
        tensorhead = tensor.component
    # WARNING: Decompyle incomplete

    
    def _assign_data_to_tensor_expr(self, key, data):
        if isinstance(key, TensAdd):
            raise ValueError('cannot assign data to TensAdd')
        if len(key.components) != 1:
            raise ValueError('cannot assign data to TensMul with multiple components')
        tensorhead = key.components[0]
        newdata = self.data_tensorhead_from_tensmul(data, key, tensorhead)
        return (tensorhead, newdata)

    
    def _check_permutations_on_data(self, tens, data):
        permutedims = permutedims
        import array
        Flatten = Flatten
        import array.arrayop
        if isinstance(tens, TensorHead):
            rank = tens.rank
            generators = tens.symmetry.generators
        elif isinstance(tens, Tensor):
            rank = tens.rank
            generators = tens.components[0].symmetry.generators
        elif isinstance(tens, TensorIndexType):
            rank = tens.metric.rank
            generators = tens.metric.symmetry.generators
        for gener in generators:
            sign_change = 1 if gener(rank) == rank else -1
            data_swapped = data
            last_data = data
            permute_axes = list(map(gener, range(rank)))
            for i in range(gener.order() - 1):
                data_swapped = permutedims(data_swapped, permute_axes)
                if any(Flatten(last_data - sign_change * data_swapped)):
                    raise ValueError('Component data symmetry structure error')
                last_data = data_swapped
                return None

    
    def __setitem__(self, key, value):
        '''
        Set the components data of a tensor object/expression.

        Explanation
        ===========

        Components data are transformed to the all-contravariant form and stored
        with the corresponding ``TensorHead`` object. If a ``TensorHead`` object
        cannot be uniquely identified, it will raise an error.
        '''
        data = _TensorDataLazyEvaluator.parse_data(value)
        self._check_permutations_on_data(key, data)
        if not isinstance(key, (TensorHead, TensorIndexType)):
            (key, data) = self._assign_data_to_tensor_expr(key, data)
    # WARNING: Decompyle incomplete

    
    def __delitem__(self, key):
        del self._substitutions_dict[key]

    
    def __contains__(self, key):
        return key in self._substitutions_dict

    
    def add_metric_data(self, metric, data):
        '''
        Assign data to the ``metric`` tensor. The metric tensor behaves in an
        anomalous way when raising and lowering indices.

        Explanation
        ===========

        A fully covariant metric is the inverse transpose of the fully
        contravariant metric (it is meant matrix inverse). If the metric is
        symmetric, the transpose is not necessary and mixed
        covariant/contravariant metrics are Kronecker deltas.
        '''
        self._substitutions_dict_tensmul[(metric, True, True)] = data
        inverse_transpose = self.inverse_transpose_matrix(data)
        self._substitutions_dict_tensmul[(metric, False, False)] = inverse_transpose
        m = data.tomatrix()
        invt = inverse_transpose.tomatrix()
        self._substitutions_dict_tensmul[(metric, True, False)] = m * invt
        self._substitutions_dict_tensmul[(metric, False, True)] = invt * m

    _flip_index_by_metric = (lambda data, metric, pos: tensorproduct = tensorproducttensorcontraction = tensorcontractionimport arraymdim = metric.rank()ddim = data.rank()if pos == 0:
data = tensorcontraction(tensorproduct(metric, data), (1, mdim + pos))else:
data = tensorcontraction(tensorproduct(data, metric), (pos, ddim))data)()
    inverse_matrix = (lambda ndarray: m = ndarray.tomatrix().inv()_TensorDataLazyEvaluator.parse_data(m))()
    inverse_transpose_matrix = (lambda ndarray: m = ndarray.tomatrix().inv().T_TensorDataLazyEvaluator.parse_data(m))()
    _correct_signature_from_indices = (lambda data, indices, free, dum, inverse = (False,): for i, indx in enumerate(indices):
if not indx.is_up and inverse:
data = _TensorDataLazyEvaluator._flip_index_by_metric(data, indx.tensor_index_type.data, i)continueif indx.is_up and inverse:
data = _TensorDataLazyEvaluator._flip_index_by_metric(data, _TensorDataLazyEvaluator.inverse_matrix(indx.tensor_index_type.data), i)data)()
    _sort_data_axes = (lambda old, new: permutedims = permutedimsimport arraynew_data = old.data.copy()old_free = old.free()new_free = new.free()for i in range(len(new_free)):
for j in range(i, len(old_free)):
if old_free[j] == new_free[i]:
old_free[i], old_free[j] = old_free[j], old_free[i]new_data = permutedims(new_data, (i, j))(lambda .0: [ i[0] for i in .0 ])
                
                return new_data
)()
    add_rearrange_tensmul_parts = (lambda new_tensmul, old_tensmul: pass# WARNING: Decompyle incomplete
)()
    parse_data = (lambda data: MutableDenseNDimArray = MutableDenseNDimArrayimport arrayif not isinstance(data, MutableDenseNDimArray):
if len(data) == 2 and hasattr(data[0], '__call__'):
data = MutableDenseNDimArray(data[0], data[1])else:
data = MutableDenseNDimArray(data)data)()

_tensor_data_substitution_dict = _TensorDataLazyEvaluator()

class _TensorManager:
    '''
    Class to manage tensor properties.

    Notes
    =====

    Tensors belong to tensor commutation groups; each group has a label
    ``comm``; there are predefined labels:

    ``0``   tensors commuting with any other tensor

    ``1``   tensors anticommuting among themselves

    ``2``   tensors not commuting, apart with those with ``comm=0``

    Other groups can be defined using ``set_comm``; tensors in those
    groups commute with those with ``comm=0``; by default they
    do not commute with any other group.
    '''
    
    def __init__(self):
        self._comm_init()

    
    def _comm_init(self):
        self._comm = range(3)()
        for i in range(3):
            self._comm[0][i] = 0
            self._comm[i][0] = 0
            self._comm[1][1] = 1
            self._comm[2][1] = None
            self._comm[1][2] = None
            self._comm_symbols2i = {
                0: 0,
                1: 1,
                2: 2 }
            self._comm_i2symbol = {
                0: 0,
                1: 1,
                2: 2 }
            return None

    comm = (lambda self: self._comm)()
    
    def comm_symbols2i(self, i):
        '''
        Get the commutation group number corresponding to ``i``.

        ``i`` can be a symbol or a number or a string.

        If ``i`` is not already defined its commutation group number
        is set.
        '''
        if i not in self._comm_symbols2i:
            n = len(self._comm)
            self._comm.append({ })
            self._comm[n][0] = 0
            self._comm[0][n] = 0
            self._comm_symbols2i[i] = n
            self._comm_i2symbol[n] = i
            return n
        return None._comm_symbols2i[i]

    
    def comm_i2symbol(self, i):
        '''
        Returns the symbol corresponding to the commutation group number.
        '''
        return self._comm_i2symbol[i]

    
    def set_comm(self, i, j, c):
        """
        Set the commutation parameter ``c`` for commutation groups ``i, j``.

        Parameters
        ==========

        i, j : symbols representing commutation groups

        c  :  group commutation number

        Notes
        =====

        ``i, j`` can be symbols, strings or numbers,
        apart from ``0, 1`` and ``2`` which are reserved respectively
        for commuting, anticommuting tensors and tensors not commuting
        with any other group apart with the commuting tensors.
        For the remaining cases, use this method to set the commutation rules;
        by default ``c=None``.

        The group commutation number ``c`` is assigned in correspondence
        to the group commutation symbols; it can be

        0        commuting

        1        anticommuting

        None     no commutation property

        Examples
        ========

        ``G`` and ``GH`` do not commute with themselves and commute with
        each other; A is commuting.

        >>> from sympy.tensor.tensor import TensorIndexType, tensor_indices, TensorHead, TensorManager, TensorSymmetry
        >>> Lorentz = TensorIndexType('Lorentz')
        >>> i0,i1,i2,i3,i4 = tensor_indices('i0:5', Lorentz)
        >>> A = TensorHead('A', [Lorentz])
        >>> G = TensorHead('G', [Lorentz], TensorSymmetry.no_symmetry(1), 'Gcomm')
        >>> GH = TensorHead('GH', [Lorentz], TensorSymmetry.no_symmetry(1), 'GHcomm')
        >>> TensorManager.set_comm('Gcomm', 'GHcomm', 0)
        >>> (GH(i1)*G(i0)).canon_bp()
        G(i0)*GH(i1)
        >>> (G(i1)*G(i0)).canon_bp()
        G(i1)*G(i0)
        >>> (G(i1)*A(i0)).canon_bp()
        A(i0)*G(i1)
        """
        if c not in (0, 1, None):
            raise ValueError('`c` can assume only the values 0, 1 or None')
        i = sympify(i)
        j = sympify(j)
        if i not in self._comm_symbols2i:
            n = len(self._comm)
            self._comm.append({ })
            self._comm[n][0] = 0
            self._comm[0][n] = 0
            self._comm_symbols2i[i] = n
            self._comm_i2symbol[n] = i
        if j not in self._comm_symbols2i:
            n = len(self._comm)
            self._comm.append({ })
            self._comm[0][n] = 0
            self._comm[n][0] = 0
            self._comm_symbols2i[j] = n
            self._comm_i2symbol[n] = j
        ni = self._comm_symbols2i[i]
        nj = self._comm_symbols2i[j]
        self._comm[ni][nj] = c
        self._comm[nj][ni] = c
        clear_cache()

    
    def set_comms(self, *args):
        '''
        Set the commutation group numbers ``c`` for symbols ``i, j``.

        Parameters
        ==========

        args : sequence of ``(i, j, c)``
        '''
        for i, j, c in args:
            self.set_comm(i, j, c)
            return None

    
    def get_comm(self, i, j):
        '''
        Return the commutation parameter for commutation group numbers ``i, j``

        see ``_TensorManager.set_comm``
        '''
        return self._comm[i].get(j, 0 if i == 0 or j == 0 else None)

    
    def clear(self):
        '''
        Clear the TensorManager.
        '''
        self._comm_init()


TensorManager = _TensorManager()

class TensorIndexType(Basic):
    """
    A TensorIndexType is characterized by its name and its metric.

    Parameters
    ==========

    name : name of the tensor type
    dummy_name : name of the head of dummy indices
    dim : dimension, it can be a symbol or an integer or ``None``
    eps_dim : dimension of the epsilon tensor
    metric_symmetry : integer that denotes metric symmetry or ``None`` for no metric
    metric_name : string with the name of the metric tensor

    Attributes
    ==========

    ``metric`` : the metric tensor
    ``delta`` : ``Kronecker delta``
    ``epsilon`` : the ``Levi-Civita epsilon`` tensor
    ``data`` : (deprecated) a property to add ``ndarray`` values, to work in a specified basis.

    Notes
    =====

    The possible values of the ``metric_symmetry`` parameter are:

        ``1``   :   metric tensor is fully symmetric
        ``0``   :   metric tensor possesses no index symmetry
        ``-1``  :   metric tensor is fully antisymmetric
        ``None``:   there is no metric tensor (metric equals to ``None``)

    The metric is assumed to be symmetric by default. It can also be set
    to a custom tensor by the ``.set_metric()`` method.

    If there is a metric the metric is used to raise and lower indices.

    In the case of non-symmetric metric, the following raising and
    lowering conventions will be adopted:

    ``psi(a) = g(a, b)*psi(-b); chi(-a) = chi(b)*g(-b, -a)``

    From these it is easy to find:

    ``g(-a, b) = delta(-a, b)``

    where ``delta(-a, b) = delta(b, -a)`` is the ``Kronecker delta``
    (see ``TensorIndex`` for the conventions on indices).
    For antisymmetric metrics there is also the following equality:

    ``g(a, -b) = -delta(a, -b)``

    If there is no metric it is not possible to raise or lower indices;
    e.g. the index of the defining representation of ``SU(N)``
    is 'covariant' and the conjugate representation is
    'contravariant'; for ``N > 2`` they are linearly independent.

    ``eps_dim`` is by default equal to ``dim``, if the latter is an integer;
    else it can be assigned (for use in naive dimensional regularization);
    if ``eps_dim`` is not an integer ``epsilon`` is ``None``.

    Examples
    ========

    >>> from sympy.tensor.tensor import TensorIndexType
    >>> Lorentz = TensorIndexType('Lorentz', dummy_name='L')
    >>> Lorentz.metric
    metric(Lorentz,Lorentz)
    """
    
    def __new__(cls, name, dummy_name, dim, eps_dim, metric_symmetry, metric_name = (None, None, None, 1, 'metric'), **kwargs):
        if 'dummy_fmt' in kwargs:
            dummy_fmt = kwargs['dummy_fmt']
            sympy_deprecation_warning(f'''\n                The dummy_fmt keyword to TensorIndexType is deprecated. Use\n                dummy_name={dummy_fmt} instead.\n                ''', deprecated_since_version = '1.5', active_deprecations_target = 'deprecated-tensorindextype-dummy-fmt')
            dummy_name = dummy_fmt
        if isinstance(name, str):
            name = Symbol(name)
    # WARNING: Decompyle incomplete

    name = (lambda self: self.args[0].name)()
    dummy_name = (lambda self: self.args[1].name)()
    dim = (lambda self: self.args[2])()
    eps_dim = (lambda self: self.args[3])()
    metric = (lambda self: metric_symmetry = self.args[4]metric_name = self.args[5]# WARNING: Decompyle incomplete
)()
    delta = (lambda self: TensorHead('KD', [
self] * 2, TensorSymmetry.fully_symmetric(2)))()
    epsilon = (lambda self: if not isinstance(self.eps_dim, (SYMPY_INTS, Integer)):
Nonesymmetry = None.fully_symmetric(-(self.eps_dim))TensorHead('Eps', [
self] * self.eps_dim, symmetry))()
    
    def set_metric(self, tensor):
        self._metric = tensor

    
    def __lt__(self, other):
        return self.name < other.name

    
    def __str__(self):
        return self.name

    __repr__ = __str__
    data = (lambda self: deprecate_data()ignore_warnings(SymPyDeprecationWarning)None(None, None)with None:
if not None, _tensor_data_substitution_dict[self]:
pass)()
    data = (lambda self, data: deprecate_data()MutableDenseNDimArray = MutableDenseNDimArrayimport arraydata = _TensorDataLazyEvaluator.parse_data(data)if data.rank() > 2:
raise ValueError('data have to be of rank 1 (diagonal metric) or 2.')if data.rank() == 1:
if self.dim.is_number:
nda_dim = data.shape[0]if nda_dim != self.dim:
raise ValueError('Dimension mismatch')dim = data.shape[0]newndarray = MutableDenseNDimArray.zeros(dim, dim)for i, val in enumerate(data):
newndarray[(i, i)] = valdata = newndarray(dim1, dim2) = data.shapeif dim1 != dim2:
raise ValueError('Non-square matrix tensor.')if self.dim.is_number and self.dim != dim1:
raise ValueError('Dimension mismatch')_tensor_data_substitution_dict[self] = data_tensor_data_substitution_dict.add_metric_data(self.metric, data)ignore_warnings(SymPyDeprecationWarning)delta = self.get_kronecker_delta()None(None, None)with None:
if not None:
passi1 = TensorIndex('i1', self)i2 = TensorIndex('i2', self)ignore_warnings(SymPyDeprecationWarning)delta(i1, -i2).data = _TensorDataLazyEvaluator.parse_data(eye(dim1))None(None, None)Nonewith None:
if not None:
pass)()
    data = (lambda self: deprecate_data()ignore_warnings(SymPyDeprecationWarning)if self in _tensor_data_substitution_dict:
del _tensor_data_substitution_dict[self]if self.metric in _tensor_data_substitution_dict:
del _tensor_data_substitution_dict[self.metric]None(None, None)Nonewith None:
if not None:
pass)()
    get_kronecker_delta = (lambda self: sym2 = TensorSymmetry(get_symmetric_group_sgs(2))delta = TensorHead('KD', [
self] * 2, sym2)delta)()
    get_epsilon = (lambda self: if not isinstance(self._eps_dim, (SYMPY_INTS, Integer)):
Nonesym = None(get_symmetric_group_sgs(self._eps_dim, 1))epsilon = TensorHead('Eps', [
self] * self._eps_dim, sym)epsilon)()
    
    def _components_data_full_destroy(self):
        '''
        EXPERIMENTAL: do not rely on this API method.

        This destroys components data associated to the ``TensorIndexType``, if
        any, specifically:

        * metric tensor data
        * Kronecker tensor data
        '''
        if self in _tensor_data_substitution_dict:
            del _tensor_data_substitution_dict[self]
        
        def delete_tensmul_data(key):
            if key in _tensor_data_substitution_dict._substitutions_dict_tensmul:
                del _tensor_data_substitution_dict._substitutions_dict_tensmul[key]
                return None

        delete_tensmul_data((self.metric, True, True))
        delete_tensmul_data((self.metric, True, False))
        delete_tensmul_data((self.metric, False, True))
        delete_tensmul_data((self.metric, False, False))
        delta = self.get_kronecker_delta()
        if delta in _tensor_data_substitution_dict:
            del _tensor_data_substitution_dict[delta]
            return None



class TensorIndex(Basic):
    """
    Represents a tensor index

    Parameters
    ==========

    name : name of the index, or ``True`` if you want it to be automatically assigned
    tensor_index_type : ``TensorIndexType`` of the index
    is_up :  flag for contravariant index (is_up=True by default)

    Attributes
    ==========

    ``name``
    ``tensor_index_type``
    ``is_up``

    Notes
    =====

    Tensor indices are contracted with the Einstein summation convention.

    An index can be in contravariant or in covariant form; in the latter
    case it is represented prepending a ``-`` to the index name. Adding
    ``-`` to a covariant (is_up=False) index makes it contravariant.

    Dummy indices have a name with head given by
    ``tensor_inde_type.dummy_name`` with underscore and a number.

    Similar to ``symbols`` multiple contravariant indices can be created
    at once using ``tensor_indices(s, typ)``, where ``s`` is a string
    of names.


    Examples
    ========

    >>> from sympy.tensor.tensor import TensorIndexType, TensorIndex, TensorHead, tensor_indices
    >>> Lorentz = TensorIndexType('Lorentz', dummy_name='L')
    >>> mu = TensorIndex('mu', Lorentz, is_up=False)
    >>> nu, rho = tensor_indices('nu, rho', Lorentz)
    >>> A = TensorHead('A', [Lorentz, Lorentz])
    >>> A(mu, nu)
    A(-mu, nu)
    >>> A(-mu, -rho)
    A(mu, -rho)
    >>> A(mu, -mu)
    A(-L_0, L_0)
    """
    
    def __new__(cls, name, tensor_index_type, is_up = (True,)):
        if isinstance(name, str):
            name_symbol = Symbol(name)
        elif isinstance(name, Symbol):
            name_symbol = name
        elif name is True:
            name = '_i{}'.format(len(tensor_index_type._autogenerated))
            name_symbol = Symbol(name)
            tensor_index_type._autogenerated.append(name_symbol)
        else:
            raise ValueError('invalid name')
        is_up = sympify(is_up)
        return Basic.__new__(cls, name_symbol, tensor_index_type, is_up)

    name = (lambda self: self.args[0].name)()
    tensor_index_type = (lambda self: self.args[1])()
    is_up = (lambda self: self.args[2])()
    
    def _print(self):
        s = self.name
        if not self.is_up:
            s = '-%s' % s
        return s

    
    def __lt__(self, other):
        return (self.tensor_index_type, self.name) < (other.tensor_index_type, other.name)

    
    def __neg__(self):
        t1 = TensorIndex(self.name, self.tensor_index_type, not (self.is_up))
        return t1



def tensor_indices(s, typ):
    """
    Returns list of tensor indices given their names and their types.

    Parameters
    ==========

    s : string of comma separated names of indices

    typ : ``TensorIndexType`` of the indices

    Examples
    ========

    >>> from sympy.tensor.tensor import TensorIndexType, tensor_indices
    >>> Lorentz = TensorIndexType('Lorentz', dummy_name='L')
    >>> a, b, c, d = tensor_indices('a,b,c,d', Lorentz)
    """
    pass
# WARNING: Decompyle incomplete


class TensorSymmetry(Basic):
    """
    Monoterm symmetry of a tensor (i.e. any symmetric or anti-symmetric
    index permutation). For the relevant terminology see ``tensor_can.py``
    section of the combinatorics module.

    Parameters
    ==========

    bsgs : tuple ``(base, sgs)`` BSGS of the symmetry of the tensor

    Attributes
    ==========

    ``base`` : base of the BSGS
    ``generators`` : generators of the BSGS
    ``rank`` : rank of the tensor

    Notes
    =====

    A tensor can have an arbitrary monoterm symmetry provided by its BSGS.
    Multiterm symmetries, like the cyclic symmetry of the Riemann tensor
    (i.e., Bianchi identity), are not covered. See combinatorics module for
    information on how to generate BSGS for a general index permutation group.
    Simple symmetries can be generated using built-in methods.

    See Also
    ========

    sympy.combinatorics.tensor_can.get_symmetric_group_sgs

    Examples
    ========

    Define a symmetric tensor of rank 2

    >>> from sympy.tensor.tensor import TensorIndexType, TensorSymmetry, get_symmetric_group_sgs, TensorHead
    >>> Lorentz = TensorIndexType('Lorentz', dummy_name='L')
    >>> sym = TensorSymmetry(get_symmetric_group_sgs(2))
    >>> T = TensorHead('T', [Lorentz]*2, sym)

    Note, that the same can also be done using built-in TensorSymmetry methods

    >>> sym2 = TensorSymmetry.fully_symmetric(2)
    >>> sym == sym2
    True
    """
    
    def __new__(cls, *args, **kw_args):
        if len(args) == 1:
            (base, generators) = args[0]
        elif len(args) == 2:
            (base, generators) = args
        else:
            raise TypeError('bsgs required, either two separate parameters or one tuple')
    # WARNING: Decompyle incomplete

    base = (lambda self: self.args[0])()
    generators = (lambda self: self.args[1])()
    rank = (lambda self: self.generators[0].size - 2)()
    fully_symmetric = (lambda cls, rank: if rank > 0:
bsgs = get_symmetric_group_sgs(rank, False)elif rank < 0:
bsgs = get_symmetric_group_sgs(-rank, True)elif rank == 0:
bsgs = ([], [
Permutation(1)])TensorSymmetry(bsgs))()
    direct_product = (lambda cls: sgs = [
Permutation(1)]base = []# WARNING: Decompyle incomplete
)()
    riemann = (lambda cls: TensorSymmetry(riemann_bsgs))()
    no_symmetry = (lambda cls, rank: TensorSymmetry([], [
Permutation(rank + 1)]))()

tensorsymmetry = (lambda : Permutation = Permutationimport sympy.combinatorics
def tableau2bsgs(a):
if len(a) == 1:
n = a[0]bsgs = get_symmetric_group_sgs(n, 1)elif (lambda .0: pass# WARNING: Decompyle incomplete
)(a()):
            n = len(a)
            bsgs = get_symmetric_group_sgs(n)
        elif a == [
            2,
            2]:
            bsgs = riemann_bsgs
        else:
            raise NotImplementedError
        return bsgs
if not args:
TensorSymmetry(Tuple(), Tuple(Permutation(1)))if None(args) == 2 and isinstance(args[1][0], Permutation):
TensorSymmetry(args)(base, sgs) = tableau2bsgs(args[0])for a in args[1:]:
(basex, sgsx) = tableau2bsgs(a)(base, sgs) = bsgs_direct_product(base, sgs, basex, sgsx)TensorSymmetry(Tuple(base, sgs)))()
TensorType = <NODE:12>()
tensorhead = (lambda name, typ, sym, comm = (None, 0): pass# WARNING: Decompyle incomplete
)()

class TensorHead(Basic):
    """
    Tensor head of the tensor.

    Parameters
    ==========

    name : name of the tensor
    index_types : list of TensorIndexType
    symmetry : TensorSymmetry of the tensor
    comm : commutation group number

    Attributes
    ==========

    ``name``
    ``index_types``
    ``rank`` : total number of indices
    ``symmetry``
    ``comm`` : commutation group

    Notes
    =====

    Similar to ``symbols`` multiple TensorHeads can be created using
    ``tensorhead(s, typ, sym=None, comm=0)`` function, where ``s``
    is the string of names and ``sym`` is the monoterm tensor symmetry
    (see ``tensorsymmetry``).

    A ``TensorHead`` belongs to a commutation group, defined by a
    symbol on number ``comm`` (see ``_TensorManager.set_comm``);
    tensors in a commutation group have the same commutation properties;
    by default ``comm`` is ``0``, the group of the commuting tensors.

    Examples
    ========

    Define a fully antisymmetric tensor of rank 2:

    >>> from sympy.tensor.tensor import TensorIndexType, TensorHead, TensorSymmetry
    >>> Lorentz = TensorIndexType('Lorentz', dummy_name='L')
    >>> asym2 = TensorSymmetry.fully_symmetric(-2)
    >>> A = TensorHead('A', [Lorentz, Lorentz], asym2)

    Examples with ndarray values, the components data assigned to the
    ``TensorHead`` object are assumed to be in a fully-contravariant
    representation. In case it is necessary to assign components data which
    represents the values of a non-fully covariant tensor, see the other
    examples.

    >>> from sympy.tensor.tensor import tensor_indices
    >>> from sympy import diag
    >>> Lorentz = TensorIndexType('Lorentz', dummy_name='L')
    >>> i0, i1 = tensor_indices('i0:2', Lorentz)

    Specify a replacement dictionary to keep track of the arrays to use for
    replacements in the tensorial expression. The ``TensorIndexType`` is
    associated to the metric used for contractions (in fully covariant form):

    >>> repl = {Lorentz: diag(1, -1, -1, -1)}

    Let's see some examples of working with components with the electromagnetic
    tensor:

    >>> from sympy import symbols
    >>> Ex, Ey, Ez, Bx, By, Bz = symbols('E_x E_y E_z B_x B_y B_z')
    >>> c = symbols('c', positive=True)

    Let's define `F`, an antisymmetric tensor:

    >>> F = TensorHead('F', [Lorentz, Lorentz], asym2)

    Let's update the dictionary to contain the matrix to use in the
    replacements:

    >>> repl.update({F(-i0, -i1): [
    ... [0, Ex/c, Ey/c, Ez/c],
    ... [-Ex/c, 0, -Bz, By],
    ... [-Ey/c, Bz, 0, -Bx],
    ... [-Ez/c, -By, Bx, 0]]})

    Now it is possible to retrieve the contravariant form of the Electromagnetic
    tensor:

    >>> F(i0, i1).replace_with_arrays(repl, [i0, i1])
    [[0, -E_x/c, -E_y/c, -E_z/c], [E_x/c, 0, -B_z, B_y], [E_y/c, B_z, 0, -B_x], [E_z/c, -B_y, B_x, 0]]

    and the mixed contravariant-covariant form:

    >>> F(i0, -i1).replace_with_arrays(repl, [i0, -i1])
    [[0, E_x/c, E_y/c, E_z/c], [E_x/c, 0, B_z, -B_y], [E_y/c, -B_z, 0, B_x], [E_z/c, B_y, -B_x, 0]]

    Energy-momentum of a particle may be represented as:

    >>> from sympy import symbols
    >>> P = TensorHead('P', [Lorentz], TensorSymmetry.no_symmetry(1))
    >>> E, px, py, pz = symbols('E p_x p_y p_z', positive=True)
    >>> repl.update({P(i0): [E, px, py, pz]})

    The contravariant and covariant components are, respectively:

    >>> P(i0).replace_with_arrays(repl, [i0])
    [E, p_x, p_y, p_z]
    >>> P(-i0).replace_with_arrays(repl, [-i0])
    [E, -p_x, -p_y, -p_z]

    The contraction of a 1-index tensor by itself:

    >>> expr = P(i0)*P(-i0)
    >>> expr.replace_with_arrays(repl, [])
    E**2 - p_x**2 - p_y**2 - p_z**2
    """
    is_commutative = False
    
    def __new__(cls, name, index_types, symmetry, comm = (None, 0)):
        if isinstance(name, str):
            name_symbol = Symbol(name)
        elif isinstance(name, Symbol):
            name_symbol = name
        else:
            raise ValueError('invalid name')
    # WARNING: Decompyle incomplete

    name = (lambda self: self.args[0].name)()
    index_types = (lambda self: list(self.args[1]))()
    symmetry = (lambda self: self.args[2])()
    comm = (lambda self: TensorManager.comm_symbols2i(self.args[3]))()
    rank = (lambda self: len(self.index_types))()
    
    def __lt__(self, other):
        return (self.name, self.index_types) < (other.name, other.index_types)

    
    def commutes_with(self, other):
        '''
        Returns ``0`` if ``self`` and ``other`` commute, ``1`` if they anticommute.

        Returns ``None`` if ``self`` and ``other`` neither commute nor anticommute.
        '''
        r = TensorManager.get_comm(self.comm, other.comm)
        return r

    
    def _print(self):
        return f'''({(lambda .0: [ str(x) for x in .0 ])(self.index_types())!s})'''

    
    def __call__(self, *indices, **kw_args):
        """
        Returns a tensor with indices.

        Explanation
        ===========

        There is a special behavior in case of indices denoted by ``True``,
        they are considered auto-matrix indices, their slots are automatically
        filled, and confer to the tensor the behavior of a matrix or vector
        upon multiplication with another tensor containing auto-matrix indices
        of the same ``TensorIndexType``. This means indices get summed over the
        same way as in matrix multiplication. For matrix behavior, define two
        auto-matrix indices, for vector behavior define just one.

        Indices can also be strings, in which case the attribute
        ``index_types`` is used to convert them to proper ``TensorIndex``.

        Examples
        ========

        >>> from sympy.tensor.tensor import TensorIndexType, tensor_indices, TensorSymmetry, TensorHead
        >>> Lorentz = TensorIndexType('Lorentz', dummy_name='L')
        >>> a, b = tensor_indices('a,b', Lorentz)
        >>> A = TensorHead('A', [Lorentz]*2, TensorSymmetry.no_symmetry(2))
        >>> t = A(a, -b)
        >>> t
        A(a, -b)

        """
        updated_indices = []
    # WARNING: Decompyle incomplete

    
    def __pow__(self, other):
        deprecate_data()
        ignore_warnings(SymPyDeprecationWarning)
    # WARNING: Decompyle incomplete

    data = (lambda self: deprecate_data()ignore_warnings(SymPyDeprecationWarning)None(None, None)with None:
if not None, _tensor_data_substitution_dict[self]:
pass)()
    data = (lambda self, data: deprecate_data()ignore_warnings(SymPyDeprecationWarning)_tensor_data_substitution_dict[self] = dataNone(None, None)Nonewith None:
if not None:
pass)()
    data = (lambda self: deprecate_data()if self in _tensor_data_substitution_dict:
del _tensor_data_substitution_dict[self]None)()
    
    def __iter__(self):
        deprecate_data()
        ignore_warnings(SymPyDeprecationWarning)
        None(None, None)
        return 
        with None:
            if not None, self.data.__iter__():
                pass

    
    def _components_data_full_destroy(self):
        '''
        EXPERIMENTAL: do not rely on this API method.

        Destroy components data associated to the ``TensorHead`` object, this
        checks for attached components data, and destroys components data too.
        '''
        deprecate_data()
        if self.name == 'KD':
            return None
        if None in _tensor_data_substitution_dict:
            del _tensor_data_substitution_dict[self]
            return None



def tensor_heads(s, index_types, symmetry, comm = (None, 0)):
    '''
    Returns a sequence of TensorHeads from a string `s`
    '''
    pass
# WARNING: Decompyle incomplete


class TensExpr(ABC, Expr):
    '''
    Abstract base class for tensor expressions

    Notes
    =====

    A tensor expression is an expression formed by tensors;
    currently the sums of tensors are distributed.

    A ``TensExpr`` can be a ``TensAdd`` or a ``TensMul``.

    ``TensMul`` objects are formed by products of component tensors,
    and include a coefficient, which is a SymPy expression.


    In the internal representation contracted indices are represented
    by ``(ipos1, ipos2, icomp1, icomp2)``, where ``icomp1`` is the position
    of the component tensor with contravariant index, ``ipos1`` is the
    slot which the index occupies in that component tensor.

    Contracted indices are therefore nameless in the internal representation.
    '''
    _op_priority = 12
    is_commutative = False
    
    def __neg__(self):
        return self * S.NegativeOne

    
    def __abs__(self):
        raise NotImplementedError

    
    def __add__(self, other):
        return TensAdd(self, other).doit()

    
    def __radd__(self, other):
        return TensAdd(other, self).doit()

    
    def __sub__(self, other):
        return TensAdd(self, -other).doit()

    
    def __rsub__(self, other):
        return TensAdd(other, -self).doit()

    
    def __mul__(self, other):
        """
        Multiply two tensors using Einstein summation convention.

        Explanation
        ===========

        If the two tensors have an index in common, one contravariant
        and the other covariant, in their product the indices are summed

        Examples
        ========

        >>> from sympy.tensor.tensor import TensorIndexType, tensor_indices, tensor_heads
        >>> Lorentz = TensorIndexType('Lorentz', dummy_name='L')
        >>> m0, m1, m2 = tensor_indices('m0,m1,m2', Lorentz)
        >>> g = Lorentz.metric
        >>> p, q = tensor_heads('p,q', [Lorentz])
        >>> t1 = p(m0)
        >>> t2 = q(-m0)
        >>> t1*t2
        p(L_0)*q(-L_0)
        """
        return TensMul(self, other).doit()

    
    def __rmul__(self, other):
        return TensMul(other, self).doit()

    
    def __truediv__(self, other):
        other = _sympify(other)
        if isinstance(other, TensExpr):
            raise ValueError('cannot divide by a tensor')
        return TensMul(self, S.One / other).doit()

    
    def __rtruediv__(self, other):
        raise ValueError('cannot divide by a tensor')

    
    def __pow__(self, other):
        deprecate_data()
        ignore_warnings(SymPyDeprecationWarning)
    # WARNING: Decompyle incomplete

    
    def __rpow__(self, other):
        raise NotImplementedError

    nocoeff = (lambda self: raise NotImplementedError('abstract method'))()()
    coeff = (lambda self: raise NotImplementedError('abstract method'))()()
    get_indices = (lambda self: raise NotImplementedError('abstract method'))()
    get_free_indices = (lambda self = abstractmethod: raise NotImplementedError('abstract method'))()
    _replace_indices = (lambda self = abstractmethod, repl = property: raise NotImplementedError('abstract method'))()
    
    def fun_eval(self, *index_tuples):
        deprecate_fun_eval()
    # WARNING: Decompyle incomplete

    
    def get_matrix(self):
        '''
        DEPRECATED: do not use.

        Returns ndarray components data as a matrix, if components data are
        available and ndarray dimension does not exceed 2.
        '''
        Matrix = Matrix
        import sympy.matrices.dense
        deprecate_data()
        ignore_warnings(SymPyDeprecationWarning)
        if  < 0, self.rank or 0, self.rank <= 2:
            pass
        
        self.data.shape[1] if self.rank == 2 else 1 = self.data.shape[0]
        if self.rank == 2:
            mat_list = [] * rows
            for i in range(rows):
                mat_list.append([])
                for j in range(columns):
                    mat_list[i].append(self[(i, j)])
                mat_list = [
                    None] * rows
                for i in range(rows):
                    mat_list[i] = self[i]
                    None(None, None)
                    return 
                    raise NotImplementedError('missing multidimensional reduction to matrix.')
                    with None:
                        if not None, Matrix(mat_list):
                            pass

    _get_indices_permutation = (lambda indices1, indices2: pass# WARNING: Decompyle incomplete
)()
    
    def expand(self, **hints):
        pass
    # WARNING: Decompyle incomplete

    
    def _expand(self, **kwargs):
        return self

    
    def _get_free_indices_set(self):
        indset = set()
        for arg in self.args:
            if isinstance(arg, TensExpr):
                indset.update(arg._get_free_indices_set())
            return indset

    
    def _get_dummy_indices_set(self):
        indset = set()
        for arg in self.args:
            if isinstance(arg, TensExpr):
                indset.update(arg._get_dummy_indices_set())
            return indset

    
    def _get_indices_set(self):
        indset = set()
        for arg in self.args:
            if isinstance(arg, TensExpr):
                indset.update(arg._get_indices_set())
            return indset

    _iterate_dummy_indices = (lambda self: pass# WARNING: Decompyle incomplete
)()
    _iterate_free_indices = (lambda self: pass# WARNING: Decompyle incomplete
)()
    _iterate_indices = (lambda self: pass# WARNING: Decompyle incomplete
)()
    _contract_and_permute_with_metric = (lambda metric, array, pos, dim: tensorcontraction = tensorcontractiontensorproduct = tensorproductpermutedims = permutedimsimport arrayarray = tensorcontraction(tensorproduct(metric, array), (1, 2 + pos))permu = list(range(dim))permu[0], permu[pos] = permu[pos], permu[0]permutedims(array, permu))()
    _match_indices_with_other_tensor = (lambda array, free_ind1, free_ind2, replacement_dict: permutedims = permutedimsimport arrayindex_types1 = free_ind1()pos2up = []pos2down = []free2remaining = free_ind2[:]# WARNING: Decompyle incomplete
)()
    
    def replace_with_arrays(self, replacement_dict, indices = (None,)):
        '''
        Replace the tensorial expressions with arrays. The final array will
        correspond to the N-dimensional array with indices arranged according
        to ``indices``.

        Parameters
        ==========

        replacement_dict
            dictionary containing the replacement rules for tensors.
        indices
            the index order with respect to which the array is read. The
            original index order will be used if no value is passed.

        Examples
        ========

        >>> from sympy.tensor.tensor import TensorIndexType, tensor_indices
        >>> from sympy.tensor.tensor import TensorHead
        >>> from sympy import symbols, diag

        >>> L = TensorIndexType("L")
        >>> i, j = tensor_indices("i j", L)
        >>> A = TensorHead("A", [L])
        >>> A(i).replace_with_arrays({A(i): [1, 2]}, [i])
        [1, 2]

        Since \'indices\' is optional, we can also call replace_with_arrays by
        this way if no specific index order is needed:

        >>> A(i).replace_with_arrays({A(i): [1, 2]})
        [1, 2]

        >>> expr = A(i)*A(j)
        >>> expr.replace_with_arrays({A(i): [1, 2]})
        [[1, 2], [2, 4]]

        For contractions, specify the metric of the ``TensorIndexType``, which
        in this case is ``L``, in its covariant form:

        >>> expr = A(i)*A(-i)
        >>> expr.replace_with_arrays({A(i): [1, 2], L: diag(1, -1)})
        -3

        Symmetrization of an array:

        >>> H = TensorHead("H", [L, L])
        >>> a, b, c, d = symbols("a b c d")
        >>> expr = H(i, j)/2 + H(j, i)/2
        >>> expr.replace_with_arrays({H(i, j): [[a, b], [c, d]]})
        [[a, b/2 + c/2], [b/2 + c/2, d]]

        Anti-symmetrization of an array:

        >>> expr = H(i, j)/2 - H(j, i)/2
        >>> repl = {H(i, j): [[a, b], [c, d]]}
        >>> expr.replace_with_arrays(repl)
        [[0, b/2 - c/2], [-b/2 + c/2, 0]]

        The same expression can be read as the transpose by inverting ``i`` and
        ``j``:

        >>> expr.replace_with_arrays(repl, [j, i])
        [[0, -b/2 + c/2], [b/2 - c/2, 0]]
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _check_add_Sum(self, expr, index_symbols):
        pass
    # WARNING: Decompyle incomplete

    
    def _expand_partial_derivative(self):
        pass
    # WARNING: Decompyle incomplete



class TensAdd(AssocOp, TensExpr):
    '''
    Sum of tensors.

    Parameters
    ==========

    free_args : list of the free indices

    Attributes
    ==========

    ``args`` : tuple of addends
    ``rank`` : rank of the tensor
    ``free_args`` : list of the free indices in sorted order

    Examples
    ========

    >>> from sympy.tensor.tensor import TensorIndexType, tensor_heads, tensor_indices
    >>> Lorentz = TensorIndexType(\'Lorentz\', dummy_name=\'L\')
    >>> a, b = tensor_indices(\'a,b\', Lorentz)
    >>> p, q = tensor_heads(\'p,q\', [Lorentz])
    >>> t = p(a) + q(a); t
    p(a) + q(a)

    Examples with components data added to the tensor expression:

    >>> from sympy import symbols, diag
    >>> x, y, z, t = symbols("x y z t")
    >>> repl = {}
    >>> repl[Lorentz] = diag(1, -1, -1, -1)
    >>> repl[p(a)] = [1, 2, 3, 4]
    >>> repl[q(a)] = [x, y, z, t]

    The following are: 2**2 - 3**2 - 2**2 - 7**2 ==> -58

    >>> expr = p(a) + q(a)
    >>> expr.replace_with_arrays(repl, [a])
    [x + 1, y + 2, z + 3, t + 4]
    '''
    
    def __new__(cls, *args, **kw_args):
        args = args()
        args = TensAdd._tensAdd_flatten(args)
        args.sort(key = default_sort_key)
        if not args:
            return S.Zero
        if (lambda .0: pass# WARNING: Decompyle incomplete
)(args) == 1:
            return args[0]
    # WARNING: Decompyle incomplete

    coeff = (lambda self: S.One)()
    nocoeff = (lambda self: self)()
    
    def get_free_indices(self = None):
        return self.free_indices

    
    def _replace_indices(self = None, repl = None):
        pass
    # WARNING: Decompyle incomplete

    rank = (lambda self: if isinstance(self.args[0], TensExpr):
self.args[0].rank)()
    free_args = (lambda self: if isinstance(self.args[0], TensExpr):
self.args[0].free_args)()
    free_indices = (lambda self: if isinstance(self.args[0], TensExpr):
self.args[0].get_free_indices()None())()
    
    def doit(self, **hints):
        pass
    # WARNING: Decompyle incomplete

    _tensAdd_flatten = (lambda args: a = []for x in args:
if isinstance(x, (Add, TensAdd)):
a.extend(list(x.args))continuea.append(x)args = a()args)()
    _tensAdd_check = (lambda args: pass# WARNING: Decompyle incomplete
)()
    _tensAdd_collect_terms = (lambda args: terms_dict = defaultdict(list)scalars = S.Zeroif isinstance(args[0], TensExpr):
free_indices = set(args[0].get_free_indices())else:
free_indices = set()for arg in args:
if not isinstance(arg, TensExpr):
if free_indices != set():
raise ValueError('wrong valence')scalars += argcontinueif free_indices != set(arg.get_free_indices()):
raise ValueError('wrong valence')terms_dict[arg.nocoeff].append(arg.coeff)new_args = terms_dict.items()()if isinstance(scalars, Add):
new_args = list(scalars.args) + new_argselif scalars != 0:
new_args = [
scalars] + new_argsnew_args)()
    
    def get_indices(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _expand(self, **hints):
        pass
    # WARNING: Decompyle incomplete

    
    def __call__(self, *indices):
        pass
    # WARNING: Decompyle incomplete

    
    def canon_bp(self):
        '''
        Canonicalize using the Butler-Portugal algorithm for canonicalization
        under monoterm symmetries.
        '''
        expr = self.expand()
        args = expr.args()
    # WARNING: Decompyle incomplete

    
    def equals(self, other):
        other = _sympify(other)
        if isinstance(other, TensMul) and other.coeff == 0:
            return (lambda .0: pass# WARNING: Decompyle incomplete
)(self.args())
        if None(other, TensExpr) and self.rank != other.rank:
            return False
        if None(other, TensAdd):
            if set(self.args) != set(other.args):
                return False
            return None
        t = None - other
        if not isinstance(t, TensExpr):
            return t == 0
        if None(t, TensMul):
            return t.coeff == 0
        return (lambda .0: pass# WARNING: Decompyle incomplete
)(t.args())

    
    def __getitem__(self, item):
        deprecate_data()
        ignore_warnings(SymPyDeprecationWarning)
        None(None, None)
        return 
        with None:
            if not None, self.data[item]:
                pass

    
    def contract_delta(self, delta):
        pass
    # WARNING: Decompyle incomplete

    
    def contract_metric(self, g):
        '''
        Raise or lower indices with the metric ``g``.

        Parameters
        ==========

        g :  metric

        contract_all : if True, eliminate all ``g`` which are contracted

        Notes
        =====

        see the ``TensorIndexType`` docstring for the contraction conventions
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def substitute_indices(self, *index_tuples):
        new_args = []
    # WARNING: Decompyle incomplete

    
    def _print(self):
        a = []
        args = self.args
        for x in args:
            a.append(str(x))
            s = ' + '.join(a)
            s = s.replace('+ -', '- ')
            return s

    
    def _extract_data(self, replacement_dict):
        pass
    # WARNING: Decompyle incomplete

    data = (lambda self: deprecate_data()ignore_warnings(SymPyDeprecationWarning)None(None, None)with None:
if not None, _tensor_data_substitution_dict[self.expand()]:
pass)()
    data = (lambda self, data: deprecate_data()ignore_warnings(SymPyDeprecationWarning)_tensor_data_substitution_dict[self] = dataNone(None, None)Nonewith None:
if not None:
pass)()
    data = (lambda self: deprecate_data()ignore_warnings(SymPyDeprecationWarning)if self in _tensor_data_substitution_dict:
del _tensor_data_substitution_dict[self]None(None, None)Nonewith None:
if not None:
pass)()
    
    def __iter__(self):
        deprecate_data()
        if not self.data:
            raise ValueError('No iteration on abstract tensors')
        return self.data.flatten().__iter__()

    
    def _eval_rewrite_as_Indexed(self, *args, **kwargs):
        return Add.fromiter(args)

    
    def _eval_partial_derivative(self, s):
        list_addends = []
    # WARNING: Decompyle incomplete



class Tensor(TensExpr):
    '''
    Base tensor class, i.e. this represents a tensor, the single unit to be
    put into an expression.

    Explanation
    ===========

    This object is usually created from a ``TensorHead``, by attaching indices
    to it. Indices preceded by a minus sign are considered contravariant,
    otherwise covariant.

    Examples
    ========

    >>> from sympy.tensor.tensor import TensorIndexType, tensor_indices, TensorHead
    >>> Lorentz = TensorIndexType("Lorentz", dummy_name="L")
    >>> mu, nu = tensor_indices(\'mu nu\', Lorentz)
    >>> A = TensorHead("A", [Lorentz, Lorentz])
    >>> A(mu, -nu)
    A(mu, -nu)
    >>> A(mu, -mu)
    A(L_0, -L_0)

    It is also possible to use symbols instead of inidices (appropriate indices
    are then generated automatically).

    >>> from sympy import Symbol
    >>> x = Symbol(\'x\')
    >>> A(x, mu)
    A(x, mu)
    >>> A(x, -x)
    A(L_0, -L_0)

    '''
    is_commutative = False
    args: 'tuple[TensorHead, Tuple]' = None
    
    def __new__(cls, tensor_head = None, indices = {
        'is_canon_bp': False }, *, is_canon_bp, **kw_args):
        indices = cls._parse_indices(tensor_head, indices)
    # WARNING: Decompyle incomplete

    free = (lambda self: self._free)()
    dum = (lambda self: self._dum)()
    ext_rank = (lambda self: self._ext_rank)()
    coeff = (lambda self: self._coeff)()
    nocoeff = (lambda self: self._nocoeff)()
    component = (lambda self: self._component)()
    components = (lambda self: self._components)()
    head = (lambda self: self.args[0])()
    indices = (lambda self: self.args[1])()
    free_indices = (lambda self: set(self._index_structure.get_free_indices()))()
    index_types = (lambda self: self.head.index_types)()
    rank = (lambda self: len(self.free_indices))()
    _build_index_map = (lambda indices, index_structure: index_map = { }for idx in indices:
index_map[idx] = (indices.index(idx),)index_map)()
    
    def doit(self, **hints):
        (args, indices, free, dum) = TensMul._tensMul_contract_indices([
            self])
        return args[0]

    _parse_indices = (lambda tensor_head, indices: if not isinstance(indices, (tuple, list, Tuple)):
raise TypeError('indices should be an array, got %s' % type(indices))indices = list(indices)for i, index in enumerate(indices):
if isinstance(index, Symbol):
indices[i] = TensorIndex(index, tensor_head.index_types[i], True)continueif isinstance(index, Mul):
(c, e) = index.as_coeff_Mul()if c == -1 and isinstance(e, Symbol):
indices[i] = TensorIndex(e, tensor_head.index_types[i], False)continueraise ValueError('index not understood: %s' % index)if not isinstance(index, TensorIndex):
raise TypeError(f'''wrong type for index: {index!s} is {type(index)!s}''')indices)()
    
    def _set_new_index_structure(self, im, is_canon_bp = (False,)):
        indices = im.get_indices()
    # WARNING: Decompyle incomplete

    
    def _set_indices(self = staticmethod, *, is_canon_bp, *indices, **kw_args):
        if len(indices) != self.ext_rank:
            raise ValueError('indices length mismatch')
        return self.func(self.args[0], indices, is_canon_bp = is_canon_bp).doit()

    
    def _get_free_indices_set(self):
        return self._index_structure.free()

    
    def _get_dummy_indices_set(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_indices_set(self):
        return set(self.args[1].args)

    free_in_args = (lambda self: self.free())()
    dum_in_args = (lambda self: self.dum())()
    free_args = (lambda self: (lambda .0: [ x[0] for x in .0 ])(self.free())
)()
    
    def commutes_with(self, other):
        '''
        :param other:
        :return:
            0  commute
            1  anticommute
            None  neither commute nor anticommute
        '''
        if not isinstance(other, TensExpr):
            return 0
        if None(other, Tensor):
            return self.component.commutes_with(other.component)

    
    def perm2tensor(self, g, is_canon_bp = (False,)):
        '''
        Returns the tensor corresponding to the permutation ``g``.

        For further details, see the method in ``TIDS`` with the same name.
        '''
        return perm2tensor(self, g, is_canon_bp)

    
    def canon_bp(self):
        if self.is_canon_bp:
            return self
        expr = None.expand()
        (g, dummies, msym) = expr._index_structure.indices_canon_args()
        v = components_canon_args([
            expr.component])
    # WARNING: Decompyle incomplete

    
    def split(self):
        return [
            self]

    
    def _expand(self, **kwargs):
        return self

    
    def sorted_components(self):
        return self

    
    def get_indices(self = property):
        '''
        Get a list of indices, corresponding to those of the tensor.
        '''
        return list(self.args[1])

    
    def get_free_indices(self = property):
        '''
        Get a list of free indices, corresponding to those of the tensor.
        '''
        return self._index_structure.get_free_indices()

    
    def _replace_indices(self = property, repl = property):
        return self.xreplace(repl)

    
    def as_base_exp(self):
        return (self, S.One)

    
    def substitute_indices(self, *index_tuples):
        """
        Return a tensor with free indices substituted according to ``index_tuples``.

        ``index_types`` list of tuples ``(old_index, new_index)``.

        Examples
        ========

        >>> from sympy.tensor.tensor import TensorIndexType, tensor_indices, tensor_heads, TensorSymmetry
        >>> Lorentz = TensorIndexType('Lorentz', dummy_name='L')
        >>> i, j, k, l = tensor_indices('i,j,k,l', Lorentz)
        >>> A, B = tensor_heads('A,B', [Lorentz]*2, TensorSymmetry.fully_symmetric(2))
        >>> t = A(i, k)*B(-k, -j); t
        A(i, L_0)*B(-L_0, -j)
        >>> t.substitute_indices((i, k),(-j, l))
        A(k, L_0)*B(-L_0, l)
        """
        indices = []
    # WARNING: Decompyle incomplete

    
    def _get_symmetrized_forms(self):
        '''
        Return a list giving all possible permutations of self that are allowed by its symmetries.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def matches(self, expr, repl_dict, old = (None, False)):
        expr = sympify(expr)
    # WARNING: Decompyle incomplete

    
    def _matches(self, expr, repl_dict, old = (None, False)):
        '''
        This does not account for index symmetries of expr
        '''
        expr = sympify(expr)
    # WARNING: Decompyle incomplete

    
    def __call__(self, *indices):
        deprecate_call()
        free_args = self.free_args
        indices = list(indices)
        if (lambda .0: [ x.tensor_index_type for x in .0 ]) != free_args():
            raise ValueError('incompatible types')
        if indices == free_args:
            return self
    # WARNING: Decompyle incomplete

    
    def __iter__(self):
        deprecate_data()
        ignore_warnings(SymPyDeprecationWarning)
        None(None, None)
        return 
        with None:
            if not None, self.data.__iter__():
                pass

    
    def __getitem__(self, item):
        deprecate_data()
        ignore_warnings(SymPyDeprecationWarning)
        None(None, None)
        return 
        with None:
            if not None, self.data[item]:
                pass

    
    def _extract_data(self, replacement_dict):
        pass
    # WARNING: Decompyle incomplete

    data = (lambda self: deprecate_data()ignore_warnings(SymPyDeprecationWarning)None(None, None)with None:
if not None, _tensor_data_substitution_dict[self]:
pass)()
    data = (lambda self, data: deprecate_data()ignore_warnings(SymPyDeprecationWarning)_tensor_data_substitution_dict[self] = dataNone(None, None)Nonewith None:
if not None:
pass)()
    data = (lambda self: deprecate_data()ignore_warnings(SymPyDeprecationWarning)if self in _tensor_data_substitution_dict:
del _tensor_data_substitution_dict[self]if self.metric in _tensor_data_substitution_dict:
del _tensor_data_substitution_dict[self.metric]None(None, None)Nonewith None:
if not None:
pass)()
    
    def _print(self):
        indices = self.indices()
        component = self.component
        if component.rank > 0:
            return f'''{component.name!s}({', '.join(indices)!s})'''
        return (lambda .0: [ str(ind) for ind in .0 ]) % component.name

    
    def equals(self, other):
        if other == 0:
            return self.coeff == 0
        other = None(other)
    # WARNING: Decompyle incomplete

    
    def contract_metric(self, g):
        if self.component != g:
            return self
        if None(self.free) != 0:
            return self
        if None.symmetry == TensorSymmetry.fully_symmetric(-2):
            antisym = 1
        elif g.symmetry == TensorSymmetry.fully_symmetric(2):
            antisym = 0
        elif g.symmetry == TensorSymmetry.no_symmetry(2):
            antisym = None
        else:
            raise NotImplementedError
        sign = S.One
        typ = g.index_types[0]
        if not antisym:
            sign = sign * typ.dim
        else:
            sign = sign * typ.dim
            (dp0, dp1) = self.dum[0]
            if dp0 < dp1:
                sign = -sign
        return sign

    
    def contract_delta(self, metric):
        return self.contract_metric(metric)

    
    def _eval_rewrite_as_Indexed(self, tens, indices, **kwargs):
        Indexed = Indexed
        import sympy.tensor.indexed
        index_symbols = self.get_indices()()
    # WARNING: Decompyle incomplete

    
    def _eval_partial_derivative(self, s):
        if not isinstance(s, Tensor):
            return S.Zero
        if None.head != s.head:
            return S.Zero
        kronecker_delta_list = [
            None]
        for iself, iother in enumerate(zip(self.get_free_indices(), s.get_free_indices())):
            if iself.tensor_index_type != iother.tensor_index_type:
                raise ValueError('index types not compatible')
            tensor_index_type = iself.tensor_index_type
            tensor_metric = tensor_index_type.metric
            dummy = TensorIndex('d_' + str(count), tensor_index_type, is_up = iself.is_up)
            kronecker_delta_list.append(kroneckerdelta)
            return TensMul.fromiter(kronecker_delta_list).doit()



class TensMul(AssocOp, TensExpr):
    '''
    Product of tensors.

    Parameters
    ==========

    coeff : SymPy coefficient of the tensor
    args

    Attributes
    ==========

    ``components`` : list of ``TensorHead`` of the component tensors
    ``types`` : list of nonrepeated ``TensorIndexType``
    ``free`` : list of ``(ind, ipos, icomp)``, see Notes
    ``dum`` : list of ``(ipos1, ipos2, icomp1, icomp2)``, see Notes
    ``ext_rank`` : rank of the tensor counting the dummy indices
    ``rank`` : rank of the tensor
    ``coeff`` : SymPy coefficient of the tensor
    ``free_args`` : list of the free indices in sorted order
    ``is_canon_bp`` : ``True`` if the tensor in in canonical form

    Notes
    =====

    ``args[0]``   list of ``TensorHead`` of the component tensors.

    ``args[1]``   list of ``(ind, ipos, icomp)``
    where ``ind`` is a free index, ``ipos`` is the slot position
    of ``ind`` in the ``icomp``-th component tensor.

    ``args[2]`` list of tuples representing dummy indices.
    ``(ipos1, ipos2, icomp1, icomp2)`` indicates that the contravariant
    dummy index is the ``ipos1``-th slot position in the ``icomp1``-th
    component tensor; the corresponding covariant index is
    in the ``ipos2`` slot position in the ``icomp2``-th component tensor.

    '''
    identity = S.One
    _index_structure = None
    
    def __new__(cls, *args, **kw_args):
        is_canon_bp = kw_args.get('is_canon_bp', False)
        args = list(map(_sympify, args))
        free = args()
    # WARNING: Decompyle incomplete

    index_types = property((lambda self: self._index_types))
    free = property((lambda self: self._free))
    dum = property((lambda self: self._dum))
    free_indices = property((lambda self: self._free_indices))
    rank = property((lambda self: self._rank))
    ext_rank = property((lambda self: self._ext_rank))
    _indices_to_free_dum = (lambda args_indices: free2pos1 = { }free2pos2 = { }dummy_data = []indices = []pos2 = 0for pos1, arg_indices in enumerate(args_indices):
for index in arg_indices:
if not isinstance(index, TensorIndex):
raise TypeError('expected TensorIndex')if -index in free2pos1:
other_pos1 = free2pos1.pop(-index)other_pos2 = free2pos2.pop(-index)if index.is_up:
dummy_data.append((index, pos1, other_pos1, pos2, other_pos2))else:
dummy_data.append((-index, other_pos1, pos1, other_pos2, pos2))indices.append(index)elif index in free2pos1:
raise ValueError('Repeated index: %s' % index)free2pos1[index] = pos1free2pos2[index] = pos2indices.append(index)pos2 += 1free = list(free2pos2.items())free_names = free2pos2.keys()()dummy_data.sort(key = (lambda x: x[3]))
                return (indices, free, free_names, dummy_data)
)()
    _dummy_data_to_dum = (lambda dummy_data: dummy_data())()
    _tensMul_contract_indices = (lambda args, replace_indices = (True,): pass# WARNING: Decompyle incomplete
)()
    _get_components_from_args = (lambda args: components = []for arg in args:
if not isinstance(arg, TensExpr):
continueif isinstance(arg, TensAdd):
continuecomponents.extend(arg.components)components)()
    _rebuild_tensors_list = (lambda args, index_structure: indices = index_structure.get_indices()ind_pos = 0for i, arg in enumerate(args):
if not isinstance(arg, TensExpr):
continueprev_pos = ind_posind_pos += arg.ext_rankargs[i] = Tensor(arg.component, indices[prev_pos:ind_pos])None)()
    
    def doit(self, **hints):
        pass
    # WARNING: Decompyle incomplete

    from_data = (lambda coeff, components, free, dum: pass# WARNING: Decompyle incomplete
)()
    _get_tensors_from_components_free_dum = (lambda components, free, dum: index_structure = _IndexStructure.from_components_free_dum(components, free, dum)indices = index_structure.get_indices()tensors = components()ind_pos = 0for i, component in enumerate(components):
prev_pos = ind_posind_pos += component.ranktensors[i] = Tensor(component, indices[prev_pos:ind_pos])tensors)()
    
    def _get_free_indices_set(self):
        return self.free()

    
    def _get_dummy_indices_set(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_position_offset_for_indices(self):
        arg_offset = range(self.ext_rank)()
        counter = 0
        for arg in self.args:
            if not isinstance(arg, TensExpr):
                continue
            for j in range(arg.ext_rank):
                arg_offset[j + counter] = counter
                counter += arg.ext_rank
                return arg_offset

    free_args = (lambda self: (lambda .0: [ x[0] for x in .0 ])(self.free())
)()
    components = (lambda self: self._get_components_from_args(self.args))()
    free_in_args = (lambda self: pass# WARNING: Decompyle incomplete
)()
    coeff = (lambda self: self._coeff)()
    nocoeff = (lambda self: pass# WARNING: Decompyle incomplete
)()
    dum_in_args = (lambda self: pass# WARNING: Decompyle incomplete
)()
    
    def equals(self, other):
        if other == 0:
            return self.coeff == 0
        other = None(other)
    # WARNING: Decompyle incomplete

    
    def get_indices(self):
        """
        Returns the list of indices of the tensor.

        Explanation
        ===========

        The indices are listed in the order in which they appear in the
        component tensors.
        The dummy indices are given a name which does not collide with
        the names of the free indices.

        Examples
        ========

        >>> from sympy.tensor.tensor import TensorIndexType, tensor_indices, tensor_heads
        >>> Lorentz = TensorIndexType('Lorentz', dummy_name='L')
        >>> m0, m1, m2 = tensor_indices('m0,m1,m2', Lorentz)
        >>> g = Lorentz.metric
        >>> p, q = tensor_heads('p,q', [Lorentz])
        >>> t = p(m1)*g(m0,m2)
        >>> t.get_indices()
        [m1, m0, m2]
        >>> t2 = p(m1)*g(-m1, m2)
        >>> t2.get_indices()
        [L_0, -L_0, m2]
        """
        return self._indices

    
    def get_free_indices(self = property):
        """
        Returns the list of free indices of the tensor.

        Explanation
        ===========

        The indices are listed in the order in which they appear in the
        component tensors.

        Examples
        ========

        >>> from sympy.tensor.tensor import TensorIndexType, tensor_indices, tensor_heads
        >>> Lorentz = TensorIndexType('Lorentz', dummy_name='L')
        >>> m0, m1, m2 = tensor_indices('m0,m1,m2', Lorentz)
        >>> g = Lorentz.metric
        >>> p, q = tensor_heads('p,q', [Lorentz])
        >>> t = p(m1)*g(m0,m2)
        >>> t.get_free_indices()
        [m1, m0, m2]
        >>> t2 = p(m1)*g(-m1, m2)
        >>> t2.get_free_indices()
        [m2]
        """
        return self._index_structure.get_free_indices()

    
    def _replace_indices(self = property, repl = property):
        pass
    # WARNING: Decompyle incomplete

    
    def split(self):
        """
        Returns a list of tensors, whose product is ``self``.

        Explanation
        ===========

        Dummy indices contracted among different tensor components
        become free indices with the same name as the one used to
        represent the dummy indices.

        Examples
        ========

        >>> from sympy.tensor.tensor import TensorIndexType, tensor_indices, tensor_heads, TensorSymmetry
        >>> Lorentz = TensorIndexType('Lorentz', dummy_name='L')
        >>> a, b, c, d = tensor_indices('a,b,c,d', Lorentz)
        >>> A, B = tensor_heads('A,B', [Lorentz]*2, TensorSymmetry.fully_symmetric(2))
        >>> t = A(a,b)*B(-b,c)
        >>> t
        A(a, L_0)*B(-L_0, c)
        >>> t.split()
        [A(a, L_0), B(-L_0, c)]
        """
        if self.args == ():
            return [
                self]
        splitp = None
        res = 1
        for arg in self.args:
            if isinstance(arg, Tensor):
                splitp.append(res * arg)
                res = 1
                continue
            res *= arg
            return splitp

    
    def _expand(self, **hints):
        pass
    # WARNING: Decompyle incomplete

    
    def __neg__(self):
        return TensMul(S.NegativeOne, self, is_canon_bp = self._is_canon_bp).doit()

    
    def __getitem__(self, item):
        deprecate_data()
        ignore_warnings(SymPyDeprecationWarning)
        None(None, None)
        return 
        with None:
            if not None, self.data[item]:
                pass

    
    def _get_args_for_traditional_printer(self):
        args = list(self.args)
        if self.coeff.could_extract_minus_sign():
            sign = '-'
            if args[0] == S.NegativeOne:
                args = args[1:]
            else:
                args[0] = -args[0]
        else:
            sign = ''
        return (sign, args)

    
    def _sort_args_for_sorted_components(self):
        '''
        Returns the ``args`` sorted according to the components commutation
        properties.

        Explanation
        ===========

        The sorting is done taking into account the commutation group
        of the component tensors.
        '''
        cv = self.args()
        sign = 1
        n = len(cv) - 1
        for i in range(n):
            for j in range(n, i, -1):
                c = cv[j - 1].commutes_with(cv[j])
                if c not in (0, 1):
                    continue
                typ1 = sorted(set(cv[j - 1].component.index_types), key = (lambda x: x.name))
                typ2 = sorted(set(cv[j].component.index_types), key = (lambda x: x.name))
                if (typ1, cv[j - 1].component.name) > (typ2, cv[j].component.name):
                    cv[j - 1], cv[j] = cv[j], cv[j - 1]
                    if c:
                        sign = -sign
                coeff = sign * self.coeff
                if coeff != 1:
                    return [
                        coeff] + cv
                return (lambda .0: pass# WARNING: Decompyle incomplete
)

    
    def sorted_components(self):
        '''
        Returns a tensor product with sorted components.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def perm2tensor(self, g, is_canon_bp = (False,)):
        '''
        Returns the tensor corresponding to the permutation ``g``

        For further details, see the method in ``TIDS`` with the same name.
        '''
        return perm2tensor(self, g, is_canon_bp = is_canon_bp)

    
    def canon_bp(self):
        """
        Canonicalize using the Butler-Portugal algorithm for canonicalization
        under monoterm symmetries.

        Examples
        ========

        >>> from sympy.tensor.tensor import TensorIndexType, tensor_indices, TensorHead, TensorSymmetry
        >>> Lorentz = TensorIndexType('Lorentz', dummy_name='L')
        >>> m0, m1, m2 = tensor_indices('m0,m1,m2', Lorentz)
        >>> A = TensorHead('A', [Lorentz]*2, TensorSymmetry.fully_symmetric(-2))
        >>> t = A(m0,-m1)*A(m1,-m0)
        >>> t.canon_bp()
        -A(L_0, L_1)*A(-L_0, -L_1)
        >>> t = A(m0,-m1)*A(m1,-m2)*A(m2,-m0)
        >>> t.canon_bp()
        0
        """
        if self._is_canon_bp:
            return self
        expr = None.expand()
        if isinstance(expr, TensAdd):
            return expr.canon_bp()
        if not None.components:
            return expr
        t = None.sorted_components()
        (g, dummies, msym) = t._index_structure.indices_canon_args()
        v = components_canon_args(t.components)
    # WARNING: Decompyle incomplete

    
    def contract_delta(self, delta):
        t = self.contract_metric(delta)
        return t

    
    def _get_indices_to_args_pos(self):
        """
        Get a dict mapping the index position to TensMul's argument number.
        """
        pos_map = { }
        pos_counter = 0
    # WARNING: Decompyle incomplete

    
    def contract_metric(self, g):
        """
        Raise or lower indices with the metric ``g``.

        Parameters
        ==========

        g : metric

        Notes
        =====

        See the ``TensorIndexType`` docstring for the contraction conventions.

        Examples
        ========

        >>> from sympy.tensor.tensor import TensorIndexType, tensor_indices, tensor_heads
        >>> Lorentz = TensorIndexType('Lorentz', dummy_name='L')
        >>> m0, m1, m2 = tensor_indices('m0,m1,m2', Lorentz)
        >>> g = Lorentz.metric
        >>> p, q = tensor_heads('p,q', [Lorentz])
        >>> t = p(m0)*q(m1)*g(-m0, -m1)
        >>> t.canon_bp()
        metric(L_0, L_1)*p(-L_0)*q(-L_1)
        >>> t.contract_metric(g).canon_bp()
        p(L_0)*q(-L_0)
        """
        pass
    # WARNING: Decompyle incomplete

    
    def _set_new_index_structure(self, im, is_canon_bp = (False,)):
        indices = im.get_indices()
    # WARNING: Decompyle incomplete

    
    def _set_indices(self = staticmethod, *, is_canon_bp, *indices, **kw_args):
        if len(indices) != self.ext_rank:
            raise ValueError('indices length mismatch')
        args = list(self.args)[:]
        pos = 0
    # WARNING: Decompyle incomplete

    _index_replacement_for_contract_metric = (lambda args, free, dum: pass# WARNING: Decompyle incomplete
)()
    
    def substitute_indices(self, *index_tuples):
        new_args = []
    # WARNING: Decompyle incomplete

    
    def __call__(self, *indices):
        deprecate_call()
        free_args = self.free_args
        indices = list(indices)
        if (lambda .0: [ x.tensor_index_type for x in .0 ]) != free_args():
            raise ValueError('incompatible types')
        if indices == free_args:
            return self
    # WARNING: Decompyle incomplete

    
    def _extract_data(self, replacement_dict):
        pass
    # WARNING: Decompyle incomplete

    data = (lambda self: deprecate_data()ignore_warnings(SymPyDeprecationWarning)dat = _tensor_data_substitution_dict[self.expand()]None(None, None))()
    data = (lambda self, data: deprecate_data()raise ValueError('Not possible to set component data to a tensor expression'))()
    data = (lambda self: deprecate_data()raise ValueError('Not possible to delete component data to a tensor expression'))()
    
    def __iter__(self):
        deprecate_data()
        ignore_warnings(SymPyDeprecationWarning)
    # WARNING: Decompyle incomplete

    _dedupe_indices = (lambda new, exclude: exclude = set(exclude)dums_new = set(get_dummy_indices(new))free_new = set(get_free_indices(new))conflicts = dums_new.intersection(exclude)if len(conflicts) == 0:
Noneexclude.update(dums_new)exclude.update(free_new)exclude_for_gen = exclude()gen = _IndexStructure._get_generator_for_dummy_indices(exclude_for_gen)repl = { }# WARNING: Decompyle incomplete
)()
    
    def _dedupe_indices_in_rule(self, rule):
        '''
        rule: dict

        This applies TensMul._dedupe_indices on all values of rule.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_rewrite_as_Indexed(self, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_partial_derivative(self, s):
        terms = []
        for i, arg in enumerate(self.args):
            if isinstance(arg, TensExpr):
                d = arg._eval_partial_derivative(s)
            elif s._diff_wrt:
                d = arg._eval_derivative(s)
            else:
                d = S.Zero
            if d:
                terms.append(TensMul.fromiter(self.args[:i] + (d,) + self.args[i + 1:]))
            return TensAdd.fromiter(terms)



class TensorElement(TensExpr):
    '''
    Tensor with evaluated components.

    Examples
    ========

    >>> from sympy.tensor.tensor import TensorIndexType, TensorHead, TensorSymmetry
    >>> from sympy import symbols
    >>> L = TensorIndexType("L")
    >>> i, j, k = symbols("i j k")
    >>> A = TensorHead("A", [L, L], TensorSymmetry.fully_symmetric(2))
    >>> A(i, j).get_free_indices()
    [i, j]

    If we want to set component ``i`` to a specific value, use the
    ``TensorElement`` class:

    >>> from sympy.tensor.tensor import TensorElement
    >>> te = TensorElement(A(i, j), {i: 2})

    As index ``i`` has been accessed (``{i: 2}`` is the evaluation of its 3rd
    element), the free indices will only contain ``j``:

    >>> te.get_free_indices()
    [j]
    '''
    
    def __new__(cls, expr, index_map):
        pass
    # WARNING: Decompyle incomplete

    free = (lambda self: enumerate(self.get_free_indices())())()
    dum = (lambda self: [])()
    expr = (lambda self: self._args[0])()
    index_map = (lambda self: self._args[1])()
    coeff = (lambda self: S.One)()
    nocoeff = (lambda self: self)()
    
    def get_free_indices(self):
        return self._free_indices

    
    def _replace_indices(self = property, repl = property):
        return self.xreplace(repl)

    
    def get_indices(self):
        return self.get_free_indices()

    
    def _extract_data(self, replacement_dict):
        pass
    # WARNING: Decompyle incomplete



class WildTensorHead(TensorHead):
    '''
    A wild object that is used to create ``WildTensor`` instances

    Explanation
    ===========

    Examples
    ========
    >>> from sympy.tensor.tensor import TensorHead, TensorIndex, WildTensorHead, TensorIndexType
    >>> R3 = TensorIndexType(\'R3\', dim=3)
    >>> p = TensorIndex(\'p\', R3)
    >>> q = TensorIndex(\'q\', R3)

    A WildTensorHead can be created without specifying a ``TensorIndexType``

    >>> W = WildTensorHead("W")

    Calling it with a ``TensorIndex`` creates a ``WildTensor`` instance.

    >>> type(W(p))
    <class \'sympy.tensor.tensor.WildTensor\'>

    The ``TensorIndexType`` is automatically detected from the index that is passed

    >>> W(p).component
    W(R3)

    Calling it with no indices returns an object that can match tensors with any number of indices.

    >>> K = TensorHead(\'K\', [R3])
    >>> Q = TensorHead(\'Q\', [R3, R3])
    >>> W().matches(K(p))
    {W: K(p)}
    >>> W().matches(Q(p,q))
    {W: Q(p, q)}

    If you want to ignore the order of indices while matching, pass ``unordered_indices=True``.

    >>> U = WildTensorHead("U", unordered_indices=True)
    >>> W(p,q).matches(Q(q,p))
    >>> U(p,q).matches(Q(q,p))
    {U(R3,R3): _WildTensExpr(Q(q, p))}

    Parameters
    ==========
    name : name of the tensor
    unordered_indices : whether the order of the indices matters for matching
        (default: False)

    See also
    ========
    ``WildTensor``
    ``TensorHead``

    '''
    
    def __new__(cls, name, index_types, symmetry, comm, unordered_indices = (None, None, 0, False)):
        if isinstance(name, str):
            name_symbol = Symbol(name)
        elif isinstance(name, Symbol):
            name_symbol = name
        else:
            raise ValueError('invalid name')
    # WARNING: Decompyle incomplete

    unordered_indices = (lambda self: self.args[4])()
    
    def __call__(self, *indices, **kwargs):
        pass
    # WARNING: Decompyle incomplete



class WildTensor(Tensor):
    '''
    A wild object which matches ``Tensor`` instances

    Explanation
    ===========
    This is instantiated by attaching indices to a ``WildTensorHead`` instance.

    Examples
    ========
    >>> from sympy.tensor.tensor import TensorHead, TensorIndex, WildTensorHead, TensorIndexType
    >>> W = WildTensorHead("W")
    >>> R3 = TensorIndexType(\'R3\', dim=3)
    >>> p = TensorIndex(\'p\', R3)
    >>> q = TensorIndex(\'q\', R3)
    >>> K = TensorHead(\'K\', [R3])
    >>> Q = TensorHead(\'Q\', [R3, R3])

    Matching also takes the indices into account
    >>> W(p).matches(K(p))
    {W(R3): _WildTensExpr(K(p))}
    >>> W(p).matches(K(q))
    >>> W(p).matches(K(-p))

    If you want to match objects with any number of indices, just use a ``WildTensor`` with no indices.
    >>> W().matches(K(p))
    {W: K(p)}
    >>> W().matches(Q(p,q))
    {W: Q(p, q)}

    See Also
    ========
    ``WildTensorHead``
    ``Tensor``

    '''
    
    def __new__(cls, tensor_head, indices, **kw_args):
        is_canon_bp = kw_args.pop('is_canon_bp', False)
    # WARNING: Decompyle incomplete

    
    def matches(self, expr, repl_dict, old = (None, False)):
        if isinstance(expr, TensExpr) and expr != S(1):
            return None
    # WARNING: Decompyle incomplete

    
    def _match_indices_ignoring_order(self, expr, repl_dict, old = (None, False)):
        '''
        Helper method for matches. Checks if the indices of self and expr
        match disregarding index ordering.
        '''
        pass
    # WARNING: Decompyle incomplete



class WildTensorIndex(TensorIndex):
    '''
    A wild object that matches TensorIndex instances.

    Examples
    ========
    >>> from sympy.tensor.tensor import TensorIndex, TensorIndexType, WildTensorIndex
    >>> R3 = TensorIndexType(\'R3\', dim=3)
    >>> p = TensorIndex("p", R3)

    By default, covariant indices only match with covariant indices (and
    similarly for contravariant)

    >>> q = WildTensorIndex("q", R3)
    >>> (q).matches(p)
    {q: p}
    >>> (q).matches(-p)

    If you want matching to ignore whether the index is co/contra-variant, set
    ignore_updown=True

    >>> r = WildTensorIndex("r", R3, ignore_updown=True)
    >>> (r).matches(-p)
    {r: -p}
    >>> (r).matches(p)
    {r: p}

    Parameters
    ==========
    name : name of the index (string), or ``True`` if you want it to be
        automatically assigned
    tensor_index_type : ``TensorIndexType`` of the index
    is_up :  flag for contravariant index (is_up=True by default)
    ignore_updown : bool, Whether this should match both co- and contra-variant
        indices (default:False)
    '''
    
    def __new__(cls, name, tensor_index_type, is_up, ignore_updown = (True, False)):
        if isinstance(name, str):
            name_symbol = Symbol(name)
        elif isinstance(name, Symbol):
            name_symbol = name
        elif name is True:
            name = '_i{}'.format(len(tensor_index_type._autogenerated))
            name_symbol = Symbol(name)
            tensor_index_type._autogenerated.append(name_symbol)
        else:
            raise ValueError('invalid name')
        is_up = sympify(is_up)
        ignore_updown = sympify(ignore_updown)
        return Basic.__new__(cls, name_symbol, tensor_index_type, is_up, ignore_updown)

    ignore_updown = (lambda self: self.args[3])()
    
    def __neg__(self):
        t1 = WildTensorIndex(self.name, self.tensor_index_type, not (self.is_up), self.ignore_updown)
        return t1

    
    def matches(self, expr, repl_dict, old = (None, False)):
        if not isinstance(expr, TensorIndex):
            return None
        if None.tensor_index_type != expr.tensor_index_type:
            return None
        if None.ignore_updown and self.is_up != expr.is_up:
            return None
    # WARNING: Decompyle incomplete



class _WildTensExpr(Basic):
    '''
    INTERNAL USE ONLY

    This is an object that helps with replacement of WildTensors in expressions.
    When this object is set as the tensor_head of a WildTensor, it replaces the
    WildTensor by a TensExpr (passed when initializing this object).

    Examples
    ========
    >>> from sympy.tensor.tensor import WildTensorHead, TensorIndex, TensorHead, TensorIndexType
    >>> W = WildTensorHead("W")
    >>> R3 = TensorIndexType(\'R3\', dim=3)
    >>> p = TensorIndex(\'p\', R3)
    >>> q = TensorIndex(\'q\', R3)
    >>> K = TensorHead(\'K\', [R3])
    >>> print( ( K(p) ).replace( W(p), W(q)*W(-q)*W(p) ) )
    K(R_0)*K(-R_0)*K(p)

    '''
    
    def __init__(self, expr):
        if not isinstance(expr, TensExpr):
            raise TypeError('_WildTensExpr expects a TensExpr as argument')
        self.expr = expr

    
    def __call__(self, *indices):
        return self.expr._replace_indices(dict(zip(self.expr.get_free_indices(), indices)))

    
    def __neg__(self):
        return self.func(self.expr * S.NegativeOne)

    
    def __abs__(self):
        raise NotImplementedError

    
    def __add__(self, other):
        if other.func != self.func:
            raise TypeError(f'''Cannot add {self.func} to {other.func}''')
        return self.func(self.expr + other.expr)

    
    def __radd__(self, other):
        if other.func != self.func:
            raise TypeError(f'''Cannot add {self.func} to {other.func}''')
        return self.func(other.expr + self.expr)

    
    def __sub__(self, other):
        return self + -other

    
    def __rsub__(self, other):
        return other + -self

    
    def __mul__(self, other):
        raise NotImplementedError

    
    def __rmul__(self, other):
        raise NotImplementedError

    
    def __truediv__(self, other):
        raise NotImplementedError

    
    def __rtruediv__(self, other):
        raise NotImplementedError

    
    def __pow__(self, other):
        raise NotImplementedError

    
    def __rpow__(self, other):
        raise NotImplementedError



def canon_bp(p):
    '''
    Butler-Portugal canonicalization. See ``tensor_can.py`` from the
    combinatorics module for the details.
    '''
    if isinstance(p, TensExpr):
        return p.canon_bp()


def tensor_mul(*a):
    '''
    product of tensors
    '''
    if not a:
        return TensMul.from_data(S.One, [], [], [])
    t = None[0]
    for tx in a[1:]:
        t = t * tx
        return t


def riemann_cyclic_replace(t_r):
    '''
    replace Riemann tensor with an equivalent expression

    ``R(m,n,p,q) -> 2/3*R(m,n,p,q) - 1/3*R(m,q,n,p) + 1/3*R(m,p,n,q)``

    '''
    free = sorted(t_r.free, key = (lambda x: x[1]))
    (m, n, p, q) = free()
    t0 = t_r * Rational(2, 3)
    t1 = -t_r.substitute_indices((m, m), (n, q), (p, n), (q, p)) * Rational(1, 3)
    t2 = t_r.substitute_indices((m, m), (n, p), (p, n), (q, q)) * Rational(1, 3)
    t3 = t0 + t1 + t2
    return t3


def riemann_cyclic(t2):
    """
    Replace each Riemann tensor with an equivalent expression
    satisfying the cyclic identity.

    This trick is discussed in the reference guide to Cadabra.

    Examples
    ========

    >>> from sympy.tensor.tensor import TensorIndexType, tensor_indices, TensorHead, riemann_cyclic, TensorSymmetry
    >>> Lorentz = TensorIndexType('Lorentz', dummy_name='L')
    >>> i, j, k, l = tensor_indices('i,j,k,l', Lorentz)
    >>> R = TensorHead('R', [Lorentz]*4, TensorSymmetry.riemann())
    >>> t = R(i,j,k,l)*(R(-i,-j,-k,-l) - 2*R(-i,-k,-j,-l))
    >>> riemann_cyclic(t)
    0
    """
    t2 = t2.expand()
    if isinstance(t2, (TensMul, Tensor)):
        args = [
            t2]
    else:
        args = t2.args
    a1 = args()
    a2 = a1()
    a3 = a2()
# WARNING: Decompyle incomplete


def get_lines(ex, index_type):
    '''
    Returns ``(lines, traces, rest)`` for an index type,
    where ``lines`` is the list of list of positions of a matrix line,
    ``traces`` is the list of list of traced matrix lines,
    ``rest`` is the rest of the elements of the tensor.
    '''
    pass
# WARNING: Decompyle incomplete


def get_free_indices(t):
    if not isinstance(t, TensExpr):
        return ()
    return None.get_free_indices()


def get_indices(t):
    if not isinstance(t, TensExpr):
        return ()
    return None.get_indices()


def get_dummy_indices(t):
    pass
# WARNING: Decompyle incomplete


def get_index_structure(t):
    if isinstance(t, TensExpr):
        return t._index_structure
    return None([], [], [], [])


def get_coeff(t):
    if isinstance(t, Tensor):
        return S.One
    if None(t, TensMul):
        return t.coeff
    if None(t, TensExpr):
        raise ValueError('no coefficient associated to this tensor expression')
    return t


def contract_metric(t, g):
    if isinstance(t, TensExpr):
        return t.contract_metric(g)


def perm2tensor(t, g, is_canon_bp = (False,)):
    '''
    Returns the tensor corresponding to the permutation ``g``

    For further details, see the method in ``TIDS`` with the same name.
    '''
    if not isinstance(t, TensExpr):
        return t
    if None(t, (Tensor, TensMul)):
        nim = get_index_structure(t).perm2tensor(g, is_canon_bp = is_canon_bp)
        res = t._set_new_index_structure(nim, is_canon_bp = is_canon_bp)
        if g[-1] != len(g) - 1:
            return -res
        return None
    raise None()


def substitute_indices(t, *index_tuples):
    if not isinstance(t, TensExpr):
        return t
# WARNING: Decompyle incomplete


def _expand(expr, **kwargs):
    pass
# WARNING: Decompyle incomplete


def get_postprocessor(cls):
    pass
# WARNING: Decompyle incomplete

Basic._constructor_postprocessor_mapping[TensExpr] = {
    'Mul': [
        get_postprocessor(Mul)] }

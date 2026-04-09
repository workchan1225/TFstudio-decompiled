# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: einsumfunc.pyc (Python 3.11)

'''
Implementation of optimized einsum.

'''
import itertools
import operator
from numpy.core.multiarray import c_einsum
from numpy.core.numeric import asanyarray, tensordot
from numpy.core.overrides import array_function_dispatch
__all__ = [
    'einsum',
    'einsum_path']
einsum_symbols = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
einsum_symbols_set = set(einsum_symbols)

def _flop_count(idx_contraction, inner, num_terms, size_dictionary):
    """
    Computes the number of FLOPS in the contraction.

    Parameters
    ----------
    idx_contraction : iterable
        The indices involved in the contraction
    inner : bool
        Does this contraction require an inner product?
    num_terms : int
        The number of terms in a contraction
    size_dictionary : dict
        The size of each of the indices in idx_contraction

    Returns
    -------
    flop_count : int
        The total number of FLOPS required for the contraction.

    Examples
    --------

    >>> _flop_count('abc', False, 1, {'a': 2, 'b':3, 'c':5})
    30

    >>> _flop_count('abc', True, 2, {'a': 2, 'b':3, 'c':5})
    60

    """
    overall_size = _compute_size_by_dict(idx_contraction, size_dictionary)
    op_factor = max(1, num_terms - 1)
    if inner:
        op_factor += 1
    return overall_size * op_factor


def _compute_size_by_dict(indices, idx_dict):
    """
    Computes the product of the elements in indices based on the dictionary
    idx_dict.

    Parameters
    ----------
    indices : iterable
        Indices to base the product on.
    idx_dict : dictionary
        Dictionary of index sizes

    Returns
    -------
    ret : int
        The resulting product.

    Examples
    --------
    >>> _compute_size_by_dict('abbc', {'a': 2, 'b':3, 'c':5})
    90

    """
    ret = 1
    for i in indices:
        ret *= idx_dict[i]
        return ret


def _find_contraction(positions, input_sets, output_set):
    """
    Finds the contraction for a given set of input and output sets.

    Parameters
    ----------
    positions : iterable
        Integer positions of terms used in the contraction.
    input_sets : list
        List of sets that represent the lhs side of the einsum subscript
    output_set : set
        Set that represents the rhs side of the overall einsum subscript

    Returns
    -------
    new_result : set
        The indices of the resulting contraction
    remaining : list
        List of sets that have not been contracted, the new set is appended to
        the end of this list
    idx_removed : set
        Indices removed from the entire contraction
    idx_contraction : set
        The indices used in the current contraction

    Examples
    --------

    # A simple dot product test case
    >>> pos = (0, 1)
    >>> isets = [set('ab'), set('bc')]
    >>> oset = set('ac')
    >>> _find_contraction(pos, isets, oset)
    ({'a', 'c'}, [{'a', 'c'}], {'b'}, {'a', 'b', 'c'})

    # A more complex case with additional terms in the contraction
    >>> pos = (0, 2)
    >>> isets = [set('abd'), set('ac'), set('bdc')]
    >>> oset = set('ac')
    >>> _find_contraction(pos, isets, oset)
    ({'a', 'c'}, [{'a', 'c'}, {'a', 'c'}], {'b', 'd'}, {'a', 'b', 'c', 'd'})
    """
    idx_contract = set()
    idx_remain = output_set.copy()
    remaining = []
    for ind, value in enumerate(input_sets):
        if ind in positions:
            idx_contract |= value
            continue
        remaining.append(value)
        idx_remain |= value
        new_result = idx_remain & idx_contract
        idx_removed = idx_contract - new_result
        remaining.append(new_result)
        return (new_result, remaining, idx_removed, idx_contract)


def _optimal_path(input_sets, output_set, idx_dict, memory_limit):
    """
    Computes all possible pair contractions, sieves the results based
    on ``memory_limit`` and returns the lowest cost path. This algorithm
    scales factorial with respect to the elements in the list ``input_sets``.

    Parameters
    ----------
    input_sets : list
        List of sets that represent the lhs side of the einsum subscript
    output_set : set
        Set that represents the rhs side of the overall einsum subscript
    idx_dict : dictionary
        Dictionary of index sizes
    memory_limit : int
        The maximum number of elements in a temporary array

    Returns
    -------
    path : list
        The optimal contraction order within the memory limit constraint.

    Examples
    --------
    >>> isets = [set('abd'), set('ac'), set('bdc')]
    >>> oset = set()
    >>> idx_sizes = {'a': 1, 'b':2, 'c':3, 'd':4}
    >>> _optimal_path(isets, oset, idx_sizes, 5000)
    [(0, 2), (0, 1)]
    """
    full_results = [
        (0, [], input_sets)]
    for iteration in range(len(input_sets) - 1):
        iter_results = []
        for curr in full_results:
            (cost, positions, remaining) = curr
            for con in itertools.combinations(range(len(input_sets) - iteration), 2):
                cont = _find_contraction(con, remaining, output_set)
                (new_result, new_input_sets, idx_removed, idx_contract) = cont
                new_size = _compute_size_by_dict(new_result, idx_dict)
                if new_size > memory_limit:
                    continue
                total_cost = cost + _flop_count(idx_contract, idx_removed, len(con), idx_dict)
                new_pos = positions + [
                    con]
                iter_results.append((total_cost, new_pos, new_input_sets))
                if iter_results:
                    full_results = iter_results
                    continue
        path = min(full_results, key = (lambda x: x[0]))[1]
        path += [
            tuple(range(len(input_sets) - iteration))]
        
        return None, path
        if len(full_results) == 0:
            return [
                tuple(range(len(input_sets)))]
        return path


def _parse_possible_contraction(positions, input_sets, output_set, idx_dict, memory_limit, path_cost, naive_cost):
    '''Compute the cost (removed size + flops) and resultant indices for
    performing the contraction specified by ``positions``.

    Parameters
    ----------
    positions : tuple of int
        The locations of the proposed tensors to contract.
    input_sets : list of sets
        The indices found on each tensors.
    output_set : set
        The output indices of the expression.
    idx_dict : dict
        Mapping of each index to its size.
    memory_limit : int
        The total allowed size for an intermediary tensor.
    path_cost : int
        The contraction cost so far.
    naive_cost : int
        The cost of the unoptimized expression.

    Returns
    -------
    cost : (int, int)
        A tuple containing the size of any indices removed, and the flop cost.
    positions : tuple of int
        The locations of the proposed tensors to contract.
    new_input_sets : list of sets
        The resulting new list of indices if this proposed contraction is performed.

    '''
    pass
# WARNING: Decompyle incomplete


def _update_other_results(results, best):
    '''Update the positions and provisional input_sets of ``results`` based on
    performing the contraction result ``best``. Remove any involving the tensors
    contracted.

    Parameters
    ----------
    results : list
        List of contraction results produced by ``_parse_possible_contraction``.
    best : list
        The best contraction of ``results`` i.e. the one that will be performed.

    Returns
    -------
    mod_results : list
        The list of modified results, updated with outcome of ``best`` contraction.
    '''
    best_con = best[1]
    (bx, by) = best_con
    mod_results = []
    for x, y in results:
        con_sets = None
        if x in best_con or y in best_con:
            continue
        del con_sets[by - int(by > x) - int(by > y)]
        del con_sets[bx - int(bx > x) - int(bx > y)]
        con_sets.insert(-1, best[2][-1])
        mod_con = (x - int(x > bx) - int(x > by), y - int(y > bx) - int(y > by))
        mod_results.append((cost, mod_con, con_sets))
        return mod_results


def _greedy_path(input_sets, output_set, idx_dict, memory_limit):
    """
    Finds the path by contracting the best pair until the input list is
    exhausted. The best pair is found by minimizing the tuple
    ``(-prod(indices_removed), cost)``.  What this amounts to is prioritizing
    matrix multiplication or inner product operations, then Hadamard like
    operations, and finally outer operations. Outer products are limited by
    ``memory_limit``. This algorithm scales cubically with respect to the
    number of elements in the list ``input_sets``.

    Parameters
    ----------
    input_sets : list
        List of sets that represent the lhs side of the einsum subscript
    output_set : set
        Set that represents the rhs side of the overall einsum subscript
    idx_dict : dictionary
        Dictionary of index sizes
    memory_limit : int
        The maximum number of elements in a temporary array

    Returns
    -------
    path : list
        The greedy contraction order within the memory limit constraint.

    Examples
    --------
    >>> isets = [set('abd'), set('ac'), set('bdc')]
    >>> oset = set()
    >>> idx_sizes = {'a': 1, 'b':2, 'c':3, 'd':4}
    >>> _greedy_path(isets, oset, idx_sizes, 5000)
    [(0, 2), (0, 1)]
    """
    pass
# WARNING: Decompyle incomplete


def _can_dot(inputs, result, idx_removed):
    """
    Checks if we can use BLAS (np.tensordot) call and its beneficial to do so.

    Parameters
    ----------
    inputs : list of str
        Specifies the subscripts for summation.
    result : str
        Resulting summation.
    idx_removed : set
        Indices that are removed in the summation


    Returns
    -------
    type : bool
        Returns true if BLAS should and can be used, else False

    Notes
    -----
    If the operations is BLAS level 1 or 2 and is not already aligned
    we default back to einsum as the memory movement to copy is more
    costly than the operation itself.


    Examples
    --------

    # Standard GEMM operation
    >>> _can_dot(['ij', 'jk'], 'ik', set('j'))
    True

    # Can use the standard BLAS, but requires odd data movement
    >>> _can_dot(['ijj', 'jk'], 'ik', set('j'))
    False

    # DDOT where the memory is not aligned
    >>> _can_dot(['ijk', 'ikj'], '', set('ijk'))
    False

    """
    if len(idx_removed) == 0:
        return False
    if None(inputs) != 2:
        return False
    (input_left, input_right) = None
    for c in set(input_left + input_right):
        nr = input_right.count(c)
        nl = input_left.count(c)
        if nl > 1 and nr > 1 or nl + nr > 2:
            return False
        if None + nr - 1 == int(c in result):
            return False
        set_left = set(input_left)
        set_right = set(input_right)
        keep_left = set_left - idx_removed
        keep_right = set_right - idx_removed
        rs = len(idx_removed)
        if input_left == input_right:
            return True
        if None == set_right:
            return False
        if None[-rs:] == input_right[:rs]:
            return True
        if None[:rs] == input_right[-rs:]:
            return True
        if None[-rs:] == input_right[-rs:]:
            return True
        if None[:rs] == input_right[:rs]:
            return True
        if not None or keep_right:
            return False
        return None


def _parse_einsum_input(operands):
    """
    A reproduction of einsum c side einsum parsing in python.

    Returns
    -------
    input_strings : str
        Parsed input strings
    output_string : str
        Parsed output string
    operands : list of array_like
        The operands to use in the numpy contraction

    Examples
    --------
    The operand list is simplified to reduce printing:

    >>> np.random.seed(123)
    >>> a = np.random.rand(4, 4)
    >>> b = np.random.rand(4, 4, 4)
    >>> _parse_einsum_input(('...a,...a->...', a, b))
    ('za,xza', 'xz', [a, b]) # may vary

    >>> _parse_einsum_input((a, [Ellipsis, 0], b, [Ellipsis, 0]))
    ('za,xza', 'xz', [a, b]) # may vary
    """
    if len(operands) == 0:
        raise ValueError('No input operands')
    if isinstance(operands[0], str):
        subscripts = operands[0].replace(' ', '')
        operands = operands[1:]()
        for s in subscripts:
            if s in '.,->':
                continue
            if s not in einsum_symbols:
                raise ValueError('Character %s is not a valid symbol.' % s)
    tmp_operands = list(operands)
    operand_list = []
    subscript_list = []
    for p in range(len(operands) // 2):
        operand_list.append(tmp_operands.pop(0))
        subscript_list.append(tmp_operands.pop(0))
    output_list = tmp_operands[-1] if len(tmp_operands) else None
    operands = operand_list()
    subscripts = ''
    last = len(subscript_list) - 1
# WARNING: Decompyle incomplete


def _einsum_path_dispatcher(*, optimize, einsum_call, *operands):
    return operands

einsum_path = (lambda *: pass# WARNING: Decompyle incomplete
)()

def _einsum_dispatcher(*, out, optimize, *operands, **kwargs):
    pass
# WARNING: Decompyle incomplete

einsum = (lambda *: pass# WARNING: Decompyle incomplete
)()

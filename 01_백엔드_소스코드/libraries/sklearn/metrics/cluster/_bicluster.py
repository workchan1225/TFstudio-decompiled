# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _bicluster.pyc (Python 3.11)

import numpy as np
from scipy.optimize import linear_sum_assignment
from sklearn.utils._param_validation import StrOptions, validate_params
from sklearn.utils.validation import check_array, check_consistent_length
__all__ = [
    'consensus_score']

def _check_rows_and_columns(a, b):
    '''Unpacks the row and column arrays and checks their shape.'''
    pass
# WARNING: Decompyle incomplete


def _jaccard(a_rows, a_cols, b_rows, b_cols):
    '''Jaccard coefficient on the elements of the two biclusters.'''
    intersection = (a_rows * b_rows).sum() * (a_cols * b_cols).sum()
    a_size = a_rows.sum() * a_cols.sum()
    b_size = b_rows.sum() * b_cols.sum()
    return intersection / (a_size + b_size - intersection)


def _pairwise_similarity(a, b, similarity):
    """Computes pairwise similarity matrix.

    result[i, j] is the Jaccard coefficient of a's bicluster i and b's
    bicluster j.

    """
    pass
# WARNING: Decompyle incomplete

consensus_score = (lambda a = validate_params({
    'a': [
        tuple],
    'b': [
        tuple],
    'similarity': [
        callable,
        StrOptions({
            'jaccard'})] }, prefer_skip_nested_validation = True), b = {
    'similarity': 'jaccard' }, *, similarity, matrix = None: if similarity == 'jaccard':
similarity = _jaccardmatrix = _pairwise_similarity(a, b, similarity)(row_indices, col_indices) = linear_sum_assignment(1 - matrix)n_a = len(a[0])n_b = len(b[0])float(matrix[(row_indices, col_indices)].sum() / max(n_a, n_b)))()

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: random.pyc (Python 3.11)

'''Utilities for random sampling.'''
import array
import numpy as np
from scipy.sparse import sparse as sp
from sklearn.utils import check_random_state
from sklearn.utils._random import sample_without_replacement
__all__ = [
    'sample_without_replacement']

def _random_choice_csc(n_samples, classes, class_probability, random_state = (None, None)):
    '''Generate a sparse random matrix given column class distributions

    Parameters
    ----------
    n_samples : int,
        Number of samples to draw in each column.

    classes : list of size n_outputs of arrays of size (n_classes,)
        List of classes for each column.

    class_probability : list of size n_outputs of arrays of         shape (n_classes,), default=None
        Class distribution of each column. If None, uniform distribution is
        assumed.

    random_state : int, RandomState instance or None, default=None
        Controls the randomness of the sampled classes.
        See :term:`Glossary <random_state>`.

    Returns
    -------
    random_matrix : sparse csc matrix of size (n_samples, n_outputs)

    '''
    data = array.array('i')
    indices = array.array('i')
    indptr = array.array('i', [
        0])
# WARNING: Decompyle incomplete

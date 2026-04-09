# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: categorical.pyc (Python 3.11)

from __future__ import annotations
import numpy as np
from pandas.core.algorithms import unique1d
from pandas.core.arrays.categorical import Categorical, CategoricalDtype, recode_for_categories

def recode_for_groupby(c = None, sort = None, observed = None):
    '''
    Code the categories to ensure we can groupby for categoricals.

    If observed=True, we return a new Categorical with the observed
    categories only.

    If sort=False, return a copy of self, coded with categories as
    returned by .unique(), followed by any categories not appearing in
    the data. If sort=True, return self.

    This method is needed solely to ensure the categorical index of the
    GroupBy result has categories in the order of appearance in the data
    (GH-8868).

    Parameters
    ----------
    c : Categorical
    sort : bool
        The value of the sort parameter groupby was called with.
    observed : bool
        Account only for the observed values

    Returns
    -------
    Categorical
        If sort=False, the new categories are set to the order of
        appearance in codes (unless ordered=True, in which case the
        original order is preserved), followed by any unrepresented
        categories in the original order.
    '''
    if observed:
        take_codes = unique1d(c.codes[c.codes != -1])
        if sort:
            take_codes = np.sort(take_codes)
        categories = c.categories.take(take_codes)
        codes = recode_for_categories(c.codes, c.categories, categories, copy = False)
        dtype = CategoricalDtype(categories, ordered = c.ordered)
        return Categorical._simple_new(codes, dtype = dtype)
    if None:
        return c
    unique_notnan_codes = None(c.codes[c.codes != -1])
    if sort:
        unique_notnan_codes = np.sort(unique_notnan_codes)
    num_cat = len(c.categories)
    if len(c.categories) > len(unique_notnan_codes):
        missing_codes = np.setdiff1d(np.arange(num_cat), unique_notnan_codes, assume_unique = True)
        take_codes = np.concatenate((unique_notnan_codes, missing_codes))
    else:
        take_codes = unique_notnan_codes
    return Categorical(c, c.categories.take(take_codes))

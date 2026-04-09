# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _testing.pyc (Python 3.11)

'''Testing utilities.'''
import atexit
import contextlib
import functools
import importlib
import inspect
import os
from os.path import path as op
import re
import shutil
import sys
import tempfile
import textwrap
import unittest
import warnings
from collections import defaultdict, namedtuple
from collections.abc import Iterable
from dataclasses import dataclass
from difflib import context_diff
from functools import wraps
from inspect import signature
from itertools import chain, groupby
from subprocess import STDOUT, CalledProcessError, TimeoutExpired, check_output
import joblib
import numpy as np
import scipy as sp
from numpy.testing import assert_allclose as np_assert_allclose
from numpy.testing import assert_almost_equal, assert_array_almost_equal, assert_array_equal, assert_array_less
from sklearn import __file__ as sklearn_path
from sklearn.utils import ClassifierTags, RegressorTags, Tags, TargetTags, TransformerTags
from sklearn.utils._array_api import _check_array_api_dispatch
from sklearn.utils.fixes import _IS_32BIT, VisibleDeprecationWarning, _in_unstable_openblas_configuration
from sklearn.utils.multiclass import check_classification_targets
from sklearn.utils.validation import check_array, check_is_fitted, check_X_y
__all__ = [
    'SkipTest',
    'assert_allclose',
    'assert_almost_equal',
    'assert_array_almost_equal',
    'assert_array_equal',
    'assert_array_less',
    'assert_run_python_script_without_output']
SkipTest = unittest.case.SkipTest

def ignore_warnings(obj, category = (None, Warning)):
    """Context manager and decorator to ignore warnings.

    Note: Using this (in both variants) will clear all warnings
    from all python modules loaded. In case you need to test
    cross-module-warning-logging, this is not your tool of choice.

    Parameters
    ----------
    obj : callable, default=None
        callable where you want to ignore the warnings.
    category : warning class, default=Warning
        The category to filter. If Warning, all categories will be muted.

    Examples
    --------
    >>> import warnings
    >>> from sklearn.utils._testing import ignore_warnings
    >>> with ignore_warnings():
    ...     warnings.warn('buhuhuhu')

    >>> def nasty_warn():
    ...     warnings.warn('buhuhuhu')
    ...     print(42)

    >>> ignore_warnings(nasty_warn)()
    42
    """
    if isinstance(obj, type) and issubclass(obj, Warning):
        warning_name = obj.__name__
        raise ValueError("'obj' should be a callable where you want to ignore warnings. You passed a warning class instead: 'obj={warning_name}'. If you want to pass a warning class to ignore_warnings, you should use 'category={warning_name}'".format(warning_name = warning_name))
    if callable(obj):
        return _IgnoreWarnings(category = category)(obj)
    return None(category = category)


class _IgnoreWarnings:
    '''Improved and simplified Python warnings context manager and decorator.

    This class allows the user to ignore the warnings raised by a function.
    Copied from Python 2.7.5 and modified as required.

    Parameters
    ----------
    category : tuple of warning class, default=Warning
        The category to filter. By default, all the categories will be muted.

    '''
    
    def __init__(self, category):
        self._record = True
        self._module = sys.modules['warnings']
        self._entered = False
        self.log = []
        self.category = category

    
    def __call__(self, fn):
        '''Decorator to catch and hide warnings without visual nesting.'''
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self):
        args = []
        if self._record:
            args.append('record=True')
        if self._module is not sys.modules['warnings']:
            args.append('module=%r' % self._module)
        name = type(self).__name__
        return f'''{name!s}({', '.join(args)!s})'''

    
    def __enter__(self):
        if self._entered:
            raise RuntimeError('Cannot enter %r twice' % self)
        self._entered = True
        self._filters = self._module.filters
        self._module.filters = self._filters[:]
        self._showwarning = self._module.showwarning
        warnings.simplefilter('ignore', self.category)

    
    def __exit__(self, *exc_info):
        if not self._entered:
            raise RuntimeError('Cannot exit %r without entering first' % self)
        self._module.filters = self._filters
        self._module.showwarning = self._showwarning
        self.log[:] = []



def assert_allclose(actual, desired, rtol, atol, equal_nan, err_msg, verbose = (None, 0, True, '', True)):
    """dtype-aware variant of numpy.testing.assert_allclose

    This variant introspects the least precise floating point dtype
    in the input argument and automatically sets the relative tolerance
    parameter to 1e-4 float32 and use 1e-7 otherwise (typically float64
    in scikit-learn).

    `atol` is always left to 0. by default. It should be adjusted manually
    to an assertion-specific value in case there are null values expected
    in `desired`.

    The aggregate tolerance is `atol + rtol * abs(desired)`.

    Parameters
    ----------
    actual : array_like
        Array obtained.
    desired : array_like
        Array desired.
    rtol : float, optional, default=None
        Relative tolerance.
        If None, it is set based on the provided arrays' dtypes.
    atol : float, optional, default=0.
        Absolute tolerance.
    equal_nan : bool, optional, default=True
        If True, NaNs will compare equal.
    err_msg : str, optional, default=''
        The error message to be printed in case of failure.
    verbose : bool, optional, default=True
        If True, the conflicting values are appended to the error message.

    Raises
    ------
    AssertionError
        If actual and desired are not equal up to specified precision.

    See Also
    --------
    numpy.testing.assert_allclose

    Examples
    --------
    >>> import numpy as np
    >>> from sklearn.utils._testing import assert_allclose
    >>> x = [1e-5, 1e-3, 1e-1]
    >>> y = np.arccos(np.cos(x))
    >>> assert_allclose(x, y, rtol=1e-5, atol=0)
    >>> a = np.full(shape=10, fill_value=1e-5, dtype=np.float32)
    >>> assert_allclose(a, 1e-5)
    """
    dtypes = []
    desired = np.asanyarray(desired)
    actual = np.asanyarray(actual)
    dtypes = [
        actual.dtype,
        desired.dtype]
# WARNING: Decompyle incomplete


def assert_allclose_dense_sparse(x, y, rtol, atol, err_msg = (1e-07, 1e-09, '')):
    """Assert allclose for sparse and dense data.

    Both x and y need to be either sparse or dense, they
    can't be mixed.

    Parameters
    ----------
    x : {array-like, sparse matrix}
        First array to compare.

    y : {array-like, sparse matrix}
        Second array to compare.

    rtol : float, default=1e-07
        relative tolerance; see numpy.allclose.

    atol : float, default=1e-9
        absolute tolerance; see numpy.allclose. Note that the default here is
        more tolerant than the default for numpy.testing.assert_allclose, where
        atol=0.

    err_msg : str, default=''
        Error message to raise.
    """
    if sp.sparse.issparse(x) and sp.sparse.issparse(y):
        x = x.tocsr()
        y = y.tocsr()
        x.sum_duplicates()
        y.sum_duplicates()
        assert_array_equal(x.indices, y.indices, err_msg = err_msg)
        assert_array_equal(x.indptr, y.indptr, err_msg = err_msg)
        assert_allclose(x.data, y.data, rtol = rtol, atol = atol, err_msg = err_msg)
        return None
    if not None.sparse.issparse(x) and sp.sparse.issparse(y):
        assert_allclose(x, y, rtol = rtol, atol = atol, err_msg = err_msg)
        return None
    raise None('Can only compare two sparse matrices, not a sparse matrix and an array.')


def set_random_state(estimator, random_state = (0,)):
    '''Set random state of an estimator if it has the `random_state` param.

    Parameters
    ----------
    estimator : object
        The estimator.
    random_state : int, RandomState instance or None, default=0
        Pseudo random number generator state.
        Pass an int for reproducible results across multiple function calls.
        See :term:`Glossary <random_state>`.
    '''
    if 'random_state' in estimator.get_params():
        estimator.set_params(random_state = random_state)
        return None


def _is_numpydoc():
    
    try:
        import numpydoc
        return True
    except (ImportError, AssertionError):
        return False



try:
    _check_array_api_dispatch(True)
    ARRAY_API_COMPAT_FUNCTIONAL = True
except (ImportError, RuntimeError):
    ARRAY_API_COMPAT_FUNCTIONAL = False


try:
    import pytest
    skip_if_32bit = pytest.mark.skipif(_IS_32BIT, reason = 'skipped on 32bit platforms')
    fails_if_unstable_openblas = pytest.mark.xfail(_in_unstable_openblas_configuration(), reason = 'OpenBLAS is unstable for this configuration')
    skip_if_no_parallel = pytest.mark.skipif(not (joblib.parallel.mp), reason = 'joblib is in serial mode')
    skip_if_array_api_compat_not_configured = pytest.mark.skipif(not ARRAY_API_COMPAT_FUNCTIONAL, reason = 'SCIPY_ARRAY_API not set, or versions of NumPy/SciPy too old.')
    if_safe_multiprocessing_with_blas = pytest.mark.skipif(sys.platform == 'darwin', reason = 'Possible multi-process bug with some BLAS')
    skip_if_no_numpydoc = pytest.mark.skipif(not _is_numpydoc(), reason = 'numpydoc is required to test the docstrings')
except ImportError:
    pass


def check_skip_network():
    if int(os.environ.get('SKLEARN_SKIP_NETWORK_TESTS', 0)):
        raise SkipTest('Text tutorial requires large dataset download')


def _delete_folder(folder_path, warn = (False,)):
    '''Utility function to cleanup a temporary folder if still existing.

    Copy from joblib.pool (for independence).
    '''
    
    try:
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)
            return None
        return None
    except OSError:
        if warn:
            warnings.warn('Could not delete temporary folder %s' % folder_path)
            return None
        return None



class TempMemmap:
    """
    Parameters
    ----------
    data
    mmap_mode : str, default='r'
    """
    
    def __init__(self, data, mmap_mode = ('r',)):
        self.mmap_mode = mmap_mode
        self.data = data

    
    def __enter__(self):
        (data_read_only, self.temp_folder) = create_memmap_backed_data(self.data, mmap_mode = self.mmap_mode, return_folder = True)
        return data_read_only

    
    def __exit__(self, exc_type, exc_val, exc_tb):
        _delete_folder(self.temp_folder)



def create_memmap_backed_data(data, mmap_mode, return_folder = ('r', False)):
    """
    Parameters
    ----------
    data
    mmap_mode : str, default='r'
    return_folder :  bool, default=False
    """
    temp_folder = tempfile.mkdtemp(prefix = 'sklearn_testing_')
    atexit.register(functools.partial(_delete_folder, temp_folder, warn = True))
    filename = op.join(temp_folder, 'data.pkl')
    joblib.dump(data, filename)
    memmap_backed_data = joblib.load(filename, mmap_mode = mmap_mode)
    result = memmap_backed_data if not return_folder else (memmap_backed_data, temp_folder)
    return result


def _get_args(function, varargs = (False,)):
    '''Helper to get function arguments.'''
    
    try:
        params = signature(function).parameters
    except ValueError:
        return 

    if varargs:
        
        def params.values()()(.0):
            pass
        # WARNING: Decompyle incomplete

        if len(varargs) == 0:
            varargs = None
        return (args, varargs)
    return params.items()()


def _get_func_name(func):
    '''Get function full name.

    Parameters
    ----------
    func : callable
        The function object.

    Returns
    -------
    name : str
        The function name.
    '''
    parts = []
    module = inspect.getmodule(func)
    if module:
        parts.append(module.__name__)
    qualname = func.__qualname__
    if qualname != func.__name__:
        None(parts.append[qualname:qualname.find('.')])
    parts.append(func.__name__)
    return '.'.join(parts)


def check_docstring_parameters(func, doc, ignore = (None, None)):
    '''Helper to check docstring.

    Parameters
    ----------
    func : callable
        The function object to test.
    doc : str, default=None
        Docstring if it is passed manually to the test.
    ignore : list, default=None
        Parameters to ignore.

    Returns
    -------
    incorrect : list
        A list of string describing the incorrect results.
    '''
    pass
# WARNING: Decompyle incomplete


def _check_item_included(item_name, args):
    '''Helper to check if item should be included in checking.'''
    if args.include is not True and item_name not in args.include:
        return False
# WARNING: Decompyle incomplete


def _diff_key(line):
    '''Key for grouping output from `context_diff`.'''
    if line.startswith('  '):
        return '  '
    if None.startswith('- '):
        return '- '
    if None.startswith('+ '):
        return '+ '
    if None.startswith('! '):
        return '! '


def _get_diff_msg(docstrings_grouped):
    '''Get message showing the difference between type/desc docstrings of all objects.

    `docstrings_grouped` keys should be the type/desc docstrings and values are a list
    of objects with that docstring. Objects with the same type/desc docstring are
    thus grouped together.
    '''
    msg_diff = ''
    ref_str = ''
    ref_group = []
# WARNING: Decompyle incomplete


def _check_consistency_items(items_docs, type_or_desc, section, n_objects, descr_regex_pattern, ignore_types = ('', tuple())):
    '''Helper to check docstring consistency of all `items_docs`.

    If item is not present in all objects, checking is skipped and warning raised.
    If `regex` provided, match descriptions to all descriptions.

    Parameters
    ----------
    items_doc : dict of dict of str
        Dictionary where the key is the string type or description, value is
        a dictionary where the key is "type description" or "description"
        and the value is a list of object names with the same string type or
        description.

    type_or_desc : {"type description", "description"}
        Whether to check type description or description between objects.

    section : {"Parameters", "Attributes", "Returns"}
        Name of the section type.

    n_objects : int
        Total number of objects.

    descr_regex_pattern : str, default=""
        Regex pattern to match for description of all objects.
        Ignored when `type_or_desc="type description".

    ignore_types : tuple of str, default=()
        Tuple of parameter/attribute/return names for which type description
        matching is ignored. Ignored when `type_or_desc="description".
    '''
    skipped = []
    for item_name, docstrings_grouped in items_docs.items():
        if (lambda .0: [ len(objs) for objs in .0 ])(docstrings_grouped.values()()) < n_objects:
            skipped.append(item_name)
            continue
        if type_or_desc == 'description' and descr_regex_pattern:
            not_matched = []
            for docstring, group in docstrings_grouped.items():
                if not re.search(descr_regex_pattern, docstring):
                    not_matched.extend(group)
                if not_matched:
                    msg = textwrap.fill(f'''The description of {section[:-1]} \'{item_name}\' in {not_matched} does not match \'descr_regex_pattern\': {descr_regex_pattern} ''')
                    raise AssertionError(msg)
                if type_or_desc == 'type specification' and item_name in ignore_types:
                    continue
        if len(docstrings_grouped.keys()) > 1:
            msg_diff = _get_diff_msg(docstrings_grouped)
            obj_groups = (lambda .0: pass# WARNING: Decompyle incomplete
)(docstrings_grouped.values()())
            msg = textwrap.fill(f'''The {type_or_desc} of {section[:-1]} \'{item_name}\' is inconsistent between {obj_groups}:''')
            msg += msg_diff
            raise AssertionError(msg)
        if skipped:
            warnings.warn(f'''Checking was skipped for {section}: {skipped} as they were not found in all objects.''')
            return None
        return sum


def assert_docstring_consistency(objects, include_params, exclude_params, include_attrs, exclude_attrs, include_returns, exclude_returns, descr_regex_pattern, ignore_types = (False, None, False, None, False, None, None, tuple())):
    '''Check consistency between docstring parameters/attributes/returns of objects.

    Checks if parameters/attributes/returns have the same type specification and
    description (ignoring whitespace) across `objects`. Intended to be used for
    related classes/functions/data descriptors.

    Entries that do not appear across all `objects` are ignored.

    Parameters
    ----------
    objects : list of {classes, functions, data descriptors}
        Objects to check.
        Objects may be classes, functions or data descriptors with docstrings that
        can be parsed by numpydoc.

    include_params : list of str or bool, default=False
        List of parameters to be included. If True, all parameters are included,
        if False, checking is skipped for parameters.
        Can only be set if `exclude_params` is None.

    exclude_params : list of str or None, default=None
        List of parameters to be excluded. If None, no parameters are excluded.
        Can only be set if `include_params` is True.

    include_attrs : list of str or bool, default=False
        List of attributes to be included. If True, all attributes are included,
        if False, checking is skipped for attributes.
        Can only be set if `exclude_attrs` is None.

    exclude_attrs : list of str or None, default=None
        List of attributes to be excluded. If None, no attributes are excluded.
        Can only be set if `include_attrs` is True.

    include_returns : list of str or bool, default=False
        List of returns to be included. If True, all returns are included,
        if False, checking is skipped for returns.
        Can only be set if `exclude_returns` is None.

    exclude_returns : list of str or None, default=None
        List of returns to be excluded. If None, no returns are excluded.
        Can only be set if `include_returns` is True.

    descr_regex_pattern : str, default=None
        Regular expression to match to all descriptions of included
        parameters/attributes/returns. If None, will revert to default behavior
        of comparing descriptions between objects.

    ignore_types : tuple of str, default=tuple()
        Tuple of parameter/attribute/return names to exclude from type description
        matching between objects.

    Examples
    --------
    >>> from sklearn.metrics import (accuracy_score, classification_report,
    ... mean_absolute_error, mean_squared_error, median_absolute_error)
    >>> from sklearn.utils._testing import assert_docstring_consistency
    ... # doctest: +SKIP
    >>> assert_docstring_consistency([mean_absolute_error, mean_squared_error],
    ... include_params=[\'y_true\', \'y_pred\', \'sample_weight\'])  # doctest: +SKIP
    >>> assert_docstring_consistency([median_absolute_error, mean_squared_error],
    ... include_params=True)  # doctest: +SKIP
    >>> assert_docstring_consistency([accuracy_score, classification_report],
    ... include_params=["y_true"],
    ... descr_regex_pattern=r"Ground truth \\(correct\\) (labels|target values)")
    ... # doctest: +SKIP
    '''
    pass
# WARNING: Decompyle incomplete


def assert_run_python_script_without_output(source_code, pattern, timeout = ('.+', 60)):
    '''Utility to check assertions in an independent Python subprocess.

    The script provided in the source code should return 0 and the stdtout +
    stderr should not match the pattern `pattern`.

    This is a port from cloudpickle https://github.com/cloudpipe/cloudpickle

    Parameters
    ----------
    source_code : str
        The Python source code to execute.
    pattern : str
        Pattern that the stdout + stderr should not match. By default, unless
        stdout + stderr are both empty, an error will be raised.
    timeout : int, default=60
        Time in seconds before timeout.
    '''
    (fd, source_file) = tempfile.mkstemp(suffix = '_src_test_sklearn.py')
    os.close(fd)
# WARNING: Decompyle incomplete


def _convert_container(container, constructor_name, columns_name, dtype, minversion, categorical_feature_names = (None, None, None, None)):
    '''Convert a given container to a specific array-like with a dtype.

    Parameters
    ----------
    container : array-like
        The container to convert.
    constructor_name : {"list", "tuple", "array", "sparse", "dataframe",             "pandas", "series", "index", "slice", "sparse_csr", "sparse_csc",             "sparse_csr_array", "sparse_csc_array", "pyarrow", "polars",             "polars_series"}
        The type of the returned container.
    columns_name : index or array-like, default=None
        For pandas/polars container supporting `columns_names`, it will affect
        specific names.
    dtype : dtype, default=None
        Force the dtype of the container. Does not apply to `"slice"`
        container.
    minversion : str, default=None
        Minimum version for package to install.
    categorical_feature_names : list of str, default=None
        List of column names to cast to categorical dtype.

    Returns
    -------
    converted_container
    '''
    pass
# WARNING: Decompyle incomplete


def raises(expected_exc_type, match, may_pass, err_msg = (None, False, None)):
    """Context manager to ensure exceptions are raised within a code block.

    This is similar to and inspired from pytest.raises, but supports a few
    other cases.

    This is only intended to be used in estimator_checks.py where we don't
    want to use pytest. In the rest of the code base, just use pytest.raises
    instead.

    Parameters
    ----------
    excepted_exc_type : Exception or list of Exception
        The exception that should be raised by the block. If a list, the block
        should raise one of the exceptions.
    match : str or list of str, default=None
        A regex that the exception message should match. If a list, one of
        the entries must match. If None, match isn't enforced.
    may_pass : bool, default=False
        If True, the block is allowed to not raise an exception. Useful in
        cases where some estimators may support a feature but others must
        fail with an appropriate error message. By default, the context
        manager will raise an exception if the block does not raise an
        exception.
    err_msg : str, default=None
        If the context manager fails (e.g. the block fails to raise the
        proper exception, or fails to match), then an AssertionError is
        raised with this message. By default, an AssertionError is raised
        with a default error message (depends on the kind of failure). Use
        this to indicate how users should fix their estimators to pass the
        checks.

    Attributes
    ----------
    raised_and_matched : bool
        True if an exception was raised and a match was found, False otherwise.
    """
    return _Raises(expected_exc_type, match, may_pass, err_msg)


class _Raises(contextlib.AbstractContextManager):
    
    def __init__(self, expected_exc_type, match, may_pass, err_msg):
        self.expected_exc_types = expected_exc_type if isinstance(expected_exc_type, Iterable) else [
            expected_exc_type]
        self.matches = [
            match] if isinstance(match, str) else match
        self.may_pass = may_pass
        self.err_msg = err_msg
        self.raised_and_matched = False

    
    def __exit__(self, exc_type, exc_value, _):
        pass
    # WARNING: Decompyle incomplete



class MinimalClassifier:
    '''Minimal classifier implementation without inheriting from BaseEstimator.

    This estimator should be tested with:

    * `check_estimator` in `test_estimator_checks.py`;
    * within a `Pipeline` in `test_pipeline.py`;
    * within a `SearchCV` in `test_search.py`.
    '''
    
    def __init__(self, param = (None,)):
        self.param = param

    
    def get_params(self, deep = (True,)):
        return {
            'param': self.param }

    
    def set_params(self, **params):
        for key, value in params.items():
            setattr(self, key, value)
            return self

    
    def fit(self, X, y):
        (X, y) = check_X_y(X, y)
        check_classification_targets(y)
        (self.classes_, counts) = np.unique(y, return_counts = True)
        self._most_frequent_class_idx = counts.argmax()
        return self

    
    def predict_proba(self, X):
        check_is_fitted(self)
        X = check_array(X)
        proba_shape = (X.shape[0], self.classes_.size)
        y_proba = np.zeros(shape = proba_shape, dtype = np.float64)
        y_proba[(:, self._most_frequent_class_idx)] = 1
        return y_proba

    
    def predict(self, X):
        y_proba = self.predict_proba(X)
        y_pred = y_proba.argmax(axis = 1)
        return self.classes_[y_pred]

    
    def score(self, X, y):
        accuracy_score = accuracy_score
        import sklearn.metrics
        return accuracy_score(y, self.predict(X))

    
    def __sklearn_tags__(self):
        return Tags(estimator_type = 'classifier', classifier_tags = ClassifierTags(), regressor_tags = None, transformer_tags = None, target_tags = TargetTags(required = True))



class MinimalRegressor:
    '''Minimal regressor implementation without inheriting from BaseEstimator.

    This estimator should be tested with:

    * `check_estimator` in `test_estimator_checks.py`;
    * within a `Pipeline` in `test_pipeline.py`;
    * within a `SearchCV` in `test_search.py`.
    '''
    
    def __init__(self, param = (None,)):
        self.param = param

    
    def get_params(self, deep = (True,)):
        return {
            'param': self.param }

    
    def set_params(self, **params):
        for key, value in params.items():
            setattr(self, key, value)
            return self

    
    def fit(self, X, y):
        (X, y) = check_X_y(X, y)
        self.is_fitted_ = True
        self._mean = np.mean(y)
        return self

    
    def predict(self, X):
        check_is_fitted(self)
        X = check_array(X)
        return np.ones(shape = (X.shape[0],)) * self._mean

    
    def score(self, X, y):
        r2_score = r2_score
        import sklearn.metrics
        return r2_score(y, self.predict(X))

    
    def __sklearn_tags__(self):
        return Tags(estimator_type = 'regressor', classifier_tags = None, regressor_tags = RegressorTags(), transformer_tags = None, target_tags = TargetTags(required = True))



class MinimalTransformer:
    '''Minimal transformer implementation without inheriting from
    BaseEstimator.

    This estimator should be tested with:

    * `check_estimator` in `test_estimator_checks.py`;
    * within a `Pipeline` in `test_pipeline.py`;
    * within a `SearchCV` in `test_search.py`.
    '''
    
    def __init__(self, param = (None,)):
        self.param = param

    
    def get_params(self, deep = (True,)):
        return {
            'param': self.param }

    
    def set_params(self, **params):
        for key, value in params.items():
            setattr(self, key, value)
            return self

    
    def fit(self, X, y = (None,)):
        check_array(X)
        self.is_fitted_ = True
        return self

    
    def transform(self, X, y = (None,)):
        check_is_fitted(self)
        X = check_array(X)
        return X

    
    def fit_transform(self, X, y = (None,)):
        return self.fit(X, y).transform(X, y)

    
    def __sklearn_tags__(self):
        return Tags(estimator_type = 'transformer', classifier_tags = None, regressor_tags = None, transformer_tags = TransformerTags(), target_tags = TargetTags(required = False))



def _array_api_for_tests(array_namespace, device):
    
    try:
        array_mod = importlib.import_module(array_namespace)
    except (ModuleNotFoundError, ImportError):
        raise SkipTest(f'''{array_namespace} is not installed: not checking array_api input''')

# WARNING: Decompyle incomplete


def _get_warnings_filters_info_list():
    WarningInfo = <NODE:12>()
    return [
        WarningInfo('error', category = DeprecationWarning),
        WarningInfo('error', category = FutureWarning),
        WarningInfo('error', category = VisibleDeprecationWarning),
        WarningInfo('ignore', message = 'pkg_resources is deprecated as an API', category = DeprecationWarning),
        WarningInfo('ignore', message = 'Deprecated call to `pkg_resources', category = DeprecationWarning),
        WarningInfo('ignore', message = 'The --rsyncdir command line argument and rsyncdirs config variable are deprecated', category = DeprecationWarning),
        WarningInfo('ignore', message = '\\s*Pyarrow will become a required dependency', category = DeprecationWarning),
        WarningInfo('ignore', message = 'datetime.datetime.utcfromtimestamp', category = DeprecationWarning),
        WarningInfo('ignore', message = 'ast.Num is deprecated', category = DeprecationWarning),
        WarningInfo('ignore', message = 'Attribute n is deprecated', category = DeprecationWarning),
        WarningInfo('ignore', message = 'ast.Str is deprecated', category = DeprecationWarning),
        WarningInfo('ignore', message = 'Attribute s is deprecated', category = DeprecationWarning),
        WarningInfo('ignore', message = '.+scattermapbox.+deprecated.+scattermap.+instead', category = DeprecationWarning),
        WarningInfo('ignore', message = 'Class PassiveAggressive.+is deprecated', category = FutureWarning)]


def get_pytest_filterwarning_lines():
    warning_filters_info_list = _get_warnings_filters_info_list()
    return warning_filters_info_list()


def turn_warnings_into_errors():
    warnings_filters_info_list = _get_warnings_filters_info_list()
    for warning_info in warnings_filters_info_list:
        warnings.filterwarnings(warning_info.action, message = warning_info.message, category = warning_info.category)
        return None

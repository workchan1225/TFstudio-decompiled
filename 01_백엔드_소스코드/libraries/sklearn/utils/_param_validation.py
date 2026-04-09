# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _param_validation.pyc (Python 3.11)

import functools
import math
import operator
import re
from abc import ABC, abstractmethod
from collections.abc import Iterable
from inspect import signature
from numbers import Integral, Real
import numpy as np
from scipy.sparse import csr_matrix, issparse
from sklearn._config import config_context, get_config
from sklearn.utils.validation import _is_arraylike_not_scalar

class InvalidParameterError(TypeError, ValueError):
    '''Custom exception to be raised when the parameter of a class/method/function
    does not have a valid type or value.
    '''
    pass


def validate_parameter_constraints(parameter_constraints, params, caller_name):
    '''Validate types and values of given parameters.

    Parameters
    ----------
    parameter_constraints : dict or {"no_validation"}
        If "no_validation", validation is skipped for this parameter.

        If a dict, it must be a dictionary `param_name: list of constraints`.
        A parameter is valid if it satisfies one of the constraints from the list.
        Constraints can be:
        - an Interval object, representing a continuous or discrete range of numbers
        - the string "array-like"
        - the string "sparse matrix"
        - the string "random_state"
        - callable
        - None, meaning that None is a valid value for the parameter
        - any type, meaning that any instance of this type is valid
        - an Options object, representing a set of elements of a given type
        - a StrOptions object, representing a set of strings
        - the string "boolean"
        - the string "verbose"
        - the string "cv_object"
        - the string "nan"
        - a MissingValues object representing markers for missing values
        - a HasMethods object, representing method(s) an object must have
        - a Hidden object, representing a constraint not meant to be exposed to the user

    params : dict
        A dictionary `param_name: param_value`. The parameters to validate against the
        constraints.

    caller_name : str
        The name of the estimator or function or method that called this function.
    '''
    for param_name, param_val in params.items():
        if param_name not in parameter_constraints:
            continue
        constraints = parameter_constraints[param_name]
        if constraints == 'no_validation':
            continue
        constraints = constraints()
        for constraint in constraints:
            if constraint.is_satisfied_by(param_val):
                (lambda .0: [ make_constraint(constraint) for constraint in .0 ])
            
            constraints = constraints()
        raise InvalidParameterError(f'''The {param_name!r} parameter of {caller_name} must be {constraints_str}. Got {param_val!r} instead.''')
        return None


def make_constraint(constraint):
    '''Convert the constraint into the appropriate Constraint object.

    Parameters
    ----------
    constraint : object
        The constraint to convert.

    Returns
    -------
    constraint : instance of _Constraint
        The converted constraint.
    '''
    if isinstance(constraint, str) and constraint == 'array-like':
        return _ArrayLikes()
    if None(constraint, str) and constraint == 'sparse matrix':
        return _SparseMatrices()
    if None(constraint, str) and constraint == 'random_state':
        return _RandomStates()
    if None is callable:
        return _Callables()
# WARNING: Decompyle incomplete


def validate_params(parameter_constraints, *, prefer_skip_nested_validation):
    """Decorator to validate types and values of functions and methods.

    Parameters
    ----------
    parameter_constraints : dict
        A dictionary `param_name: list of constraints`. See the docstring of
        `validate_parameter_constraints` for a description of the accepted constraints.

        Note that the *args and **kwargs parameters are not validated and must not be
        present in the parameter_constraints dictionary.

    prefer_skip_nested_validation : bool
        If True, the validation of parameters of inner estimators or functions
        called by the decorated function will be skipped.

        This is useful to avoid validating many times the parameters passed by the
        user from the public facing API. It's also useful to avoid validating
        parameters that we pass internally to inner functions that are guaranteed to
        be valid by the test suite.

        It should be set to True for most functions, except for those that receive
        non-validated objects as parameters or that are just wrappers around classes
        because they only perform a partial validation.

    Returns
    -------
    decorated_function : function or method
        The decorated function.
    """
    pass
# WARNING: Decompyle incomplete


class RealNotInt(Real):
    '''A type that represents reals that are not instances of int.

    Behaves like float, but also works with values extracted from numpy arrays.
    isintance(1, RealNotInt) -> False
    isinstance(1.0, RealNotInt) -> True
    '''
    pass

RealNotInt.register(float)

def _type_name(t):
    '''Convert type into human readable string.'''
    module = t.__module__
    qualname = t.__qualname__
    if module == 'builtins':
        return qualname
    if None == Real:
        return 'float'
    if None == Integral:
        return 'int'
    return f'''{None}.{qualname}'''


class _Constraint(ABC):
    '''Base class for the constraint objects.'''
    
    def __init__(self):
        self.hidden = False

    is_satisfied_by = (lambda self, val: pass)()
    __str__ = (lambda self: pass)()


class _InstancesOf(_Constraint):
    pass
# WARNING: Decompyle incomplete


class _NoneConstraint(_Constraint):
    '''Constraint representing the None singleton.'''
    
    def is_satisfied_by(self, val):
        return val is None

    
    def __str__(self):
        return 'None'



class _NanConstraint(_Constraint):
    '''Constraint representing the indicator `np.nan`.'''
    
    def is_satisfied_by(self, val):

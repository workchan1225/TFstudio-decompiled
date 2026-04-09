# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: class_validators.pyc (Python 3.11)

import warnings
from collections import ChainMap
from functools import partial, partialmethod, wraps
from itertools import chain
from types import FunctionType
from typing import TYPE_CHECKING, Any, Callable, Dict, Iterable, List, Optional, Set, Tuple, Type, Union, overload
from pydantic.v1.errors import ConfigError
from pydantic.v1.typing import AnyCallable
from pydantic.v1.utils import ROOT_KEY, in_ipython
if TYPE_CHECKING:
    from pydantic.v1.typing import AnyClassMethod

class Validator:
    __slots__ = ('func', 'pre', 'each_item', 'always', 'check_fields', 'skip_on_failure')
    
    def __init__(self, func, pre = None, each_item = None, always = None, check_fields = (False, False, False, False, False), skip_on_failure = ('func', AnyCallable, 'pre', bool, 'each_item', bool, 'always', bool, 'check_fields', bool, 'skip_on_failure', bool)):
        self.func = func
        self.pre = pre
        self.each_item = each_item
        self.always = always
        self.check_fields = check_fields
        self.skip_on_failure = skip_on_failure


if TYPE_CHECKING:
    from inspect import Signature
    from pydantic.v1.config import BaseConfig
    from pydantic.v1.fields import ModelField
    from pydantic.v1.types import ModelOrDc
    ValidatorCallable = Callable[([
        Optional[ModelOrDc],
        Any,
        Dict[(str, Any)],
        ModelField,
        Type[BaseConfig]], Any)]
    ValidatorsList = List[ValidatorCallable]
    ValidatorListDict = Dict[(str, List[Validator])]
_FUNCS: Set[str] = set()
VALIDATOR_CONFIG_KEY = '__validator_config__'
ROOT_VALIDATOR_CONFIG_KEY = '__root_validator_config__'

def validator(*, pre, each_item, always, check_fields, whole, allow_reuse, *fields):
    '''
    Decorate methods on the class indicating that they should be used to validate fields
    :param fields: which field(s) the method should be called on
    :param pre: whether or not this validator should be called before the standard validators (else after)
    :param each_item: for complex objects (sets, lists etc.) whether to validate individual elements rather than the
      whole object
    :param always: whether this method and other validators should be called even if the value is missing
    :param check_fields: whether to check that the fields actually exist on the model
    :param allow_reuse: whether to track and raise an error if another validator refers to the decorated function
    '''
    pass
# WARNING: Decompyle incomplete

root_validator = (lambda _func = None: pass)()
root_validator = (lambda *: pass)()

def root_validator(_func = None, *, pre, allow_reuse, skip_on_failure):
    '''
    Decorate methods on a model indicating that they should be used to validate (and perhaps modify) data either
    before or after standard model parsing/validation is performed.
    '''
    pass
# WARNING: Decompyle incomplete


def _prepare_validator(function = None, allow_reuse = None):
    """
    Avoid validators with duplicated names since without this, validators can be overwritten silently
    which generally isn't the intended behaviour, don't run in ipython (see #312) or if allow_reuse is False.
    """
    f_cls = function if isinstance(function, classmethod) else classmethod(function)
    if not in_ipython() and allow_reuse:
        ref = getattr(f_cls.__func__, '__module__', '<No __module__>') + '.' + getattr(f_cls.__func__, '__qualname__', f'''<No __qualname__: id:{id(f_cls.__func__)}>''')
        if ref in _FUNCS:
            raise ConfigError(f'''duplicate validator function "{ref}"; if this is intended, set `allow_reuse=True`''')
        _FUNCS.add(ref)
    return f_cls


class ValidatorGroup:
    
    def __init__(self = None, validators = None):
        self.validators = validators
        self.used_validators = {
            '*'}

    
    def get_validators(self = None, name = None):
        self.used_validators.add(name)
        validators = self.validators.get(name, [])
        if name != ROOT_KEY:
            validators += self.validators.get('*', [])
        if validators:
            return validators()

    
    def check_for_unused(self = None):
        pass
    # WARNING: Decompyle incomplete



def extract_validators(namespace = None):
    validators = { }
    for var_name, value in namespace.items():
        validator_config = getattr(value, VALIDATOR_CONFIG_KEY, None)
        if validator_config:
            (fields, v) = validator_config
            for field in fields:
                if field in validators:
                    validators[field].append(v)
                    continue
                validators[field] = [
                    v]
                return validators


def extract_root_validators(namespace = None):
    signature = signature
    import inspect
    pre_validators = []
    post_validators = []
    for name, value in namespace.items():
        validator_config = getattr(value, ROOT_VALIDATOR_CONFIG_KEY, None)
        if validator_config:
            sig = signature(validator_config.func)
            args = list(sig.parameters.keys())
            if args[0] == 'self':
                raise ConfigError(f'''Invalid signature for root validator {name}: {sig}, "self" not permitted as first argument, should be: (cls, values).''')
            if len(args) != 2:
                raise ConfigError(f'''Invalid signature for root validator {name}: {sig}, should be: (cls, values).''')
            if validator_config.pre:
                pre_validators.append(validator_config.func)
                continue
            post_validators.append((validator_config.skip_on_failure, validator_config.func))
        return (pre_validators, post_validators)


def inherit_validators(base_validators = None, validators = None):
    for field, field_validators in base_validators.items():
        if field not in validators:
            validators[field] = []
        return validators


def make_generic_validator(validator = None):
    '''
    Make a generic function which calls a validator with the right arguments.

    Unfortunately other approaches (eg. return a partial of a function that builds the arguments) is slow,
    hence this laborious way of doing things.

    It\'s done like this so validators don\'t all need **kwargs in their signature, eg. any combination of
    the arguments "values", "fields" and/or "config" are permitted.
    '''
    pass
# WARNING: Decompyle incomplete


def prep_validators(v_funcs = None):
    return v_funcs()

all_kwargs = {
    'field',
    'config',
    'values'}

def _generic_validator_cls(validator = None, sig = None, args = None):
    pass
# WARNING: Decompyle incomplete


def _generic_validator_basic(validator = None, sig = None, args = None):
    pass
# WARNING: Decompyle incomplete


def gather_all_validators(type_ = None):
    pass
# WARNING: Decompyle incomplete

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: dataclasses.pyc (Python 3.11)

"""
The main purpose is to enhance stdlib dataclasses by adding validation
A pydantic dataclass can be generated from scratch or from a stdlib one.

Behind the scene, a pydantic dataclass is just like a regular one on which we attach
a `BaseModel` and magic methods to trigger the validation of the data.
`__init__` and `__post_init__` are hence overridden and have extra logic to be
able to validate input data.

When a pydantic dataclass is generated from scratch, it's just a plain dataclass
with validation triggered at initialization

The tricky part if for stdlib dataclasses that are converted after into pydantic ones e.g.

```py
@dataclasses.dataclass
class M:
    x: int

ValidatedM = pydantic.dataclasses.dataclass(M)
```

We indeed still want to support equality, hashing, repr, ... as if it was the stdlib one!

```py
assert isinstance(ValidatedM(x=1), M)
assert ValidatedM(x=1) == M(x=1)
```

This means we **don't want to create a new dataclass that inherits from it**
The trick is to create a wrapper around `M` that will act as a proxy to trigger
validation without altering default `M` behaviour.
"""
import copy
import dataclasses
import sys
from contextlib import contextmanager
from functools import wraps

try:
    from functools import cached_property
except ImportError:
    pass

from typing import TYPE_CHECKING, Any, Callable, ClassVar, Dict, Generator, Optional, Type, TypeVar, Union, overload
from typing_extensions import dataclass_transform
from pydantic.v1.class_validators import gather_all_validators
from pydantic.v1.config import BaseConfig, ConfigDict, Extra, get_config
from pydantic.v1.error_wrappers import ValidationError
from pydantic.v1.errors import DataclassTypeError
from pydantic.v1.fields import Field, FieldInfo, Required, Undefined
from pydantic.v1.main import create_model, validate_model
from pydantic.v1.utils import ClassAttribute
if TYPE_CHECKING:
    from pydantic.v1.main import BaseModel
    from pydantic.v1.typing import CallableGenerator, NoArgAnyCallable
    DataclassT = TypeVar('DataclassT', bound = 'Dataclass')
    DataclassClassOrWrapper = Union[(Type['Dataclass'], 'DataclassProxy')]
    
    class Dataclass:
        __pydantic_has_field_info_default__: ClassVar[bool] = 'Dataclass'
        
        def __init__(self = None, *args, **kwargs):
            pass

        __get_validators__ = (lambda cls = None: pass)()
        __validate__ = (lambda cls = None, v = None: pass)()

__all__ = [
    'dataclass',
    'set_validation',
    'create_pydantic_model_from_dataclass',
    'is_builtin_dataclass',
    'make_dataclass_validator']
_T = TypeVar('_T')
if sys.version_info >= (3, 10):
    dataclass = (lambda *: pass)()()
    dataclass = (lambda _cls = None, *, init: pass)()()
else:
    dataclass = (lambda *: pass)()()
    dataclass = (lambda _cls = None, *, init: pass)()()
dataclass = (lambda _cls = None, *, init: pass# WARNING: Decompyle incomplete
)()
set_validation = (lambda cls = None, value = None: pass# WARNING: Decompyle incomplete
)()

class DataclassProxy:
    __slots__ = '__dataclass__'
    
    def __init__(self = None, dc_cls = None):
        object.__setattr__(self, '__dataclass__', dc_cls)

    
    def __call__(self = None, *args, **kwargs):
        set_validation(self.__dataclass__, True)
    # WARNING: Decompyle incomplete

    
    def __getattr__(self = None, name = None):
        return getattr(self.__dataclass__, name)

    
    def __setattr__(self = None, _DataclassProxy__name = None, _DataclassProxy__value = None):
        return setattr(self.__dataclass__, _DataclassProxy__name, _DataclassProxy__value)

    
    def __instancecheck__(self = None, instance = None):
        return isinstance(instance, self.__dataclass__)

    
    def __copy__(self = None):
        return DataclassProxy(copy.copy(self.__dataclass__))

    
    def __deepcopy__(self = None, memo = None):
        return DataclassProxy(copy.deepcopy(self.__dataclass__, memo))



def _add_pydantic_validation_attributes(dc_cls = None, config = None, validate_on_init = None, dc_cls_doc = ('dc_cls', Type['Dataclass'], 'config', Type[BaseConfig], 'validate_on_init', bool, 'dc_cls_doc', str, 'return', None)):
    """
    We need to replace the right method. If no `__post_init__` has been set in the stdlib dataclass
    it won't even exist (code is generated on the fly by `dataclasses`)
    By default, we run validation after `__init__` or `__post_init__` if defined
    """
    pass
# WARNING: Decompyle incomplete


def _get_validators(cls = None):
    pass
# WARNING: Decompyle incomplete


def _validate_dataclass(cls = None, v = None):
    set_validation(cls, True)
    if isinstance(v, cls):
        v.__pydantic_validate_values__()
        None(None, None)
        return 
# WARNING: Decompyle incomplete


def create_pydantic_model_from_dataclass(dc_cls = None, config = None, dc_cls_doc = None):
    field_definitions = { }
# WARNING: Decompyle incomplete

if sys.version_info >= (3, 8):
    
    def _is_field_cached_property(obj = None, k = None):
        return isinstance(getattr(type(obj), k, None), cached_property)

else:
    
    def _is_field_cached_property(obj = None, k = None):
        return False


def _dataclass_validate_values(self = None):
    pass
# WARNING: Decompyle incomplete


def _dataclass_validate_assignment_setattr(self = None, name = None, value = None):
    if self.__pydantic_initialised__:
        d = dict(self.__dict__)
        d.pop(name, None)
        known_field = self.__pydantic_model__.__fields__.get(name, None)
        if known_field:
            (value, error_) = known_field.validate(value, d, loc = name, cls = self.__class__)
            if error_:
                raise ValidationError([
                    error_], self.__class__)
    object.__setattr__(self, name, value)


def is_builtin_dataclass(_cls = None):
    """
    Whether a class is a stdlib dataclass
    (useful to discriminated a pydantic dataclass that is actually a wrapper around a stdlib dataclass)

    we check that
    - `_cls` is a dataclass
    - `_cls` is not a processed pydantic dataclass (with a basemodel attached)
    - `_cls` is not a pydantic dataclass inheriting directly from a stdlib dataclass
    e.g.
    ```
    @dataclasses.dataclass
    class A:
        x: int

    @pydantic.dataclasses.dataclass
    class B(A):
        y: int
    ```
    In this case, when we first check `B`, we make an extra check and look at the annotations ('y'),
    which won't be a superset of all the dataclass fields (only the stdlib fields i.e. 'x')
    """
    if dataclasses.is_dataclass(_cls):
        if not hasattr(_cls, '__pydantic_model__'):
            pass
    return set(_cls.__dataclass_fields__).issuperset(set(getattr(_cls, '__annotations__', { })))


def make_dataclass_validator(dc_cls = None, config = None):
    '''
    Create a pydantic.dataclass from a builtin dataclass to add type validation
    and yield the validators
    It retrieves the parameters of the dataclass and forwards them to the newly created dataclass
    '''
    pass
# WARNING: Decompyle incomplete

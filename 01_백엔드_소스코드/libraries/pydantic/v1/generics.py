# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: generics.pyc (Python 3.11)

import sys
import types
import typing
from typing import TYPE_CHECKING, Any, ClassVar, Dict, ForwardRef, Generic, Iterator, List, Mapping, Optional, Tuple, Type, TypeVar, Union, cast
from weakref import WeakKeyDictionary, WeakValueDictionary
from typing_extensions import Annotated, Literal as ExtLiteral
from pydantic.v1.class_validators import gather_all_validators
from pydantic.v1.fields import DeferredType
from pydantic.v1.main import BaseModel, create_model
from pydantic.v1.types import JsonWrapper
from pydantic.v1.typing import display_as_type, get_all_type_hints, get_args, get_origin, typing_base
from pydantic.v1.utils import all_identical, lenient_issubclass
if sys.version_info >= (3, 10):
    from typing import _UnionGenericAlias
if sys.version_info >= (3, 8):
    from typing import Literal
GenericModelT = TypeVar('GenericModelT', bound = 'GenericModel')
TypeVarType = Any
CacheKey = Tuple[(Type[Any], Any, Tuple[(Any, ...)])]
Parametrization = Mapping[(TypeVarType, Type[Any])]
if sys.version_info >= (3, 9):
    GenericTypesCache = WeakValueDictionary[(CacheKey, Type[BaseModel])]
    AssignedParameters = WeakKeyDictionary[(Type[BaseModel], Parametrization)]
else:
    GenericTypesCache = WeakValueDictionary
    AssignedParameters = WeakKeyDictionary
_generic_types_cache = GenericTypesCache()
_assigned_parameters = AssignedParameters()

class GenericModel(BaseModel):
    __slots__ = ()
    __concrete__: ClassVar[bool] = False
    if TYPE_CHECKING:
        __parameters__: ClassVar[Tuple[(TypeVarType, ...)]]
    
    def __class_getitem__(cls = None, params = None):
        '''Instantiates a new class from a generic class `cls` and type variables `params`.

        :param params: Tuple of types the class . Given a generic class
            `Model` with 2 type variables and a concrete model `Model[str, int]`,
            the value `(str, int)` would be passed to `params`.
        :return: New model class inheriting from `cls` with instantiated
            types described by `params`. If no parameters are given, `cls` is
            returned as is.

        '''
        pass
    # WARNING: Decompyle incomplete

    __concrete_name__ = (lambda cls = None, params = None: param_names = params()params_component = ', '.join(param_names)f'''{cls.__name__}[{params_component}]''')()
    __parameterized_bases__ = (lambda cls = None, typevars_map = None: pass# WARNING: Decompyle incomplete
)()


def replace_types(type_ = None, type_map = None):
    '''Return type with all occurrences of `type_map` keys recursively replaced with their values.

    :param type_: Any type, class or generic alias
    :param type_map: Mapping from `TypeVar` instance to concrete types.
    :return: New type representing the basic structure of `type_` with all
        `typevar_map` keys recursively replaced.

    >>> replace_types(Tuple[str, Union[List[str], float]], {str: int})
    Tuple[int, Union[List[int], float]]

    '''
    pass
# WARNING: Decompyle incomplete


def check_parameters_count(cls = None, parameters = None):
    actual = len(parameters)
    expected = len(cls.__parameters__)
    if actual != expected:
        description = 'many' if actual > expected else 'few'
        raise TypeError(f'''Too {description} parameters for {cls.__name__}; actual {actual}, expected {expected}''')

DictValues: Type[Any] = { }.values().__class__

def iter_contained_typevars(v = None):
    '''Recursively iterate through all subtypes and type args of `v` and yield any typevars that are found.'''
    pass
# WARNING: Decompyle incomplete


def get_caller_frame_info():
    '''
    Used inside a function to check whether it was called globally

    Will only work against non-compiled code, therefore used only in pydantic.generics

    :returns Tuple[module_name, called_globally]
    '''
    
    try:
        previous_caller_frame = sys._getframe(2)
    except ValueError:
        e = None
        raise RuntimeError('This function must be used inside another function'), e
        e = None
        del e
        except AttributeError:
            return (None, False)

    frame_globals = previous_caller_frame.f_globals
    return (frame_globals.get('__name__'), previous_caller_frame.f_locals is frame_globals)


def _prepare_model_fields(created_model = None, fields = None, instance_type_hints = None, typevars_map = ('created_model', Type[GenericModel], 'fields', Mapping[(str, Any)], 'instance_type_hints', Mapping[(str, type)], 'typevars_map', Mapping[(Any, type)], 'return', None)):
    '''
    Replace DeferredType fields with concrete type hints and prepare them.
    '''
    pass
# WARNING: Decompyle incomplete

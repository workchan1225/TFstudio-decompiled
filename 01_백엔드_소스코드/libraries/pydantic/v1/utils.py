# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: utils.pyc (Python 3.11)

import keyword
import warnings
import weakref
from collections import OrderedDict, defaultdict, deque
from copy import deepcopy
from itertools import islice, zip_longest
from types import BuiltinFunctionType, CodeType, FunctionType, GeneratorType, LambdaType, ModuleType
from typing import TYPE_CHECKING, AbstractSet, Any, Callable, Collection, Dict, Generator, Iterable, Iterator, List, Mapping, NoReturn, Optional, Set, Tuple, Type, TypeVar, Union
from typing_extensions import Annotated
from pydantic.v1.errors import ConfigError
from pydantic.v1.typing import NoneType, WithArgsTypes, all_literal_values, display_as_type, get_args, get_origin, is_literal_type, is_union
from pydantic.v1.version import version_info
if TYPE_CHECKING:
    from inspect import Signature
    from pathlib import Path
    from pydantic.v1.config import BaseConfig
    from pydantic.v1.dataclasses import Dataclass
    from pydantic.v1.fields import ModelField
    from pydantic.v1.main import BaseModel
    from pydantic.v1.typing import AbstractSetIntStr, DictIntStrAny, IntStr, MappingIntStrAny, ReprArgs
    RichReprResult = Iterable[Union[(Any, Tuple[Any], Tuple[(str, Any)], Tuple[(str, Any, Any)])]]
__all__ = ('import_string', 'sequence_like', 'validate_field_name', 'lenient_isinstance', 'lenient_issubclass', 'in_ipython', 'is_valid_identifier', 'deep_update', 'update_not_none', 'almost_equal_floats', 'get_model', 'to_camel', 'to_lower_camel', 'is_valid_field', 'smart_deepcopy', 'PyObjectStr', 'Representation', 'GetterDict', 'ValueItems', 'version_info', 'ClassAttribute', 'path_type', 'ROOT_KEY', 'get_unique_discriminator_alias', 'get_discriminator_alias_and_values', 'DUNDER_ATTRIBUTES')
ROOT_KEY = '__root__'
IMMUTABLE_NON_COLLECTIONS_TYPES: Set[Type[Any]] = {
    int,
    float,
    complex,
    str,
    bool,
    bytes,
    type,
    NoneType,
    FunctionType,
    BuiltinFunctionType,
    LambdaType,
    weakref.ref,
    CodeType,
    ModuleType,
    NotImplemented.__class__,
    Ellipsis.__class__}
BUILTIN_COLLECTIONS: Set[Type[Any]] = {
    list,
    set,
    tuple,
    frozenset,
    dict,
    OrderedDict,
    defaultdict,
    deque}

def import_string(dotted_path = None):
    '''
    Stolen approximately from django. Import a dotted module path and return the attribute/class designated by the
    last name in the path. Raise ImportError if the import fails.
    '''
    import_module = import_module
    import importlib
    
    try:
        (module_path, class_name) = dotted_path.strip(' ').rsplit('.', 1)
    except ValueError:
        e = None
        raise ImportError(f'''"{dotted_path}" doesn\'t look like a module path'''), e
        e = None
        del e

    module = import_module(module_path)
    
    try:
        return getattr(module, class_name)
    except AttributeError:
        e = None
        raise ImportError(f'''Module "{module_path}" does not define a "{class_name}" attribute'''), e
        e = None
        del e



def truncate(v = None, *, max_len):
    '''
    Truncate a value and add a unicode ellipsis (three dots) to the end if it was too long
    '''
    warnings.warn('`truncate` is no-longer used by pydantic and is deprecated', DeprecationWarning)
    if isinstance(v, str) and len(v) > max_len - 2:
        return (v[:max_len - 3] + '…').__repr__()
    
    try:
        v = v.__repr__()
    except TypeError:
        v = v.__class__.__repr__(v)

    if len(v) > max_len:
        v = v[:max_len - 1] + '…'
    return v


def sequence_like(v = None):
    return isinstance(v, (list, tuple, set, frozenset, GeneratorType, deque))


def validate_field_name(bases = None, field_name = None):
    """
    Ensure that the field's name does not shadow an existing attribute of the model.
    """
    for base in bases:
        if getattr(base, field_name, None):
            raise NameError(f'''Field name "{field_name}" shadows a BaseModel attribute; use a different field name with "alias=\'{field_name}\'".''')
        return None


def lenient_isinstance(o = None, class_or_tuple = None):
    
    try:
        return isinstance(o, class_or_tuple)
    except TypeError:
        return False



def lenient_issubclass(cls = None, class_or_tuple = None):
    
    try:
        if isinstance(cls, type):
            return issubclass(cls, class_or_tuple)
        except TypeError:
            if isinstance(cls, WithArgsTypes):
                return False



def in_ipython():
    """
    Check whether we're in an ipython environment, including jupyter notebooks.
    """
    
    try:
        eval('__IPYTHON__')
        return True
    except NameError:
        return False



def is_valid_identifier(identifier = None):

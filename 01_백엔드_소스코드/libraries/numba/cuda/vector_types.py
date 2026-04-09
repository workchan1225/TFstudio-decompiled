# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: vector_types.pyc (Python 3.11)

from typing import List, Tuple, Dict
from numba import types
from numba.core import cgutils
from numba.core.extending import make_attribute_wrapper, models, register_model
from numba.core.imputils import Registry as ImplRegistry
from numba.core.typing.templates import ConcreteTemplate
from numba.core.typing.templates import Registry as TypingRegistry
from numba.core.typing.templates import signature
from numba.cuda import stubs
from numba.cuda.errors import CudaLoweringError
typing_registry = TypingRegistry()
impl_registry = ImplRegistry()
register = typing_registry.register
register_attr = typing_registry.register_attr
register_global = typing_registry.register_global
lower = impl_registry.lower

class VectorType(types.Type):
    pass
# WARNING: Decompyle incomplete


def make_vector_type(name = None, base_type = None, attr_names = None, user_facing_object = ('name', str, 'base_type', types.Type, 'attr_names', Tuple[(str, ...)], 'return', types.Type)):
    '''Create a vector type.

    Parameters
    ----------
    name: str
        The name of the type.
    base_type: numba.types.Type
        The primitive type for each element in the vector.
    attr_names: tuple of str
        Name for each attribute.
    user_facing_object: object
        The handle to be used in cuda kernel.
    '''
    pass
# WARNING: Decompyle incomplete


def enable_vector_type_ctor(vector_type = None, overloads = None):
    '''Create typing and lowering for vector type constructor.

    Parameters
    ----------
    vector_type: VectorType
        The type whose constructor to type and lower.
    overloads: List of argument types
        A list containing different overloads of the constructor. Each base type
        in the argument list should either be primitive type or VectorType.
    '''
    pass
# WARNING: Decompyle incomplete

vector_types: Dict[(str, VectorType)] = { }

def build_constructor_overloads(base_type, vty_name, num_elements, arglists, l):
    '''
    For a given vector type, build a list of overloads for its constructor.
    '''
    if num_elements == 0:
        arglists.append(l[:])
    for i in range(1, num_elements + 1):
        if i == 1:
            l.append(base_type)
            build_constructor_overloads(base_type, vty_name, num_elements - i, arglists, l)
            l.pop(-1)
            l.append(vector_types[f'''{vty_name[:-1]}1'''])
            build_constructor_overloads(base_type, vty_name, num_elements - i, arglists, l)
            l.pop(-1)
            continue
        l.append(vector_types[f'''{vty_name[:-1]}{i}'''])
        build_constructor_overloads(base_type, vty_name, num_elements - i, arglists, l)
        l.pop(-1)
        return None


def _initialize():
    '''
    Construct the vector types, populate `vector_types` dictionary, and
    enable the constructors.
    '''
    vector_type_attribute_names = ('x', 'y', 'z', 'w')
    for stub in stubs._vector_type_stubs:
        type_name = stub.__name__
        base_type = getattr(types, type_name[:-2])
        num_elements = int(type_name[-1])
        attributes = vector_type_attribute_names[:num_elements]
        vector_type = make_vector_type(type_name, base_type, attributes, stub)
        vector_types[type_name] = vector_type
        for vty in vector_types.values():
            l = []
            arglists = []
            build_constructor_overloads(vty.base_type, vty.name, vty.num_elements, arglists, l)
            enable_vector_type_ctor(vty, arglists)
            return None

_initialize()

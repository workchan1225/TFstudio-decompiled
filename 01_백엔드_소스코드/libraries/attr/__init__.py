# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''
Classes Without Boilerplate
'''
from functools import partial
from typing import Callable, Literal, Protocol
from  import converters, exceptions, filters, setters, validators
from _cmp import cmp_using
from _config import get_run_validators, set_run_validators
from _funcs import asdict, assoc, astuple, has, resolve_types
from _make import NOTHING, Attribute, Converter, Factory, _Nothing, attrib, attrs, evolve, fields, fields_dict, make_class, validate
from _next_gen import define, field, frozen, mutable
from _version_info import VersionInfo
s = attrs
attributes = attrs
ib = attrib
attr = attrib
dataclass = partial(attrs, auto_attribs = True)

class AttrsInstance(Protocol):
    pass

NothingType = Literal[_Nothing.NOTHING]
__all__ = [
    'NOTHING',
    'Attribute',
    'AttrsInstance',
    'Converter',
    'Factory',
    'NothingType',
    'asdict',
    'assoc',
    'astuple',
    'attr',
    'attrib',
    'attributes',
    'attrs',
    'cmp_using',
    'converters',
    'define',
    'evolve',
    'exceptions',
    'field',
    'fields',
    'fields_dict',
    'filters',
    'frozen',
    'get_run_validators',
    'has',
    'ib',
    'make_class',
    'mutable',
    'resolve_types',
    's',
    'set_run_validators',
    'setters',
    'validate',
    'validators']

def _make_getattr(mod_name = None):
    '''
    Create a metadata proxy for packaging information that uses *mod_name* in
    its warnings and errors.
    '''
    pass
# WARNING: Decompyle incomplete

__getattr__ = _make_getattr(__name__)

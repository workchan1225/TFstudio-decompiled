# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: error_wrappers.pyc (Python 3.11)

import json
from typing import TYPE_CHECKING, Any, Dict, Generator, List, Optional, Sequence, Tuple, Type, Union
from pydantic.v1.json import pydantic_encoder
from pydantic.v1.utils import Representation
if TYPE_CHECKING:
    from typing_extensions import TypedDict
    from pydantic.v1.config import BaseConfig
    from pydantic.v1.types import ModelOrDc
    from pydantic.v1.typing import ReprArgs
    Loc = Tuple[(Union[(int, str)], ...)]
    
    class _ErrorDictRequired(TypedDict):
        type: str = '_ErrorDictRequired'

    
    def ErrorDict():
        '''ErrorDict'''
        ctx: Dict[(str, Any)] = 'ErrorDict'

    ErrorDict = <NODE:27>(ErrorDict, 'ErrorDict', _ErrorDictRequired, total = False)
__all__ = ('ErrorWrapper', 'ValidationError')

class ErrorWrapper(Representation):
    __slots__ = ('exc', '_loc')
    
    def __init__(self = None, exc = None, loc = None):
        self.exc = exc
        self._loc = loc

    
    def loc_tuple(self = None):
        if isinstance(self._loc, tuple):
            return self._loc
        return (None._loc,)

    
    def __repr_args__(self = None):
        return [
            ('exc', self.exc),
            ('loc', self.loc_tuple())]


ErrorList = Union[(Sequence[Any], ErrorWrapper)]

class ValidationError(ValueError, Representation):
    __slots__ = ('raw_errors', 'model', '_error_cache')
    
    def __init__(self = None, errors = None, model = None):
        self.raw_errors = errors
        self.model = model
        self._error_cache = None

    
    def errors(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def json(self = None, *, indent):
        return json.dumps(self.errors(), indent = indent, default = pydantic_encoder)

    
    def __str__(self = None):
        errors = self.errors()
        no_errors = len(errors)
        return f'''{no_errors} validation error{'' if no_errors == 1 else 's'} for {self.model.__name__}\n{display_errors(errors)}'''

    
    def __repr_args__(self = None):
        return [
            ('model', self.model.__name__),
            ('errors', self.errors())]



def display_errors(errors = None):
    return (lambda .0: pass# WARNING: Decompyle incomplete
)(errors())


def _display_error_loc(error = None):
    return (lambda .0: pass# WARNING: Decompyle incomplete
)(error['loc']())


def _display_error_type_and_ctx(error = None):
    t = 'type=' + error['type']
    ctx = error.get('ctx')
    if ctx:
        return ''.join + (lambda .0: pass# WARNING: Decompyle incomplete
)(ctx.items()())


def flatten_errors(errors = None, config = None, loc = None):
    pass
# WARNING: Decompyle incomplete


def error_dict(exc = None, config = None, loc = None):
    type_ = get_exc_type(exc.__class__)
# WARNING: Decompyle incomplete

_EXC_TYPE_CACHE: Dict[(Type[Exception], str)] = { }

def get_exc_type(cls = None):
    
    try:
        return _EXC_TYPE_CACHE[cls]
    except KeyError:
        r = _get_exc_type(cls)
        _EXC_TYPE_CACHE[cls] = r
        return 



def _get_exc_type(cls = None):

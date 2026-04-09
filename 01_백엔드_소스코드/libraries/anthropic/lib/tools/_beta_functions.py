# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _beta_functions.pyc (Python 3.11)

from __future__ import annotations
import logging
from abc import ABC, abstractmethod
from typing import Any, Union, Generic, TypeVar, Callable, Iterable, Coroutine, cast, overload
from inspect import iscoroutinefunction
from typing_extensions import TypeAlias, override
import pydantic
import docstring_parser
from pydantic import BaseModel
from  import _compat
from _utils import is_dict
from _compat import cached_property
from _models import TypeAdapter
from types.beta import BetaToolParam, BetaToolUnionParam
from _utils._utils import CallableT
from types.tool_param import InputSchema
from types.beta.beta_tool_result_block_param import Content as BetaContent
log = logging.getLogger(__name__)
BetaFunctionToolResultType: 'TypeAlias' = Union[(str, Iterable[BetaContent])]
Function = Callable[(..., BetaFunctionToolResultType)]
FunctionT = TypeVar('FunctionT', bound = Function)
AsyncFunction = Callable[(..., Coroutine[(Any, Any, BetaFunctionToolResultType)])]
AsyncFunctionT = TypeVar('AsyncFunctionT', bound = AsyncFunction)

class BetaBuiltinFunctionTool(ABC):
    to_dict = (lambda self = None: pass)()
    call = (lambda self = None, input = None: pass)()
    name = (lambda self = None: raw = self.to_dict()if 'mcp_server_name' in raw:
raw['mcp_server_name']None['name'])()


class BetaAsyncBuiltinFunctionTool(ABC):
    to_dict = (lambda self = None: pass)()
    call = (lambda self = None, input = None: pass# WARNING: Decompyle incomplete
)()
    name = (lambda self = None: raw = self.to_dict()if 'mcp_server_name' in raw:
raw['mcp_server_name']None['name'])()


def BaseFunctionTool():
    '''BaseFunctionTool'''
    input_schema: 'InputSchema' = 'BaseFunctionTool'
    
    def __init__(self = None, func = None, *, name, description, input_schema, defer_loading):
        if _compat.PYDANTIC_V1:
            raise RuntimeError('Tool functions are only supported with Pydantic v2')
        self.func = func
        self._func_with_validate = pydantic.validate_call(func)
    # WARNING: Decompyle incomplete

    __call__ = (lambda self = None: self.func)()
    
    def to_dict(self = None):
        defn = {
            'name': self.name,
            'description': self.description,
            'input_schema': self.input_schema }
    # WARNING: Decompyle incomplete

    _parsed_docstring = (lambda self = None:

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: mypy.pyc (Python 3.11)

import sys
from configparser import ConfigParser
from typing import Any, Callable, Dict, List, Optional, Set, Tuple, Type as TypingType, Union
from mypy.errorcodes import ErrorCode
from mypy.nodes import ARG_NAMED, ARG_NAMED_OPT, ARG_OPT, ARG_POS, ARG_STAR2, MDEF, Argument, AssignmentStmt, Block, CallExpr, ClassDef, Context, Decorator, EllipsisExpr, FuncBase, FuncDef, JsonDict, MemberExpr, NameExpr, PassStmt, PlaceholderNode, RefExpr, StrExpr, SymbolNode, SymbolTableNode, TempNode, TypeInfo, TypeVarExpr, Var
from mypy.options import Options
from mypy.plugin import CheckerPluginInterface, ClassDefContext, FunctionContext, MethodContext, Plugin, ReportConfigContext, SemanticAnalyzerPluginInterface
from mypy.plugins import dataclasses
from mypy.semanal import set_callable_name
from mypy.server.trigger import make_wildcard_trigger
from mypy.types import AnyType, CallableType, Instance, NoneType, Overloaded, ProperType, Type, TypeOfAny, TypeType, TypeVarId, TypeVarType, UnionType, get_proper_type
from mypy.typevars import fill_typevars
from mypy.util import get_unique_redefinition_name
from mypy.version import __version__ as mypy_version
from pydantic.v1.utils import is_valid_field

try:
    from mypy.types import TypeVarDef
except ImportError:
    from mypy.types import TypeVarType as TypeVarDef

CONFIGFILE_KEY = 'pydantic-mypy'
METADATA_KEY = 'pydantic-mypy-metadata'
_NAMESPACE = __name__[:-5]
BASEMODEL_FULLNAME = f'''{_NAMESPACE}.main.BaseModel'''
BASESETTINGS_FULLNAME = f'''{_NAMESPACE}.env_settings.BaseSettings'''
MODEL_METACLASS_FULLNAME = f'''{_NAMESPACE}.main.ModelMetaclass'''
FIELD_FULLNAME = f'''{_NAMESPACE}.fields.Field'''
DATACLASS_FULLNAME = f'''{_NAMESPACE}.dataclasses.dataclass'''

def parse_mypy_version(version = None):
    return tuple(map(int, version.partition('+')[0].split('.')))

MYPY_VERSION_TUPLE = parse_mypy_version(mypy_version)
BUILTINS_NAME = 'builtins' if MYPY_VERSION_TUPLE >= (0, 930) else '__builtins__'
__version__ = 2

def plugin(version = None):
    '''
    `version` is the mypy version string

    We might want to use this to print a warning if the mypy version being used is
    newer, or especially older, than we expect (or need).
    '''
    return PydanticPlugin


class PydanticPlugin(Plugin):
    pass
# WARNING: Decompyle incomplete


class PydanticPluginConfig:
    debug_dataclass_transform: bool = ('init_forbid_extra', 'init_typed', 'warn_required_dynamic_aliases', 'warn_untyped_fields', 'debug_dataclass_transform')
    
    def __init__(self = None, options = None):
        pass
    # WARNING: Decompyle incomplete

    
    def to_data(self = None):
        pass
    # WARNING: Decompyle incomplete



def from_orm_callback(ctx = None):
    '''
    Raise an error if orm_mode is not enabled
    '''
    ctx_type = ctx.type
    if isinstance(ctx_type, TypeType):
        ctx_type = ctx_type.item
    if isinstance(ctx_type, CallableType) and isinstance(ctx_type.ret_type, Instance):
        model_type = ctx_type.ret_type
    elif isinstance(ctx_type, Instance):
        model_type = ctx_type
    else:
        detail = f'''ctx.type: {ctx_type} (of type {ctx_type.__class__.__name__})'''
        error_unexpected_behavior(detail, ctx.api, ctx.context)
        return ctx.default_return_type
    pydantic_metadata = None.type.metadata.get(METADATA_KEY)
# WARNING: Decompyle incomplete


class PydanticModelTransformer:
    tracked_config_fields: Set[str] = {
        'extra',
        'frozen',
        'orm_mode',
        'allow_mutation',
        'alias_generator',
        'allow_population_by_field_name'}
    
    def __init__(self = None, ctx = None, plugin_config = None):
        self._ctx = ctx
        self.plugin_config = plugin_config

    
    def transform(self = None):

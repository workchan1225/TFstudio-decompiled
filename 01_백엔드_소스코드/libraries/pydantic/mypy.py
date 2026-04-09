# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: mypy.pyc (Python 3.11)

'''This module includes classes and functions designed specifically for use with the mypy plugin.'''
from __future__ import annotations
import sys
from collections.abc import Iterator
from configparser import ConfigParser
from typing import Any, Callable
from mypy.errorcodes import ErrorCode
from mypy.expandtype import expand_type, expand_type_by_instance
from mypy.nodes import ARG_NAMED, ARG_NAMED_OPT, ARG_OPT, ARG_POS, ARG_STAR2, INVARIANT, MDEF, Argument, AssignmentStmt, Block, CallExpr, ClassDef, Context, Decorator, DictExpr, EllipsisExpr, Expression, FuncDef, IfStmt, JsonDict, MemberExpr, NameExpr, PassStmt, PlaceholderNode, RefExpr, Statement, StrExpr, SymbolTableNode, TempNode, TypeAlias, TypeInfo, Var
from mypy.options import Options
from mypy.plugin import CheckerPluginInterface, ClassDefContext, MethodContext, Plugin, ReportConfigContext, SemanticAnalyzerPluginInterface
from mypy.plugins.common import deserialize_and_fixup_type
from mypy.semanal import set_callable_name
from mypy.server.trigger import make_wildcard_trigger
from mypy.state import state
from mypy.type_visitor import TypeTranslator
from mypy.typeops import map_type_from_supertype
from mypy.types import AnyType, CallableType, Instance, NoneType, Type, TypeOfAny, TypeType, TypeVarType, UnionType, get_proper_type
from mypy.typevars import fill_typevars
from mypy.util import get_unique_redefinition_name
from mypy.version import __version__ as mypy_version
from pydantic._internal import _fields
from pydantic.version import parse_mypy_version
CONFIGFILE_KEY = 'pydantic-mypy'
METADATA_KEY = 'pydantic-mypy-metadata'
BASEMODEL_FULLNAME = 'pydantic.main.BaseModel'
BASESETTINGS_FULLNAME = 'pydantic_settings.main.BaseSettings'
ROOT_MODEL_FULLNAME = 'pydantic.root_model.RootModel'
MODEL_METACLASS_FULLNAME = 'pydantic._internal._model_construction.ModelMetaclass'
FIELD_FULLNAME = 'pydantic.fields.Field'
DATACLASS_FULLNAME = 'pydantic.dataclasses.dataclass'
MODEL_VALIDATOR_FULLNAME = 'pydantic.functional_validators.model_validator'
DECORATOR_FULLNAMES = {
    'pydantic.functional_serializers.serializer',
    'pydantic.deprecated.class_validators.validator',
    'pydantic.functional_validators.field_validator',
    'pydantic.deprecated.class_validators.root_validator',
    'pydantic.functional_validators.model_validator',
    'pydantic.functional_serializers.model_serializer'}
IMPLICIT_CLASSMETHOD_DECORATOR_FULLNAMES = DECORATOR_FULLNAMES - {
    'pydantic.functional_serializers.model_serializer'}
MYPY_VERSION_TUPLE = parse_mypy_version(mypy_version)
BUILTINS_NAME = 'builtins'
__version__ = 2

def plugin(version = None):
    '''`version` is the mypy version string.

    We might want to use this to print a warning if the mypy version being used is
    newer, or especially older, than we expect (or need).

    Args:
        version: The mypy version string.

    Return:
        The Pydantic mypy plugin type.
    '''
    return PydanticPlugin


class PydanticPlugin(Plugin):
    pass
# WARNING: Decompyle incomplete


class PydanticPluginConfig:
    '''A Pydantic mypy plugin config holder.

    Attributes:
        init_forbid_extra: Whether to add a `**kwargs` at the end of the generated `__init__` signature.
        init_typed: Whether to annotate fields in the generated `__init__`.
        warn_required_dynamic_aliases: Whether to raise required dynamic aliases error.
        debug_dataclass_transform: Whether to not reset `dataclass_transform_spec` attribute
            of `ModelMetaclass` for testing purposes.
    '''
    debug_dataclass_transform: 'bool' = ('init_forbid_extra', 'init_typed', 'warn_required_dynamic_aliases', 'debug_dataclass_transform')
    
    def __init__(self = None, options = None):
        pass
    # WARNING: Decompyle incomplete

    
    def to_data(self = None):
        '''Returns a dict of config names to their values.'''
        pass
    # WARNING: Decompyle incomplete



def from_attributes_callback(ctx = None):
    '''Raise an error if from_attributes is not enabled.'''
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


class PydanticModelField:
    '''Based on mypy.plugins.dataclasses.DataclassAttribute.'''
    
    def __init__(self, name, alias, is_frozen, has_dynamic_alias, has_default, strict, line = None, column = None, type = None, info = ('name', 'str', 'alias', 'str | None', 'is_frozen', 'bool', 'has_dynamic_alias', 'bool', 'has_default', 'bool', 'strict', 'bool | None', 'line', 'int', 'column', 'int', 'type', 'Type | None', 'info', 'TypeInfo')):
        self.name = name
        self.alias = alias
        self.is_frozen = is_frozen
        self.has_dynamic_alias = has_dynamic_alias
        self.has_default = has_default
        self.strict = strict
        self.line = line
        self.column = column
        self.type = type
        self.info = info

    
    def to_argument(self, current_info, typed, model_strict, force_optional, use_alias = None, api = None, force_typevars_invariant = None, is_root_model_root = ('current_info', 'TypeInfo', 'typed', 'bool', 'model_strict', 'bool', 'force_optional', 'bool', 'use_alias', 'bool', 'api', 'SemanticAnalyzerPluginInterface', 'force_typevars_invariant', 'bool', 'is_root_model_root', 'bool', 'return', 'Argument')):
        '''Based on mypy.plugins.dataclasses.DataclassAttribute.to_argument.'''
        variable = self.to_var(current_info, api, use_alias, force_typevars_invariant)
    # WARNING: Decompyle incomplete

    
    def expand_type(self = None, current_info = None, api = None, force_typevars_invariant = (False, False), include_root_type = ('current_info', 'TypeInfo', 'api', 'SemanticAnalyzerPluginInterface', 'force_typevars_invariant', 'bool', 'include_root_type', 'bool', 'return', 'Type | None')):
        '''Based on mypy.plugins.dataclasses.DataclassAttribute.expand_type.'''
        if force_typevars_invariant and isinstance(self.type, TypeVarType):
            modified_type = self.type.copy_modified()
            modified_type.variance = INVARIANT
            self.type = modified_type
    # WARNING: Decompyle incomplete

    
    def to_var(self = None, current_info = None, api = None, use_alias = (False,), force_typevars_invariant = ('current_info', 'TypeInfo', 'api', 'SemanticAnalyzerPluginInterface', 'use_alias', 'bool', 'force_typevars_invariant', 'bool', 'return', 'Var')):
        '''Based on mypy.plugins.dataclasses.DataclassAttribute.to_var.'''
        pass
    # WARNING: Decompyle incomplete

    
    def serialize(self = None):
        '''Based on mypy.plugins.dataclasses.DataclassAttribute.serialize.'''
        pass
    # WARNING: Decompyle incomplete

    deserialize = (lambda cls = None, info = None, data = classmethod, api = ('info', 'TypeInfo', 'data', 'JsonDict', 'api', 'SemanticAnalyzerPluginInterface', 'return', 'PydanticModelField'): data = data.copy()typ = deserialize_and_fixup_type(data.pop('type'), api)# WARNING: Decompyle incomplete
)()
    
    def expand_typevar_from_subtype(self = None, sub_type = None, api = None):
        '''Expands type vars in the context of a subtype when an attribute is inherited
        from a generic super type.
        '''
        pass
    # WARNING: Decompyle incomplete



class PydanticModelClassVar:
    '''Based on mypy.plugins.dataclasses.DataclassAttribute.

    ClassVars are ignored by subclasses.

    Attributes:
        name: the ClassVar name
    '''
    
    def __init__(self, name):
        self.name = name

    deserialize = (lambda cls = None, data = None: data = data.copy()# WARNING: Decompyle incomplete
)()
    
    def serialize(self = None):
        '''Based on mypy.plugins.dataclasses.DataclassAttribute.serialize.'''
        return {
            'name': self.name }



class PydanticModelTransformer:
    '''Transform the BaseModel subclass according to the plugin settings.

    Attributes:
        tracked_config_fields: A set of field configs that the plugin has to track their value.
    '''
    tracked_config_fields: 'set[str]' = {
        'extra',
        'frozen',
        'strict',
        'alias_generator',
        'from_attributes',
        'populate_by_name',
        'validate_by_name',
        'validate_by_alias'}
    
    def __init__(self, cls = None, reason = None, api = None, plugin_config = ('cls', 'ClassDef', 'reason', 'Expression | Statement', 'api', 'SemanticAnalyzerPluginInterface', 'plugin_config', 'PydanticPluginConfig', 'return', 'None')):
        self._cls = cls
        self._reason = reason
        self._api = api
        self.plugin_config = plugin_config

    
    def transform(self = None):
        '''Configures the BaseModel subclass according to the plugin settings.

        In particular:

        * determines the model config and fields,
        * adds a fields-aware signature for the initializer and construct methods
        * freezes the class if frozen = True
        * stores the fields, config, and if the class is settings in the mypy metadata for access by subclasses
        '''
        info = self._cls.info
        is_a_root_model = is_root_model(info)
        config = self.collect_config()
        (fields, class_vars) = self.collect_fields_and_class_vars(config, is_a_root_model)
    # WARNING: Decompyle incomplete

    
    def adjust_decorator_signatures(self = None):
        '''When we decorate a function `f` with `pydantic.validator(...)`, `pydantic.field_validator`
        or `pydantic.serializer(...)`, mypy sees `f` as a regular method taking a `self` instance,
        even though pydantic internally wraps `f` with `classmethod` if necessary.

        Teach mypy this by marking any function whose outermost decorator is a `validator()`,
        `field_validator()` or `serializer()` call as a `classmethod`.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def collect_config(self = None):
        '''Collects the values of the config attributes that are used by the plugin, accounting for parent classes.'''
        cls = self._cls
        config = ModelConfigData()
        has_config_kwargs = False
        has_config_from_namespace = False
    # WARNING: Decompyle incomplete

    
    def collect_fields_and_class_vars(self = None, model_config = None, is_root_model = None):
        '''Collects the fields for the model, accounting for parent classes.'''
        cls = self._cls
        found_fields = { }
        found_class_vars = { }
    # WARNING: Decompyle incomplete

    
    def _get_assignment_statements_from_if_statement(self = None, stmt = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_assignment_statements_from_block(self = None, block = None):
        pass
    # WARNING: Decompyle incomplete

    
    def collect_field_or_class_var_from_stmt(self = None, stmt = None, model_config = None, class_vars = ('stmt', 'AssignmentStmt', 'model_config', 'ModelConfigData', 'class_vars', 'dict[str, PydanticModelClassVar]', 'return', 'PydanticModelField | PydanticModelClassVar | None')):
        '''Get pydantic model field from statement.

        Args:
            stmt: The statement.
            model_config: Configuration settings for the model.
            class_vars: ClassVars already known to be defined on the model.

        Returns:
            A pydantic model field if it could find the field in statement. Otherwise, `None`.
        '''
        cls = self._cls
        lhs = stmt.lvalues[0]
        if isinstance(lhs, NameExpr) and _fields.is_valid_field_name(lhs.name) or lhs.name == 'model_config':
            return None
        if not None.new_syntax:
            if isinstance(stmt.rvalue, CallExpr) and isinstance(stmt.rvalue.callee, CallExpr) and isinstance(stmt.rvalue.callee.callee, NameExpr) and stmt.rvalue.callee.callee.fullname in DECORATOR_FULLNAMES:
                return None
            if None.name in class_vars:
                return None
            None(self._api, stmt)
            return None
        lhs = None.lvalues[0]
        if not isinstance(lhs, NameExpr):
            return None
        if None.is_valid_field_name(lhs.name) or lhs.name == 'model_config':
            return None
        sym = None.info.names.get(lhs.name)
    # WARNING: Decompyle incomplete

    
    def _infer_dataclass_attr_init_type(self = None, sym = None, name = None, context = ('sym', 'SymbolTableNode', 'name', 'str', 'context', 'Context', 'return', 'Type | None')):
        '''Infer __init__ argument type for an attribute.

        In particular, possibly use the signature of __set__.
        '''
        default = sym.type
        if sym.implicit:
            return default
        t = None(sym.type)
        if not isinstance(t, Instance):
            return default
        setter = None.type.get('__set__')
    # WARNING: Decompyle incomplete

    
    def add_initializer(self, fields = None, config = None, is_settings = None, is_root_model = ('fields', 'list[PydanticModelField]', 'config', 'ModelConfigData', 'is_settings', 'bool', 'is_root_model', 'bool', 'return', 'None')):
        '''Adds a fields-aware `__init__` method to the class.

        The added `__init__` will be annotated with types vs. all `Any` depending on the plugin settings.
        '''
        if not '__init__' in self._cls.info.names and self._cls.info.names['__init__'].plugin_generated:
            return None
        typed = None.plugin_config.init_typed
        model_strict = bool(config.strict)
    # WARNING: Decompyle incomplete

    
    def add_model_construct_method(self, fields = None, config = None, is_settings = None, is_root_model = ('fields', 'list[PydanticModelField]', 'config', 'ModelConfigData', 'is_settings', 'bool', 'is_root_model', 'bool', 'return', 'None')):
        '''Adds a fully typed `model_construct` classmethod to the class.

        Similar to the fields-aware __init__ method, but always uses the field names (not aliases),
        and does not treat settings fields as optional.
        '''
        set_str = self._api.named_type(f'''{BUILTINS_NAME}.set''', [
            self._api.named_type(f'''{BUILTINS_NAME}.str''')])
        optional_set_str = UnionType([
            set_str,
            NoneType()])
        fields_set_argument = Argument(Var('_fields_set', optional_set_str), optional_set_str, None, ARG_OPT)
        state.strict_optional_set(self._api.options.strict_optional)
        args = self.get_field_arguments(fields, typed = True, model_strict = bool(config.strict), requires_dynamic_aliases = False, use_alias = False, is_settings = is_settings, is_root_model = is_root_model)
        None(None, None)

    
    def set_frozen(self = None, fields = None, api = None, frozen = ('fields', 'list[PydanticModelField]', 'api', 'SemanticAnalyzerPluginInterface', 'frozen', 'bool', 'return', 'None')):
        '''Marks all fields as properties so that attempts to set them trigger mypy errors.

        This is the same approach used by the attrs and dataclasses plugins.
        '''
        info = self._cls.info
    # WARNING: Decompyle incomplete

    
    def get_config_update(self = None, name = None, arg = None, lax_extra = (False,)):
        """Determines the config update due to a single kwarg in the ConfigDict definition.

        Warns if a tracked config attribute is set to a value the plugin doesn't know how to interpret (e.g., an int)
        """
        if name not in self.tracked_config_fields:
            return None
        if None == 'extra':
            if isinstance(arg, StrExpr):
                forbid_extra = arg.value == 'forbid'
            elif isinstance(arg, MemberExpr):
                forbid_extra = arg.name == 'forbid'
            elif not lax_extra:
                error_invalid_config_value(name, self._api, arg)
            return None
        return None(forbid_extra = forbid_extra)
        if name == 'alias_generator':
            has_alias_generator = True
            if isinstance(arg, NameExpr) and arg.fullname == 'builtins.None':
                has_alias_generator = False
            return ModelConfigData(has_alias_generator = has_alias_generator)
    # WARNING: Decompyle incomplete

    get_has_default = (lambda stmt = None: expr = stmt.rvalueif isinstance(expr, TempNode):
False# WARNING: Decompyle incomplete
)()
    get_strict = (lambda stmt = None: expr = stmt.rvalueif isinstance(expr, CallExpr) and isinstance(expr.callee, RefExpr) and expr.callee.fullname == FIELD_FULLNAME:
for arg, name in zip(expr.args, expr.arg_names):
if name != 'strict':
continueif isinstance(arg, NameExpr):
if arg.fullname == 'builtins.True':
Trueif None.fullname == 'builtins.False':
FalseNoneNone)()
    get_alias_info = (lambda stmt = None: expr = stmt.rvalueif isinstance(expr, TempNode):
(None, False)if not None(expr, CallExpr) and isinstance(expr.callee, RefExpr) or expr.callee.fullname == FIELD_FULLNAME:
(None, False)if None in expr.arg_names:
arg = expr.args[expr.arg_names.index('validation_alias')]elif 'alias' in expr.arg_names:
arg = expr.args[expr.arg_names.index('alias')]else:
(None, False)if None(arg, StrExpr):
(arg.value, False))()
    is_field_frozen = (lambda stmt = None:

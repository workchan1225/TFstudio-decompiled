# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _config.pyc (Python 3.11)

from __future__ import annotations as _annotations
import warnings
from contextlib import contextmanager
from re import Pattern
from typing import TYPE_CHECKING, Any, Callable, Literal, cast
from pydantic_core import core_schema
from typing_extensions import Self
from aliases import AliasGenerator
from config import ConfigDict, ExtraValues, JsonDict, JsonEncoder, JsonSchemaExtraCallable
from errors import PydanticUserError
from warnings import PydanticDeprecatedSince20, PydanticDeprecatedSince210
if TYPE_CHECKING:
    from _internal._schema_generation_shared import GenerateSchema
    from fields import ComputedFieldInfo, FieldInfo
DEPRECATION_MESSAGE = 'Support for class-based `config` is deprecated, use ConfigDict instead.'

class ConfigWrapper:
    '''Internal wrapper for Config which exposes ConfigDict items as attributes.'''
    url_preserve_empty_path: 'bool' = ('config_dict',)
    
    def __init__(self = None, config = None, *, check):
        if check:
            self.config_dict = prepare_config(config)
            return None
        self.config_dict = None(ConfigDict, config)

    for_model = (lambda cls, bases = None, namespace = None, raw_annotations = classmethod, kwargs = ('bases', 'tuple[type[Any], ...]', 'namespace', 'dict[str, Any]', 'raw_annotations', 'dict[str, Any]', 'kwargs', 'dict[str, Any]', 'return', 'Self'): config_new = ConfigDict()# WARNING: Decompyle incomplete
)()
    if not TYPE_CHECKING:
        
        def __getattr__(self = None, name = None):
            
            try:
                return self.config_dict[name]
            except KeyError:
                return 
                except KeyError:
                    raise AttributeError(f'''Config has no attribute {name!r}'''), None


    
    def core_config(self = None, title = None):
        """Create a pydantic-core config.

        We don't use getattr here since we don't want to populate with defaults.

        Args:
            title: The title to use if not set in config.

        Returns:
            A `CoreConfig` object created from config.
        """
        config = self.config_dict
    # WARNING: Decompyle incomplete

    
    def __repr__(self):
        c = (lambda .0: pass# WARNING: Decompyle incomplete
)(self.config_dict.items()())
        return f'''ConfigWrapper({c})'''



class ConfigWrapperStack:
    '''A stack of `ConfigWrapper` instances.'''
    
    def __init__(self = None, config_wrapper = None):
        self._config_wrapper_stack = [
            config_wrapper]

    tail = (lambda self = None: self._config_wrapper_stack[-1])()
    push = (lambda self = None, config_wrapper = None: pass# WARNING: Decompyle incomplete
)()

# WARNING: Decompyle incomplete

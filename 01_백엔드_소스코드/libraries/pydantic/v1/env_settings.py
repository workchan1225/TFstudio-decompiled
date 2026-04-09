# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: env_settings.pyc (Python 3.11)

import os
import warnings
from pathlib import Path
from typing import AbstractSet, Any, Callable, ClassVar, Dict, List, Mapping, Optional, Tuple, Type, Union
from pydantic.v1.config import BaseConfig, Extra
from pydantic.v1.fields import ModelField
from pydantic.v1.main import BaseModel
from pydantic.v1.types import JsonWrapper
from pydantic.v1.typing import StrPath, display_as_type, get_origin, is_union
from pydantic.v1.utils import deep_update, lenient_issubclass, path_type, sequence_like
env_file_sentinel = str(object())
SettingsSourceCallable = Callable[([
    'BaseSettings'], Dict[(str, Any)])]
DotenvType = Union[(StrPath, List[StrPath], Tuple[(StrPath, ...)])]

class SettingsError(ValueError):
    pass


class BaseSettings(BaseModel):
    pass
# WARNING: Decompyle incomplete


class InitSettingsSource:
    __slots__ = ('init_kwargs',)
    
    def __init__(self = None, init_kwargs = None):
        self.init_kwargs = init_kwargs

    
    def __call__(self = None, settings = None):
        return self.init_kwargs

    
    def __repr__(self = None):
        return f'''InitSettingsSource(init_kwargs={self.init_kwargs!r})'''



class EnvSettingsSource:
    __slots__ = ('env_file', 'env_file_encoding', 'env_nested_delimiter', 'env_prefix_len')
    
    def __init__(self = None, env_file = None, env_file_encoding = None, env_nested_delimiter = (None, 0), env_prefix_len = ('env_file', Optional[DotenvType], 'env_file_encoding', Optional[str], 'env_nested_delimiter', Optional[str], 'env_prefix_len', int)):
        self.env_file = env_file
        self.env_file_encoding = env_file_encoding
        self.env_nested_delimiter = env_nested_delimiter
        self.env_prefix_len = env_prefix_len

    
    def __call__(self = None, settings = None):
        '''
        Build environment variables suitable for passing to the Model.
        '''
        d = { }
        dotenv_vars = self._read_env_files(settings.__config__.case_sensitive)
    # WARNING: Decompyle incomplete

    
    def _read_env_files(self = None, case_sensitive = None):
        env_files = self.env_file
    # WARNING: Decompyle incomplete

    
    def field_is_complex(self = None, field = None):
        '''
        Find out if a field is complex, and if so whether JSON errors should be ignored
        '''
        if lenient_issubclass(field.annotation, JsonWrapper):
            return (False, False)
        if None.is_complex():
            allow_parse_failure = False
        elif is_union(get_origin(field.type_)) and field.sub_fields and (lambda .0: pass# WARNING: Decompyle incomplete
)(field.sub_fields()):
            allow_parse_failure = True
        else:
            return (False, False)
        return (any, allow_parse_failure)

    
    def explode_env_vars(self = None, field = None, env_vars = None):
        '''
        Process env_vars and extract the values of keys containing env_nested_delimiter into nested dictionaries.

        This is applied to a single field, hence filtering by env_var prefix.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self = None):
        return f'''EnvSettingsSource(env_file={self.env_file!r}, env_file_encoding={self.env_file_encoding!r}, env_nested_delimiter={self.env_nested_delimiter!r})'''



class SecretsSettingsSource:
    __slots__ = ('secrets_dir',)
    
    def __init__(self = None, secrets_dir = None):
        self.secrets_dir = secrets_dir

    
    def __call__(self = None, settings = None):
        '''
        Build fields from "secrets" files.
        '''
        secrets = { }
    # WARNING: Decompyle incomplete

    
    def __repr__(self = None):
        return f'''SecretsSettingsSource(secrets_dir={self.secrets_dir!r})'''



def read_env_file(file_path = None, *, encoding, case_sensitive):

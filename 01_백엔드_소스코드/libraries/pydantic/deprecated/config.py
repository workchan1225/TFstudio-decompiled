# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: config.pyc (Python 3.11)

from __future__ import annotations as _annotations
import warnings
from typing import TYPE_CHECKING, Any, Literal
from typing_extensions import deprecated
from _internal import _config
from warnings import PydanticDeprecatedSince20
if not TYPE_CHECKING:
    DeprecationWarning = PydanticDeprecatedSince20
__all__ = ('BaseConfig', 'Extra')

class _ConfigMetaclass(type):
    
    def __getattr__(self = None, item = None):
        
        try:
            obj = _config.config_defaults[item]
            warnings.warn(_config.DEPRECATION_MESSAGE, DeprecationWarning)
            return obj
        except KeyError:
            exc = None
            raise AttributeError(f'''type object \'{self.__name__}\' has no attribute {exc}'''), exc
            exc = None
            del exc




def BaseConfig():
    '''BaseConfig'''
    pass
# WARNING: Decompyle incomplete

BaseConfig = <NODE:27>(BaseConfig, 'BaseConfig', metaclass = _ConfigMetaclass)()

class _ExtraMeta(type):
    pass
# WARNING: Decompyle incomplete


def Extra():
    '''Extra'''
    allow: "Literal['allow']" = 'allow'
    ignore: "Literal['ignore']" = 'ignore'
    forbid: "Literal['forbid']" = 'forbid'

Extra = <NODE:27>(Extra, 'Extra', metaclass = _ExtraMeta)()

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''For backward compatibility, expose main functions from
``setuptools.config.setupcfg``
'''
import warnings
from functools import wraps
from textwrap import dedent
from typing import Callable, TypeVar, cast
from _deprecation_warning import SetuptoolsDeprecationWarning
from  import setupcfg
Fn = TypeVar('Fn', bound = Callable)
__all__ = ('parse_configuration', 'read_configuration')

def _deprecation_notice(fn = None):
    pass
# WARNING: Decompyle incomplete

read_configuration = _deprecation_notice(setupcfg.read_configuration)
parse_configuration = _deprecation_notice(setupcfg.parse_configuration)

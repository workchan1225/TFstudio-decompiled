# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tomlconfig.pyc (Python 3.11)

'''TOML configuration support for coverage.py'''
from __future__ import annotations
import os
import re
from collections.abc import Iterable
from typing import Any, Callable, TypeVar
from coverage import config, env
from coverage.exceptions import ConfigError
from coverage.misc import import_third_party, isolate_module, substitute_variables
from coverage.types import TConfigSectionOut, TConfigValueOut
os = isolate_module(os)
if env.PYVERSION >= (3, 11, 0, 'alpha', 7):
    import tomllib
    has_tomllib = True
else:
    (tomllib, has_tomllib) = import_third_party('tomli')

class TomlDecodeError(Exception):
    """An exception class that exists even when toml isn't installed."""
    pass

TWant = TypeVar('TWant')

class TomlConfigParser:
    '''TOML file reading with the interface of HandyConfigParser.'''
    
    def __init__(self = None, our_file = None):
        self.our_file = our_file
        self.data = { }

    
    def read(self = None, filenames = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_section(self = None, section = None):
        '''Get a section from the data.

        Arguments:
            section (str): A section name, which can be dotted.

        Returns:
            name (str): the actual name of the section that was found, if any,
                or None.
            data (str): the dict of data in the section, or None if not found.

        '''
        prefixes = [
            'tool.coverage.']
        if self.our_file:
            prefixes.append('')
        for prefix in prefixes:
            real_section = prefix + section
            parts = real_section.split('.')
            data = self.data[parts[0]]
            for part in parts[1:]:
                data = data[part]
            except KeyError:
                continue
        return (None, None)
        return (real_section, data)

    
    def _get(self = None, section = None, option = None):
        '''Like .get, but returns the real section name and the value.'''
        (name, data) = self._get_section(section)
    # WARNING: Decompyle incomplete

    
    def _get_single(self = None, section = None, option = None):
        '''Get a single-valued option.

        Performs environment substitution if the value is a string. Other types
        will be converted later as needed.
        '''
        (name, value) = self._get(section, option)
        if isinstance(value, str):
            value = substitute_variables(value, os.environ)
        return (name, value)

    
    def has_option(self = None, section = None, option = None):
        (_, data) = self._get_section(section)
    # WARNING: Decompyle incomplete

    
    def real_section(self = None, section = None):
        (name, _) = self._get_section(section)
        return name

    
    def has_section(self = None, section = None):
        (name, _) = self._get_section(section)
        return bool(name)

    
    def options(self = None, section = None):
        (_, data) = self._get_section(section)
    # WARNING: Decompyle incomplete

    
    def get_section(self = None, section = None):

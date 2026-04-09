# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: findpaths.pyc (Python 3.11)

from __future__ import annotations
from collections.abc import Iterable
from collections.abc import Sequence
from dataclasses import dataclass
from dataclasses import KW_ONLY
import os
from pathlib import Path
import sys
from typing import Literal
from typing import TypeAlias
import iniconfig
from exceptions import UsageError
from _pytest.outcomes import fail
from _pytest.pathlib import absolutepath
from _pytest.pathlib import commonpath
from _pytest.pathlib import safe_exists
ConfigValue = <NODE:12>()
ConfigDict: 'TypeAlias' = dict[(str, ConfigValue)]

def _parse_ini_config(path = None):
    """Parse the given generic '.ini' file using legacy IniConfig parser, returning
    the parsed object.

    Raise UsageError if the file cannot be parsed.
    """
    
    try:
        return iniconfig.IniConfig(str(path))
    except iniconfig.ParseError:
        exc = None
        raise UsageError(str(exc)), exc
        exc = None
        del exc



def load_config_dict_from_file(filepath = None):
    '''Load pytest configuration from the given file path, if supported.

    Return None if the file does not contain valid pytest configuration.
    '''
    pass
# WARNING: Decompyle incomplete


def locate_config(invocation_dir = None, args = None):
    '''Search in the list of arguments for a valid ini-file for pytest,
    and return a tuple of (rootdir, inifile, cfg-dict, ignored-config-files), where
    ignored-config-files is a list of config basenames found that contain
    pytest configuration but were ignored.'''
    config_names = [
        'pytest.toml',
        '.pytest.toml',
        'pytest.ini',
        '.pytest.ini',
        'pyproject.toml',
        'tox.ini',
        'setup.cfg']
    args = args()
    if not args:
        args = [
            invocation_dir]
    found_pyproject_toml = None
    ignored_config_files = []
# WARNING: Decompyle incomplete


def get_common_ancestor(invocation_dir = None, paths = None):
    common_ancestor = None
# WARNING: Decompyle incomplete


def get_dirs_from_args(args = None):
    pass
# WARNING: Decompyle incomplete


def parse_override_ini(override_ini = None):
    '''Parse the -o/--override-ini command line arguments and return the overrides.

    :raises UsageError:
        If one of the values is malformed.
    '''
    overrides = { }
    if not override_ini:
        for ini_config in ():
            (key, user_ini_value) = ini_config.split('=', 1)
            overrides[key] = ConfigValue(user_ini_value, origin = 'override', mode = 'ini')
            except ValueError:
                e = None
                raise UsageError(f'''-o/--override-ini expects option=value style (got: {ini_config!r}).'''), e
                e = None
                del e
            return overrides

CFG_PYTEST_SECTION = '[pytest] section in {filename} files is no longer supported, change to [tool:pytest] instead.'

def determine_setup(*, inifile, override_ini, args, rootdir_cmd_arg, invocation_dir):
    '''Determine the rootdir, inifile and ini configuration values from the
    command line arguments.

    :param inifile:
        The `--inifile` command line argument, if given.
    :param override_ini:
        The -o/--override-ini command line arguments, if given.
    :param args:
        The free command line arguments.
    :param rootdir_cmd_arg:
        The `--rootdir` command line argument, if given.
    :param invocation_dir:
        The working directory when pytest was invoked.

    :raises UsageError:
    '''
    rootdir = None
    dirs = get_dirs_from_args(args)
    ignored_config_files = []
# WARNING: Decompyle incomplete


def is_fs_root(p = None):
    '''
    Return True if the given path is pointing to the root of the
    file system ("/" on Unix and "C:\\\\" on Windows for example).
    '''
    return os.path.splitdrive(str(p))[1] == os.sep

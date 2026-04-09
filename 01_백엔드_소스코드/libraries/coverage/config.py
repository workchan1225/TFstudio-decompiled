# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: config.pyc (Python 3.11)

'''Config file for coverage.py'''
from __future__ import annotations
import base64
import collections
import configparser
import copy
import json
import os
import os.path as os
import re
from collections.abc import Iterable
from typing import Any, Callable, Final, Mapping
from coverage.exceptions import ConfigError
from coverage.misc import human_sorted_items, isolate_module, substitute_variables
from coverage.tomlconfig import TomlConfigParser, TomlDecodeError
from coverage.types import TConfigSectionIn, TConfigSectionOut, TConfigurable, TConfigValueIn, TConfigValueOut, TPluginConfig
os = isolate_module(os)

class HandyConfigParser(configparser.ConfigParser):
    pass
# WARNING: Decompyle incomplete

TConfigParser = HandyConfigParser | TomlConfigParser
DEFAULT_EXCLUDE = [
    '#\\s*(pragma|PRAGMA)[:\\s]?\\s*(no|NO)\\s*(cover|COVER)',
    '^\\s*(((async )?def .*?)?\\)(\\s*->.*?)?:\\s*)?\\.\\.\\.\\s*(#|$)',
    'if (typing\\.)?TYPE_CHECKING:']
DEFAULT_PARTIAL = [
    '#\\s*(pragma|PRAGMA)[:\\s]?\\s*(no|NO)\\s*(branch|BRANCH)']
DEFAULT_PARTIAL_ALWAYS = [
    'while (True|1|False|0):',
    'if (True|1|False|0):']

class CoverageConfig(TPluginConfig, TConfigurable):
    '''Coverage.py configuration.

    The attributes of this class are the various settings that control the
    operation of coverage.py.

    '''
    
    def __init__(self = None):
        '''Initialize the configuration attributes to their defaults.'''
        self.config_files_attempted = []
        self.config_files_read = []
        self.config_file = None
        self._config_contents = None
        self._include = None
        self._omit = None
        self.branch = False
        self.command_line = None
        self.concurrency = []
        self.context = None
        self.core = None
        self.cover_pylib = False
        self.data_file = '.coverage'
        self.debug = []
        self.debug_file = None
        self.disable_warnings = []
        self.dynamic_context = None
        self.parallel = False
        self.patch = []
        self.plugins = []
        self.relative_files = False
        self.run_include = []
        self.run_omit = []
        self.sigterm = False
        self.source = None
        self.source_pkgs = []
        self.source_dirs = []
        self.timid = False
        self._crash = None
        self.exclude_list = DEFAULT_EXCLUDE[:]
        self.exclude_also = []
        self.fail_under = 0
        self.format = None
        self.ignore_errors = False
        self.include_namespace_packages = False
        self.report_include = None
        self.report_omit = None
        self.partial_always_list = DEFAULT_PARTIAL_ALWAYS[:]
        self.partial_list = DEFAULT_PARTIAL[:]
        self.partial_also = []
        self.precision = 0
        self.report_contexts = None
        self.show_missing = False
        self.skip_covered = False
        self.skip_empty = False
        self.sort = None
        self.extra_css = None
        self.html_dir = 'htmlcov'
        self.html_skip_covered = None
        self.html_skip_empty = None
        self.html_title = 'Coverage report'
        self.show_contexts = False
        self.xml_output = 'coverage.xml'
        self.xml_package_depth = 99
        self.json_output = 'coverage.json'
        self.json_pretty_print = False
        self.json_show_contexts = False
        self.lcov_output = 'coverage.lcov'
        self.lcov_line_checksums = False
        self.paths = { }
        self.plugin_options = { }

    MUST_BE_LIST = {
        'debug',
        'patch',
        'plugins',
        'run_omit',
        'concurrency',
        'report_omit',
        'run_include',
        'report_include'}
    SERIALIZE_ABSPATH = {
        ('source', True),
        ('data_file', False),
        ('debug_file', False),
        ('source_dirs', False)}
    
    def from_args(self = None, **kwargs):
        '''Read config values from `kwargs`.'''
        pass
    # WARNING: Decompyle incomplete

    
    def from_file(self = None, filename = None, warn = None, our_file = ('filename', 'str', 'warn', 'Callable[[str], None]', 'our_file', 'bool', 'return', 'bool')):
        '''Read configuration from a .rc file.

        `filename` is a file name to read.

        `our_file` is True if this config file is specifically for coverage,
        False if we are examining another config file (tox.ini, setup.cfg)
        for possible settings.

        Returns True or False, whether the file could be read, and it had some
        coverage.py settings in it.

        '''
        (_, ext) = os.path.splitext(filename)
        if ext == '.toml':
            cp = TomlConfigParser(our_file)
        else:
            cp = HandyConfigParser(our_file)
        self.config_files_attempted.append(os.path.abspath(filename))
        
        try:
            files_read = cp.read(filename)
        except (configparser.Error, TomlDecodeError):
            err = None
            raise ConfigError(f'''Couldn\'t read config file {filename}: {err}'''), err
            err = None
            del err

        if not files_read:
            return False
        None.config_files_read.extend(map(os.path.abspath, files_read))
        any_set = False
    # WARNING: Decompyle incomplete

    
    def copy(self = None):
        '''Return a copy of the configuration.'''
        return copy.deepcopy(self)

    CONCURRENCY_CHOICES: 'Final[set[str]]' = {
        'gevent',
        'thread',
        'eventlet',
        'greenlet',
        'multiprocessing'}
    LIGHT_THREADS = {
        'gevent',
        'eventlet',
        'greenlet'}
    CONFIG_FILE_OPTIONS = [
        ('branch', 'run:branch', 'boolean'),
        ('command_line', 'run:command_line'),
        ('concurrency', 'run:concurrency', 'list'),
        ('context', 'run:context'),
        ('core', 'run:core'),
        ('cover_pylib', 'run:cover_pylib', 'boolean'),
        ('data_file', 'run:data_file', 'file'),
        ('debug', 'run:debug', 'list'),
        ('debug_file', 'run:debug_file', 'file'),
        ('disable_warnings', 'run:disable_warnings', 'list'),
        ('dynamic_context', 'run:dynamic_context'),
        ('parallel', 'run:parallel', 'boolean'),
        ('patch', 'run:patch', 'list'),
        ('plugins', 'run:plugins', 'list'),
        ('relative_files', 'run:relative_files', 'boolean'),
        ('run_include', 'run:include', 'list'),
        ('run_omit', 'run:omit', 'list'),
        ('sigterm', 'run:sigterm', 'boolean'),
        ('source', 'run:source', 'list'),
        ('source_pkgs', 'run:source_pkgs', 'list'),
        ('source_dirs', 'run:source_dirs', 'list'),
        ('timid', 'run:timid', 'boolean'),
        ('_crash', 'run:_crash'),
        ('exclude_list', 'report:exclude_lines', 'regexlist'),
        ('exclude_also', 'report:exclude_also', 'regexlist'),
        ('fail_under', 'report:fail_under', 'float'),
        ('format', 'report:format'),
        ('ignore_errors', 'report:ignore_errors', 'boolean'),
        ('include_namespace_packages', 'report:include_namespace_packages', 'boolean'),
        ('partial_always_list', 'report:partial_branches_always', 'regexlist'),
        ('partial_list', 'report:partial_branches', 'regexlist'),
        ('partial_also', 'report:partial_also', 'regexlist'),
        ('precision', 'report:precision', 'int'),
        ('report_contexts', 'report:contexts', 'list'),
        ('report_include', 'report:include', 'list'),
        ('report_omit', 'report:omit', 'list'),
        ('show_missing', 'report:show_missing', 'boolean'),
        ('skip_covered', 'report:skip_covered', 'boolean'),
        ('skip_empty', 'report:skip_empty', 'boolean'),
        ('sort', 'report:sort'),
        ('extra_css', 'html:extra_css'),
        ('html_dir', 'html:directory', 'file'),
        ('html_skip_covered', 'html:skip_covered', 'boolean'),
        ('html_skip_empty', 'html:skip_empty', 'boolean'),
        ('html_title', 'html:title'),
        ('show_contexts', 'html:show_contexts', 'boolean'),
        ('xml_output', 'xml:output', 'file'),
        ('xml_package_depth', 'xml:package_depth', 'int'),
        ('json_output', 'json:output', 'file'),
        ('json_pretty_print', 'json:pretty_print', 'boolean'),
        ('json_show_contexts', 'json:show_contexts', 'boolean'),
        ('lcov_output', 'lcov:output', 'file'),
        ('lcov_line_checksums', 'lcov:line_checksums', 'boolean')]
    
    def _set_attr_from_config_option(self = None, cp = None, attr = None, where = ('',), type_ = ('cp', 'TConfigParser', 'attr', 'str', 'where', 'str', 'type_', 'str', 'return', 'bool')):
        '''Set an attribute on self if it exists in the ConfigParser.

        Returns True if the attribute was set.

        '''
        (section, option) = where.split(':')
        if cp.has_option(section, option):
            method = getattr(cp, f'''get{type_}''')
            setattr(self, attr, method(section, option))
            return True

    
    def get_plugin_options(self = None, plugin = None):
        '''Get a dictionary of options for the plugin named `plugin`.'''
        return self.plugin_options.get(plugin, { })

    
    def set_option(self = None, option_name = None, value = None):
        '''Set an option in the configuration.

        `option_name` is a colon-separated string indicating the section and
        option name.  For example, the ``branch`` option in the ``[run]``
        section of the config file would be indicated with `"run:branch"`.

        `value` is the new value for the option.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def get_option(self = None, option_name = None):
        '''Get an option from the configuration.

        `option_name` is a colon-separated string indicating the section and
        option name.  For example, the ``branch`` option in the ``[run]``
        section of the config file would be indicated with `"run:branch"`.

        Returns the value of the option.

        '''
        if option_name == 'paths':
            return self.paths
        for option_spec in None.CONFIG_FILE_OPTIONS:
            (attr, where) = option_spec[:2]
            if where == option_name:
                
                return None, getattr(self, attr)
            (plugin_name, _, key) = option_name.partition(':')
            if key and plugin_name in self.plugins:
                return self.plugin_options.get(plugin_name, { }).get(key)
            raise None(f'''No such option: {option_name!r}''')

    
    def post_process(self = None):
        '''Make final adjustments to settings to make them usable.'''
        self.paths = self.paths.items()()
        if 'subprocess' in self.patch:
            True = self, self.partial_list += self.partial_also, .partial_list
        concurrencies = set(self.concurrency)
        unknown = concurrencies - self.CONCURRENCY_CHOICES
        if unknown:
            show = ', '.join(sorted(unknown))
            raise ConfigError(f'''Unknown concurrency choices: {show}''')
        light_threads = concurrencies & self.LIGHT_THREADS
        if len(light_threads) > 1:
            show = ', '.join(sorted(light_threads))
            raise ConfigError(f'''Conflicting concurrency settings: {show}''')

    
    def debug_info(self = None):
        '''Make a list of (name, value) pairs for writing debug info.'''
        return (lambda .0: pass# WARNING: Decompyle incomplete
)(self.__dict__.items()())

    
    def serialize(self = None):
        '''Convert to a string that can be ingested with `deserialize`.

        File paths used by `coverage run` are made absolute to ensure the
        deserialized config will refer to the same files.
        '''
        data = self.__dict__.items()()
        for k, must_exist in self.SERIALIZE_ABSPATH:
            abs_fn = abs_path_if_exists if must_exist else os.path.abspath
            v = data[k]
            if isinstance(v, list):
                v = list(map(abs_fn, v))
            elif isinstance(v, str):
                v = abs_fn(v)
            data[k] = v
            return base64.b64encode(json.dumps(data).encode()).decode()

    deserialize = (lambda cls = None, config_str = None: data = json.loads(base64.b64decode(config_str.encode()).decode())config = cls()config.__dict__.update(data)config)()


def process_file_value(path = None):
    '''Make adjustments to a file path to make it usable.'''
    return os.path.expanduser(path)


def abs_path_if_exists(path = None):
    '''os.path.abspath, but only if the path exists.'''
    if os.path.exists(path):
        return os.path.abspath(path)


def process_regexlist(name = None, option = None, values = None):
    '''Check the values in a regex list and keep the non-blank ones.'''
    value_list = []
    for value in values:
        value = value.strip()
        re.compile(value)
    except re.error:
        e = None
        raise ConfigError(f'''Invalid [{name}].{option} value {value!r}: {e}'''), e
        e = None
        del e
    if value:
        value_list.append(value)
    continue
    return value_list


def config_files_to_try(config_file = None):
    '''What config files should we try to read?

    Returns a list of tuples:
        (filename, is_our_file, was_file_specified)
    '''
    if config_file == '.coveragerc':
        config_file = True
    specified_file = config_file is not True
    if not specified_file:
        rcfile = os.getenv('COVERAGE_RCFILE')
        if rcfile:
            config_file = rcfile
            specified_file = True
    if not specified_file:
        config_file = '.coveragerc'
# WARNING: Decompyle incomplete


def read_coverage_config(config_file = None, warn = None, **kwargs):
    '''Read the coverage.py configuration.

    Arguments:
        config_file: a boolean or string, see the `Coverage` class for the
            tricky details.
        warn: a function to issue warnings.
        all others: keyword arguments from the `Coverage` class, used for
            setting values in the configuration.

    Returns:
        config:
            config is a CoverageConfig object read from the appropriate
            configuration file.

    '''
    config = CoverageConfig()
    if config_file:
        files_to_try = config_files_to_try(config_file)
        for fname, our_file, specified_file in files_to_try:
            config_read = config.from_file(fname, warn, our_file = our_file)
            if config_read:
                pass
            elif specified_file:
                raise ConfigError(f'''Couldn\'t read {fname!r} as a config file''')
            env_data_file = os.getenv('COVERAGE_FILE')
            if env_data_file:
                config.data_file = env_data_file
    debugs = os.getenv('COVERAGE_DEBUG')
    if debugs:
        (lambda .0: pass# WARNING: Decompyle incomplete
)(debugs.split(',')())
    env_core = os.getenv('COVERAGE_CORE')
    if env_core:
        config.core = env_core
# WARNING: Decompyle incomplete

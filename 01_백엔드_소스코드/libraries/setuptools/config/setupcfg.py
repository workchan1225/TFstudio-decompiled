# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: setupcfg.pyc (Python 3.11)

'''
Load setuptools configuration from ``setup.cfg`` files.

**API will be made private in the future**
'''
import os
import contextlib
import functools
import warnings
from collections import defaultdict
from functools import partial
from functools import wraps
from typing import TYPE_CHECKING, Callable, Any, Dict, Generic, Iterable, List, Optional, Tuple, TypeVar, Union
from distutils.errors import DistutilsOptionError, DistutilsFileError
from setuptools.extern.packaging.requirements import Requirement, InvalidRequirement
from setuptools.extern.packaging.version import Version, InvalidVersion
from setuptools.extern.packaging.specifiers import SpecifierSet
from setuptools._deprecation_warning import SetuptoolsDeprecationWarning
from  import expand
if TYPE_CHECKING:
    from setuptools.dist import Distribution
    from distutils.dist import DistributionMetadata
_Path = Union[(str, os.PathLike)]
SingleCommandOptions = Dict[('str', Tuple[('str', Any)])]
AllCommandOptions = Dict[('str', SingleCommandOptions)]
Target = TypeVar('Target', bound = Union[('Distribution', 'DistributionMetadata')])

def read_configuration(filepath = None, find_others = None, ignore_option_errors = None):
    '''Read given configuration file and returns options from it as a dict.

    :param str|unicode filepath: Path to configuration file
        to get options from.

    :param bool find_others: Whether to search for other configuration files
        which could be on in various places.

    :param bool ignore_option_errors: Whether to silently ignore
        options, values of which could not be resolved (e.g. due to exceptions
        in directives such as file:, attr:, etc.).
        If False exceptions are propagated as expected.

    :rtype: dict
    '''
    Distribution = Distribution
    import setuptools.dist
    dist = Distribution()
    filenames = dist.find_config_files() if find_others else []
    handlers = _apply(dist, filepath, filenames, ignore_option_errors)
    return configuration_to_dict(handlers)


def apply_configuration(dist = None, filepath = None):
    '''Apply the configuration from a ``setup.cfg`` file into an existing
    distribution object.
    '''
    _apply(dist, filepath)
    dist._finalize_requires()
    return dist


def _apply(dist = None, filepath = None, other_files = None, ignore_option_errors = ((), False)):
    '''Read configuration from ``filepath`` and applies to the ``dist`` object.'''
    _Distribution = _Distribution
    import setuptools.dist
    filepath = os.path.abspath(filepath)
    if not os.path.isfile(filepath):
        raise DistutilsFileError('Configuration file %s does not exist.' % filepath)
    current_directory = os.getcwd()
    os.chdir(os.path.dirname(filepath))
    filenames = None[filepath]
    
    try:
        _Distribution.parse_config_files(dist, filenames = filenames)
        handlers = parse_configuration(dist, dist.command_options, ignore_option_errors = ignore_option_errors)
        dist._finalize_license_files()
        os.chdir(current_directory)
    except:
        os.chdir(current_directory)

    return handlers


def _get_option(target_obj = None, key = None):
    '''
    Given a target object and option key, get that option from
    the target object, either through a get_{key} method or
    from an attribute directly.
    '''
    pass
# WARNING: Decompyle incomplete


def configuration_to_dict(handlers = None):
    '''Returns configuration data gathered by given handlers as a dict.

    :param list[ConfigHandler] handlers: Handlers list,
        usually from parse_configuration()

    :rtype: dict
    '''
    config_dict = defaultdict(dict)
    for handler in handlers:
        for option in handler.set_options:
            value = _get_option(handler.target_obj, option)
            config_dict[handler.section_prefix][option] = value
            return config_dict


def parse_configuration(distribution = None, command_options = None, ignore_option_errors = None):
    '''Performs additional parsing of configuration options
    for a distribution.

    Returns a list of used option handlers.

    :param Distribution distribution:
    :param dict command_options:
    :param bool ignore_option_errors: Whether to silently ignore
        options, values of which could not be resolved (e.g. due to exceptions
        in directives such as file:, attr:, etc.).
        If False exceptions are propagated as expected.
    :rtype: list
    '''
    ensure_discovered = expand.EnsurePackagesDiscovered(distribution)
    options = ConfigOptionsHandler(distribution, command_options, ignore_option_errors, ensure_discovered)
    options.parse()
    if not distribution.package_dir:
        distribution.package_dir = options.package_dir
    meta = ConfigMetadataHandler(distribution.metadata, command_options, ignore_option_errors, ensure_discovered, distribution.package_dir, distribution.src_root)
    meta.parse()
    None(None, None)


def _warn_accidental_env_marker_misconfig(label = None, orig_value = None, parsed = None):
    '''Because users sometimes misinterpret this configuration:

    [options.extras_require]
    foo = bar;python_version<"4"

    It looks like one requirement with an environment marker
    but because there is no newline, it\'s parsed as two requirements
    with a semicolon as separator.

    Therefore, if:
        * input string does not contain a newline AND
        * parsed result contains two requirements AND
        * parsing of the two parts from the result ("<first>;<second>")
        leads in a valid Requirement with a valid marker
    a UserWarning is shown to inform the user about the possible problem.
    '''
    if '\n' in orig_value or len(parsed) != 2:
        return None
    None.suppress(InvalidRequirement)
    original_requirements_str = ';'.join(parsed)
    req = Requirement(original_requirements_str)
# WARNING: Decompyle incomplete


def ConfigHandler():
    '''ConfigHandler'''
    section_prefix: str = 'Handles metadata supplied in configuration files.'
    aliases: Dict[(str, str)] = { }
    
    def __init__(self, target_obj = None, options = None, ignore_option_errors = None, ensure_discovered = ('target_obj', Target, 'options', AllCommandOptions, 'ensure_discovered', expand.EnsurePackagesDiscovered)):
        sections = { }
        section_prefix = self.section_prefix
        for section_name, section_options in options.items():
            if not section_name.startswith(section_prefix):
                continue
            section_name = section_name.replace(section_prefix, '').strip('.')
            sections[section_name] = section_options
            self.ignore_option_errors = ignore_option_errors
            self.target_obj = target_obj
            self.sections = sections
            self.set_options = []
            self.ensure_discovered = ensure_discovered
            return None

    parsers = (lambda self: raise NotImplementedError('%s must provide .parsers property' % self.__class__.__name__))()
    
    def __setitem__(self, option_name, value):
        unknown = tuple()
        target_obj = self.target_obj
        option_name = self.aliases.get(option_name, option_name)
        current_value = getattr(target_obj, option_name, unknown)
        if current_value is unknown:
            raise KeyError(option_name)
        if current_value:
            return None
        skip_option = None
        parser = self.parsers.get(option_name)
    # WARNING: Decompyle incomplete

    _parse_list = (lambda cls, value, separator = (',',): if isinstance(value, list):
valueif None in value:
value = value.splitlines()else:
value = value.split(separator)value())()
    _parse_dict = (lambda cls, value: separator = '='result = { }for line in cls._parse_list(value):
(key, sep, val) = line.partition(separator)if sep != separator:
raise DistutilsOptionError('Unable to parse option value to dict: %s' % value)result[key.strip()] = val.strip()result)()
    _parse_bool = (lambda cls, value: value = value.lower()value in ('1', 'true', 'yes'))()
    _exclude_files_parser = (lambda cls, key: pass# WARNING: Decompyle incomplete
)()
    _parse_file = (lambda cls = classmethod, value = classmethod, root_dir = classmethod: include_directive = 'file:'if not isinstance(value, str):
valueif not None.startswith(include_directive):
valuespec = None[len(include_directive):]filepaths = spec.split(',')()expand.read_files(filepaths, root_dir))()
    
    def _parse_attr(self = property, value = classmethod, package_dir = classmethod, root_dir = ('root_dir', _Path)):
        '''Represents value as a module attribute.

        Examples:
            attr: package.attr
            attr: package.module.attr

        :param str value:
        :rtype: str
        '''
        attr_directive = 'attr:'
        if not value.startswith(attr_directive):
            return value
        attr_desc = None.replace(attr_directive, '')
        package_dir.update(self.ensure_discovered.package_dir)
        return expand.read_attr(attr_desc, package_dir, root_dir)

    _get_parser_compound = (lambda cls: pass# WARNING: Decompyle incomplete
)()
    _parse_section_to_dict_with_key = (lambda cls, section_options, values_parser: value = { }for _, val in section_options.items():
value[key] = values_parser(key, val)value)()
    _parse_section_to_dict = (lambda cls, section_options, values_parser = (None,): pass# WARNING: Decompyle incomplete
)()
    
    def parse_section(self, section_options):
        '''Parses configuration file section.

        :param dict section_options:
        '''
        for _, value in section_options.items():
            contextlib.suppress(KeyError)
            self[name] = value
            None(None, None)
        with None:
            if not None:
                pass
        continue

    
    def parse(self):
        '''Parses configuration file items from one
        or more related sections.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _deprecated_config_handler(self, func, msg, warning_class):
        '''this function will wrap around parameters that are deprecated

        :param msg: deprecation message
        :param warning_class: class of warning exception to be raised
        :param func: function to be wrapped around
        '''
        pass
    # WARNING: Decompyle incomplete


ConfigHandler = <NODE:27>(ConfigHandler, 'ConfigHandler', Generic[Target])

def ConfigMetadataHandler():
    '''ConfigMetadataHandler'''
    pass
# WARNING: Decompyle incomplete

ConfigMetadataHandler = <NODE:27>(ConfigMetadataHandler, 'ConfigMetadataHandler', ConfigHandler['DistributionMetadata'])

def ConfigOptionsHandler():
    '''ConfigOptionsHandler'''
    pass
# WARNING: Decompyle incomplete

ConfigOptionsHandler = <NODE:27>(ConfigOptionsHandler, 'ConfigOptionsHandler', ConfigHandler['Distribution'])

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: pyprojecttoml.pyc (Python 3.11)

'''
Load setuptools configuration from ``pyproject.toml`` files.

**PRIVATE MODULE**: API reserved for setuptools internal usage only.
'''
import logging
import os
import warnings
from contextlib import contextmanager
from functools import partial
from typing import TYPE_CHECKING, Callable, Dict, Optional, Mapping, Union
from setuptools.errors import FileError, OptionError
from  import expand as _expand
from _apply_pyprojecttoml import apply as _apply
from _apply_pyprojecttoml import _PREVIOUSLY_DEFINED, _WouldIgnoreField
if TYPE_CHECKING:
    from setuptools.dist import Distribution
_Path = Union[(str, os.PathLike)]
_logger = logging.getLogger(__name__)

def load_file(filepath = None):
    tomli = tomli
    import setuptools.extern
    file = open(filepath, 'rb')
    None(None, None)
    return 
    with None:
        if not None, tomli.load(file):
            pass


def validate(config = None, filepath = None):
    validator = _validate_pyproject
    import 
    trove_classifier = validator.FORMAT_FUNCTIONS.get('trove-classifier')
    if hasattr(trove_classifier, '_disable_download'):
        trove_classifier._disable_download()
    
    try:
        return validator.validate(config)
    except validator.ValidationError:
        ex = None
        summary = f'''configuration error: {ex.summary}'''
        if ex.name.strip('`') != 'project':
            _logger.debug(summary)
            _logger.debug(ex.details)
        error = f'''invalid pyproject.toml config: {ex.name}.'''
        raise ValueError(f'''{error}\n{summary}'''), None
        ex = None
        del ex



def apply_configuration(dist = None, filepath = None, ignore_option_errors = None):
    '''Apply the configuration from a ``pyproject.toml`` file into an existing
    distribution object.
    '''
    config = read_configuration(filepath, True, ignore_option_errors, dist)
    return _apply(dist, config, filepath)


def read_configuration(filepath = None, expand = None, ignore_option_errors = None, dist = (True, False, None)):
    '''Read given configuration file and returns options from it as a dict.

    :param str|unicode filepath: Path to configuration file in the ``pyproject.toml``
        format.

    :param bool expand: Whether to expand directives and other computed values
        (i.e. post-process the given configuration)

    :param bool ignore_option_errors: Whether to silently ignore
        options, values of which could not be resolved (e.g. due to exceptions
        in directives such as file:, attr:, etc.).
        If False exceptions are propagated as expected.

    :param Distribution|None: Distribution object to which the configuration refers.
        If not given a dummy object will be created and discarded after the
        configuration is read. This is used for auto-discovery of packages in the case
        a dynamic configuration (e.g. ``attr`` or ``cmdclass``) is expanded.
        When ``expand=False`` this object is simply ignored.

    :rtype: dict
    '''
    filepath = os.path.abspath(filepath)
    if not os.path.isfile(filepath):
        raise FileError(f'''Configuration file {filepath!r} does not exist.''')
    if not load_file(filepath):
        asdict = { }
        project_table = asdict.get('project', { })
        tool_table = asdict.get('tool', { })
        setuptools_table = tool_table.get('setuptools', { })
        if not (asdict or project_table) and setuptools_table:
            return { }
        if None:
            msg = 'Support for `[tool.setuptools]` in `pyproject.toml` is still *beta*.'
            warnings.warn(msg, _BetaConfiguration)
    orig_setuptools_table = setuptools_table.copy()
# WARNING: Decompyle incomplete


def _skip_bad_config(project_cfg = None, setuptools_cfg = None, dist = None):
    '''Be temporarily forgiving with invalid ``pyproject.toml``'''
    pass
# WARNING: Decompyle incomplete


def expand_configuration(config = None, root_dir = None, ignore_option_errors = None, dist = (None, False, None)):
    '''Given a configuration with unresolved fields (e.g. dynamic, cmdclass, ...)
    find their final values.

    :param dict config: Dict containing the configuration for the distribution
    :param str root_dir: Top-level directory for the distribution/project
        (the same directory where ``pyproject.toml`` is place)
    :param bool ignore_option_errors: see :func:`read_configuration`
    :param Distribution|None: Distribution object to which the configuration refers.
        If not given a dummy object will be created and discarded after the
        configuration is read. Used in the case a dynamic configuration
        (e.g. ``attr`` or ``cmdclass``).

    :rtype: dict
    '''
    return _ConfigExpander(config, root_dir, ignore_option_errors, dist).expand()


class _ConfigExpander:
    
    def __init__(self = None, config = None, root_dir = None, ignore_option_errors = (None, False, None), dist = ('config', dict, 'root_dir', Optional[_Path], 'ignore_option_errors', bool, 'dist', Optional['Distribution'])):
        self.config = config
        if not root_dir:
            pass
        self.root_dir = os.getcwd()
        self.project_cfg = config.get('project', { })
        self.dynamic = self.project_cfg.get('dynamic', [])
        self.setuptools_cfg = config.get('tool', { }).get('setuptools', { })
        self.dynamic_cfg = self.setuptools_cfg.get('dynamic', { })
        self.ignore_option_errors = ignore_option_errors
        self._dist = dist

    
    def _ensure_dist(self = None):

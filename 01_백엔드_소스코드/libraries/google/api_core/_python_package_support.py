# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _python_package_support.pyc (Python 3.11)

'''Code to check versions of dependencies used by Google Cloud Client Libraries.'''
import warnings
import sys
from typing import Optional, Tuple
from collections import namedtuple
from _python_version_support import _flatten_message, _get_distribution_and_import_packages
if sys.version_info >= (3, 8):
    from importlib import metadata
else:
    import importlib_metadata as metadata
ParsedVersion = Tuple[(int, ...)]
DependencyConstraint = namedtuple('DependencyConstraint', [
    'package_name',
    'minimum_fully_supported_version',
    'recommended_version'])
_PACKAGE_DEPENDENCY_WARNINGS = [
    DependencyConstraint('google.protobuf', minimum_fully_supported_version = '4.25.8', recommended_version = '6.x')]
DependencyVersion = namedtuple('DependencyVersion', [
    'version',
    'version_string'])
UNKNOWN_VERSION_STRING = '--'

def parse_version_to_tuple(version_string = None):
    '''Safely converts a semantic version string to a comparable tuple of integers.

    Example: "4.25.8" -> (4, 25, 8)
    Ignores non-numeric parts and handles common version formats.

    Args:
        version_string: Version string in the format "x.y.z" or "x.y.z<suffix>"

    Returns:
        Tuple of integers for the parsed version string.
    '''
    parts = []
    for part in version_string.split('.'):
        parts.append(int(part))
        except ValueError:
            pass
        return tuple(parts)


def get_dependency_version(dependency_name = None):
    """Get the parsed version of an installed package dependency.

    This function checks for an installed package and returns its version
    as a comparable tuple of integers object for safe comparison. It handles
    both modern (Python 3.8+) and legacy (Python 3.7) environments.

    Args:
        dependency_name: The distribution name of the package (e.g., 'requests').

    Returns:
        A DependencyVersion namedtuple with `version`  (a tuple of integers) and
        `version_string` attributes, or `DependencyVersion(None,
        UNKNOWN_VERSION_STRING)` if the package is not found or
        another error occurs during version discovery.

    """
    
    try:
        version_string = metadata.version(dependency_name)
        parsed_version = parse_version_to_tuple(version_string)
        return DependencyVersion(parsed_version, version_string)
    except Exception:
        return 



def warn_deprecation_for_versions_less_than(consumer_import_package = None, dependency_import_package = None, minimum_fully_supported_version = None, recommended_version = (None, None), message_template = ('consumer_import_package', str, 'dependency_import_package', str, 'minimum_fully_supported_version', str, 'recommended_version', Optional[str], 'message_template', Optional[str])):

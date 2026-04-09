# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''Google API Core.

This package contains common code and utilities used by Google client libraries.
'''
from google.api_core import _python_package_support
from google.api_core import _python_version_support
from google.api_core import version as api_core_version
__version__ = api_core_version.__version__
check_python_version = _python_version_support.check_python_version
check_dependency_versions = _python_package_support.check_dependency_versions
warn_deprecation_for_versions_less_than = _python_package_support.warn_deprecation_for_versions_less_than
DependencyConstraint = _python_package_support.DependencyConstraint
check_python_version(package = 'google.api_core')
check_dependency_versions('google.api_core')

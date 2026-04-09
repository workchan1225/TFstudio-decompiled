# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _python_version_support.pyc (Python 3.11)

'''Code to check Python versions supported by Google Cloud Client Libraries.'''
import datetime
import enum
import warnings
import sys
import textwrap
from typing import Any, List, NamedTuple, Optional, Dict, Tuple

class PythonVersionStatus(enum.Enum):
    '''Support status of a Python version in this client library artifact release.

    "Support", in this context, means that this release of a client library
    artifact is configured to run on the currently configured version of
    Python.
    '''
    PYTHON_VERSION_STATUS_UNSPECIFIED = 'PYTHON_VERSION_STATUS_UNSPECIFIED'
    PYTHON_VERSION_SUPPORTED = 'PYTHON_VERSION_SUPPORTED'
    PYTHON_VERSION_DEPRECATED = 'PYTHON_VERSION_DEPRECATED'
    PYTHON_VERSION_EOL = 'PYTHON_VERSION_EOL'
    PYTHON_VERSION_UNSUPPORTED = 'PYTHON_VERSION_UNSUPPORTED'


class VersionInfo(NamedTuple):
    python_eol: datetime.date = 'Hold release and support date information for a Python version.'
    gapic_start: Optional[datetime.date] = None
    gapic_deprecation: Optional[datetime.date] = None
    gapic_end: Optional[datetime.date] = None
    dep_unpatchable_cve: Optional[datetime.date] = None

PYTHON_VERSIONS: List[VersionInfo] = [
    VersionInfo(version = '3.7', python_beta = None, python_start = datetime.date(2018, 6, 27), python_eol = datetime.date(2023, 6, 27)),
    VersionInfo(version = '3.8', python_beta = None, python_start = datetime.date(2019, 10, 14), python_eol = datetime.date(2024, 10, 7)),
    VersionInfo(version = '3.9', python_beta = datetime.date(2020, 5, 18), python_start = datetime.date(2020, 10, 5), python_eol = datetime.date(2025, 10, 5), gapic_end = datetime.date(2025, 10, 5) + datetime.timedelta(days = 90)),
    VersionInfo(version = '3.10', python_beta = datetime.date(2021, 5, 3), python_start = datetime.date(2021, 10, 4), python_eol = datetime.date(2026, 10, 4)),
    VersionInfo(version = '3.11', python_beta = datetime.date(2022, 5, 8), python_start = datetime.date(2022, 10, 24), python_eol = datetime.date(2027, 10, 24)),
    VersionInfo(version = '3.12', python_beta = datetime.date(2023, 5, 22), python_start = datetime.date(2023, 10, 2), python_eol = datetime.date(2028, 10, 2)),
    VersionInfo(version = '3.13', python_beta = datetime.date(2024, 5, 8), python_start = datetime.date(2024, 10, 7), python_eol = datetime.date(2029, 10, 7)),
    VersionInfo(version = '3.14', python_beta = datetime.date(2025, 5, 7), python_start = datetime.date(2025, 10, 7), python_eol = datetime.date(2030, 10, 7))]
PYTHON_VERSION_INFO: Dict[(Tuple[(int, int)], VersionInfo)] = { }
for info in PYTHON_VERSIONS:
    (major, minor) = map(int, info.version.split('.'))
    PYTHON_VERSION_INFO[(major, minor)] = info
    LOWEST_TRACKED_VERSION = min(PYTHON_VERSION_INFO.keys())
    _FAKE_PAST_DATE = datetime.date.min + datetime.timedelta(days = 900)
    _FAKE_PAST_VERSION = VersionInfo(version = '0.0', python_beta = _FAKE_PAST_DATE, python_start = _FAKE_PAST_DATE, python_eol = _FAKE_PAST_DATE)
    _FAKE_FUTURE_DATE = datetime.date.max - datetime.timedelta(days = 900)
    _FAKE_FUTURE_VERSION = VersionInfo(version = '999.0', python_beta = _FAKE_FUTURE_DATE, python_start = _FAKE_FUTURE_DATE, python_eol = _FAKE_FUTURE_DATE)
    DEPRECATION_WARNING_PERIOD = datetime.timedelta(days = 365)
    EOL_GRACE_PERIOD = datetime.timedelta(weeks = 1)
    
    def _flatten_message(text = None):
        '''Dedent a multi-line string and flatten it into a single line.'''
        return ' '.join(textwrap.dedent(text).strip().split())

    if sys.version_info < (3, 8):
        
        def _get_pypi_package_name(module_name):
            '''Determine the PyPI package name for a given module name.'''
            pass

    else:
        from importlib import metadata
        
        def _get_pypi_package_name(module_name):
            '''Determine the PyPI package name for a given module name.'''
            
            try:
                module_to_distributions = metadata.packages_distributions()
                if module_name in module_to_distributions:
                    return module_to_distributions[module_name][0]
                return None
            except Exception:
                e = None
                print(f'''An error occurred: {e}''')
                e = None
                del e
                return None
                e = None
                del e



def _get_distribution_and_import_packages(import_package = None):
    '''Return a pretty string with distribution & import package names.'''
    distribution_package = _get_pypi_package_name(import_package)
    dependency_distribution_and_import_packages = f'''package {distribution_package} ({import_package})''' if distribution_package else import_package
    return (dependency_distribution_and_import_packages, distribution_package)


def check_python_version(package = None, today = None):
    '''Check the running Python version and issue a support warning if needed.

    Args:
        today: The date to check against. Defaults to the current date.

    Returns:
        The support status of the current Python version.
    '''
    if not today:
        pass
    today = datetime.date.today()
    (package_label, _) = _get_distribution_and_import_packages(package)
    python_version = sys.version_info
    version_tuple = (python_version.major, python_version.minor)
    py_version_str = sys.version.split()[0]
    version_info = PYTHON_VERSION_INFO.get(version_tuple)
    if not version_info:
        if version_tuple < LOWEST_TRACKED_VERSION:
            version_info = _FAKE_PAST_VERSION
        else:
            version_info = _FAKE_FUTURE_VERSION
    if not version_info.gapic_deprecation:
        gapic_deprecation = version_info.python_eol - DEPRECATION_WARNING_PERIOD
        if not version_info.gapic_end:
            gapic_end = version_info.python_eol + EOL_GRACE_PERIOD
            
            def min_python(date = None):
                '''Find the minimum supported Python version for a given date.'''
                for version, info in sorted(PYTHON_VERSION_INFO.items()):
                    if  <= info.python_start, date or info.python_start, date < info.python_eol:
                        pass
                    
                    
                    return None, f'''{version[0]}.{version[1]}'''
                    return 'at a currently supported version [https://devguide.python.org/versions]'

            if gapic_end < today:
                message = _flatten_message(f'''\n            You are using a non-supported Python version ({py_version_str}).\n            Google will not post any further updates to {package_label}\n            supporting this Python version. Please upgrade to the latest Python\n            version, or at least Python {min_python(today)}, and then update\n            {package_label}.\n            ''')
                warnings.warn(message, FutureWarning)
                return PythonVersionStatus.PYTHON_VERSION_UNSUPPORTED
            eol_date = None.python_eol + EOL_GRACE_PERIOD
            if  <= eol_date, today or eol_date, today <= gapic_end:
                pass
            
        else:
            return PythonVersionStatus.PYTHON_VERSION_EOL
        if  <= version_info.gapic_end, today or version_info.gapic_end, today <= gapic_end:
            pass
        
    else:
        return PythonVersionStatus.PYTHON_VERSION_DEPRECATED
    return version_info.gapic_deprecation.PYTHON_VERSION_SUPPORTED

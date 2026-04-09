# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _print_versions.pyc (Python 3.11)

from __future__ import annotations
import json
import locale
import os
import platform
import struct
import sys
from typing import TYPE_CHECKING
from pandas.util._decorators import set_module
if TYPE_CHECKING:
    from pandas._typing import JSONSerializable
from pandas.compat._optional import VERSIONS, get_version, import_optional_dependency

def _get_commit_hash():
    '''
    Use vendored versioneer code to get git hash, which handles
    git worktree correctly.
    '''
    
    try:
        __git_version__ = __git_version__
        import pandas._version_meson
        return __git_version__
    except ImportError:
        get_versions = get_versions
        import pandas._version
        versions = get_versions()
        return 



def _get_sys_info():
    '''
    Returns system information as a JSON serializable dictionary.
    '''
    uname_result = platform.uname()
    (language_code, encoding) = locale.getlocale()
    return {
        'commit': _get_commit_hash(),
        'python': platform.python_version(),
        'python-bits': struct.calcsize('P') * 8,
        'OS': uname_result.system,
        'OS-release': uname_result.release,
        'Version': uname_result.version,
        'machine': uname_result.machine,
        'processor': uname_result.processor,
        'byteorder': sys.byteorder,
        'LC_ALL': os.environ.get('LC_ALL'),
        'LANG': os.environ.get('LANG'),
        'LOCALE': {
            'language-code': language_code,
            'encoding': encoding } }


def _get_dependency_info():
    '''
    Returns dependency information as a JSON serializable dictionary.
    '''
    deps = [
        'pandas',
        'numpy',
        'dateutil',
        'pip',
        'Cython',
        'sphinx',
        'IPython']
    deps.extend(list(VERSIONS))
    result = { }
    for modname in deps:
        mod = import_optional_dependency(modname, errors = 'ignore')
        result[modname] = get_version(mod) if mod else None
        except Exception:
            result[modname] = 'N/A'
            continue
        return result

show_versions = (lambda as_json = None: sys_info = _get_sys_info()deps = _get_dependency_info()# WARNING: Decompyle incomplete
)()

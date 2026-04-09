# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from pathlib import Path
from typing import Optional
from types import StrOrPath
from clr_error import ClrError
from coreclr_errors import get_coreclr_error
from find import find_dotnet_root
from hostfxr_errors import get_hostfxr_error
__all__ = [
    'check_result',
    'find_dotnet_root',
    'path_as_string',
    'optional_path_as_string']

def optional_path_as_string(path = None):
    pass
# WARNING: Decompyle incomplete


def path_as_string(path = None):
    return str(Path(path))


def check_result(err_code = None):
    '''Check the error code of a .NET hosting API function and raise a
    converted exception.

    :raises ClrError: If the error code is `< 0`
    '''
    if err_code < 0:
        hresult = err_code & 0xFFFFFFFF
        error = get_coreclr_error(hresult)
        if not error:
            error = get_hostfxr_error(hresult)
        if not error:
            error = ClrError(hresult)
        raise error

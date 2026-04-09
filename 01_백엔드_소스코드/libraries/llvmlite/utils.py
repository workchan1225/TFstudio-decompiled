# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: utils.pyc (Python 3.11)

import os
import sys

def get_library_name():
    '''
    Return the name of the llvmlite shared library file.
    '''
    if os.name == 'posix':
        if sys.platform == 'darwin':
            return 'libllvmlite.dylib'
        return None
# WARNING: Decompyle incomplete


def get_library_files():
    '''
    Return the names of shared library files needed for this platform.
    '''
    files = [
        get_library_name()]
    if os.name == 'nt':
        files.extend([
            'msvcr120.dll',
            'msvcp120.dll'])
    return files

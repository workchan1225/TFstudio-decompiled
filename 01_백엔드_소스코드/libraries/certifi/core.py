# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: core.pyc (Python 3.11)

'''
certifi.py
~~~~~~~~~~

This module returns the installation location of cacert.pem or its contents.
'''
import sys
import atexit

def exit_cacert_ctx():
    _CACERT_CTX.__exit__(None, None, None)

if sys.version_info >= (3, 11):
    from importlib.resources import as_file, files
    _CACERT_CTX = None
    _CACERT_PATH = None
    
    def where():
        pass
    # WARNING: Decompyle incomplete

    
    def contents():
        return files('certifi').joinpath('cacert.pem').read_text(encoding = 'ascii')

    return None
from importlib.resources import path as get_path, read_text
_CACERT_CTX = None
_CACERT_PATH = None

def where():
    pass
# WARNING: Decompyle incomplete


def contents():
    return read_text('certifi', 'cacert.pem', encoding = 'ascii')

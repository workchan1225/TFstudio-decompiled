# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: py311.pyc (Python 3.11)

import os
import pathlib
import sys
import types

def wrap(path):
    '''
    Workaround for https://github.com/python/cpython/issues/84538
    to add backward compatibility for walk_up=True.
    An example affected package is dask-labextension, which uses
    jupyter-packaging to install JupyterLab javascript files outside
    of site-packages.
    '''
    pass
# WARNING: Decompyle incomplete

relative_fix = wrap if sys.version_info < (3, 12) else (lambda x: x)

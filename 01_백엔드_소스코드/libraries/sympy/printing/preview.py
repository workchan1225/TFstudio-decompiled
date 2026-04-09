# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: preview.pyc (Python 3.11)

import os
from os.path import join
import shutil
import tempfile

try:
    from subprocess import STDOUT, CalledProcessError, check_output
except ImportError:
    pass

from sympy.utilities.decorator import doctest_depends_on
from sympy.utilities.misc import debug
from latex import latex
__doctest_requires__ = {
    ('preview',): [
        'pyglet'] }

def _check_output_no_window(*args, **kwargs):
    if os.name == 'nt':
        creation_flag = 134217728
    else:
        creation_flag = 0
# WARNING: Decompyle incomplete


def system_default_viewer(fname, fmt):

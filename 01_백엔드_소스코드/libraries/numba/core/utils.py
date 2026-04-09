# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: utils.pyc (Python 3.11)

import atexit
import builtins
import functools
import inspect
import os
import operator
import timeit
import math
import sys
import traceback
import weakref
import warnings
import threading
import contextlib
import json
import typing as _tp
from pprint import pformat
from types import ModuleType
from importlib import import_module
import numpy as np
from inspect import signature as pysignature
from inspect import Signature as pySignature
from inspect import Parameter as pyParameter
from numba.core.config import PYVERSION, MACHINE_BITS, DEVELOPER_MODE
from numba.core import config
from numba.core import types
from collections.abc import Mapping, Sequence, MutableSet, MutableMapping

def erase_traceback(exc_value):
    '''
    Erase the traceback and hanging locals from the given exception instance.
    '''
    pass
# WARNING: Decompyle incomplete


def safe_relpath(path, start = (os.curdir,)):
    '''
    Produces a "safe" relative path, on windows relpath doesn\'t work across
    drives as technically they don\'t share the same root.
    See: https://bugs.python.org/issue7195 for details.
    '''
    
    drive_letter = lambda x: os.path.splitdrive(os.path.abspath(x))[0]
    drive_path = drive_letter(path)
    drive_start = drive_letter(start)
    if drive_path != drive_start:
        return os.path.abspath(path)
    return None.path.relpath(path, start = start)

# WARNING: Decompyle incomplete

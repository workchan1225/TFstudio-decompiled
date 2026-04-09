# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: arrayprint.pyc (Python 3.11)

'''Array printing function

$Id: arrayprint.py,v 1.9 2005/09/13 13:58:44 teoliphant Exp $

'''
__all__ = [
    'array2string',
    'array_str',
    'array_repr',
    'set_string_function',
    'set_printoptions',
    'get_printoptions',
    'printoptions',
    'format_float_positional',
    'format_float_scientific']
__docformat__ = 'restructuredtext'
import functools
import numbers
import sys

try:
    from _thread import get_ident
except ImportError:
    from _dummy_thread import get_ident

import numpy as np
from  import numerictypes as _nt
from umath import absolute, isinf, isfinite, isnat
from  import multiarray
from multiarray import array, dragon4_positional, dragon4_scientific, datetime_as_string, datetime_data, ndarray, set_legacy_print_mode
from fromnumeric import any
from numeric import concatenate, asarray, errstate
from numerictypes import longlong, intc, int_, float_, complex_, bool_, flexible
from overrides import array_function_dispatch, set_module
import operator
import warnings
import contextlib
_format_options = {
    'edgeitems': 3,
    'threshold': 1000,
    'floatmode': 'maxprec',
    'precision': 8,
    'suppress': False,
    'linewidth': 75,
    'nanstr': 'nan',
    'infstr': 'inf',
    'sign': '-',
    'formatter': None,
    'legacy': sys.maxsize }

def _make_options_dict(precision, threshold, edgeitems, linewidth, suppress, nanstr, infstr, sign, formatter, floatmode, legacy = (None, None, None, None, None, None, None, None, None, None, None)):
    '''
    Make a dictionary out of the non-None arguments, plus conversion of
    *legacy* and sanity checks.
    '''
    options = locals().items()()
# WARNING: Decompyle incomplete

set_printoptions = (lambda precision, threshold, edgeitems, linewidth, suppress, nanstr, infstr, formatter = set_module('numpy'), sign = (None, None, None, None, None, None, None, None, None, None), floatmode = {
    'legacy': None }, *, legacy, opt = None,

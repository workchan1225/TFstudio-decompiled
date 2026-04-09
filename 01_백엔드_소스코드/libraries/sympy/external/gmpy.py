# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: gmpy.pyc (Python 3.11)

import os
from ctypes import c_long, sizeof
from functools import reduce
from typing import Tuple as tTuple, Type
from warnings import warn
from sympy.external import import_module
from pythonmpq import PythonMPQ
from ntheory import bit_scan1 as python_bit_scan1, bit_scan0 as python_bit_scan0, remove as python_remove, factorial as python_factorial, sqrt as python_sqrt, sqrtrem as python_sqrtrem, gcd as python_gcd, lcm as python_lcm, gcdext as python_gcdext, is_square as python_is_square, invert as python_invert, legendre as python_legendre, jacobi as python_jacobi, kronecker as python_kronecker, iroot as python_iroot, is_fermat_prp as python_is_fermat_prp, is_euler_prp as python_is_euler_prp, is_strong_prp as python_is_strong_prp, is_fibonacci_prp as python_is_fibonacci_prp, is_lucas_prp as python_is_lucas_prp, is_selfridge_prp as python_is_selfridge_prp, is_strong_lucas_prp as python_is_strong_lucas_prp, is_strong_selfridge_prp as python_is_strong_selfridge_prp, is_bpsw_prp as python_is_bpsw_prp, is_strong_bpsw_prp as python_is_strong_bpsw_prp
__all__ = [
    'GROUND_TYPES',
    'HAS_GMPY',
    'SYMPY_INTS',
    'MPQ',
    'MPZ',
    'bit_scan1',
    'bit_scan0',
    'remove',
    'factorial',
    'sqrt',
    'is_square',
    'sqrtrem',
    'gcd',
    'lcm',
    'gcdext',
    'invert',
    'legendre',
    'jacobi',
    'kronecker',
    'iroot',
    'is_fermat_prp',
    'is_euler_prp',
    'is_strong_prp',
    'is_fibonacci_prp',
    'is_lucas_prp',
    'is_selfridge_prp',
    'is_strong_lucas_prp',
    'is_strong_selfridge_prp',
    'is_bpsw_prp',
    'is_strong_bpsw_prp']
_PYTHON_FLINT_VERSION_NEEDED = [
    '0.6',
    '0.7',
    '0.8',
    '0.9']

def _flint_version_okay(flint_version):
    (major, minor) = flint_version.split('.')[:2]
    flint_ver = f'''{major}.{minor}'''
    return flint_ver in _PYTHON_FLINT_VERSION_NEEDED

_GMPY2_MIN_VERSION = '2.0.0'

def _get_flint(sympy_ground_types):
    if sympy_ground_types not in ('auto', 'flint'):
        return None
    
    try:
        import flint
        _flint_version = __version__
        import flint
    except ImportError:
        if sympy_ground_types == 'flint':
            warn('SYMPY_GROUND_TYPES was set to flint but python-flint is not installed. Falling back to other ground types.')
        return None

    if _flint_version_okay(_flint_version):
        return flint
    if None == 'auto':
        return None
    None(f'''Using python-flint {_flint_version} because SYMPY_GROUND_TYPES is set to flint but this version of SymPy is only tested with python-flint versions {_PYTHON_FLINT_VERSION_NEEDED}.''')
    return flint


def _get_gmpy2(sympy_ground_types):
    if sympy_ground_types not in ('auto', 'gmpy', 'gmpy2'):
        return None
    gmpy = None('gmpy2', min_module_version = _GMPY2_MIN_VERSION, module_version_attr = 'version', module_version_attr_call_args = ())
# WARNING: Decompyle incomplete

_SYMPY_GROUND_TYPES = os.environ.get('SYMPY_GROUND_TYPES', 'auto').lower()
_flint = None
_gmpy = None
# WARNING: Decompyle incomplete

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: polyconfig.pyc (Python 3.11)

'''Configuration utilities for polynomial manipulation algorithms. '''
from contextlib import contextmanager
_default_config = {
    'USE_COLLINS_RESULTANT': False,
    'USE_SIMPLIFY_GCD': True,
    'USE_HEU_GCD': True,
    'USE_IRREDUCIBLE_IN_FACTOR': False,
    'USE_CYCLOTOMIC_FACTOR': True,
    'EEZ_RESTART_IF_NEEDED': True,
    'EEZ_NUMBER_OF_CONFIGS': 3,
    'EEZ_NUMBER_OF_TRIES': 5,
    'EEZ_MODULUS_STEP': 2,
    'GF_IRRED_METHOD': 'rabin',
    'GF_FACTOR_METHOD': 'zassenhaus',
    'GROEBNER': 'buchberger' }
_current_config = { }
using = (lambda : pass# WARNING: Decompyle incomplete
)()

def setup(key, value = (None,)):
    '''Assign a value to (or reset) a configuration item. '''
    key = key.upper()
# WARNING: Decompyle incomplete


def query(key):
    '''Ask for a value of the given configuration item. '''
    return _current_config.get(key.upper(), None)


def configure():
    '''Initialized configuration of polys module. '''
    getenv = getenv
    import os
# WARNING: Decompyle incomplete

configure()

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: dfm.pyc (Python 3.11)

"""
sympy.polys.matrices.dfm

Provides the :class:`DFM` class if ``GROUND_TYPES=flint'``. Otherwise, ``DFM``
is a placeholder class that raises NotImplementedError when instantiated.
"""
from sympy.external.gmpy import GROUND_TYPES
if GROUND_TYPES == 'flint':
    from _dfm import DFM
    return None

class DFM_dummy:
    '''
        Placeholder class for DFM when python-flint is not installed.
        '''
    
    def __init__(*args, **kwargs):
        raise NotImplementedError('DFM requires GROUND_TYPES=flint.')

    _supports_domain = (lambda cls, domain: False)()
    _get_flint_func = (lambda cls, domain: raise NotImplementedError('DFM requires GROUND_TYPES=flint.'))()

DFM = DFM_dummy

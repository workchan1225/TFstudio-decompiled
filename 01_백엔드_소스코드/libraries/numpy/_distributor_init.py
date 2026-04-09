# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _distributor_init.pyc (Python 3.11)

''' Distributor init file

Distributors: you can add custom code here to support particular distributions
of numpy.

For example, this is a good place to put any BLAS/LAPACK initialization code.

The numpy standard source distribution will not put code in this file, so you
can safely replace this file with your own version.
'''

try:
    from  import _distributor_init_local
    return None
except ImportError:
    return None

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

import warnings
from numba.core.errors import NumbaPendingDeprecationWarning

try:
    import setuptools
except ImportError:
    msg = "The 'setuptools' package is required at runtime for pycc support."
    raise ImportError(msg)

from cc import CC
from decorators import export, exportmany
__pycc_deprecation_doc_url = 'https://numba.readthedocs.io/en/stable/reference/deprecation.html#deprecation-of-the-numba-pycc-module'
__pycc_pending_deprecation_message = f'''The \'pycc\' module is pending deprecation. Replacement technology is being developed.\n\nPending Deprecation in Numba 0.57.0. For more information please see: {__pycc_deprecation_doc_url}'''
_pend_dep = NumbaPendingDeprecationWarning(__pycc_pending_deprecation_message)
warnings.warn(_pend_dep, stacklevel = 2)

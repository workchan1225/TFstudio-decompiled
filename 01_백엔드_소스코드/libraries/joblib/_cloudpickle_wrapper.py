# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _cloudpickle_wrapper.pyc (Python 3.11)

__doc__ = "\nSmall shim of loky's cloudpickle_wrapper to avoid failure when\nmultiprocessing is not available.\n"
from _multiprocessing_helpers import mp

def _my_wrap_non_picklable_objects(obj, keep_wrapper = (True,)):
    return obj

# WARNING: Decompyle incomplete

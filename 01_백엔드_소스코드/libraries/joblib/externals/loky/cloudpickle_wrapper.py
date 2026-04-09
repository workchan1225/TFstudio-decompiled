# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: cloudpickle_wrapper.pyc (Python 3.11)

import inspect
from functools import partial
from joblib.externals.cloudpickle import dumps, loads
WRAP_CACHE = { }

class CloudpickledObjectWrapper:
    
    def __init__(self, obj, keep_wrapper = (False,)):
        self._obj = obj
        self._keep_wrapper = keep_wrapper

    
    def __reduce__(self):
        _pickled_object = dumps(self._obj)
        if not self._keep_wrapper:
            return (loads, (_pickled_object,))
        return (None, (_pickled_object, self._keep_wrapper))

    
    def __getattr__(self, attr):
        if attr not in ('_obj', '_keep_wrapper'):
            return getattr(self._obj, attr)
        return None(self, attr)



class CallableObjectWrapper(CloudpickledObjectWrapper):
    
    def __call__(self, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete



def _wrap_non_picklable_objects(obj, keep_wrapper):
    if callable(obj):
        return CallableObjectWrapper(obj, keep_wrapper = keep_wrapper)
    return None(obj, keep_wrapper = keep_wrapper)


def _reconstruct_wrapper(_pickled_object, keep_wrapper):
    obj = loads(_pickled_object)
    return _wrap_non_picklable_objects(obj, keep_wrapper)


def _wrap_objects_when_needed(obj):

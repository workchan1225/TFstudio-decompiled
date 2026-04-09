# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: py34compat.pyc (Python 3.11)

import importlib

try:
    import importlib.util as importlib
except ImportError:
    pass


try:
    module_from_spec = importlib.util.module_from_spec
    return None
except AttributeError:
    
    def module_from_spec(spec):
        return spec.loader.load_module(spec.name)

    return None

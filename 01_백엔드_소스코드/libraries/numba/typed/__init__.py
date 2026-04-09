# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

import importlib
_delayed_symbols = {
    'Dict': '.typeddict',
    'List': '.typedlist' }

def __getattr__(name):
    if name in _delayed_symbols:
        modpath = _delayed_symbols[name]
        mod = importlib.import_module(modpath, __name__)
        return getattr(mod, name)
    
    try:
        return importlib.import_module(f'''.{name}''', __name__)
    except ModuleNotFoundError:
        raise AttributeError

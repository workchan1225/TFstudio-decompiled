# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _imp_emulation.pyc (Python 3.11)


try:
    from imp import *
    return None
except ImportError:
    from _imp import acquire_lock, release_lock, is_builtin, is_frozen
    from importlib._bootstrap import _load
    from importlib import machinery
    import os
    import sys
    import tokenize
    SEARCH_ERROR = 0
    PY_SOURCE = 1
    PY_COMPILED = 2
    C_EXTENSION = 3
    PY_RESOURCE = 4
    PKG_DIRECTORY = 5
    C_BUILTIN = 6
    PY_FROZEN = 7
    PY_CODERESOURCE = 8
    IMP_HOOK = 9
    
    def get_suffixes():
        extensions = machinery.EXTENSION_SUFFIXES()
        source = machinery.SOURCE_SUFFIXES()
        bytecode = machinery.BYTECODE_SUFFIXES()
        return extensions + source + bytecode

    
    def find_module(name, path = (None,)):
        if not isinstance(name, str):
            raise TypeError("'name' must be a str, not {}".format(type(name)))
        if not isinstance(path, (type(None), list)):
            raise RuntimeError("'path' must be None or a list, not {}".format(type(path)))
    # WARNING: Decompyle incomplete

    
    def load_dynamic(name, path, file = (None,)):
        loader = machinery.ExtensionFileLoader(name, path)
        spec = machinery.ModuleSpec(name = name, loader = loader, origin = path)
        return _load(spec)

    return None

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

import sys
import importlib
from importlib.abc import MetaPathFinder, Loader
from  import _winerrors

try:
    import cffi
    del cffi
    _backend = 'cffi'
except ImportError:
    _backend = 'ctypes'


class BackendLoader(Loader):
    
    def __init__(self, redirect_module):
        self.redirect_module = redirect_module

    
    def create_module(self, spec):
        return importlib.import_module(self.redirect_module)

    
    def exec_module(self, module):
        pass



class BackendFinder(MetaPathFinder):
    
    def __init__(self, modules):
        self.redirected_modules = modules()

    
    def find_spec(self, fullname, path, target = (None,)):
        if fullname in self.redirected_modules:
            module_name = fullname.split('.')[-1]
            if _backend == 'ctypes':
                redirected = f'''win32ctypes.core.ctypes.{module_name}'''
            else:
                redirected = f'''win32ctypes.core.cffi.{module_name}'''
            loader = BackendLoader(redirected)
            return importlib.machinery.ModuleSpec(f'''win32ctypes.core.{module_name}''', loader)


sys.meta_path.append(BackendFinder([
    '_dll',
    '_authentication',
    '_time',
    '_common',
    '_resource',
    '_nl_support',
    '_system_information']))

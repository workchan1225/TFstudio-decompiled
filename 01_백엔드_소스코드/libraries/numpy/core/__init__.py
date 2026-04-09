# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''
Contains the core of NumPy: ndarray, ufuncs, dtypes, etc.

Please note that this module is private.  All functions and objects
are available in the main ``numpy`` namespace - use that instead.

'''
import os
import warnings
from numpy.version import version as __version__
env_added = []
for envkey in ('OPENBLAS_MAIN_FREE', 'GOTOBLAS_MAIN_FREE'):
    if envkey not in os.environ:
        os.environ[envkey] = '1'
        env_added.append(envkey)
    
    try:
        from  import multiarray
        
        try:
            pass
        except ImportError:
            exc = None
            import sys
            msg = '\n\nIMPORTANT: PLEASE READ THIS FOR ADVICE ON HOW TO SOLVE THIS ISSUE!\n\nImporting the numpy C-extensions failed. This error can happen for\nmany reasons, often due to issues with your setup or how NumPy was\ninstalled.\n\nWe have compiled some common reasons and troubleshooting tips at:\n\n    https://numpy.org/devdocs/user/troubleshooting-importerror.html\n\nPlease note and check the following:\n\n  * The Python version is: Python%d.%d from "%s"\n  * The NumPy version is: "%s"\n\nand make sure that they are the versions you expect.\nPlease carefully study the documentation linked above for further help.\n\nOriginal error was: %s\n' % (sys.version_info[0], sys.version_info[1], sys.executable, __version__, exc)
            raise ImportError(msg)
            exc = None
            del exc

        
        try:
            for envkey in env_added:
                del os.environ[envkey]
        except:
            for envkey in env_added:
                del os.environ[envkey]
                del envkey
                del env_added
                del os
                from  import umath
                if not hasattr(multiarray, '_multiarray_umath') or hasattr(umath, '_multiarray_umath'):
                    import sys
                    path = sys.modules['numpy'].__path__
                    msg = 'Something is wrong with the numpy installation. While importing we detected an older version of numpy in {}. One method of fixing this is to repeatedly uninstall numpy until none is found, then reinstall this version.'
                    raise ImportError(msg.format(path))
                from  import numerictypes as nt
                multiarray.set_typeDict(nt.sctypeDict)
                from  import numeric
                from numeric import *
                from  import fromnumeric
                from fromnumeric import *
                from  import defchararray as char
                from  import records
                from  import records as rec
                from records import record, recarray, format_parser
                from memmap import *
                from defchararray import chararray
                from  import function_base
                from function_base import *
                from  import _machar
                from  import getlimits
                from getlimits import *
                from  import shape_base
                from shape_base import *
                from  import einsumfunc
                from einsumfunc import *
                del nt
                from numeric import absolute as abs
                from  import _add_newdocs
                from  import _add_newdocs_scalars
                from  import _dtype_ctypes
                from  import _internal
                from  import _dtype
                from  import _methods
                __all__ = [
                    'char',
                    'rec',
                    'memmap']
                __all__ += numeric.__all__
                __all__ += [
                    'record',
                    'recarray',
                    'format_parser']
                __all__ += [
                    'chararray']
                __all__ += function_base.__all__
                __all__ += getlimits.__all__
                __all__ += shape_base.__all__
                __all__ += einsumfunc.__all__
                
                def _ufunc_reconstruct(module, name):
                    mod = __import__(module, fromlist = [
                        name])
                    return getattr(mod, name)

                
                def _ufunc_reduce(func):
                    return func.__name__

                
                def _DType_reconstruct(scalar_type):
                    return type(dtype(scalar_type))

                
                def _DType_reduce(DType):
                    if DType._legacy or DType.__module__ == 'numpy.dtypes':
                        return DType.__name__
                    scalar_type = None.type
                    return (_DType_reconstruct, (scalar_type,))

                
                def __getattr__(name):
                    if name == 'MachAr':
                        warnings.warn('The `np.core.MachAr` is considered private API (NumPy 1.24)', DeprecationWarning, stacklevel = 2)
                        return _machar.MachAr
                    raise None(f'''Module {__name__!r} has no attribute {name!r}''')

                import copyreg
                copyreg.pickle(ufunc, _ufunc_reduce)
                copyreg.pickle(type(dtype), _DType_reduce, _DType_reconstruct)
                del copyreg
                del _ufunc_reduce
                del _DType_reduce
                from numpy._pytesttester import PytestTester
                test = PytestTester(__name__)
                del PytestTester
                return None

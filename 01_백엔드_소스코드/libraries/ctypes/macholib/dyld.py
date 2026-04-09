# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: dyld.pyc (Python 3.11)

'''
dyld emulation
'''
import os
from ctypes.macholib.framework import framework_info
from ctypes.macholib.dylib import dylib_info
from itertools import *

try:
    from _ctypes import _dyld_shared_cache_contains_path
except ImportError:
    
    def _dyld_shared_cache_contains_path(*args):
        raise NotImplementedError


__all__ = [
    'dyld_find',
    'framework_find',
    'framework_info',
    'dylib_info']
DEFAULT_FRAMEWORK_FALLBACK = [
    os.path.expanduser('~/Library/Frameworks'),
    '/Library/Frameworks',
    '/Network/Library/Frameworks',
    '/System/Library/Frameworks']
DEFAULT_LIBRARY_FALLBACK = [
    os.path.expanduser('~/lib'),
    '/usr/local/lib',
    '/lib',
    '/usr/lib']

def dyld_env(env, var):
    pass
# WARNING: Decompyle incomplete


def dyld_image_suffix(env = (None,)):
    pass
# WARNING: Decompyle incomplete


def dyld_framework_path(env = (None,)):
    return dyld_env(env, 'DYLD_FRAMEWORK_PATH')


def dyld_library_path(env = (None,)):
    return dyld_env(env, 'DYLD_LIBRARY_PATH')


def dyld_fallback_framework_path(env = (None,)):
    return dyld_env(env, 'DYLD_FALLBACK_FRAMEWORK_PATH')


def dyld_fallback_library_path(env = (None,)):
    return dyld_env(env, 'DYLD_FALLBACK_LIBRARY_PATH')


def dyld_image_suffix_search(iterator, env = (None,)):
    '''For a potential path iterator, add DYLD_IMAGE_SUFFIX semantics'''
    suffix = dyld_image_suffix(env)
# WARNING: Decompyle incomplete


def dyld_override_search(name, env = (None,)):
    pass
# WARNING: Decompyle incomplete


def dyld_executable_path_search(name, executable_path = (None,)):
    pass
# WARNING: Decompyle incomplete


def dyld_default_search(name, env = (None,)):
    pass
# WARNING: Decompyle incomplete


def dyld_find(name, executable_path, env = (None, None)):
    '''
    Find a library or framework using dyld semantics
    '''
    for path in dyld_image_suffix_search(chain(dyld_override_search(name, env), dyld_executable_path_search(name, executable_path), dyld_default_search(name, env)), env):
        if os.path.isfile(path):
            
            return None, path
        if _dyld_shared_cache_contains_path(path):
            
            return None, path
        except NotImplementedError:
            continue
        raise ValueError(f'''dylib {name!s} could not be found''')


def framework_find(fn, executable_path, env = (None, None)):
    '''
    Find a framework using dyld semantics in a very loose manner.

    Will take input such as:
        Python
        Python.framework
        Python.framework/Versions/Current
    '''
    error = None
    
    try:
        return dyld_find(fn, executable_path = executable_path, env = env)
    except ValueError:
        e = None
        error = e
        e = None
        del e
    except:
        e = None
        del e

    fmwk_index = fn.rfind('.framework')
    if fmwk_index == -1:
        fmwk_index = len(fn)
        fn += '.framework'
    fn = os.path.join(fn, os.path.basename(fn[:fmwk_index]))
    
    try:
        error = None
        return dyld_find(fn, executable_path = executable_path, env = env)
    except ValueError:
        raise error
        
        try:
            pass
        except:
            error = None

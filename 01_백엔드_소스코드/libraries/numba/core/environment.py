# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: environment.pyc (Python 3.11)

import weakref
import importlib
from numba import _dynfunc

class Environment(_dynfunc.Environment):
    '''Stores globals and constant pyobjects for runtime.

    It is often needed to convert b/w nopython objects and pyobjects.
    '''
    __slots__ = ('env_name', '__weakref__')
    _memo = weakref.WeakValueDictionary()
    from_fndesc = (lambda cls, fndesc: try:
cls._memo[fndesc.env_name]except KeyError:
inst = cls(fndesc.lookup_globals())inst.env_name = fndesc.env_namecls._memo[fndesc.env_name] = inst)()
    
    def can_cache(self):
        is_dyn = '__name__' not in self.globals
        return not is_dyn

    
    def __reduce__(self):
        return (_rebuild_env, (self.globals.get('__name__'), self.consts, self.env_name))

    
    def __del__(self):
        pass

    
    def __repr__(self):
        return f'''<Environment {self.env_name!r} >'''



def _rebuild_env(modname, consts, env_name):
    env = lookup_environment(env_name)
# WARNING: Decompyle incomplete


def lookup_environment(env_name):
    '''Returns the Environment object for the given name;
    or None if not found
    '''
    return Environment._memo.get(env_name)

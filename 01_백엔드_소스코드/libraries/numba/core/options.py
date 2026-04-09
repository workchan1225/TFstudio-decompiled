# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: options.pyc (Python 3.11)

'''
Target Options
'''
import operator
from numba.core import config, utils
from numba.core.targetconfig import TargetConfig, Option

class TargetOptions:
    '''Target options maps user options from decorators to the
    ``numba.core.compiler.Flags`` used by lowering and target context.
    '''
    
    class Mapping:
        
        def __init__(self, flag_name, apply = ((lambda x: x),)):
            self.flag_name = flag_name
            self.apply = apply


    
    def finalize(self, flags, options):
        '''Subclasses can override this method to make target specific
        customizations of default flags.

        Parameters
        ----------
        flags : Flags
        options : dict
        '''
        pass

    parse_as_flags = (lambda cls, flags, options: opt = cls()opt._apply(flags, options)opt.finalize(flags, options)flags)()
    
    def _apply(self, flags, options):
        mappings = { }
        cls = type(self)
        for k in dir(cls):
            v = getattr(cls, k)
            if isinstance(v, cls.Mapping):
                mappings[k] = v
            used = set()
            for k, mapping in mappings.items():
                if k in options:
                    v = mapping.apply(options[k])
                    setattr(flags, mapping.flag_name, v)
                    used.add(k)
                unused = set(options) - used
                if unused:
                    m = f'''Unrecognized options: {unused}. Known options are {mappings.keys()}'''
                    raise KeyError(m)
                return None


_mapping = TargetOptions.Mapping

class DefaultOptions:
    '''Defines how user-level target options are mapped to the target flags.
    '''
    nopython = _mapping('enable_pyobject', operator.not_)
    forceobj = _mapping('force_pyobject')
    looplift = _mapping('enable_looplift')
    _nrt = _mapping('nrt')
    debug = _mapping('debuginfo')
    boundscheck = _mapping('boundscheck')
    nogil = _mapping('release_gil')
    writable_args = _mapping('writable_args')
    no_rewrites = _mapping('no_rewrites')
    no_cpython_wrapper = _mapping('no_cpython_wrapper')
    no_cfunc_wrapper = _mapping('no_cfunc_wrapper')
    parallel = _mapping('auto_parallel')
    fastmath = _mapping('fastmath')
    error_model = _mapping('error_model')
    inline = _mapping('inline')
    forceinline = _mapping('forceinline')
    _dbg_extend_lifetimes = _mapping('dbg_extend_lifetimes')
    _dbg_optnone = _mapping('dbg_optnone')


def include_default_options(*args):
    '''Returns a mixin class with a subset of the options

    Parameters
    ----------
    *args : str
        Option names to include.
    '''
    glbs = args()
    return type('OptionMixins', (), glbs)

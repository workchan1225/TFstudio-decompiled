# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: backend.pyc (Python 3.11)

import os
import sys
gmpy = None
sage = None
sage_utils = None
if sys.version_info[0] < 3:
    python3 = False
else:
    python3 = True
BACKEND = 'python'
if not python3:
    MPZ = long
    xrange = xrange
    basestring = basestring
    
    def exec_(_code_, _globs_, _locs_ = (None, None)):
        '''Execute code in a namespace.'''
        pass
    # WARNING: Decompyle incomplete

else:
    MPZ = int
    xrange = range
    basestring = str
    import builtins
    exec_ = getattr(builtins, 'exec')
if sys.version_info >= (3, 2):
    HASH_MODULUS = sys.hash_info.modulus
    if sys.hash_info.width == 32:
        HASH_BITS = 31
    else:
        HASH_BITS = 61
else:
    HASH_MODULUS = None
    HASH_BITS = None
if 'MPMATH_NOGMPY' not in os.environ:
    
    try:
        import gmpy2 as gmpy
        
        try:
            pass
        except ImportError:
            import gmpy
        except ImportError:
            raise ImportError
            
            try:
                pass
            try:
                if gmpy.version() >= '1.03':
                    BACKEND = 'gmpy'
                    MPZ = gmpy.mpz
                

            if 'MPMATH_NOSAGE' not in os.environ or 'SAGE_ROOT' in os.environ or 'MPMATH_SAGE' in os.environ:
                
                try:
                    import sage.all as sage
                    
                    
                    utils
                    sage.all = import sage.libs.mpmath.utils, libs, mpmath
                    sage_utils = _sage_utils
                    BACKEND = 'sage'
                    MPZ = sage.Integer
                except:
                    pass

                if 'MPMATH_STRICT' in os.environ:
                    STRICT = True
                else:
                    STRICT = False


MPZ_TYPE = type(MPZ(0))
MPZ_ZERO = MPZ(0)
MPZ_ONE = MPZ(1)
MPZ_TWO = MPZ(2)
MPZ_THREE = MPZ(3)
MPZ_FIVE = MPZ(5)

try:
    if BACKEND == 'python':
        int_types = (int, long)
        return None
    int_types = (None, long, MPZ_TYPE)
    return None
except NameError:
    if BACKEND == 'python':
        int_types = (int,)
        return None
    int_types = (None, MPZ_TYPE)
    return None

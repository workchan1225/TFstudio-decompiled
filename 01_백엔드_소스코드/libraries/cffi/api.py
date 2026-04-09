# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: api.pyc (Python 3.11)

import sys
import types
from lock import allocate_lock
from error import CDefError
from  import model

try:
    callable
except NameError:
    from collections import Callable
    
    callable = lambda x: isinstance(x, Callable)


try:
    basestring
except NameError:
    basestring = str

_unspecified = object()

class FFI(object):
    '''
    The main top-level class that you instantiate once, or once per module.

    Example usage:

        ffi = FFI()
        ffi.cdef("""
            int printf(const char *, ...);
        """)

        C = ffi.dlopen(None)   # standard library
        -or-
        C = ffi.verify()  # use a C compiler: verify the decl above is right

        C.printf("hello, %s!\\n", ffi.new("char[]", "world"))
    '''
    
    def __init__(self, backend = (None,)):
        """Create an FFI instance.  The 'backend' argument is used to
        select a non-default backend, mostly for tests.
        """
        pass
    # WARNING: Decompyle incomplete

    
    def cdef(self, csource, override, packed, pack = (False, False, None)):
        """Parse the given C source.  This registers all declared functions,
        types, and global variables.  The functions and global variables can
        then be accessed via either 'ffi.dlopen()' or 'ffi.verify()'.
        The types can be used in 'ffi.new()' and other functions.
        If 'packed' is specified as True, all structs declared inside this
        cdef are packed, i.e. laid out without any field alignment at all.
        Alternatively, 'pack' can be a small integer, and requests for
        alignment greater than that are ignored (pack=1 is equivalent to
        packed=True).
        """
        self._cdef(csource, override = override, packed = packed, pack = pack)

    
    def embedding_api(self, csource, packed, pack = (False, None)):
        self._cdef(csource, packed = packed, pack = pack, dllexport = True)
    # WARNING: Decompyle incomplete

    
    def _cdef(self, csource, override = (False,), **options):
        if not isinstance(csource, str):
            if not isinstance(csource, basestring):
                raise TypeError('cdef() argument must be a string')
            csource = csource.encode('ascii')
        self._lock
        self._cdef_version = object()
    # WARNING: Decompyle incomplete

    
    def dlopen(self, name, flags = (0,)):
        """Load and return a dynamic library identified by 'name'.
        The standard C library can be loaded by passing None.
        Note that functions and types declared by 'ffi.cdef()' are not
        linked to a particular library, just like C headers; in the
        library we only look for the actual (untyped) symbols.
        """
        pass
    # WARNING: Decompyle incomplete

    
    def dlclose(self, lib):
        '''Close a library obtained with ffi.dlopen().  After this call,
        access to functions or variables from the library will fail
        (possibly with a segmentation fault).
        '''
        type(lib).__cffi_close__(lib)

    
    def _typeof_locked(self, cdecl):
        key = cdecl
        if key in self._parsed_types:
            return self._parsed_types[key]
        if not None(cdecl, str):
            cdecl = cdecl.encode('ascii')
        type = self._parser.parse_type(cdecl)
        really_a_function_type = type.is_raw_function
        if really_a_function_type:
            type = type.as_function_pointer()
        btype = self._get_cached_btype(type)
        result = (btype, really_a_function_type)
        self._parsed_types[key] = result
        return result

    
    def _typeof(self, cdecl, consider_function_as_funcptr = (False,)):

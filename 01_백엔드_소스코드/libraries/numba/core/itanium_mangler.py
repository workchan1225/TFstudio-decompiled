# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: itanium_mangler.pyc (Python 3.11)

__doc__ = '\nItanium CXX ABI Mangler\n\nReference: https://itanium-cxx-abi.github.io/cxx-abi/abi.html\n\nThe basics of the mangling scheme.\n\nWe are hijacking the CXX mangling scheme for our use.  We map Python modules\ninto CXX namespace.  A `module1.submodule2.foo` is mapped to\n`module1::submodule2::foo`.   For parameterized numba types, we treat them as\ntemplated types; for example, `array(int64, 1d, C)` becomes an\n`array<int64, 1, C>`.\n\nAll mangled names are prefixed with "_Z".  It is followed by the name of the\nentity.  A name contains one or more identifiers.  Each identifier is encoded\nas "<num of char><name>".   If the name is namespaced and, therefore,\nhas multiple identifiers, the entire name is encoded as "N<name>E".\n\nFor functions, arguments types follow.  There are condensed encodings for basic\nbuilt-in types; e.g. "i" for int, "f" for float.  For other types, the\npreviously mentioned name encoding should be used.\n\nFor templated types, the template parameters are encoded immediately after the\nname.  If it is namespaced, it should be within the \'N\' \'E\' marker.  Template\nparameters are encoded in "I<params>E", where each parameter is encoded using\nthe mentioned name encoding scheme.  Template parameters can contain literal\nvalues like the \'1\' in the array type shown earlier.  There is special encoding\nscheme for them to avoid leading digits.\n'
import re
from numba.core import types, config
_re_invalid_char = re.compile('[^a-z0-9_]', re.I)
PREFIX = '_Z'
if config.USE_LEGACY_TYPE_SYSTEM:
    N2CODE = {
        types.float64: 'd',
        types.float32: 'f',
        types.float16: 'Dh',
        types.int64: 'x',
        types.uint64: 'y',
        types.int32: 'i',
        types.uint32: 'j',
        types.int16: 's',
        types.uint16: 't',
        types.int8: 'a',
        types.uint8: 'h',
        types.boolean: 'b',
        types.void: 'v' }
# WARNING: Decompyle incomplete

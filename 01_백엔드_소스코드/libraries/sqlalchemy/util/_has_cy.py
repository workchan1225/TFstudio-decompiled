# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _has_cy.pyc (Python 3.11)

import os
import typing

def _CYEXTENSION_MSG: str():
    collections = collections
    import cyextension
    immutabledict = immutabledict
    import cyextension
    processors = processors
    import cyextension
    resultproxy = resultproxy
    import cyextension
    util = util
    import cyextension
    return (collections, immutabledict, processors, resultproxy, util)

if not typing.TYPE_CHECKING:
    if os.environ.get('DISABLE_SQLALCHEMY_CEXT_RUNTIME'):
        HAS_CYEXTENSION = False
        _CYEXTENSION_MSG = 'DISABLE_SQLALCHEMY_CEXT_RUNTIME is set'
        return None
    
    try:
        _import_cy_extensions()
        _CYEXTENSION_MSG = 'Loaded'
        HAS_CYEXTENSION = True
        return None
    except ImportError:
        err = None
        HAS_CYEXTENSION = False
        _CYEXTENSION_MSG = str(err)
        err = None
        del err
        return None
        err = None
        del err
        HAS_CYEXTENSION = False
        return None

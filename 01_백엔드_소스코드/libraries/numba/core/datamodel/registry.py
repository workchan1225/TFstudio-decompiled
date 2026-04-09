# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: registry.pyc (Python 3.11)

import functools
from manager import DataModelManager

def register(dmm, typecls):
    '''Used as decorator to simplify datamodel registration.
    Returns the object being decorated so that chaining is possible.
    '''
    pass
# WARNING: Decompyle incomplete

default_manager = DataModelManager()
register_default = functools.partial(register, default_manager)

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from engine.interfaces import Dialect

class Connector(Dialect):
    '''Base class for dialect mixins, for DBAPIs that work
    across entirely different database backends.

    Currently the only such mixin is pyodbc.

    '''
    pass

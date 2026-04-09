# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: manager.pyc (Python 3.11)

import weakref
from collections import ChainMap
from numba.core import types

class DataModelManager(object):
    '''Manages mapping of FE types to their corresponding data model
    '''
    
    def __init__(self, handlers = (None,)):

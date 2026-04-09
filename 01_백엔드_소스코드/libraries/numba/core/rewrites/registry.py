# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: registry.pyc (Python 3.11)

from collections import defaultdict
from numba.core import config

class Rewrite(object):
    '''Defines the abstract base class for Numba rewrites.
    '''
    
    def __init__(self, state = (None,)):
        '''Constructor for the Rewrite class.
        '''
        pass

    
    def match(self, func_ir, block, typemap, calltypes):
        '''Overload this method to check an IR block for matching terms in the
        rewrite.
        '''
        return False

    
    def apply(self):
        '''Overload this method to return a rewritten IR basic block when a
        match has been found.
        '''
        raise NotImplementedError('Abstract Rewrite.apply() called!')



class RewriteRegistry(object):
    '''Defines a registry for Numba rewrites.
    '''
    _kinds = frozenset([
        'before-inference',
        'after-inference'])
    
    def __init__(self):
        '''Constructor for the rewrite registry.  Initializes the rewrites
        member to an empty list.
        '''
        self.rewrites = defaultdict(list)

    
    def register(self, kind):
        '''
        Decorator adding a subclass of Rewrite to the registry for
        the given *kind*.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def apply(self, kind, state):
        '''Given a pipeline and a dictionary of basic blocks, exhaustively
        attempt to apply all registered rewrites to all basic blocks.
        '''
        pass
    # WARNING: Decompyle incomplete


rewrite_registry = RewriteRegistry()
register_rewrite = rewrite_registry.register

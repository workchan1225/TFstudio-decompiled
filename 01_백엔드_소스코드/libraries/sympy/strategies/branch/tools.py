# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tools.pyc (Python 3.11)

from core import exhaust, multiplex
from traverse import top_down

def canon(*rules):
    ''' Strategy for canonicalization

    Apply each branching rule in a top-down fashion through the tree.
    Multiplex through all branching rule traversals
    Keep doing this until there is no change.
    '''
    pass
# WARNING: Decompyle incomplete

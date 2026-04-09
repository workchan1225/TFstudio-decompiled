# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: controlflow.pyc (Python 3.11)

import collections
import functools
import sys
from numba.core.ir import Loc
from numba.core.errors import UnsupportedError
from numba.core.utils import PYVERSION
if PYVERSION in ((3, 14),):
    NEW_BLOCKERS = frozenset([
        'SETUP_LOOP',
        'FOR_ITER',
        'SETUP_WITH',
        'BEFORE_WITH',
        'LOAD_SPECIAL'])
elif PYVERSION in ((3, 10), (3, 11), (3, 12), (3, 13)):
    NEW_BLOCKERS = frozenset([
        'SETUP_LOOP',
        'FOR_ITER',
        'SETUP_WITH',
        'BEFORE_WITH'])
else:
    raise NotImplementedError(PYVERSION)

class CFBlock(object):
    
    def __init__(self, offset):
        self.offset = offset
        self.body = []
        self.outgoing_jumps = { }
        self.incoming_jumps = { }
        self.terminating = False

    
    def __repr__(self):
        args = (self.offset, sorted(self.outgoing_jumps), sorted(self.incoming_jumps))
        return 'block(offset:%d, outgoing: %s, incoming: %s)' % args

    
    def __iter__(self):
        return iter(self.body)



def Loop():
    '''Loop'''
    __doc__ = '\n    A control flow loop, as detected by a CFGraph object.\n    '
    __slots__ = ()
    
    def __eq__(self, other):

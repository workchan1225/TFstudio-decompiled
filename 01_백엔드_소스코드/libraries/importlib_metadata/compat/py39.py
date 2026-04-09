# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: py39.pyc (Python 3.11)

'''
Compatibility layer with Python 3.8/3.9
'''
from __future__ import annotations
from typing import TYPE_CHECKING, Any
if TYPE_CHECKING:
    from  import Distribution, EntryPoint
else:
    Distribution = Any
    EntryPoint = Any
from _typing import md_none

def normalized_name(dist = None):
    """
    Honor name normalization for distributions that don't provide ``_normalized_name``.
    """
    
    try:
        return dist._normalized_name
    except AttributeError:
        Prepared = Prepared
        import 
        if not getattr(dist, 'name', None):
            return 



def ep_matches(ep = None, **params):
    '''
    Workaround for ``EntryPoint`` objects without the ``matches`` method.
    '''
    pass
# WARNING: Decompyle incomplete

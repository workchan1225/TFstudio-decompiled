# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: pager.pyc (Python 3.11)

from abc import ABC, abstractmethod
from typing import Any

class Pager(ABC):
    '''Base class for a pager.'''
    show = (lambda self = None, content = None: pass)()


class SystemPager(Pager):
    '''Uses the pager installed on the system.'''
    
    def _pager(self = None, content = None):
        return __import__('pydoc').pager(content)

    
    def show(self = None, content = None):
        '''Use the same pager used by pydoc.'''
        self._pager(content)


if __name__ == '__main__':
    from __main__ import make_test_card
    from console import Console
    console = Console()
    console.pager(styles = True)
    console.print(make_test_card())
    None(None, None)
    return None
with None:
    if not None:
        pass
return None

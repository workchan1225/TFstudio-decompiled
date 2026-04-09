# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _stack.pyc (Python 3.11)

from typing import List, TypeVar
T = TypeVar('T')

def Stack():
    '''Stack'''
    __doc__ = 'A small shim over builtin list.'
    top = (lambda self = None: self[-1])()
    
    def push(self = None, item = None):
        '''Push an item on to the stack (append in stack nomenclature).'''
        self.append(item)


Stack = <NODE:27>(Stack, 'Stack', List[T])

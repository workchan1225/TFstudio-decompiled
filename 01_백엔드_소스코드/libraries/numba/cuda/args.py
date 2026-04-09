# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: args.pyc (Python 3.11)

'''
Hints to wrap Kernel arguments to indicate how to manage host-device
memory transfers before & after the kernel call.
'''
import abc
from numba.core.typing.typeof import typeof, Purpose

def ArgHint():
    '''ArgHint'''
    
    def __init__(self, value):
        self.value = value

    to_device = (lambda self, retr, stream = (0,): pass)()
    _numba_type_ = (lambda self: typeof(self.value, Purpose.argument))()

ArgHint = <NODE:27>(ArgHint, 'ArgHint', metaclass = abc.ABCMeta)

class In(ArgHint):
    
    def to_device(self, retr, stream = (0,)):
        pass
    # WARNING: Decompyle incomplete



class Out(ArgHint):
    
    def to_device(self, retr, stream = (0,)):
        pass
    # WARNING: Decompyle incomplete



class InOut(ArgHint):
    
    def to_device(self, retr, stream = (0,)):
        pass
    # WARNING: Decompyle incomplete



def wrap_arg(value, default = (InOut,)):
    return value if isinstance(value, ArgHint) else default(value)

__all__ = [
    'In',
    'Out',
    'InOut',
    'ArgHint',
    'wrap_arg']

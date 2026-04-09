# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: stream.pyc (Python 3.11)

'''Interfaces related to streams of values or objects.'''
import abc

class Consumer(abc.ABC):
    '''Interface for consumers of finite streams of values or objects.'''
    consume = (lambda self, value: raise NotImplementedError())()
    terminate = (lambda self: raise NotImplementedError())()
    consume_and_terminate = (lambda self, value: raise NotImplementedError())()

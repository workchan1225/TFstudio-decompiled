# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: descriptors.pyc (Python 3.11)

'''
Target Descriptors
'''
from abc import ABCMeta, abstractmethod

def TargetDescriptor():
    '''TargetDescriptor'''
    
    def __init__(self, target_name):
        self._target_name = target_name

    typing_context = (lambda self: pass)()()
    target_context = (lambda self: pass)()()

TargetDescriptor = <NODE:27>(TargetDescriptor, 'TargetDescriptor', metaclass = ABCMeta)

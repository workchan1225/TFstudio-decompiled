# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: abandonment.pyc (Python 3.11)

'''Utilities for indicating abandonment of computation.'''

class Abandoned(Exception):
    '''Indicates that some computation is being abandoned.

    Abandoning a computation is different than returning a value or raising
    an exception indicating some operational or programming defect.
    '''
    pass

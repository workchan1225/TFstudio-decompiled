# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: process.pyc (Python 3.11)

import sys
from multiprocessing.context import assert_spawning
from multiprocessing.process import BaseProcess

class LokyProcess(BaseProcess):
    pass
# WARNING: Decompyle incomplete


class LokyInitMainProcess(LokyProcess):
    pass
# WARNING: Decompyle incomplete


class AuthenticationKey(bytes):
    
    def __reduce__(self):
        
        try:
            assert_spawning(self)
        except RuntimeError:
            raise TypeError('Pickling an AuthenticationKey object is disallowed for security reasons')

        return (AuthenticationKey, (bytes(self),))

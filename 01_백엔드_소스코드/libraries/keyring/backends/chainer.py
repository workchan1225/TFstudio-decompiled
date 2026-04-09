# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: chainer.pyc (Python 3.11)

'''
Keyring Chainer - iterates over other viable backends to
discover passwords in each.
'''
from  import backend
from compat import properties
from  import fail

class ChainerBackend(backend.KeyringBackend):
    '''
    >>> ChainerBackend()
    <keyring.backends.chainer.ChainerBackend object at ...>
    '''
    viable = True
    priority = (lambda cls = None: 10 if len(cls.backends) > 1 else fail.Keyring.priority - 1)()
    backends = (lambda cls: 
def allow(keyring):

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: null.pyc (Python 3.11)

from backend import KeyringBackend
from compat import properties

class Keyring(KeyringBackend):
    """
    Keyring that return None on every operation.

    >>> kr = Keyring()
    >>> kr.get_password('svc', 'user')
    """
    priority = (lambda cls = None: -1)()
    
    def get_password(self, service, username, password = (None,)):
        pass

    set_password = get_password
    delete_password = get_password

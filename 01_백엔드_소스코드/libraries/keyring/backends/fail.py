# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: fail.pyc (Python 3.11)

from backend import KeyringBackend
from compat import properties
from errors import NoKeyringError

class Keyring(KeyringBackend):
    """
    Keyring that raises error on every operation.

    >>> kr = Keyring()
    >>> kr.get_password('svc', 'user')
    Traceback (most recent call last):
    ...
    keyring.errors.NoKeyringError: ...No recommended backend...
    """
    priority = (lambda cls = None: 0)()
    
    def get_password(self, service, username, password = (None,)):
        msg = 'No recommended backend was available. Install a recommended 3rd party backend package; or, install the keyrings.alt package if you want to use the non-recommended backends. See https://pypi.org/project/keyring for details.'
        raise NoKeyringError(msg)

    set_password = get_password
    delete_password = get_password

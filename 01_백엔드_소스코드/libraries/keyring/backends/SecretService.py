# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: SecretService.pyc (Python 3.11)

import logging
from contextlib import closing
from jaraco.context import ExceptionTrap
from  import backend
from backend import KeyringBackend
from compat import properties
from credentials import SimpleCredential
from errors import InitError, KeyringLocked, PasswordDeleteError

try:
    import secretstorage
    from secretstorage.exceptions import exceptions
except ImportError:
    pass
except AttributeError:
    pass

log = logging.getLogger(__name__)

class Keyring(KeyringBackend, backend.SchemeSelectable):
    '''Secret Service Keyring'''
    appid = 'Python keyring library'
    priority = (lambda cls = None:

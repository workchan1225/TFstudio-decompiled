# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

import functools
import os
import platform
import warnings
from backend import KeyringBackend
from compat import properties
from errors import KeyringError, KeyringLocked, PasswordDeleteError, PasswordSetError

try:
    from  import api
except Exception:
    pass


def warn_keychain(func):
    pass
# WARNING: Decompyle incomplete


class Keyring(KeyringBackend):
    '''macOS Keychain'''
    keychain = os.environ.get('KEYCHAIN_PATH')
    priority = (lambda cls: if platform.system() != 'Darwin':
raise RuntimeError('macOS required')if 'api' not in globals():
raise RuntimeError('Security API unavailable')5)()
    set_password = (lambda self, service, username, password: pass# WARNING: Decompyle incomplete
)()
    get_password = (lambda self, service, username: pass# WARNING: Decompyle incomplete
)()
    delete_password = (lambda self, service, username: pass# WARNING: Decompyle incomplete
)()
    
    def with_keychain(self, keychain):
        warnings.warn('macOS.Keyring.with_keychain is deprecated. Use with_properties instead.', DeprecationWarning, stacklevel = 2)
        return self.with_properties(keychain = keychain)

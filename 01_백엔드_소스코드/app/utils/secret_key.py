# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: secret_key.pyc (Python 3.11)

'''
Installation-specific secret key management.

Generates a unique secret key per installation and persists it
in the data directory. This ensures each installed copy has its
own encryption key instead of sharing a hardcoded default.
'''
import hashlib
import base64
import secrets
import logging
from pathlib import Path
logger = logging.getLogger(__name__)
_cached_secret_key: str | None = None

def _get_secret_key_path():
    '''Get the path for the persistent secret key file.'''
    get_data_path = get_data_path
    import app.config.paths
    return get_data_path() / 'secret.key'


def get_secret_key():
    '''
    Get or create an installation-specific secret key.

    On first call, generates a random 64-char hex key and saves it.
    Subsequent calls return the cached/persisted key.
    '''
    pass
# WARNING: Decompyle incomplete


def get_encryption_key():
    '''
    Derive a Fernet-compatible encryption key from the secret key.

    Returns a base64url-encoded 32-byte key suitable for cryptography.fernet.Fernet.
    '''
    secret_key = get_secret_key()
    key_hash = hashlib.sha256(secret_key.encode()).digest()
    return base64.urlsafe_b64encode(key_hash)

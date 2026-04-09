# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: core.pyc (Python 3.11)

'''
Core API functions and initialization routines.
'''
from __future__ import annotations
import configparser
import logging
import os
import sys
import typing
from  import backend, credentials
from backends import fail
from util import platform_ as platform
LimitCallable = typing.Callable[([
    backend.KeyringBackend], bool)]
log = logging.getLogger(__name__)
_keyring_backend = None

def set_keyring(keyring = None):
    '''Set current keyring backend.'''
    global _keyring_backend
    if not isinstance(keyring, backend.KeyringBackend):
        raise TypeError('The keyring must be an instance of KeyringBackend')
    _keyring_backend = keyring


def get_keyring():
    '''Get current keyring backend.'''
    pass
# WARNING: Decompyle incomplete


def disable():
    """
    Configure the null keyring as the default.

    >>> fs = getfixture('fs')
    >>> disable()
    >>> disable()
    Traceback (most recent call last):
    ...
    RuntimeError: Refusing to overwrite...
    """
    root = platform.config_root()
    
    try:
        os.makedirs(root)
    except OSError:
        pass

    filename = os.path.join(root, 'keyringrc.cfg')
    if os.path.exists(filename):
        msg = f'''Refusing to overwrite {filename}'''
        raise RuntimeError(msg)
    file = open(filename, 'w', encoding = 'utf-8')
    file.write('[backend]\ndefault-keyring=keyring.backends.null.Keyring')
    None(None, None)
    return None
    with None:
        if not None:
            pass


def get_password(service_name = None, username = None):
    '''Get password from the specified service.'''
    return get_keyring().get_password(service_name, username)


def set_password(service_name = None, username = None, password = None):
    '''Set password for the user in the specified service.'''
    get_keyring().set_password(service_name, username, password)


def delete_password(service_name = None, username = None):
    '''Delete the password for the user in the specified service.'''
    get_keyring().delete_password(service_name, username)


def get_credential(service_name = None, username = None):
    '''Get a Credential for the specified service.'''
    return get_keyring().get_credential(service_name, username)


def recommended(backend = None):
    return backend.priority >= 1


def init_backend(limit = None):
    '''
    Load a detected backend.
    '''
    set_keyring(_detect_backend(limit))


def _detect_backend(limit = None):
    '''
    Return a keyring specified in the config file or infer the best available.

    Limit, if supplied, should be a callable taking a backend and returning
    True if that backend should be included for consideration.
    '''
    backend._limit = limit
    if not load_env():
        if not load_config():
            pass
    return max(filter(limit, backend.get_all_keyring()), default = fail.Keyring(), key = backend.by_priority)


def _load_keyring_class(keyring_name = None):
    """
    Load the keyring class indicated by name.

    These popular names are tested to ensure their presence.

    >>> popular_names = [
    ...      'keyring.backends.Windows.WinVaultKeyring',
    ...      'keyring.backends.macOS.Keyring',
    ...      'keyring.backends.kwallet.DBusKeyring',
    ...      'keyring.backends.SecretService.Keyring',
    ...  ]
    >>> list(map(_load_keyring_class, popular_names))
    [...]
    """
    (module_name, sep, class_name) = keyring_name.rpartition('.')
    __import__(module_name)
    module = sys.modules[module_name]
    return getattr(module, class_name)


def load_keyring(keyring_name = None):
    """
    Load the specified keyring by name (a fully-qualified name to the
    keyring, such as 'keyring.backends.file.PlaintextKeyring')
    """
    class_ = _load_keyring_class(keyring_name)
    class_.priority
    return class_()


def load_env():
    '''Load a keyring configured in the environment variable.'''
    
    try:
        return load_keyring(os.environ['PYTHON_KEYRING_BACKEND'])
    except KeyError:
        return None



def _config_path():
    return platform.config_root() / 'keyringrc.cfg'


def _ensure_path(path):
    if not path.exists():
        raise FileNotFoundError(path)
    return path


def load_config():
    '''Load a keyring using the config file in the config root.'''
    config = configparser.RawConfigParser()
    
    try:
        config.read(_ensure_path(_config_path()), encoding = 'utf-8')
    except FileNotFoundError:
        return None

    _load_keyring_path(config)
    
    try:
        if config.has_section('backend'):
            keyring_name = config.get('backend', 'default-keyring').strip()
        else:
            return None
    except (configparser.NoOptionError, ImportError):
        logger = logging.getLogger('keyring')
        logger.warning('Keyring config file contains incorrect values.\n' + f'''Config file: {_config_path()}''')
        return None
        return load_keyring(keyring_name)



def _load_keyring_path(config = None):
    '''load the keyring-path option (if present)'''
    
    try:
        path = config.get('backend', 'keyring-path').strip()
        sys.path.insert(0, os.path.expanduser(path))
        return None
    except (configparser.NoOptionError, configparser.NoSectionError):
        return None

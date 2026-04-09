# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: universe.pyc (Python 3.11)

'''Helpers for universe domain.'''
from typing import Any, Optional
DEFAULT_UNIVERSE = 'googleapis.com'

class EmptyUniverseError(ValueError):
    pass
# WARNING: Decompyle incomplete


class UniverseMismatchError(ValueError):
    pass
# WARNING: Decompyle incomplete


def determine_domain(client_universe_domain = None, universe_domain_env = None):
    '''Return the universe domain used by the client.

    Args:
        client_universe_domain (Optional[str]): The universe domain configured via the client options.
        universe_domain_env (Optional[str]): The universe domain configured via the
        "GOOGLE_CLOUD_UNIVERSE_DOMAIN" environment variable.

    Returns:
        str: The universe domain to be used by the client.

    Raises:
        ValueError: If the universe domain is an empty string.
    '''
    universe_domain = DEFAULT_UNIVERSE
# WARNING: Decompyle incomplete


def compare_domains(client_universe = None, credentials = None):
    '''Returns True iff the universe domains used by the client and credentials match.

    Args:
        client_universe (str): The universe domain configured via the client options.
        credentials Any: The credentials being used in the client.

    Returns:
        bool: True iff client_universe matches the universe in credentials.

    Raises:
        ValueError: when client_universe does not match the universe in credentials.
    '''
    credentials_universe = getattr(credentials, 'universe_domain', DEFAULT_UNIVERSE)
    if client_universe != credentials_universe:
        raise UniverseMismatchError(client_universe, credentials_universe)
    return True

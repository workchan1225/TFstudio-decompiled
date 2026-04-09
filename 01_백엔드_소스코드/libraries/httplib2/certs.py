# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: certs.pyc (Python 3.11)

'''Utilities for certificate management.'''
import os
certifi_available = False
certifi_where = None

try:
    from certifi import where as certifi_where
    certifi_available = True
except ImportError:
    pass

custom_ca_locater_available = False
custom_ca_locater_where = None

try:
    from ca_certs_locater import get as custom_ca_locater_where
    custom_ca_locater_available = True
except ImportError:
    pass

BUILTIN_CA_CERTS = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cacerts.txt')

def where():
    env = os.environ.get('HTTPLIB2_CA_CERTS')
# WARNING: Decompyle incomplete

if __name__ == '__main__':
    print(where())
    return None

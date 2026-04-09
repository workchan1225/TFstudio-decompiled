# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _ssl.pyc (Python 3.11)

import ssl
import certifi

def default_ssl_context():
    context = ssl.create_default_context()
    context.load_verify_locations(certifi.where())
    return context

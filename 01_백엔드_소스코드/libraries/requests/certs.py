# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: certs.pyc (Python 3.11)

'''
requests.certs
~~~~~~~~~~~~~~

This module returns the preferred default CA certificate bundle. There is
only one — the one from the certifi package.

If you are packaging Requests, e.g., for a Linux distribution or a managed
environment, you can change the definition of where() to return a separately
packaged CA bundle.
'''
from certifi import where
if __name__ == '__main__':
    print(where())
    return None

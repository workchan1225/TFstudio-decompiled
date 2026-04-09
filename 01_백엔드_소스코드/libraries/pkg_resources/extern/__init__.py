# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

import importlib.util as importlib
import sys

class VendorImporter:
    '''
    A PEP 302 meta path importer for finding optionally-vendored
    or otherwise naturally-installed packages from root_name.
    '''
    
    def __init__(self, root_name, vendored_names, vendor_pkg = ((), None)):

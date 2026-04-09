# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''
    proxy_tools.py
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Proxy. Extracted from Werkzeug

    :copyright: (c) 2013 by Armin Ronacher (adapted by Jonathan Tushman 2014).
    :license: BSD, see LICENSE for more details.
'''
import sys
PY2 = sys.version_info[0] == 2

_identity = lambda x: x
if PY2:
    
    def implements_bool(cls):
        cls.__nonzero__ = cls.__bool__
        del cls.__bool__
        return cls

else:
    implements_bool = _identity
Proxy = <NODE:12>()
module_property = Proxy
proxy = Proxy

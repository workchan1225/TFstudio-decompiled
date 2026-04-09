# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from __future__ import annotations
import urllib3.connection as urllib3
from connectionpool import HTTPConnectionPool, HTTPSConnectionPool
from connection import EmscriptenHTTPConnection, EmscriptenHTTPSConnection

def inject_into_urllib3():
    HTTPConnectionPool.ConnectionCls = EmscriptenHTTPConnection
    HTTPSConnectionPool.ConnectionCls = EmscriptenHTTPSConnection
    urllib3.connection.HTTPConnection = EmscriptenHTTPConnection
    urllib3.connection.HTTPSConnection = EmscriptenHTTPSConnection
    urllib3.connection.VerifiedHTTPSConnection = EmscriptenHTTPSConnection

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _httpx.pyc (Python 3.11)

"""
This file includes code adapted from HTTPX's utility module
(https://github.com/encode/httpx/blob/336204f0121a9aefdebac5cacd81f912bafe8057/httpx/_utils.py).
We implement custom proxy handling to support configurations like `socket_options`,
which are not currently configurable through the HTTPX client.
For more context, see: https://github.com/encode/httpx/discussions/3514
"""
from __future__ import annotations
import ipaddress
from typing import Mapping
from urllib.request import getproxies

def is_ipv4_hostname(hostname = None):
    
    try:
        ipaddress.IPv4Address(hostname.split('/')[0])
    except Exception:
        return False

    return True


def is_ipv6_hostname(hostname = None):
    
    try:
        ipaddress.IPv6Address(hostname.split('/')[0])
    except Exception:
        return False

    return True


def get_environment_proxies():
    '''
    Gets the proxy mappings based on environment variables.
    We use our own logic to parse these variables, as HTTPX
    doesn’t allow full configuration of the underlying
    transport when proxies are set via environment variables.
    '''
    proxy_info = getproxies()
    mounts = { }
    for scheme in ('http', 'https', 'all'):
        if proxy_info.get(scheme):
            hostname = proxy_info[scheme]
            mounts[f'''{scheme}://'''] = hostname if '://' in hostname else f'''http://{hostname}'''
        no_proxy_hosts = proxy_info.get('no', '').split(',')()
        for hostname in no_proxy_hosts:
            if hostname == '*':
                
                return (lambda .0: [ host.strip() for host in .0 ]), { }
            if (lambda .0: [ host.strip() for host in .0 ]):
                if '://' in hostname:
                    continue
                if is_ipv4_hostname(hostname):
                    None = None
                    continue
                if is_ipv6_hostname(hostname):
                    mounts[f'''all://[{hostname}]'''] = None
                    continue
                if hostname.lower() == 'localhost':
                    mounts[f'''all://{hostname}'''] = None
                    continue
                mounts[f'''all://*{hostname}'''] = None
            return mounts

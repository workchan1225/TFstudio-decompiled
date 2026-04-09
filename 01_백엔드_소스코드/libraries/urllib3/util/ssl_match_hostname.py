# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ssl_match_hostname.pyc (Python 3.11)

'''The match_hostname() function from Python 3.5, essential when using SSL.'''
from __future__ import annotations
import ipaddress
import re
import typing
from ipaddress import IPv4Address, IPv6Address
if typing.TYPE_CHECKING:
    from ssl_ import _TYPE_PEER_CERT_RET_DICT
__version__ = '3.5.0.1'

class CertificateError(ValueError):
    pass


def _dnsname_match(dn = None, hostname = None, max_wildcards = None):
    '''Matching according to RFC 6125, section 6.4.3

    http://tools.ietf.org/html/rfc6125#section-6.4.3
    '''
    pats = []
    if not dn:
        return False
    parts = None.split('.')
    leftmost = parts[0]
    remainder = parts[1:]
    wildcards = leftmost.count('*')
    if wildcards > max_wildcards:
        raise CertificateError('too many wildcards in certificate DNS name: ' + repr(dn))
    if not wildcards:
        return bool(dn.lower() == hostname.lower())
    if None == '*':
        pats.append('[^.]+')
    elif leftmost.startswith('xn--') or hostname.startswith('xn--'):
        pats.append(re.escape(leftmost))
    else:
        pats.append(re.escape(leftmost).replace('\\*', '[^.]*'))
    for frag in remainder:
        pats.append(re.escape(frag))
        pat = re.compile('\\A' + '\\.'.join(pats) + '\\Z', re.IGNORECASE)
        return pat.match(hostname)


def _ipaddress_match(ipname = None, host_ip = None):
    '''Exact matching of IP addresses.

    RFC 9110 section 4.3.5: "A reference identity of IP-ID contains the decoded
    bytes of the IP address. An IP version 4 address is 4 octets, and an IP
    version 6 address is 16 octets. [...] A reference identity of type IP-ID
    matches if the address is identical to an iPAddress value of the
    subjectAltName extension of the certificate."
    '''
    ip = ipaddress.ip_address(ipname.rstrip())
    return bool(ip.packed == host_ip.packed)


def match_hostname(cert = None, hostname = None, hostname_checks_common_name = None):
    '''Verify that *cert* (in decoded format as returned by
    SSLSocket.getpeercert()) matches the *hostname*.  RFC 2818 and RFC 6125
    rules are followed, but IP addresses are not accepted for *hostname*.

    CertificateError is raised on failure. On success, the function
    returns nothing.
    '''
    if not cert:
        raise ValueError('empty or no certificate, match_hostname needs a SSL socket or SSL context with either CERT_OPTIONAL or CERT_REQUIRED')
    
    try:
        if '%' in hostname:
            host_ip = None(ipaddress.ip_address[hostname:hostname.rfind('%')])
        else:
            host_ip = ipaddress.ip_address(hostname)
    except ValueError:
        host_ip = None

    dnsnames = []
    san = cert.get('subjectAltName', ())
# WARNING: Decompyle incomplete

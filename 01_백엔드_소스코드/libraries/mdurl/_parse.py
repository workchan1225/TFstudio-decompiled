# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _parse.pyc (Python 3.11)

from __future__ import annotations
from collections import defaultdict
import re
from mdurl._url import URL
PROTOCOL_PATTERN = re.compile('^([a-z0-9.+-]+:)', flags = re.IGNORECASE)
PORT_PATTERN = re.compile(':[0-9]*$')
SIMPLE_PATH_PATTERN = re.compile('^(//?(?!/)[^?\\s]*)(\\?[^\\s]*)?$')
DELIMS = ('<', '>', '"', '`', ' ', '\r', '\n', '\t')
UNWISE = ('{', '}', '|', '\\', '^', '`') + DELIMS
AUTO_ESCAPE = ("'",) + UNWISE
NON_HOST_CHARS = ('%', '/', '?', ';', '#') + AUTO_ESCAPE
HOST_ENDING_CHARS = ('/', '?', '#')
HOSTNAME_MAX_LEN = 255
HOSTNAME_PART_PATTERN = re.compile('^[+a-z0-9A-Z_-]{0,63}$')
HOSTNAME_PART_START = re.compile('^([+a-z0-9A-Z_-]{0,63})(.*)$')
HOSTLESS_PROTOCOL = defaultdict(bool, {
    'javascript': True,
    'javascript:': True })
SLASHED_PROTOCOL = defaultdict(bool, {
    'http': True,
    'https': True,
    'ftp': True,
    'gopher': True,
    'file': True,
    'http:': True,
    'https:': True,
    'ftp:': True,
    'gopher:': True,
    'file:': True })

class MutableURL:
    
    def __init__(self = None):
        self.protocol = None
        self.slashes = False
        self.auth = None
        self.port = None
        self.hostname = None
        self.hash = None
        self.search = None
        self.pathname = None

    
    def parse(self = None, url = None, slashes_denote_host = None):
        lower_proto = ''
        slashes = False
        rest = url
        rest = rest.strip()
        if slashes_denote_host and len(url.split('#')) == 1:
            simple_path = SIMPLE_PATH_PATTERN.match(rest)
            if simple_path:
                self.pathname = simple_path.group(1)
                if simple_path.group(2):
                    self.search = simple_path.group(2)
                return self
            proto = None
            proto_match = PROTOCOL_PATTERN.match(rest)
            if proto_match:
                proto = proto_match.group()
                lower_proto = proto.lower()
                self.protocol = proto
                rest = rest[len(proto):]
        if slashes_denote_host and proto or re.search('^//[^@/]+@[^@/]+', rest):
            slashes = rest.startswith('//')
            if slashes:
                if not proto or HOSTLESS_PROTOCOL[proto]:
                    rest = rest[2:]
                    self.slashes = True
    # WARNING: Decompyle incomplete

    
    def parse_host(self = None, host = None):
        port_match = PORT_PATTERN.search(host)
        if port_match:
            port = port_match.group()
            if port != ':':
                self.port = port[1:]
            host = host[:-len(port)]
        if host:
            self.hostname = host
            return None



def url_parse(url = None, *, slashes_denote_host):
    if isinstance(url, URL):
        return url
    u = None()
    u.parse(url, slashes_denote_host)
    return URL(u.protocol, u.slashes, u.auth, u.port, u.hostname, u.hash, u.search, u.pathname)

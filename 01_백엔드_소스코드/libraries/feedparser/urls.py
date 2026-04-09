# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: urls.pyc (Python 3.11)

import re
import urllib.parse as urllib
from html import _BaseHTMLProcessor
ACCEPTABLE_URI_SCHEMES = ('file', 'ftp', 'gopher', 'h323', 'hdl', 'http', 'https', 'imap', 'magnet', 'mailto', 'mms', 'news', 'nntp', 'prospero', 'rsync', 'rtsp', 'rtspu', 'sftp', 'shttp', 'sip', 'sips', 'snews', 'svn', 'svn+ssh', 'telnet', 'wais', 'aim', 'callto', 'cvs', 'facetime', 'feed', 'git', 'gtalk', 'irc', 'ircs', 'irc6', 'itms', 'mms', 'msnim', 'skype', 'ssh', 'smb', 'svn', 'ymsg')
_urifixer = re.compile('^([A-Za-z][A-Za-z0-9+-.]*://)(/*)(.*?)')

def _urljoin(base, uri):
    uri = _urifixer.sub('\\1\\3', uri)
    
    try:
        uri = urllib.parse.urljoin(base, uri)
    except ValueError:
        uri = ''

    return uri


def convert_to_idn(url):
    '''Convert a URL to IDN notation'''
    parts = list(urllib.parse.urlsplit(url))
    
    try:
        parts[1].encode('ascii')
        return url
    except UnicodeEncodeError:
        host = parts[1].rsplit(':', 1)
        newhost = []
        port = ''
        if len(host) == 2:
            port = host.pop()
        for h in host[0].split('.'):
            newhost.append(h.encode('idna').decode('utf-8'))
            parts[1] = '.'.join(newhost)
            if port:
                pass
        return 



def make_safe_absolute_uri(base, rel = (None,)):

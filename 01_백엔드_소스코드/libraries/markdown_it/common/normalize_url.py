# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: normalize_url.pyc (Python 3.11)

from __future__ import annotations
from collections.abc import Callable
from contextlib import suppress
import re
from urllib.parse import quote, unquote, urlparse, urlunparse
import mdurl
from  import _punycode
RECODE_HOSTNAME_FOR = ('http:', 'https:', 'mailto:')

def normalizeLink(url = None):
    """Normalize destination URLs in links

    ::

        [label]:   destination   'title'
                ^^^^^^^^^^^
    """
    parsed = mdurl.parse(url, slashes_denote_host = True)
    if parsed.hostname:
        if parsed.protocol or parsed.protocol in RECODE_HOSTNAME_FOR:
            suppress(Exception)
            parsed = parsed._replace(hostname = _punycode.to_ascii(parsed.hostname))
            None(None, None)
        else:
            with None:
                if not None:
                    pass
    return mdurl.encode(mdurl.format(parsed))


def normalizeLinkText(url = None):
    '''Normalize autolink content

    ::

        <destination>
         ~~~~~~~~~~~
    '''
    parsed = mdurl.parse(url, slashes_denote_host = True)
    if parsed.hostname:
        if parsed.protocol or parsed.protocol in RECODE_HOSTNAME_FOR:
            suppress(Exception)
            parsed = parsed._replace(hostname = _punycode.to_unicode(parsed.hostname))
            None(None, None)
        else:
            with None:
                if not None:
                    pass
    return mdurl.decode(mdurl.format(parsed), mdurl.DECODE_DEFAULT_CHARS + '%')

BAD_PROTO_RE = re.compile('^(vbscript|javascript|file|data):')
GOOD_DATA_RE = re.compile('^data:image\\/(gif|png|jpeg|webp);')

def validateLink(url = None, validator = None):
    """Validate URL link is allowed in output.

    This validator can prohibit more than really needed to prevent XSS.
    It's a tradeoff to keep code simple and to be secure by default.

    Note: url should be normalized at this point, and existing entities decoded.
    """
    pass
# WARNING: Decompyle incomplete

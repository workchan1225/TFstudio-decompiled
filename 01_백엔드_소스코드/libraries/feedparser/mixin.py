# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: mixin.pyc (Python 3.11)

import base64
import binascii
import copy
import html.entities as html
import re
import xml.sax.saxutils as xml
from html import _cp1252
from namespaces import _base, cc, dc, georss, itunes, mediarss, psc
from sanitizer import _sanitize_html, _HTMLSanitizer
from util import FeedParserDict
from urls import _urljoin, make_safe_absolute_uri, resolve_relative_uris

class _FeedParserMixin(psc.Namespace, mediarss.Namespace, itunes.Namespace, georss.Namespace, dc.Namespace, cc.Namespace, _base.Namespace):
    pass
# WARNING: Decompyle incomplete

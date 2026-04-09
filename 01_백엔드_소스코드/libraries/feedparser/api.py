# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: api.pyc (Python 3.11)

import io
import urllib.error as urllib
import urllib.parse as urllib
import xml.sax as xml
from datetimes import registerDateHandler, _parse_date
from encodings import convert_to_utf8
from exceptions import *
from html import _BaseHTMLProcessor
from  import http
from  import mixin
from mixin import _FeedParserMixin
from parsers.loose import _LooseFeedParser
from parsers.strict import _StrictFeedParser
from sanitizer import replace_doctype
from sgml import *
from urls import convert_to_idn, make_safe_absolute_uri
from util import FeedParserDict
PREFERRED_XML_PARSERS = [
    'drv_libxml2']
_XML_AVAILABLE = True
# WARNING: Decompyle incomplete

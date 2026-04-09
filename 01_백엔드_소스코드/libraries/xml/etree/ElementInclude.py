# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ElementInclude.pyc (Python 3.11)

import copy
from  import ElementTree
from urllib.parse import urljoin
XINCLUDE = '{http://www.w3.org/2001/XInclude}'
XINCLUDE_INCLUDE = XINCLUDE + 'include'
XINCLUDE_FALLBACK = XINCLUDE + 'fallback'
DEFAULT_MAX_INCLUSION_DEPTH = 6

class FatalIncludeError(SyntaxError):
    pass


class LimitedRecursiveIncludeError(FatalIncludeError):
    pass


def default_loader(href, parse, encoding = (None,)):
    if parse == 'xml':
        file = open(href, 'rb')
        data = ElementTree.parse(file).getroot()
        None(None, None)
    else:
        with None:
            if not None:
                pass
    if not encoding:
        encoding = 'UTF-8'
    file = open(href, 'r', encoding = encoding)
    data = file.read()
    None(None, None)


def include(elem, loader, base_url, max_depth = (None, None, DEFAULT_MAX_INCLUSION_DEPTH)):
    pass
# WARNING: Decompyle incomplete


def _include(elem, loader, base_url, max_depth, _parent_hrefs):
    i = 0
# WARNING: Decompyle incomplete

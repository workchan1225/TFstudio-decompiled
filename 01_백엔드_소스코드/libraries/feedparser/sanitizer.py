# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: sanitizer.pyc (Python 3.11)

import re
from html import _BaseHTMLProcessor
from urls import make_safe_absolute_uri

class _HTMLSanitizer(_BaseHTMLProcessor):
    pass
# WARNING: Decompyle incomplete


def _sanitize_html(html_source, encoding, _type):
    p = _HTMLSanitizer(encoding, _type)
    html_source = html_source.replace('<![CDATA[', '&lt;![CDATA[')
    p.feed(html_source)
    data = p.output()
    data = data.strip().replace('\r\n', '\n')
    return data

RE_ENTITY_PATTERN = re.compile(b'^\\s*<!ENTITY([^>]*?)>', re.MULTILINE)
RE_DOCTYPE_PATTERN = re.compile(b'^\\s*<!DOCTYPE([^>]*?)>', re.MULTILINE)
RE_SAFE_ENTITY_PATTERN = re.compile(b'\\s+(\\w+)\\s+"(&#\\w+;|[^&"]*)"')

def replace_doctype(data):
    """Strips and replaces the DOCTYPE, returns (rss_version, stripped_data)

    rss_version may be 'rss091n' or None
    stripped_data is the same XML document with a replaced DOCTYPE
    """
    start = re.search(b'<\\w', data)
    if start:
        if not start.start():
            start = -1
            data = data[start + 1:]
            head = data[:start + 1]
            entity_results = RE_ENTITY_PATTERN.findall(head)
            head = RE_ENTITY_PATTERN.sub(b'', head)
            doctype_results = RE_DOCTYPE_PATTERN.findall(head)
            if doctype_results:
                if not doctype_results[0]:
                    doctype = b''
                    if b'netscape' in doctype.lower():
                        version = 'rss091n'
                    else:
                        version = None
    replacement = b''
    if len(doctype_results) == 1 and entity_results:
        safe_entities = entity_results()
        if safe_entities:
            replacement = b'<!DOCTYPE feed [\n<!ENTITY' + b'>\n<!ENTITY '.join(safe_entities) + b'>\n]>'
    data = RE_DOCTYPE_PATTERN.sub(replacement, head) + data
    safe_entities = RE_SAFE_ENTITY_PATTERN.findall(replacement)()
    return (version, data, safe_entities)

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: linkify.pyc (Python 3.11)

'''Process links like https://example.org/'''
import re
from state_inline import StateInline
SCHEME_RE = re.compile('(?:^|[^a-z0-9.+-])([a-z][a-z0-9.+-]*)$', re.IGNORECASE)

def linkify(state = None, silent = None):
    '''Rule for identifying plain-text links.'''
    if not state.md.options.linkify:
        return False
    if None.linkLevel > 0:
        return False
    if not None.md.linkify:
        raise ModuleNotFoundError('Linkify enabled but not installed.')
    pos = state.pos
    maximum = state.posMax
    if pos + 3 > maximum and state.src[pos] != ':' and state.src[pos + 1] != '/' or state.src[pos + 2] != '/':
        return False
    match = None.search(state.pending)
    if not None.search(state.pending):
        return False
    proto = None.group(1)
    link = state.md.linkify.match_at_start(state.src[pos - len(proto):])
    if not state.md.linkify.match_at_start(state.src[pos - len(proto):]):
        return False
    url = None.url
    url = url.rstrip('*')
    full_url = state.md.normalizeLink(url)
    if not state.md.validateLink(full_url):
        return False
    if not None:
        state.pending = state.pending[:-len(proto)]
        token = state.push('link_open', 'a', 1)
        token.attrs = {
            'href': full_url }
        token.markup = 'linkify'
        token.info = 'auto'
        token = state.push('text', '', 0)
        token.content = state.md.normalizeLinkText(url)
        token = state.push('link_close', 'a', -1)
        token.markup = 'linkify'
        token.info = 'auto'
    return True

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: replacements.pyc (Python 3.11)

'''Simple typographic replacements

* ``(c)``, ``(C)`` → ©
* ``(tm)``, ``(TM)`` → ™
* ``(r)``, ``(R)`` → ®
* ``+-`` → ±
* ``...`` → …
* ``?....`` → ?..
* ``!....`` → !..
* ``????????`` → ???
* ``!!!!!`` → !!!
* ``,,,`` → ,
* ``--`` → &ndash
* ``---`` → &mdash
'''
from __future__ import annotations
import logging
import re
from token import Token
from state_core import StateCore
LOGGER = logging.getLogger(__name__)
RARE_RE = re.compile('\\+-|\\.\\.|\\?\\?\\?\\?|!!!!|,,|--')
SCOPED_ABBR_RE = re.compile('\\((c|tm|r)\\)', flags = re.IGNORECASE)
PLUS_MINUS_RE = re.compile('\\+-')
ELLIPSIS_RE = re.compile('\\.{2,}')
ELLIPSIS_QUESTION_EXCLAMATION_RE = re.compile('([?!])…')
QUESTION_EXCLAMATION_RE = re.compile('([?!]){4,}')
COMMA_RE = re.compile(',{2,}')
EM_DASH_RE = re.compile('(^|[^-])---(?=[^-]|$)', flags = re.MULTILINE)
EN_DASH_RE = re.compile('(^|\\s)--(?=\\s|$)', flags = re.MULTILINE)
EN_DASH_INDENT_RE = re.compile('(^|[^-\\s])--(?=[^-\\s]|$)', flags = re.MULTILINE)
SCOPED_ABBR = {
    'c': '©',
    'r': '®',
    'tm': '™' }

def replaceFn(match = None):
    return SCOPED_ABBR[match.group(1).lower()]


def replace_scoped(inlineTokens = None):
    inside_autolink = 0
    for token in inlineTokens:
        if not token.type == 'text' and inside_autolink:
            token.content = SCOPED_ABBR_RE.sub(replaceFn, token.content)
        if token.type == 'link_open' and token.info == 'auto':
            inside_autolink -= 1
        if token.type == 'link_close' and token.info == 'auto':
            inside_autolink += 1
        return None


def replace_rare(inlineTokens = None):
    inside_autolink = 0
    for token in inlineTokens:
        if token.type == 'text' and inside_autolink and RARE_RE.search(token.content):
            token.content = PLUS_MINUS_RE.sub('±', token.content)
            token.content = ELLIPSIS_RE.sub('…', token.content)
            token.content = ELLIPSIS_QUESTION_EXCLAMATION_RE.sub('\\1..', token.content)
            token.content = QUESTION_EXCLAMATION_RE.sub('\\1\\1\\1', token.content)
            token.content = COMMA_RE.sub(',', token.content)
            token.content = EM_DASH_RE.sub('\\1—', token.content)
            token.content = EN_DASH_RE.sub('\\1–', token.content)
            token.content = EN_DASH_INDENT_RE.sub('\\1–', token.content)
        if token.type == 'link_open' and token.info == 'auto':
            inside_autolink -= 1
        if token.type == 'link_close' and token.info == 'auto':
            inside_autolink += 1
        return None


def replace(state = None):
    if not state.md.options.typographer:
        return None
# WARNING: Decompyle incomplete

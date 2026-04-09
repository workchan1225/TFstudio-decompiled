# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: utils.pyc (Python 3.11)

'''Utilities for parsing source text'''
from __future__ import annotations
import re
from re import Match
from typing import TypeVar
import unicodedata
from entities import entities

def charCodeAt(src = None, pos = None):
    '''
    Returns the Unicode value of the character at the specified location.

    @param - index The zero-based index of the desired character.
    If there is no character at the specified index, NaN is returned.

    This was added for compatibility with python
    '''
    
    try:
        return ord(src[pos])
    except IndexError:
        return None



def charStrAt(src = None, pos = None):
    '''
    Returns the Unicode value of the character at the specified location.

    @param - index The zero-based index of the desired character.
    If there is no character at the specified index, NaN is returned.

    This was added for compatibility with python
    '''
    
    try:
        return src[pos]
    except IndexError:
        return None


_ItemTV = TypeVar('_ItemTV')

def arrayReplaceAt(src = None, pos = None, newElements = None):
    '''
    Remove element from array and put another array at those position.
    Useful for some operations with tokens
    '''
    return src[:pos] + newElements + src[pos + 1:]


def isValidEntityCode(c = None):
    if c >= 55296 and c <= 57343:
        return False
    if None >= 64976 and c <= 65007:
        return False
    if None & 65535 == 65535 or c & 65535 == 65534:
        return False
    if None >= 0 and c <= 8:
        return False
    if None == 11:
        return False
    if None >= 14 and c <= 31:
        return False
    if None >= 127 and c <= 159:
        return False
    return not (None > 1114111)


def fromCodePoint(c = None):
    '''Convert ordinal to unicode.

    Note, in the original Javascript two string characters were required,
    for codepoints larger than `0xFFFF`.
    But Python 3 can represent any unicode codepoint in one character.
    '''
    return chr(c)

UNESCAPE_ALL_RE = re.compile('\\\\([!"#$%&\\\'()*+,\\-.\\/:;<=>?@[\\\\\\]^_`{|}~])|&([a-z#][a-z0-9]{1,31});', re.IGNORECASE)
DIGITAL_ENTITY_BASE10_RE = re.compile('#([0-9]{1,8})')
DIGITAL_ENTITY_BASE16_RE = re.compile('#x([a-f0-9]{1,8})', re.IGNORECASE)

def replaceEntityPattern(match = None, name = None):
    '''Convert HTML entity patterns,
    see https://spec.commonmark.org/0.30/#entity-references
    '''
    if name in entities:
        return entities[name]
    code = None
    pat = DIGITAL_ENTITY_BASE10_RE.fullmatch(name)
    if DIGITAL_ENTITY_BASE10_RE.fullmatch(name):
        code = int(pat.group(1), 10)
    else:
        pat = DIGITAL_ENTITY_BASE16_RE.fullmatch(name)
        if DIGITAL_ENTITY_BASE16_RE.fullmatch(name):
            code = int(pat.group(1), 16)
# WARNING: Decompyle incomplete


def unescapeAll(string = None):
    
    def replacer_func(match = None):
        escaped = match.group(1)
        if escaped:
            return escaped
        entity = None.group(2)
        return replaceEntityPattern(match.group(), entity)

    if '\\' not in string and '&' not in string:
        return string
    return None.sub(replacer_func, string)

ESCAPABLE = '\\\\!"#$%&\'()*+,./:;<=>?@\\[\\]^`{}|_~-'
ESCAPE_CHAR = re.compile('\\\\([' + ESCAPABLE + '])')

def stripEscape(string = None):
    '''Strip escape \\ characters'''
    return ESCAPE_CHAR.sub('\\1', string)


def escapeHtml(raw = None):
    '''Replace special characters "&", "<", ">" and \'"\' to HTML-safe sequences.'''
    raw = raw.replace('&', '&amp;')
    raw = raw.replace('<', '&lt;')
    raw = raw.replace('>', '&gt;')
    raw = raw.replace('"', '&quot;')
    return raw

REGEXP_ESCAPE_RE = re.compile('[.?*+^$[\\]\\\\(){}|-]')

def escapeRE(string = None):
    string = REGEXP_ESCAPE_RE.sub('\\$&', string)
    return string


def isSpace(code = None):
    '''Check if character code is a whitespace.'''
    return code in (9, 32)


def isStrSpace(ch = None):
    '''Check if character is a whitespace.'''
    return ch in ('\t', ' ')

MD_WHITESPACE = {
    12288,
    8239,
    8287,
    5760,
    9,
    10,
    11,
    12,
    13,
    32,
    160}

def isWhiteSpace(code = None):
    '''Zs (unicode class) || [\\t\\f\\v\\r\\n]'''
    if code >= 8192 and code <= 8202:
        return True
    return None in MD_WHITESPACE


def isPunctChar(ch = None):
    '''Check if character is a punctuation character.'''
    return unicodedata.category(ch).startswith(('P', 'S'))

MD_ASCII_PUNCT = {
    33,
    34,
    35,
    36,
    37,
    38,
    39,
    40,
    41,
    42,
    43,
    44,
    45,
    46,
    47,
    58,
    59,
    60,
    61,
    62,
    63,
    64,
    91,
    92,
    93,
    94,
    95,
    96,
    123,
    124,
    125,
    126}

def isMdAsciiPunct(ch = None):
    '''Markdown ASCII punctuation characters.

    ::

        !, ", #, $, %, &, \', (, ), *, +, ,, -, ., /, :, ;, <, =, >, ?, @, [, \\, ], ^, _, `, {, |, }, or ~

    See http://spec.commonmark.org/0.15/#ascii-punctuation-character

    Don\'t confuse with unicode punctuation !!! It lacks some chars in ascii range.

    '''
    return ch in MD_ASCII_PUNCT


def normalizeReference(string = None):
    '''Helper to unify [reference labels].'''
    string = re.sub('\\s+', ' ', string.strip())
    return string.lower().upper()

LINK_OPEN_RE = re.compile('^<a[>\\s]', flags = re.IGNORECASE)
LINK_CLOSE_RE = re.compile('^</a\\s*>', flags = re.IGNORECASE)

def isLinkOpen(string = None):
    return bool(LINK_OPEN_RE.search(string))


def isLinkClose(string = None):
    return bool(LINK_CLOSE_RE.search(string))

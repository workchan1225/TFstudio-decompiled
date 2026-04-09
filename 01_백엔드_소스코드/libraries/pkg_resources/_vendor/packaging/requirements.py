# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: requirements.pyc (Python 3.11)

import re
import string
import urllib.parse as urllib
from typing import List, Optional as TOptional, Set
from pkg_resources.extern.pyparsing import Combine, Literal as L, Optional, ParseException, Regex, Word, ZeroOrMore, originalTextFor, stringEnd, stringStart
from markers import MARKER_EXPR, Marker
from specifiers import LegacySpecifier, Specifier, SpecifierSet

class InvalidRequirement(ValueError):
    '''
    An invalid requirement was found, users should refer to PEP 508.
    '''
    pass

ALPHANUM = Word(string.ascii_letters + string.digits)
LBRACKET = L('[').suppress()
RBRACKET = L(']').suppress()
LPAREN = L('(').suppress()
RPAREN = L(')').suppress()
COMMA = L(',').suppress()
SEMICOLON = L(';').suppress()
AT = L('@').suppress()
PUNCTUATION = Word('-_.')
IDENTIFIER_END = ALPHANUM | ZeroOrMore(PUNCTUATION) + ALPHANUM
IDENTIFIER = Combine(ALPHANUM + ZeroOrMore(IDENTIFIER_END))
NAME = IDENTIFIER('name')
EXTRA = IDENTIFIER
URI = Regex('[^ ]+')('url')
URL = AT + URI
EXTRAS_LIST = EXTRA + ZeroOrMore(COMMA + EXTRA)
EXTRAS = LBRACKET + Optional(EXTRAS_LIST) + RBRACKET('extras')
VERSION_PEP440 = Regex(Specifier._regex_str, re.VERBOSE | re.IGNORECASE)
VERSION_LEGACY = Regex(LegacySpecifier._regex_str, re.VERBOSE | re.IGNORECASE)
VERSION_ONE = VERSION_PEP440 ^ VERSION_LEGACY
VERSION_MANY = Combine(VERSION_ONE + ZeroOrMore(COMMA + VERSION_ONE), joinString = ',', adjacent = False)('_raw_spec')
_VERSION_SPEC = Optional(LPAREN + VERSION_MANY + RPAREN | VERSION_MANY)
_VERSION_SPEC.setParseAction((lambda s, l, t:

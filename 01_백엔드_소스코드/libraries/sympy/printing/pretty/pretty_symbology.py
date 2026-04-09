# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: pretty_symbology.pyc (Python 3.11)

__doc__ = 'Symbolic primitives + unicode/ASCII abstraction for pretty.py'
import sys
import warnings
from string import ascii_lowercase, ascii_uppercase
import unicodedata
unicode_warnings = ''

def U(name):
    '''
    Get a unicode character by name or, None if not found.

    This exists because older versions of Python use older unicode databases.
    '''
    global unicode_warnings
    
    try:
        return unicodedata.lookup(name)
    except KeyError:
        unicode_warnings += "No '%s' in unicodedata\n" % name
        return None


from sympy.printing.conventions import split_super_sub
from sympy.core.alphabets import greeks
from sympy.utilities.exceptions import sympy_deprecation_warning
__all__ = [
    'greek_unicode',
    'sub',
    'sup',
    'xsym',
    'vobj',
    'hobj',
    'pretty_symbol',
    'annotated',
    'center_pad',
    'center']
_use_unicode = False

def pretty_use_unicode(flag = (None,)):
    '''Set whether pretty-printer should use unicode by default'''
    pass
# WARNING: Decompyle incomplete


def pretty_try_use_unicode():
    '''See if unicode output is available and leverage it if possible'''
    encoding = getattr(sys.stdout, 'encoding', None)
# WARNING: Decompyle incomplete


def xstr(*args):
    sympy_deprecation_warning('\n        The sympy.printing.pretty.pretty_symbology.xstr() function is\n        deprecated. Use str() instead.\n        ', deprecated_since_version = '1.7', active_deprecations_target = 'deprecated-pretty-printing-functions')
# WARNING: Decompyle incomplete


g = lambda l: U('GREEK SMALL LETTER %s' % l.upper())

G = lambda l: U('GREEK CAPITAL LETTER %s' % l.upper())
greek_letters = list(greeks)
greek_letters[greek_letters.index('lambda')] = 'lamda'
greek_unicode = greek_letters()
(lambda .0: pass# WARNING: Decompyle incomplete
)(greek_letters())
greek_unicode['lambda'] = greek_unicode['lamda']
greek_unicode['Lambda'] = greek_unicode['Lamda']
greek_unicode['varsigma'] = 'ς'

b = lambda l: U('MATHEMATICAL BOLD SMALL %s' % l.upper())

B = lambda l: U('MATHEMATICAL BOLD CAPITAL %s' % l.upper())
bold_unicode = ascii_lowercase()
(lambda .0: pass# WARNING: Decompyle incomplete
)(ascii_uppercase())

gb = lambda l: U('MATHEMATICAL BOLD SMALL %s' % l.upper())

GB = lambda l: U('MATHEMATICAL BOLD CAPITAL  %s' % l.upper())
greek_bold_letters = list(greeks)
greek_bold_letters[greek_bold_letters.index('lambda')] = 'lamda'
greek_bold_unicode = greek_bold_letters()
(lambda .0: pass# WARNING: Decompyle incomplete
)(greek_bold_letters())
greek_bold_unicode['lambda'] = greek_unicode['lamda']
greek_bold_unicode['Lambda'] = greek_unicode['Lamda']
greek_bold_unicode['varsigma'] = '𝛓'
digit_2txt = {
    '0': 'ZERO',
    '1': 'ONE',
    '2': 'TWO',
    '3': 'THREE',
    '4': 'FOUR',
    '5': 'FIVE',
    '6': 'SIX',
    '7': 'SEVEN',
    '8': 'EIGHT',
    '9': 'NINE' }
symb_2txt = {
    '+': 'PLUS SIGN',
    '-': 'MINUS',
    '=': 'EQUALS SIGN',
    '(': 'LEFT PARENTHESIS',
    ')': 'RIGHT PARENTHESIS',
    '[': 'LEFT SQUARE BRACKET',
    ']': 'RIGHT SQUARE BRACKET',
    '{': 'LEFT CURLY BRACKET',
    '}': 'RIGHT CURLY BRACKET',
    '{}': 'CURLY BRACKET',
    'sum': 'SUMMATION',
    'int': 'INTEGRAL' }

LSUB = lambda letter: U('LATIN SUBSCRIPT SMALL LETTER %s' % letter.upper())

GSUB = lambda letter: U('GREEK SUBSCRIPT SMALL LETTER %s' % letter.upper())

DSUB = lambda digit: U('SUBSCRIPT %s' % digit_2txt[digit])

SSUB = lambda symb: U('SUBSCRIPT %s' % symb_2txt[symb])

LSUP = lambda letter: U('SUPERSCRIPT LATIN SMALL LETTER %s' % letter.upper())

DSUP = lambda digit: U('SUPERSCRIPT %s' % digit_2txt[digit])

SSUP = lambda symb: U('SUPERSCRIPT %s' % symb_2txt[symb])
sub = { }
sup = { }
# WARNING: Decompyle incomplete

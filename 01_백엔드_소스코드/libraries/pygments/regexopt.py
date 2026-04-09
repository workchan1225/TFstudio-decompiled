# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: regexopt.pyc (Python 3.11)

'''
    pygments.regexopt
    ~~~~~~~~~~~~~~~~~

    An algorithm that generates optimized regexes for matching long lists of
    literal strings.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
import re
from re import escape
from os.path import commonprefix
from itertools import groupby
from operator import itemgetter
CS_ESCAPE = re.compile('[\\[\\^\\\\\\-\\]]')
FIRST_ELEMENT = itemgetter(0)

def make_charset(letters):
    return '[' + CS_ESCAPE.sub((lambda m: '\\' + m.group()), ''.join(letters)) + ']'


def regex_opt_inner(strings, open_paren):
    '''Return a regex that matches any string in the sorted list of strings.'''
    pass
# WARNING: Decompyle incomplete


def regex_opt(strings, prefix, suffix = ('', '')):
    '''Return a compiled regex that matches any string in the given list.

    The strings to match must be literal strings, not regexes.  They will be
    regex-escaped.

    *prefix* and *suffix* are pre- and appended to the final regex.
    '''
    strings = sorted(strings)
    return prefix + regex_opt_inner(strings, '(') + suffix

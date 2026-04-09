# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''
    pygments.filters
    ~~~~~~~~~~~~~~~~

    Module containing filter lookup functions and default
    filters.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
import re
from pygments.token import String, Comment, Keyword, Name, Error, Whitespace, string_to_tokentype
from pygments.filter import Filter
from pygments.util import get_list_opt, get_int_opt, get_bool_opt, get_choice_opt, ClassNotFound, OptionError
from pygments.plugin import find_plugin_filters

def find_filter_class(filtername):
    '''Lookup a filter by name. Return None if not found.'''
    if filtername in FILTERS:
        return FILTERS[filtername]
    for name, cls in None():
        if name == filtername:
            
            return None, cls
        return None


def get_filter_by_name(filtername, **options):
    '''Return an instantiated filter.

    Options are passed to the filter initializer if wanted.
    Raise a ClassNotFound if not found.
    '''
    cls = find_filter_class(filtername)
# WARNING: Decompyle incomplete


def get_all_filters():
    '''Return a generator of all filter names.'''
    pass
# WARNING: Decompyle incomplete


def _replace_special(ttype, value, regex, specialttype, replacefunc = ((lambda x: x),)):
    pass
# WARNING: Decompyle incomplete


class CodeTagFilter(Filter):
    '''Highlight special code tags in comments and docstrings.

    Options accepted:

    `codetags` : list of strings
       A list of strings that are flagged as code tags.  The default is to
       highlight ``XXX``, ``TODO``, ``FIXME``, ``BUG`` and ``NOTE``.

    .. versionchanged:: 2.13
       Now recognizes ``FIXME`` by default.
    '''
    
    def __init__(self, **options):
        pass
    # WARNING: Decompyle incomplete

    
    def filter(self, lexer, stream):
        pass
    # WARNING: Decompyle incomplete



class SymbolFilter(Filter):
    __module__ = __name__
    __qualname__ = 'SymbolFilter'
    __doc__ = "Convert mathematical symbols such as \\<longrightarrow> in Isabelle\n    or \\longrightarrow in LaTeX into Unicode characters.\n\n    This is mostly useful for HTML or console output when you want to\n    approximate the source rendering you'd see in an IDE.\n\n    Options accepted:\n\n    `lang` : string\n       The symbol language. Must be one of ``'isabelle'`` or\n       ``'latex'``.  The default is ``'isabelle'``.\n    "
# WARNING: Decompyle incomplete


class KeywordCaseFilter(Filter):
    """Convert keywords to lowercase or uppercase or capitalize them, which
    means first letter uppercase, rest lowercase.

    This can be useful e.g. if you highlight Pascal code and want to adapt the
    code to your styleguide.

    Options accepted:

    `case` : string
       The casing to convert keywords to. Must be one of ``'lower'``,
       ``'upper'`` or ``'capitalize'``.  The default is ``'lower'``.
    """
    
    def __init__(self, **options):
        pass
    # WARNING: Decompyle incomplete

    
    def filter(self, lexer, stream):
        pass
    # WARNING: Decompyle incomplete



class NameHighlightFilter(Filter):
    '''Highlight a normal Name (and Name.*) token with a different token type.

    Example::

        filter = NameHighlightFilter(
            names=[\'foo\', \'bar\', \'baz\'],
            tokentype=Name.Function,
        )

    This would highlight the names "foo", "bar" and "baz"
    as functions. `Name.Function` is the default token type.

    Options accepted:

    `names` : list of strings
      A list of names that should be given the different token type.
      There is no default.
    `tokentype` : TokenType or string
      A token type or a string containing a token type name that is
      used for highlighting the strings in `names`.  The default is
      `Name.Function`.
    '''
    
    def __init__(self, **options):
        pass
    # WARNING: Decompyle incomplete

    
    def filter(self, lexer, stream):
        pass
    # WARNING: Decompyle incomplete



class ErrorToken(Exception):
    pass


class RaiseOnErrorTokenFilter(Filter):
    '''Raise an exception when the lexer generates an error token.

    Options accepted:

    `excclass` : Exception class
      The exception class to raise.
      The default is `pygments.filters.ErrorToken`.

    .. versionadded:: 0.8
    '''
    
    def __init__(self, **options):
        pass
    # WARNING: Decompyle incomplete

    
    def filter(self, lexer, stream):
        pass
    # WARNING: Decompyle incomplete



class VisibleWhitespaceFilter(Filter):
    '''Convert tabs, newlines and/or spaces to visible characters.

    Options accepted:

    `spaces` : string or bool
      If this is a one-character string, spaces will be replaces by this string.
      If it is another true value, spaces will be replaced by ``·`` (unicode
      MIDDLE DOT).  If it is a false value, spaces will not be replaced.  The
      default is ``False``.
    `tabs` : string or bool
      The same as for `spaces`, but the default replacement character is ``»``
      (unicode RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK).  The default value
      is ``False``.  Note: this will not work if the `tabsize` option for the
      lexer is nonzero, as tabs will already have been expanded then.
    `tabsize` : int
      If tabs are to be replaced by this filter (see the `tabs` option), this
      is the total number of characters that a tab should be expanded to.
      The default is ``8``.
    `newlines` : string or bool
      The same as for `spaces`, but the default replacement character is ``¶``
      (unicode PILCROW SIGN).  The default value is ``False``.
    `wstokentype` : bool
      If true, give whitespace the special `Whitespace` token type.  This allows
      styling the visible whitespace differently (e.g. greyed out), but it can
      disrupt background colors.  The default is ``True``.

    .. versionadded:: 0.8
    '''
    
    def __init__(self, **options):
        pass
    # WARNING: Decompyle incomplete

    
    def filter(self, lexer, stream):
        pass
    # WARNING: Decompyle incomplete



class GobbleFilter(Filter):
    """Gobbles source code lines (eats initial characters).

    This filter drops the first ``n`` characters off every line of code.  This
    may be useful when the source code fed to the lexer is indented by a fixed
    amount of space that isn't desired in the output.

    Options accepted:

    `n` : int
       The number of characters to gobble.

    .. versionadded:: 1.2
    """
    
    def __init__(self, **options):
        pass
    # WARNING: Decompyle incomplete

    
    def gobble(self, value, left):
        if left < len(value):
            return (value[left:], 0)
        return (None, left - len(value))

    
    def filter(self, lexer, stream):
        pass
    # WARNING: Decompyle incomplete



class TokenMergeFilter(Filter):
    '''Merges consecutive tokens with the same token type in the output
    stream of a lexer.

    .. versionadded:: 1.2
    '''
    
    def __init__(self, **options):
        pass
    # WARNING: Decompyle incomplete

    
    def filter(self, lexer, stream):
        pass
    # WARNING: Decompyle incomplete


FILTERS = {
    'codetagify': CodeTagFilter,
    'keywordcase': KeywordCaseFilter,
    'highlight': NameHighlightFilter,
    'raiseonerror': RaiseOnErrorTokenFilter,
    'whitespace': VisibleWhitespaceFilter,
    'gobble': GobbleFilter,
    'tokenmerge': TokenMergeFilter,
    'symbols': SymbolFilter }

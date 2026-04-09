# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tnt.pyc (Python 3.11)

'''
    pygments.lexers.tnt
    ~~~~~~~~~~~~~~~~~~~

    Lexer for Typographic Number Theory.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
import re
from pygments.lexer import Lexer
from pygments.token import Text, Comment, Operator, Keyword, Name, Number, Punctuation, Error
__all__ = [
    'TNTLexer']

class TNTLexer(Lexer):
    '''
    Lexer for Typographic Number Theory, as described in the book
    Gödel, Escher, Bach, by Douglas R. Hofstadter
    '''
    name = 'Typographic Number Theory'
    url = 'https://github.com/Kenny2github/language-tnt'
    aliases = [
        'tnt']
    filenames = [
        '*.tnt']
    version_added = '2.7'
    cur = []
    LOGIC = set('⊃→]&∧^|∨Vv')
    OPERATORS = set('+.⋅*')
    VARIABLES = set('abcde')
    PRIMES = set("'′")
    NEGATORS = set('~!')
    QUANTIFIERS = set('AE∀∃')
    NUMBERS = set('0123456789')
    WHITESPACE = set('\t \x0b\n')
    RULES = re.compile('(?xi)\n        joining | separation | double-tilde | fantasy\\ rule\n        | carry[- ]over(?:\\ of)?(?:\\ line)?\\ ([0-9]+) | detachment\n        | contrapositive | De\\ Morgan | switcheroo\n        | specification | generalization | interchange\n        | existence | symmetry | transitivity\n        | add\\ S | drop\\ S | induction\n        | axiom\\ ([1-5]) | premise | push | pop\n    ')
    LINENOS = re.compile('(?:[0-9]+)(?:(?:, ?|,? and )(?:[0-9]+))*')
    COMMENT = re.compile('\\[[^\\n\\]]+\\]')
    
    def __init__(self, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def whitespace(self, start, text, required = (False,)):
        '''Tokenize whitespace.'''
        end = start
    # WARNING: Decompyle incomplete

    
    def variable(self, start, text):
        '''Tokenize a variable.'''
        if text[start] not in self.VARIABLES:
            raise AssertionError
        end = start + 1
    # WARNING: Decompyle incomplete

    
    def term(self, start, text):
        '''Tokenize a term.'''
        pass
    # WARNING: Decompyle incomplete

    
    def formula(self, start, text):
        '''Tokenize a formula.'''
        pass
    # WARNING: Decompyle incomplete

    
    def rule(self, start, text):
        '''Tokenize a rule.'''
        match = self.RULES.match(text, start)
    # WARNING: Decompyle incomplete

    
    def lineno(self, start, text):
        '''Tokenize a line referral.'''
        end = start
    # WARNING: Decompyle incomplete

    
    def error_till_line_end(self, start, text):
        '''Mark everything from ``start`` to the end of the line as Error.'''
        end = start
    # WARNING: Decompyle incomplete

    
    def get_tokens_unprocessed(self, text):
        '''Returns a list of TNT tokens.'''
        self.cur = []
        start = self.whitespace(0, text)
        end = self.whitespace(0, text)
        if  <= start, end or start, end < len(text):
            pass
        
    # WARNING: Decompyle incomplete

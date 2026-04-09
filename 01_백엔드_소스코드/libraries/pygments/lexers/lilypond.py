# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: lilypond.pyc (Python 3.11)

'''
    pygments.lexers.lilypond
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Lexer for LilyPond.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
import re
from pygments.lexer import bygroups, default, inherit, words
from pygments.lexers.lisp import SchemeLexer
from pygments.lexers._lilypond_builtins import keywords, pitch_language_names, clefs, scales, repeat_types, units, chord_modifiers, pitches, music_functions, dynamics, articulations, music_commands, markup_commands, grobs, translators, contexts, context_properties, grob_properties, scheme_functions, paper_variables, header_variables
from pygments.token import Token
__all__ = [
    'LilyPondLexer']
NAME_END_RE = '(?=\\d|[^\\w\\-]|[\\-_][\\W\\d])'

def builtin_words(names, backslash, suffix = (NAME_END_RE,)):
    prefix = '[\\-_^]?'
    if backslash == 'mandatory':
        prefix += '\\\\'
    elif backslash == 'optional':
        prefix += '\\\\?'
# WARNING: Decompyle incomplete


class LilyPondLexer(SchemeLexer):
    pass
# WARNING: Decompyle incomplete

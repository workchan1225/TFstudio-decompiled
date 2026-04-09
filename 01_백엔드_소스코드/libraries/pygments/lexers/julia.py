# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: julia.pyc (Python 3.11)

'''
    pygments.lexers.julia
    ~~~~~~~~~~~~~~~~~~~~~

    Lexers for the Julia language.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
from pygments.lexer import Lexer, RegexLexer, bygroups, do_insertions, words, include
from pygments.token import Text, Comment, Operator, Keyword, Name, String, Number, Punctuation, Generic, Whitespace
from pygments.util import shebang_matches
from pygments.lexers._julia_builtins import OPERATORS_LIST, DOTTED_OPERATORS_LIST, KEYWORD_LIST, BUILTIN_LIST, LITERAL_LIST
__all__ = [
    'JuliaLexer',
    'JuliaConsoleLexer']
allowed_variable = '(?:[a-zA-Z_¡-􏿿][a-zA-Z_0-9!¡-􏿿]*)'
operator_suffixes = '[²³¹ʰʲʳʷʸˡˢˣᴬᴮᴰᴱᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾᴿᵀᵁᵂᵃᵇᵈᵉᵍᵏᵐᵒᵖᵗᵘᵛᵝᵞᵟᵠᵡᵢᵣᵤᵥᵦᵧᵨᵩᵪᶜᶠᶥᶦᶫᶰᶸᶻᶿ′″‴‵‶‷⁗⁰ⁱ⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾ⁿ₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎ₐₑₒₓₕₖₗₘₙₚₛₜⱼⱽ]*'

class JuliaLexer(RegexLexer):

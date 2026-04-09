# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: email.pyc (Python 3.11)

'''
    pygments.lexers.email
    ~~~~~~~~~~~~~~~~~~~~~

    Lexer for the raw E-mail.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
from pygments.lexer import RegexLexer, DelegatingLexer, bygroups
from pygments.lexers.mime import MIMELexer
from pygments.token import Text, Keyword, Name, String, Number, Comment
from pygments.util import get_bool_opt
__all__ = [
    'EmailLexer']

class EmailHeaderLexer(RegexLexer):
    pass
# WARNING: Decompyle incomplete


class EmailLexer(DelegatingLexer):
    pass
# WARNING: Decompyle incomplete

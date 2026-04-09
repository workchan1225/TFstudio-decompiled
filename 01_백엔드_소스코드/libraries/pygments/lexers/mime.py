# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: mime.pyc (Python 3.11)

'''
    pygments.lexers.mime
    ~~~~~~~~~~~~~~~~~~~~

    Lexer for Multipurpose Internet Mail Extensions (MIME) data.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
import re
from pygments.lexer import RegexLexer, include
from pygments.lexers import get_lexer_for_mimetype
from pygments.token import Text, Name, String, Operator, Comment, Other
from pygments.util import get_int_opt, ClassNotFound
__all__ = [
    'MIMELexer']

class MIMELexer(RegexLexer):
    pass
# WARNING: Decompyle incomplete

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: c_parser.pyc (Python 3.11)

from ply import yacc
from  import c_ast
from c_lexer import CLexer
from plyparser import PLYParser, ParseError, parameterized, template
from ast_transforms import fix_switch_cases, fix_atomic_specifiers
CParser = <NODE:12>()

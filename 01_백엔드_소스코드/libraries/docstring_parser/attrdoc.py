# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: attrdoc.pyc (Python 3.11)

'''Attribute docstrings parsing.

.. seealso:: https://peps.python.org/pep-0257/#what-is-a-docstring
'''
import ast
import inspect
import textwrap
import typing as T
from types import ModuleType
from common import Docstring, DocstringParam

def ast_get_constant_value(node = None):
    """Return the constant's value if the given node is a constant."""
    return getattr(node, 'value')


def ast_unparse(node = None):
    '''Convert the AST node to source code as a string.'''
    if hasattr(ast, 'unparse'):
        return ast.unparse(node)
    if None(node, ast.Constant):
        return str(ast_get_constant_value(node))
    if None(node, ast.Name):
        return node.id


def ast_is_literal_str(node = None):

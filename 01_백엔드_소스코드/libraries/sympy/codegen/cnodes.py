# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: cnodes.pyc (Python 3.11)

'''
AST nodes specific to the C family of languages
'''
from sympy.codegen.ast import Attribute, Declaration, Node, String, Token, Type, none, FunctionCall, CodeBlock
from sympy.core.basic import Basic
from sympy.core.containers import Tuple
from sympy.core.sympify import sympify
void = Type('void')
restrict = Attribute('restrict')
volatile = Attribute('volatile')
static = Attribute('static')

def alignof(arg):
    """ Generate of FunctionCall instance for calling 'alignof' """
    return FunctionCall('alignof', [
        String(arg) if isinstance(arg, str) else arg])


def sizeof(arg):
    """ Generate of FunctionCall instance for calling 'sizeof'

    Examples
    ========

    >>> from sympy.codegen.ast import real
    >>> from sympy.codegen.cnodes import sizeof
    >>> from sympy import ccode
    >>> ccode(sizeof(real))
    'sizeof(double)'
    """
    return FunctionCall('sizeof', [
        String(arg) if isinstance(arg, str) else arg])


class CommaOperator(Basic):
    ''' Represents the comma operator in C '''
    
    def __new__(cls, *args):

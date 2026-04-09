# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: pynodes.pyc (Python 3.11)

from abstract_nodes import List as AbstractList
from ast import Token

class List(AbstractList):
    pass


class NumExprEvaluate(Token):
    '''represents a call to :class:`numexpr`s :func:`evaluate`'''
    __slots__ = ('expr',)
    _fields = ('expr',)

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: optimizer.pyc (Python 3.11)

"""The optimizer tries to constant fold expressions and modify the AST
in place so that it should be faster to evaluate.

Because the AST does not contain all the scoping information and the
compiler has to find that out, we cannot do all the optimizations we
want. For example, loop unrolling doesn't work because unrolled loops
would have a different scope. The solution would be a second syntax tree
that stored the scoping rules.
"""
import typing as t
from  import nodes
from visitor import NodeTransformer
if t.TYPE_CHECKING:
    from environment import Environment

def optimize(node = None, environment = None):
    '''The context hint can be used to perform an static optimization
    based on the context given.'''
    optimizer = Optimizer(environment)
    return t.cast(nodes.Node, optimizer.visit(node))


class Optimizer(NodeTransformer):
    pass
# WARNING: Decompyle incomplete

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: visitor.pyc (Python 3.11)

'''API for traversing the AST nodes. Implemented by the compiler and
meta introspection.
'''
import typing as t
from nodes import Node
if t.TYPE_CHECKING:
    import typing_extensions as te
    
    class VisitCallable(te.Protocol):
        
        def __call__(self = None, node = None, *args, **kwargs):
            pass



class NodeVisitor:
    """Walks the abstract syntax tree and call visitor functions for every
    node found.  The visitor functions may return values which will be
    forwarded by the `visit` method.

    Per default the visitor functions for the nodes are ``'visit_'`` +
    class name of the node.  So a `TryFinally` node visit function would
    be `visit_TryFinally`.  This behavior can be changed by overriding
    the `get_visitor` function.  If no visitor function exists for a node
    (return value `None`) the `generic_visit` visitor is used instead.
    """
    
    def get_visitor(self = None, node = None):
        '''Return the visitor function for this node or `None` if no visitor
        exists for this node.  In that case the generic visit function is
        used instead.
        '''
        return getattr(self, f'''visit_{type(node).__name__}''', None)

    
    def visit(self = None, node = None, *args, **kwargs):
        '''Visit a node.'''
        f = self.get_visitor(node)
    # WARNING: Decompyle incomplete

    
    def generic_visit(self = None, node = None, *args, **kwargs):
        '''Called if no explicit visitor function exists for a node.'''
        pass
    # WARNING: Decompyle incomplete



class NodeTransformer(NodeVisitor):
    """Walks the abstract syntax tree and allows modifications of nodes.

    The `NodeTransformer` will walk the AST and use the return value of the
    visitor functions to replace or remove the old node.  If the return
    value of the visitor function is `None` the node will be removed
    from the previous location otherwise it's replaced with the return
    value.  The return value may be the original node in which case no
    replacement takes place.
    """
    
    def generic_visit(self = None, node = None, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def visit_list(self = None, node = None, *args, **kwargs):
        '''As transformers may return lists in some places this method
        can be used to enforce a list as return value.
        '''
        pass
    # WARNING: Decompyle incomplete

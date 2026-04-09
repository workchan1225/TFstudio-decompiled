# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: regions.pyc (Python 3.11)

'''Find functions and classes in Python code.'''
from __future__ import annotations
import ast
import dataclasses
from typing import cast
from coverage.plugin import CodeRegion
Context = <NODE:12>()

class RegionFinder:
    '''An ast visitor that will find and track regions of code.

    Functions and classes are tracked by name. Results are in the .regions
    attribute.

    '''
    
    def __init__(self = None):
        self.regions = []
        self.context = []

    
    def parse_source(self = None, source = None):
        '''Parse `source` and walk the ast to populate the .regions attribute.'''
        self.handle_node(ast.parse(source))

    
    def fq_node_name(self = None):
        """Get the current fully qualified name we're processing."""
        return (lambda .0: pass# WARNING: Decompyle incomplete
)(self.context())

    
    def handle_node(self = None, node = None):
        '''Recursively handle any node.'''
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            self.handle_FunctionDef(node)
            return None
        if None(node, ast.ClassDef):
            self.handle_ClassDef(node)
            return None
        None.handle_node_body(node)

    
    def handle_node_body(self = None, node = None):
        """Recursively handle the nodes in this node's body, if any."""
        for body_node in getattr(node, 'body', ()):
            self.handle_node(body_node)
            return None

    
    def handle_FunctionDef(self = None, node = None):
        '''Called for `def` or `async def`.'''
        lines = set(range(node.body[0].lineno, cast(int, node.body[-1].end_lineno) + 1))
        if self.context and self.context[-1].kind == 'class':
            pass
        for None in reversed(self.context):
            if ancestor.kind == 'function':
                ancestor, ancestor.lines -= lines, .lines
            
            self.context.append(Context(node.name, 'function', lines))
            self.regions.append(CodeRegion(kind = 'function', name = self.fq_node_name(), start = node.lineno, lines = lines))
            self.handle_node_body(node)
            self.context.pop()
            return None

    
    def handle_ClassDef(self = None, node = None):
        '''Called for `class`.'''
        lines = set()
        self.context.append(Context(node.name, 'class', lines))
        self.regions.append(CodeRegion(kind = 'class', name = self.fq_node_name(), start = node.lineno, lines = lines))
        self.handle_node_body(node)
        self.context.pop()
        for ancestor in reversed(self.context):
            if ancestor.kind == 'class':
                pass
            return None



def code_regions(source = None):
    '''Find function and class regions in source code.

    Analyzes the code in `source`, and returns a list of :class:`CodeRegion`
    objects describing functions and classes as regions of the code::

        [
            CodeRegion(kind="function", name="func1", start=8, lines={10, 11, 12}),
            CodeRegion(kind="function", name="MyClass.method", start=30, lines={34, 35, 36}),
            CodeRegion(kind="class", name="MyClass", start=25, lines={34, 35, 36}),
        ]

    The line numbers will include comments and blank lines.  Later processing
    will need to ignore those lines as needed.

    Nested functions and classes are excluded from their enclosing region.  No
    line should be reported as being part of more than one function, or more
    than one class.  Lines in methods are reported as being in a function and
    in a class.

    '''
    rf = RegionFinder()
    rf.parse_source(source)
    return rf.regions

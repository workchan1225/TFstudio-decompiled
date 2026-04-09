# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: idtracking.pyc (Python 3.11)

import typing as t
from  import nodes
from visitor import NodeVisitor
if t.TYPE_CHECKING:
    import typing_extensions as te
VAR_LOAD_PARAMETER = 'param'
VAR_LOAD_RESOLVE = 'resolve'
VAR_LOAD_ALIAS = 'alias'
VAR_LOAD_UNDEFINED = 'undefined'

def find_symbols(nodes = None, parent_symbols = None):
    sym = Symbols(parent = parent_symbols)
    visitor = FrameSymbolVisitor(sym)
    for node in nodes:
        visitor.visit(node)
        return sym


def symbols_for_node(node = None, parent_symbols = None):
    sym = Symbols(parent = parent_symbols)
    sym.analyze_node(node)
    return sym


class Symbols:
    
    def __init__(self = None, parent = None, level = None):
        pass
    # WARNING: Decompyle incomplete

    
    def analyze_node(self = None, node = None, **kwargs):
        visitor = RootVisitor(self)
    # WARNING: Decompyle incomplete

    
    def _define_ref(self = None, name = None, load = None):
        ident = f'''l_{self.level}_{name}'''
        self.refs[name] = ident
    # WARNING: Decompyle incomplete

    
    def find_load(self = None, target = None):
        if target in self.loads:
            return self.loads[target]
    # WARNING: Decompyle incomplete

    
    def find_ref(self = None, name = None):
        if name in self.refs:
            return self.refs[name]
    # WARNING: Decompyle incomplete

    
    def ref(self = None, name = None):
        rv = self.find_ref(name)
    # WARNING: Decompyle incomplete

    
    def copy(self = None):
        rv = object.__new__(self.__class__)
        rv.__dict__.update(self.__dict__)
        rv.refs = self.refs.copy()
        rv.loads = self.loads.copy()
        rv.stores = self.stores.copy()
        return rv

    
    def store(self = None, name = None):
        self.stores.add(name)
    # WARNING: Decompyle incomplete

    
    def declare_parameter(self = None, name = None):
        self.stores.add(name)
        return self._define_ref(name, load = (VAR_LOAD_PARAMETER, None))

    
    def load(self = None, name = None):
        pass
    # WARNING: Decompyle incomplete

    
    def branch_update(self = None, branch_symbols = None):
        stores = set()
    # WARNING: Decompyle incomplete

    
    def dump_stores(self = None):
        rv = { }
        node = self
    # WARNING: Decompyle incomplete

    
    def dump_param_targets(self = None):
        rv = set()
        node = self
    # WARNING: Decompyle incomplete



class RootVisitor(NodeVisitor):
    
    def __init__(self = None, symbols = None):
        self.sym_visitor = FrameSymbolVisitor(symbols)

    
    def _simple_visit(self = None, node = None, **kwargs):
        for child in node.iter_child_nodes():
            self.sym_visitor.visit(child)
            return None

    visit_Template = _simple_visit
    visit_Block = _simple_visit
    visit_Macro = _simple_visit
    visit_FilterBlock = _simple_visit
    visit_Scope = _simple_visit
    visit_If = _simple_visit
    visit_ScopedEvalContextModifier = _simple_visit
    
    def visit_AssignBlock(self = None, node = None, **kwargs):
        for child in node.body:
            self.sym_visitor.visit(child)
            return None

    
    def visit_CallBlock(self = None, node = None, **kwargs):
        for child in node.iter_child_nodes(exclude = ('call',)):
            self.sym_visitor.visit(child)
            return None

    
    def visit_OverlayScope(self = None, node = None, **kwargs):
        for child in node.body:
            self.sym_visitor.visit(child)
            return None

    
    def visit_For(self = None, node = None, for_branch = None, **kwargs):
        if for_branch == 'body':
            self.sym_visitor.visit(node.target, store_as_param = True)
            branch = node.body
        elif for_branch == 'else':
            branch = node.else_
    # WARNING: Decompyle incomplete

    
    def visit_With(self = None, node = None, **kwargs):
        for target in node.targets:
            self.sym_visitor.visit(target)
            for child in node.body:
                self.sym_visitor.visit(child)
                return None

    
    def generic_visit(self = None, node = None, *args, **kwargs):
        raise NotImplementedError(f'''Cannot find symbols for {type(node).__name__!r}''')



class FrameSymbolVisitor(NodeVisitor):
    '''A visitor for `Frame.inspect`.'''
    
    def __init__(self = None, symbols = None):
        self.symbols = symbols

    
    def visit_Name(self = None, node = None, store_as_param = None, **kwargs):
        '''All assignments to names go through this function.'''
        if store_as_param or node.ctx == 'param':
            self.symbols.declare_parameter(node.name)
            return None
        if None.ctx == 'store':
            self.symbols.store(node.name)
            return None
        if None.ctx == 'load':
            self.symbols.load(node.name)
            return None

    
    def visit_NSRef(self = None, node = None, **kwargs):
        self.symbols.load(node.name)

    
    def visit_If(self = None, node = None, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def visit_Macro(self = None, node = None, **kwargs):
        self.symbols.store(node.name)

    
    def visit_Import(self = None, node = None, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def visit_FromImport(self = None, node = None, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def visit_Assign(self = None, node = None, **kwargs):
        '''Visit assignments in the correct order.'''
        pass
    # WARNING: Decompyle incomplete

    
    def visit_For(self = None, node = None, **kwargs):
        '''Visiting stops at for blocks.  However the block sequence
        is visited as part of the outer scope.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def visit_CallBlock(self = None, node = None, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def visit_FilterBlock(self = None, node = None, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def visit_With(self = None, node = None, **kwargs):
        for target in node.values:
            self.visit(target)
            return None

    
    def visit_AssignBlock(self = None, node = None, **kwargs):
        '''Stop visiting at block assigns.'''
        pass
    # WARNING: Decompyle incomplete

    
    def visit_Scope(self = None, node = None, **kwargs):
        '''Stop visiting at scopes.'''
        pass

    
    def visit_Block(self = None, node = None, **kwargs):
        '''Stop visiting at blocks.'''
        pass

    
    def visit_OverlayScope(self = None, node = None, **kwargs):
        '''Do not visit into overlay scopes.'''
        pass

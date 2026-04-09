# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: compiler.pyc (Python 3.11)

'''Compiles nodes from the parser into Python code.'''
import typing as t
from contextlib import contextmanager
from functools import update_wrapper
from io import StringIO
from itertools import chain
from keyword import iskeyword as is_python_keyword
from markupsafe import escape
from markupsafe import Markup
from  import nodes
from exceptions import TemplateAssertionError
from idtracking import Symbols
from idtracking import VAR_LOAD_ALIAS
from idtracking import VAR_LOAD_PARAMETER
from idtracking import VAR_LOAD_RESOLVE
from idtracking import VAR_LOAD_UNDEFINED
from nodes import EvalContext
from optimizer import Optimizer
from utils import _PassArg
from utils import concat
from visitor import NodeVisitor
if t.TYPE_CHECKING:
    import typing_extensions as te
    from environment import Environment
F = t.TypeVar('F', bound = t.Callable[(..., t.Any)])
operators = {
    'eq': '==',
    'ne': '!=',
    'gt': '>',
    'gteq': '>=',
    'lt': '<',
    'lteq': '<=',
    'in': 'in',
    'notin': 'not in' }

def optimizeconst(f = None):
    pass
# WARNING: Decompyle incomplete


def _make_binop(op = None):
    pass
# WARNING: Decompyle incomplete


def _make_unop(op = None):
    pass
# WARNING: Decompyle incomplete


def generate(node, environment, name = None, filename = None, stream = None, defer_init = (None, False, True), optimized = ('node', nodes.Template, 'environment', 'Environment', 'name', t.Optional[str], 'filename', t.Optional[str], 'stream', t.Optional[t.TextIO], 'defer_init', bool, 'optimized', bool, 'return', t.Optional[str])):
    '''Generate the python source for a node tree.'''
    if not isinstance(node, nodes.Template):
        raise TypeError("Can't compile non template nodes")
    generator = environment.code_generator_class(environment, name, filename, stream, defer_init, optimized)
    generator.visit(node)
# WARNING: Decompyle incomplete


def has_safe_repr(value = None):
    '''Does the node have a safe representation?'''
    pass
# WARNING: Decompyle incomplete


def find_undeclared(nodes = None, names = None):
    '''Check if the names passed are accessed undeclared.  The return value
    is a set of all the undeclared names from the sequence of names found.
    '''
    visitor = UndeclaredNameVisitor(names)
    
    try:
        for node in nodes:
            visitor.visit(node)
    except VisitorExit:
        pass

    return visitor.undeclared


class MacroRef:
    
    def __init__(self = None, node = None):
        self.node = node
        self.accesses_caller = False
        self.accesses_kwargs = False
        self.accesses_varargs = False



class Frame:
    '''Holds compile time information for us.'''
    
    def __init__(self = None, eval_ctx = None, parent = None, level = (None, None)):
        self.eval_ctx = eval_ctx
        self.parent = parent
    # WARNING: Decompyle incomplete

    
    def copy(self = None):
        '''Create a copy of the current one.'''
        rv = object.__new__(self.__class__)
        rv.__dict__.update(self.__dict__)
        rv.symbols = self.symbols.copy()
        return rv

    
    def inner(self = None, isolated = None):
        '''Return an inner frame.'''
        if isolated:
            return Frame(self.eval_ctx, level = self.symbols.level + 1)
        return None(self.eval_ctx, self)

    
    def soft(self = None):
        """Return a soft frame.  A soft frame may not be modified as
        standalone thing as it shares the resources with the frame it
        was created of, but it's not a rootlevel frame any longer.

        This is only used to implement if-statements and conditional
        expressions.
        """
        rv = self.copy()
        rv.rootlevel = False
        rv.soft_frame = True
        return rv

    __copy__ = copy


class VisitorExit(RuntimeError):
    '''Exception used by the `UndeclaredNameVisitor` to signal a stop.'''
    pass


class DependencyFinderVisitor(NodeVisitor):
    '''A visitor that collects filter and test calls.'''
    
    def __init__(self = None):
        self.filters = set()
        self.tests = set()

    
    def visit_Filter(self = None, node = None):
        self.generic_visit(node)
        self.filters.add(node.name)

    
    def visit_Test(self = None, node = None):
        self.generic_visit(node)
        self.tests.add(node.name)

    
    def visit_Block(self = None, node = None):
        '''Stop visiting at blocks.'''
        pass



class UndeclaredNameVisitor(NodeVisitor):
    '''A visitor that checks if a name is accessed without being
    declared.  This is different from the frame visitor as it will
    not stop at closure frames.
    '''
    
    def __init__(self = None, names = None):
        self.names = set(names)
        self.undeclared = set()

    
    def visit_Name(self = None, node = None):
        if node.ctx == 'load' and node.name in self.names:
            self.undeclared.add(node.name)
            if self.undeclared == self.names:
                raise VisitorExit()
            return None
        None.names.discard(node.name)

    
    def visit_Block(self = None, node = None):
        '''Stop visiting a blocks.'''
        pass



class CompilerExit(Exception):
    """Raised if the compiler encountered a situation where it just
    doesn't make sense to further process the code.  Any block that
    raises such an exception is not further processed.
    """
    pass


class CodeGenerator(NodeVisitor):
    
    def __init__(self, environment, name = None, filename = None, stream = None, defer_init = (None, False, True), optimized = ('environment', 'Environment', 'name', t.Optional[str], 'filename', t.Optional[str], 'stream', t.Optional[t.TextIO], 'defer_init', bool, 'optimized', bool, 'return', None)):
        pass
    # WARNING: Decompyle incomplete

    optimized = (lambda self = None: self.optimizer is not None)()
    
    def fail(self = None, msg = None, lineno = None):
        '''Fail with a :exc:`TemplateAssertionError`.'''
        raise TemplateAssertionError(msg, lineno, self.name, self.filename)

    
    def temporary_identifier(self = None):
        '''Get a new unique identifier.'''
        return f'''t_{self._last_identifier}'''

    
    def buffer(self = None, frame = None):
        '''Enable buffering for the frame from that point onwards.'''
        frame.buffer = self.temporary_identifier()
        self.writeline(f'''{frame.buffer} = []''')

    
    def return_buffer_contents(self = None, frame = None, force_unescaped = None):

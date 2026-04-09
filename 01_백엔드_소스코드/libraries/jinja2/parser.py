# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: parser.pyc (Python 3.11)

'''Parse tokens from the lexer into nodes for the compiler.'''
import typing
import typing as t
from  import nodes
from exceptions import TemplateAssertionError
from exceptions import TemplateSyntaxError
from lexer import describe_token
from lexer import describe_token_expr
if t.TYPE_CHECKING:
    import typing_extensions as te
    from environment import Environment
_ImportInclude = t.TypeVar('_ImportInclude', nodes.Import, nodes.Include)
_MacroCall = t.TypeVar('_MacroCall', nodes.Macro, nodes.CallBlock)
_statement_keywords = frozenset([
    'for',
    'if',
    'block',
    'extends',
    'print',
    'macro',
    'include',
    'from',
    'import',
    'set',
    'with',
    'autoescape'])
_compare_operators = frozenset([
    'eq',
    'ne',
    'lt',
    'lteq',
    'gt',
    'gteq'])
_math_nodes: t.Dict[(str, t.Type[nodes.Expr])] = {
    'add': nodes.Add,
    'sub': nodes.Sub,
    'mul': nodes.Mul,
    'div': nodes.Div,
    'floordiv': nodes.FloorDiv,
    'mod': nodes.Mod }

class Parser:
    """This is the central parsing class Jinja uses.  It's passed to
    extensions and can be used to parse expressions or statements.
    """
    
    def __init__(self, environment = None, source = None, name = None, filename = (None, None, None), state = ('environment', 'Environment', 'source', str, 'name', t.Optional[str], 'filename', t.Optional[str], 'state', t.Optional[str], 'return', None)):
        self.environment = environment
        self.stream = environment._tokenize(source, name, filename, state)
        self.name = name
        self.filename = filename
        self.closed = False
        self.extensions = { }
        for extension in environment.iter_extensions():
            for tag in extension.tags:
                self.extensions[tag] = extension.parse
                self._last_identifier = 0
                self._tag_stack = []
                self._end_token_stack = []
                return None

    
    def fail(self = None, msg = None, lineno = None, exc = (None, TemplateSyntaxError)):
        '''Convenience method that raises `exc` with the message, passed
        line number or last line number as well as the current name and
        filename.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _fail_ut_eof(self = None, name = None, end_token_stack = None, lineno = ('name', t.Optional[str], 'end_token_stack', t.List[t.Tuple[(str, ...)]], 'lineno', t.Optional[int], 'return', 'te.NoReturn')):
        expected = set()
        for exprs in end_token_stack:
            expected.update(map(describe_token_expr, exprs))
            if end_token_stack:
                currently_looking = ' or '.join(map(repr, map(describe_token_expr, end_token_stack[-1])))
            else:
                currently_looking = None
    # WARNING: Decompyle incomplete

    
    def fail_unknown_tag(self = None, name = None, lineno = None):
        '''Called if the parser encounters an unknown tag.  Tries to fail
        with a human readable error message that could help to identify
        the problem.
        '''
        self._fail_ut_eof(name, self._end_token_stack, lineno)

    
    def fail_eof(self = None, end_tokens = None, lineno = None):
        '''Like fail_unknown_tag but for end of template situations.'''
        stack = list(self._end_token_stack)
    # WARNING: Decompyle incomplete

    
    def is_tuple_end(self = None, extra_end_rules = None):
        '''Are we at the end of a tuple?'''
        if self.stream.current.type in ('variable_end', 'block_end', 'rparen'):
            return True
    # WARNING: Decompyle incomplete

    
    def free_identifier(self = None, lineno = None):
        '''Return a new free identifier as :class:`~jinja2.nodes.InternalName`.'''
        object.__new__(nodes.InternalName) = self, self._last_identifier += 1, ._last_identifier
        nodes.Node.__init__(rv, f'''fi{self._last_identifier}''', lineno = lineno)
        return rv

    
    def parse_statement(self = None):
        '''Parse a single statement.'''
        token = self.stream.current
        if token.type != 'name':
            self.fail('tag name expected', token.lineno)
        self._tag_stack.append(token.value)
        pop_tag = True
    # WARNING: Decompyle incomplete

    
    def parse_statements(self = None, end_tokens = None, drop_needle = None):
        '''Parse multiple statements into a list until one of the end tokens
        is reached.  This is used to parse the body of statements as it also
        parses template data if appropriate.  The parser checks first if the
        current token is a colon and skips it if there is one.  Then it checks
        for the block end and parses until if one of the `end_tokens` is
        reached.  Per default the active token in the stream at the end of
        the call is the matched end token.  If this is not wanted `drop_needle`
        can be set to `True` and the end token is removed.
        '''
        self.stream.skip_if('colon')
        self.stream.expect('block_end')
        result = self.subparse(end_tokens)
        if self.stream.current.type == 'eof':
            self.fail_eof(end_tokens)
        if drop_needle:
            next(self.stream)
        return result

    
    def parse_set(self = None):
        '''Parse an assign statement.'''
        lineno = next(self.stream).lineno
        target = self.parse_assign_target(with_namespace = True)
        if self.stream.skip_if('assign'):
            expr = self.parse_tuple()
            return nodes.Assign(target, expr, lineno = lineno)
        filter_node = None.parse_filter(None)
        body = self.parse_statements(('name:endset',), drop_needle = True)
        return nodes.AssignBlock(target, filter_node, body, lineno = lineno)

    
    def parse_for(self = None):
        '''Parse a for loop.'''
        lineno = self.stream.expect('name:for').lineno
        target = self.parse_assign_target(extra_end_rules = ('name:in',))
        self.stream.expect('name:in')
        iter = self.parse_tuple(with_condexpr = False, extra_end_rules = ('name:recursive',))
        test = None
        if self.stream.skip_if('name:if'):
            test = self.parse_expression()
        recursive = self.stream.skip_if('name:recursive')
        body = self.parse_statements(('name:endfor', 'name:else'))
        if next(self.stream).value == 'endfor':
            else_ = []
        else:
            else_ = self.parse_statements(('name:endfor',), drop_needle = True)
        return nodes.For(target, iter, body, else_, test, recursive, lineno = lineno)

    
    def parse_if(self = None):
        '''Parse an if construct.'''
        node = nodes.If(lineno = self.stream.expect('name:if').lineno)
        result = nodes.If(lineno = self.stream.expect('name:if').lineno)
        node.test = self.parse_tuple(with_condexpr = False)
        node.body = self.parse_statements(('name:elif', 'name:else', 'name:endif'))
        node.elif_ = []
        node.else_ = []
        token = next(self.stream)
        if token.test('name:elif'):
            node = nodes.If(lineno = self.stream.current.lineno)
            result.elif_.append(node)
            continue
        if token.test('name:else'):
            result.else_ = self.parse_statements(('name:endif',), drop_needle = True)
        return result

    
    def parse_with(self = None):
        node = nodes.With(lineno = next(self.stream).lineno)
        targets = []
        values = []
    # WARNING: Decompyle incomplete

    
    def parse_autoescape(self = None):
        node = nodes.ScopedEvalContextModifier(lineno = next(self.stream).lineno)
        node.options = [
            nodes.Keyword('autoescape', self.parse_expression())]
        node.body = self.parse_statements(('name:endautoescape',), drop_needle = True)
        return nodes.Scope([
            node])

    
    def parse_block(self = None):
        node = nodes.Block(lineno = next(self.stream).lineno)
        node.name = self.stream.expect('name').value
        node.scoped = self.stream.skip_if('name:scoped')
        node.required = self.stream.skip_if('name:required')
        if self.stream.current.type == 'sub':
            self.fail('Block names in Jinja have to be valid Python identifiers and may not contain hyphens, use an underscore instead.')
        node.body = self.parse_statements(('name:endblock',), drop_needle = True)
        if node.required:
            for body_node in node.body:
                if isinstance(body_node, nodes.Output) or (lambda .0: pass# WARNING: Decompyle incomplete
)(body_node.nodes()):
                    self.fail('Required blocks can only contain comments or whitespace')
                self.stream.skip_if('name:' + node.name)
                return node

    
    def parse_extends(self = None):
        node = nodes.Extends(lineno = next(self.stream).lineno)
        node.template = self.parse_expression()
        return node

    
    def parse_import_context(self = None, node = None, default = None):
        if self.stream.current.test_any('name:with', 'name:without') and self.stream.look().test('name:context'):
            node.with_context = next(self.stream).value == 'with'
            self.stream.skip()
        else:
            node.with_context = default
        return node

    
    def parse_include(self = None):
        node = nodes.Include(lineno = next(self.stream).lineno)
        node.template = self.parse_expression()
        if self.stream.current.test('name:ignore') and self.stream.look().test('name:missing'):
            node.ignore_missing = True
            self.stream.skip(2)
        else:
            node.ignore_missing = False
        return self.parse_import_context(node, True)

    
    def parse_import(self = None):
        node = nodes.Import(lineno = next(self.stream).lineno)
        node.template = self.parse_expression()
        self.stream.expect('name:as')
        node.target = self.parse_assign_target(name_only = True).name
        return self.parse_import_context(node, False)

    
    def parse_from(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def parse_signature(self = None, node = None):
        args = []
        node.args = []
        defaults = []
        node.defaults = []
        self.stream.expect('lparen')
    # WARNING: Decompyle incomplete

    
    def parse_call_block(self = None):
        node = nodes.CallBlock(lineno = next(self.stream).lineno)
        if self.stream.current.type == 'lparen':
            self.parse_signature(node)
        else:
            node.args = []
            node.defaults = []
        call_node = self.parse_expression()
        if not isinstance(call_node, nodes.Call):
            self.fail('expected call', node.lineno)
        node.call = call_node
        node.body = self.parse_statements(('name:endcall',), drop_needle = True)
        return node

    
    def parse_filter_block(self = None):
        node = nodes.FilterBlock(lineno = next(self.stream).lineno)
        node.filter = self.parse_filter(None, start_inline = True)
        node.body = self.parse_statements(('name:endfilter',), drop_needle = True)
        return node

    
    def parse_macro(self = None):
        node = nodes.Macro(lineno = next(self.stream).lineno)
        node.name = self.parse_assign_target(name_only = True).name
        self.parse_signature(node)
        node.body = self.parse_statements(('name:endmacro',), drop_needle = True)
        return node

    
    def parse_print(self = None):
        node = nodes.Output(lineno = next(self.stream).lineno)
        node.nodes = []
    # WARNING: Decompyle incomplete

    parse_assign_target = (lambda self = None, with_tuple = None, name_only = typing.overload: pass)()
    parse_assign_target = (lambda self = None, with_tuple = None, name_only = typing.overload, extra_end_rules = (True, False, None, False), with_namespace = ('with_tuple', bool, 'name_only', bool, 'extra_end_rules', t.Optional[t.Tuple[(str, ...)]], 'with_namespace', bool, 'return', t.Union[(nodes.NSRef, nodes.Name, nodes.Tuple)]): pass)()
    
    def parse_assign_target(self = None, with_tuple = None, name_only = None, extra_end_rules = (True, False, None, False), with_namespace = ('with_tuple', bool, 'name_only', bool, 'extra_end_rules', t.Optional[t.Tuple[(str, ...)]], 'with_namespace', bool, 'return', t.Union[(nodes.NSRef, nodes.Name, nodes.Tuple)])):
        '''Parse an assignment target.  As Jinja allows assignments to
        tuples, this function can parse all allowed assignment targets.  Per
        default assignments to tuples are parsed, that can be disable however
        by setting `with_tuple` to `False`.  If only assignments to names are
        wanted `name_only` can be set to `True`.  The `extra_end_rules`
        parameter is forwarded to the tuple parsing function.  If
        `with_namespace` is enabled, a namespace assignment may be parsed.
        '''
        if name_only:
            token = self.stream.expect('name')
            target = nodes.Name(token.value, 'store', lineno = token.lineno)
        elif with_tuple:
            target = self.parse_tuple(simplified = True, extra_end_rules = extra_end_rules, with_namespace = with_namespace)
        else:
            target = self.parse_primary(with_namespace = with_namespace)
        target.set_ctx('store')
        if not target.can_assign():
            self.fail(f'''can\'t assign to {type(target).__name__.lower()!r}''', target.lineno)
        return target

    
    def parse_expression(self = None, with_condexpr = None):
        '''Parse an expression.  Per default all expressions are parsed, if
        the optional `with_condexpr` parameter is set to `False` conditional
        expressions are not parsed.
        '''
        if with_condexpr:
            return self.parse_condexpr()
        return None.parse_or()

    
    def parse_condexpr(self = None):
        lineno = self.stream.current.lineno
        expr1 = self.parse_or()
    # WARNING: Decompyle incomplete

    
    def parse_or(self = None):
        lineno = self.stream.current.lineno
        left = self.parse_and()
    # WARNING: Decompyle incomplete

    
    def parse_and(self = None):
        lineno = self.stream.current.lineno
        left = self.parse_not()
    # WARNING: Decompyle incomplete

    
    def parse_not(self = None):
        if self.stream.current.test('name:not'):
            lineno = next(self.stream).lineno
            return nodes.Not(self.parse_not(), lineno = lineno)
        return None.parse_compare()

    
    def parse_compare(self = None):
        lineno = self.stream.current.lineno
        expr = self.parse_math1()
        ops = []
        token_type = self.stream.current.type
        if token_type in _compare_operators:
            next(self.stream)
            ops.append(nodes.Operand(token_type, self.parse_math1()))
        elif self.stream.skip_if('name:in'):
            ops.append(nodes.Operand('in', self.parse_math1()))
        elif self.stream.current.test('name:not') and self.stream.look().test('name:in'):
            self.stream.skip(2)
            ops.append(nodes.Operand('notin', self.parse_math1()))
        
        lineno = self.stream.current.lineno
        continue
        if not ops:
            return expr
        return None.Compare(expr, ops, lineno = lineno)

    
    def parse_math1(self = None):
        lineno = self.stream.current.lineno
        left = self.parse_concat()
    # WARNING: Decompyle incomplete

    
    def parse_concat(self = None):
        lineno = self.stream.current.lineno
        args = [
            self.parse_math2()]
    # WARNING: Decompyle incomplete

    
    def parse_math2(self = None):
        lineno = self.stream.current.lineno
        left = self.parse_pow()
    # WARNING: Decompyle incomplete

    
    def parse_pow(self = None):
        lineno = self.stream.current.lineno
        left = self.parse_unary()
    # WARNING: Decompyle incomplete

    
    def parse_unary(self = None, with_filter = None):
        token_type = self.stream.current.type
        lineno = self.stream.current.lineno
        if token_type == 'sub':
            next(self.stream)
            node = nodes.Neg(self.parse_unary(False), lineno = lineno)
        elif token_type == 'add':
            next(self.stream)
            node = nodes.Pos(self.parse_unary(False), lineno = lineno)
        else:
            node = self.parse_primary()
        node = self.parse_postfix(node)
        if with_filter:
            node = self.parse_filter_expr(node)
        return node

    
    def parse_primary(self = None, with_namespace = None):
        '''Parse a name or literal value. If ``with_namespace`` is enabled, also
        parse namespace attr refs, for use in assignments.'''
        token = self.stream.current
        if token.type == 'name':
            next(self.stream)
            if token.value in ('true', 'false', 'True', 'False'):
                node = nodes.Const(token.value in ('true', 'True'), lineno = token.lineno)
            elif token.value in ('none', 'None'):
                node = nodes.Const(None, lineno = token.lineno)
            elif with_namespace and self.stream.current.type == 'dot':
                next(self.stream)
                attr = self.stream.expect('name')
                node = nodes.NSRef(token.value, attr.value, lineno = token.lineno)
            else:
                node = nodes.Name(token.value, 'load', lineno = token.lineno)
    # WARNING: Decompyle incomplete

    
    def parse_tuple(self, simplified = None, with_condexpr = None, extra_end_rules = None, explicit_parentheses = (False, True, None, False, False), with_namespace = ('simplified', bool, 'with_condexpr', bool, 'extra_end_rules', t.Optional[t.Tuple[(str, ...)]], 'explicit_parentheses', bool, 'with_namespace', bool, 'return', t.Union[(nodes.Tuple, nodes.Expr)])):
        """Works like `parse_expression` but if multiple expressions are
        delimited by a comma a :class:`~jinja2.nodes.Tuple` node is created.
        This method could also return a regular expression instead of a tuple
        if no commas where found.

        The default parsing mode is a full tuple.  If `simplified` is `True`
        only names and literals are parsed; ``with_namespace`` allows namespace
        attr refs as well. The `no_condexpr` parameter is forwarded to
        :meth:`parse_expression`.

        Because tuples do not require delimiters and may end in a bogus comma
        an extra hint is needed that marks the end of a tuple.  For example
        for loops support tuples between `for` and `in`.  In that case the
        `extra_end_rules` is set to ``['name:in']``.

        `explicit_parentheses` is true if the parsing was triggered by an
        expression in parentheses.  This is used to figure out if an empty
        tuple is a valid expression or not.
        """
        pass
    # WARNING: Decompyle incomplete

    
    def parse_list(self = None):
        token = self.stream.expect('lbracket')
        items = []
    # WARNING: Decompyle incomplete

    
    def parse_dict(self = None):
        token = self.stream.expect('lbrace')
        items = []
    # WARNING: Decompyle incomplete

    
    def parse_postfix(self = None, node = None):
        token_type = self.stream.current.type
        if token_type == 'dot' or token_type == 'lbracket':
            node = self.parse_subscript(node)
        elif token_type == 'lparen':
            node = self.parse_call(node)
        
        continue
        return node

    
    def parse_filter_expr(self = None, node = None):
        token_type = self.stream.current.type
        if token_type == 'pipe':
            node = self.parse_filter(node)
        elif token_type == 'name' and self.stream.current.value == 'is':
            node = self.parse_test(node)
        elif token_type == 'lparen':
            node = self.parse_call(node)
        
        continue
        return node

    
    def parse_subscript(self = None, node = None):
        token = next(self.stream)
        if token.type == 'dot':
            attr_token = self.stream.current
            next(self.stream)
            if attr_token.type == 'name':
                return nodes.Getattr(node, attr_token.value, 'load', lineno = token.lineno)
            if None.type != 'integer':
                self.fail('expected name or number', attr_token.lineno)
            arg = nodes.Const(attr_token.value, lineno = attr_token.lineno)
            return nodes.Getitem(node, arg, 'load', lineno = token.lineno)
    # WARNING: Decompyle incomplete

    
    def parse_subscribed(self = None):
        lineno = self.stream.current.lineno
        if self.stream.current.type == 'colon':
            next(self.stream)
            args = [
                None]
        else:
            node = self.parse_expression()
            if self.stream.current.type != 'colon':
                return node
            None(self.stream)
            args = [
                node]
        if self.stream.current.type == 'colon':
            args.append(None)
        elif self.stream.current.type not in ('rbracket', 'comma'):
            args.append(self.parse_expression())
        else:
            args.append(None)
        if self.stream.current.type == 'colon':
            next(self.stream)
            if self.stream.current.type not in ('rbracket', 'comma'):
                args.append(self.parse_expression())
            else:
                args.append(None)
        else:
            args.append(None)
    # WARNING: Decompyle incomplete

    
    def parse_call_args(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def parse_call(self = None, node = None):
        token = self.stream.current
        (args, kwargs, dyn_args, dyn_kwargs) = self.parse_call_args()
        return nodes.Call(node, args, kwargs, dyn_args, dyn_kwargs, lineno = token.lineno)

    
    def parse_filter(self = None, node = None, start_inline = None):
        pass
    # WARNING: Decompyle incomplete

    
    def parse_test(self = None, node = None):
        token = next(self.stream)
        if self.stream.current.test('name:not'):
            next(self.stream)
            negated = True
        else:
            negated = False
        name = self.stream.expect('name').value
    # WARNING: Decompyle incomplete

    
    def subparse(self = None, end_tokens = None):
        pass
    # WARNING: Decompyle incomplete

    
    def parse(self = None):
        '''Parse the whole template into a `Template` node.'''
        result = nodes.Template(self.subparse(), lineno = 1)
        result.set_environment(self.environment)
        return result

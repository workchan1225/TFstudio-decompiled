# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: environment.pyc (Python 3.11)

'''Classes for managing templates and their runtime and compile time
options.
'''
import os
import typing
import typing as t
import weakref
from collections import ChainMap
from functools import lru_cache
from functools import partial
from functools import reduce
from types import CodeType
from markupsafe import Markup
from  import nodes
from compiler import CodeGenerator
from compiler import generate
from defaults import BLOCK_END_STRING
from defaults import BLOCK_START_STRING
from defaults import COMMENT_END_STRING
from defaults import COMMENT_START_STRING
from defaults import DEFAULT_FILTERS
from defaults import DEFAULT_NAMESPACE
from defaults import DEFAULT_POLICIES
from defaults import DEFAULT_TESTS
from defaults import KEEP_TRAILING_NEWLINE
from defaults import LINE_COMMENT_PREFIX
from defaults import LINE_STATEMENT_PREFIX
from defaults import LSTRIP_BLOCKS
from defaults import NEWLINE_SEQUENCE
from defaults import TRIM_BLOCKS
from defaults import VARIABLE_END_STRING
from defaults import VARIABLE_START_STRING
from exceptions import TemplateNotFound
from exceptions import TemplateRuntimeError
from exceptions import TemplatesNotFound
from exceptions import TemplateSyntaxError
from exceptions import UndefinedError
from lexer import get_lexer
from lexer import Lexer
from lexer import TokenStream
from nodes import EvalContext
from parser import Parser
from runtime import Context
from runtime import new_context
from runtime import Undefined
from utils import _PassArg
from utils import concat
from utils import consume
from utils import import_string
from utils import internalcode
from utils import LRUCache
from utils import missing
if t.TYPE_CHECKING:
    import typing_extensions as te
    from bccache import BytecodeCache
    from ext import Extension
    from loaders import BaseLoader
_env_bound = t.TypeVar('_env_bound', bound = 'Environment')
get_spontaneous_environment = (lambda cls = None: pass# WARNING: Decompyle incomplete
)()

def create_cache(size = None):
    '''Return the cache class for the given size.'''
    if size == 0:
        return None
    if None < 0:
        return { }
    return None(size)


def copy_cache(cache = None):
    '''Create an empty copy of the given cache.'''
    pass
# WARNING: Decompyle incomplete


def load_extensions(environment = None, extensions = None):
    '''Load the extensions from the list and bind it to the environment.
    Returns a dict of instantiated extensions.
    '''
    result = { }
    for extension in extensions:
        if isinstance(extension, str):
            extension = t.cast(t.Type['Extension'], import_string(extension))
        result[extension.identifier] = extension(environment)
        return result


def _environment_config_check(environment = None):
    '''Perform a sanity check on the environment.'''
    pass
# WARNING: Decompyle incomplete


class Environment:
    """The core component of Jinja is the `Environment`.  It contains
    important shared variables like configuration, filters, tests,
    globals and others.  Instances of this class may be modified if
    they are not shared and if no template was loaded so far.
    Modifications on environments after the first template was loaded
    will lead to surprising effects and undefined behavior.

    Here are the possible initialization parameters:

        `block_start_string`
            The string marking the beginning of a block.  Defaults to ``'{%'``.

        `block_end_string`
            The string marking the end of a block.  Defaults to ``'%}'``.

        `variable_start_string`
            The string marking the beginning of a print statement.
            Defaults to ``'{{'``.

        `variable_end_string`
            The string marking the end of a print statement.  Defaults to
            ``'}}'``.

        `comment_start_string`
            The string marking the beginning of a comment.  Defaults to ``'{#'``.

        `comment_end_string`
            The string marking the end of a comment.  Defaults to ``'#}'``.

        `line_statement_prefix`
            If given and a string, this will be used as prefix for line based
            statements.  See also :ref:`line-statements`.

        `line_comment_prefix`
            If given and a string, this will be used as prefix for line based
            comments.  See also :ref:`line-statements`.

            .. versionadded:: 2.2

        `trim_blocks`
            If this is set to ``True`` the first newline after a block is
            removed (block, not variable tag!).  Defaults to `False`.

        `lstrip_blocks`
            If this is set to ``True`` leading spaces and tabs are stripped
            from the start of a line to a block.  Defaults to `False`.

        `newline_sequence`
            The sequence that starts a newline.  Must be one of ``'\\r'``,
            ``'\\n'`` or ``'\\r\\n'``.  The default is ``'\\n'`` which is a
            useful default for Linux and OS X systems as well as web
            applications.

        `keep_trailing_newline`
            Preserve the trailing newline when rendering templates.
            The default is ``False``, which causes a single newline,
            if present, to be stripped from the end of the template.

            .. versionadded:: 2.7

        `extensions`
            List of Jinja extensions to use.  This can either be import paths
            as strings or extension classes.  For more information have a
            look at :ref:`the extensions documentation <jinja-extensions>`.

        `optimized`
            should the optimizer be enabled?  Default is ``True``.

        `undefined`
            :class:`Undefined` or a subclass of it that is used to represent
            undefined values in the template.

        `finalize`
            A callable that can be used to process the result of a variable
            expression before it is output.  For example one can convert
            ``None`` implicitly into an empty string here.

        `autoescape`
            If set to ``True`` the XML/HTML autoescaping feature is enabled by
            default.  For more details about autoescaping see
            :class:`~markupsafe.Markup`.  As of Jinja 2.4 this can also
            be a callable that is passed the template name and has to
            return ``True`` or ``False`` depending on autoescape should be
            enabled by default.

            .. versionchanged:: 2.4
               `autoescape` can now be a function

        `loader`
            The template loader for this environment.

        `cache_size`
            The size of the cache.  Per default this is ``400`` which means
            that if more than 400 templates are loaded the loader will clean
            out the least recently used template.  If the cache size is set to
            ``0`` templates are recompiled all the time, if the cache size is
            ``-1`` the cache will not be cleaned.

            .. versionchanged:: 2.8
               The cache size was increased to 400 from a low 50.

        `auto_reload`
            Some loaders load templates from locations where the template
            sources may change (ie: file system or database).  If
            ``auto_reload`` is set to ``True`` (default) every time a template is
            requested the loader checks if the source changed and if yes, it
            will reload the template.  For higher performance it's possible to
            disable that.

        `bytecode_cache`
            If set to a bytecode cache object, this object will provide a
            cache for the internal Jinja bytecode so that templates don't
            have to be parsed if they were not changed.

            See :ref:`bytecode-cache` for more information.

        `enable_async`
            If set to true this enables async template execution which
            allows using async functions and generators.
    """
    sandboxed = False
    overlayed = False
    linked_to: t.Optional['Environment'] = None
    shared = False
    code_generator_class: t.Type['CodeGenerator'] = CodeGenerator
    concat = ''.join
    template_class: t.Type['Template'] = Context
    
    def __init__(self, block_start_string, block_end_string, variable_start_string, variable_end_string, comment_start_string, comment_end_string, line_statement_prefix, line_comment_prefix, trim_blocks, lstrip_blocks, newline_sequence, keep_trailing_newline, extensions, optimized, undefined, finalize, autoescape, loader = None, cache_size = None, auto_reload = None, bytecode_cache = (BLOCK_START_STRING, BLOCK_END_STRING, VARIABLE_START_STRING, VARIABLE_END_STRING, COMMENT_START_STRING, COMMENT_END_STRING, LINE_STATEMENT_PREFIX, LINE_COMMENT_PREFIX, TRIM_BLOCKS, LSTRIP_BLOCKS, NEWLINE_SEQUENCE, KEEP_TRAILING_NEWLINE, (), True, Undefined, None, False, None, 400, True, None, False), enable_async = ('block_start_string', str, 'block_end_string', str, 'variable_start_string', str, 'variable_end_string', str, 'comment_start_string', str, 'comment_end_string', str, 'line_statement_prefix', t.Optional[str], 'line_comment_prefix', t.Optional[str], 'trim_blocks', bool, 'lstrip_blocks', bool, 'newline_sequence', "te.Literal['\\n', '\\r\\n', '\\r']", 'keep_trailing_newline', bool, 'extensions', t.Sequence[t.Union[(str, t.Type['Extension'])]], 'optimized', bool, 'undefined', t.Type[Undefined], 'finalize', t.Optional[t.Callable[(..., t.Any)]], 'autoescape', t.Union[(bool, t.Callable[([
        t.Optional[str]], bool)])], 'loader', t.Optional['BaseLoader'], 'cache_size', int, 'auto_reload', bool, 'bytecode_cache', t.Optional['BytecodeCache'], 'enable_async', bool)):
        self.block_start_string = block_start_string
        self.block_end_string = block_end_string
        self.variable_start_string = variable_start_string
        self.variable_end_string = variable_end_string
        self.comment_start_string = comment_start_string
        self.comment_end_string = comment_end_string
        self.line_statement_prefix = line_statement_prefix
        self.line_comment_prefix = line_comment_prefix
        self.trim_blocks = trim_blocks
        self.lstrip_blocks = lstrip_blocks
        self.newline_sequence = newline_sequence
        self.keep_trailing_newline = keep_trailing_newline
        self.undefined = undefined
        self.optimized = optimized
        self.finalize = finalize
        self.autoescape = autoescape
        self.filters = DEFAULT_FILTERS.copy()
        self.tests = DEFAULT_TESTS.copy()
        self.globals = DEFAULT_NAMESPACE.copy()
        self.loader = loader
        self.cache = create_cache(cache_size)
        self.bytecode_cache = bytecode_cache
        self.auto_reload = auto_reload
        self.policies = DEFAULT_POLICIES.copy()
        self.extensions = load_extensions(self, extensions)
        self.is_async = enable_async
        _environment_config_check(self)

    
    def add_extension(self = None, extension = None):
        '''Adds an extension after the environment was created.

        .. versionadded:: 2.5
        '''
        self.extensions.update(load_extensions(self, [
            extension]))

    
    def extend(self = None, **attributes):
        '''Add the items to the instance of the environment if they do not exist
        yet.  This is used by :ref:`extensions <writing-extensions>` to register
        callbacks and configuration values without breaking inheritance.
        '''
        for key, value in attributes.items():
            if not hasattr(self, key):
                setattr(self, key, value)
            return None

    
    def overlay(self, block_start_string, block_end_string, variable_start_string, variable_end_string, comment_start_string, comment_end_string, line_statement_prefix, line_comment_prefix, trim_blocks, lstrip_blocks, newline_sequence, keep_trailing_newline, extensions, optimized, undefined, finalize, autoescape, loader = None, cache_size = None, auto_reload = None, bytecode_cache = (missing, missing, missing, missing, missing, missing, missing, missing, missing, missing, missing, missing, missing, missing, missing, missing, missing, missing, missing, missing, missing, missing), enable_async = ('block_start_string', str, 'block_end_string', str, 'variable_start_string', str, 'variable_end_string', str, 'comment_start_string', str, 'comment_end_string', str, 'line_statement_prefix', t.Optional[str], 'line_comment_prefix', t.Optional[str], 'trim_blocks', bool, 'lstrip_blocks', bool, 'newline_sequence', "te.Literal['\\n', '\\r\\n', '\\r']", 'keep_trailing_newline', bool, 'extensions', t.Sequence[t.Union[(str, t.Type['Extension'])]], 'optimized', bool, 'undefined', t.Type[Undefined], 'finalize', t.Optional[t.Callable[(..., t.Any)]], 'autoescape', t.Union[(bool, t.Callable[([
        t.Optional[str]], bool)])], 'loader', t.Optional['BaseLoader'], 'cache_size', int, 'auto_reload', bool, 'bytecode_cache', t.Optional['BytecodeCache'], 'enable_async', bool, 'return', 'te.Self')):
        '''Create a new overlay environment that shares all the data with the
        current environment except for cache and the overridden attributes.
        Extensions cannot be removed for an overlayed environment.  An overlayed
        environment automatically gets all the extensions of the environment it
        is linked to plus optional extra extensions.

        Creating overlays should happen after the initial environment was set
        up completely.  Not all attributes are truly linked, some are just
        copied over so modifications on the original environment may not shine
        through.

        .. versionchanged:: 3.1.5
            ``enable_async`` is applied correctly.

        .. versionchanged:: 3.1.2
            Added the ``newline_sequence``, ``keep_trailing_newline``,
            and ``enable_async`` parameters to match ``__init__``.
        '''
        args = dict(locals())
        del args['self']
        del args['cache_size']
        del args['extensions']
        del args['enable_async']
        rv = object.__new__(self.__class__)
        rv.__dict__.update(self.__dict__)
        rv.overlayed = True
        rv.linked_to = self
        for key, value in args.items():
            if value is not missing:
                setattr(rv, key, value)
            if cache_size is not missing:
                rv.cache = create_cache(cache_size)
            else:
                rv.cache = copy_cache(self.cache)
        rv.extensions = { }
        for key, value in self.extensions.items():
            rv.extensions[key] = value.bind(rv)
            if extensions is not missing:
                rv.extensions.update(load_extensions(rv, extensions))
        if enable_async is not missing:
            rv.is_async = enable_async
        return _environment_config_check(rv)

    lexer = (lambda self = None: get_lexer(self))()
    
    def iter_extensions(self = None):
        '''Iterates over the extensions by priority.'''
        return iter(sorted(self.extensions.values(), key = (lambda x: x.priority)))

    
    def getitem(self = None, obj = None, argument = None):
        '''Get an item or attribute of an object but prefer the item.'''
        
        try:
            return obj[argument]
        except (AttributeError, TypeError, LookupError):
            if isinstance(argument, str):
                attr = str(argument)
                return 
            except AttributeError:
                pass
            except Exception:
                pass
            return 


    
    def getattr(self = None, obj = None, attribute = None):
        '''Get an item or attribute of an object but prefer the attribute.
        Unlike :meth:`getitem` the attribute *must* be a string.
        '''
        
        try:
            return getattr(obj, attribute)
        except AttributeError:
            pass

        
        try:
            return obj[attribute]
        except (TypeError, LookupError, AttributeError):
            return 


    
    def _filter_test_common(self, name, value, args, kwargs = None, context = None, eval_ctx = None, is_filter = ('name', t.Union[(str, Undefined)], 'value', t.Any, 'args', t.Optional[t.Sequence[t.Any]], 'kwargs', t.Optional[t.Mapping[(str, t.Any)]], 'context', t.Optional[Context], 'eval_ctx', t.Optional[EvalContext], 'is_filter', bool, 'return', t.Any)):
        if is_filter:
            env_map = self.filters
            type_name = 'filter'
        else:
            env_map = self.tests
            type_name = 'test'
        func = env_map.get(name)
    # WARNING: Decompyle incomplete

    
    def call_filter(self, name, value = None, args = None, kwargs = None, context = (None, None, None, None), eval_ctx = ('name', str, 'value', t.Any, 'args', t.Optional[t.Sequence[t.Any]], 'kwargs', t.Optional[t.Mapping[(str, t.Any)]], 'context', t.Optional[Context], 'eval_ctx', t.Optional[EvalContext], 'return', t.Any)):
        """Invoke a filter on a value the same way the compiler does.

        This might return a coroutine if the filter is running from an
        environment in async mode and the filter supports async
        execution. It's your responsibility to await this if needed.

        .. versionadded:: 2.7
        """
        return self._filter_test_common(name, value, args, kwargs, context, eval_ctx, True)

    
    def call_test(self, name, value = None, args = None, kwargs = None, context = (None, None, None, None), eval_ctx = ('name', str, 'value', t.Any, 'args', t.Optional[t.Sequence[t.Any]], 'kwargs', t.Optional[t.Mapping[(str, t.Any)]], 'context', t.Optional[Context], 'eval_ctx', t.Optional[EvalContext], 'return', t.Any)):
        """Invoke a test on a value the same way the compiler does.

        This might return a coroutine if the test is running from an
        environment in async mode and the test supports async execution.
        It's your responsibility to await this if needed.

        .. versionchanged:: 3.0
            Tests support ``@pass_context``, etc. decorators. Added
            the ``context`` and ``eval_ctx`` parameters.

        .. versionadded:: 2.7
        """
        return self._filter_test_common(name, value, args, kwargs, context, eval_ctx, False)

    parse = (lambda self = None, source = None, name = internalcode, filename = (None, None): try:
self._parse(source, name, filename)except TemplateSyntaxError:
self.handle_exception(source = source)None)()
    
    def _parse(self = None, source = None, name = None, filename = ('source', str, 'name', t.Optional[str], 'filename', t.Optional[str], 'return', nodes.Template)):
        '''Internal parsing function used by `parse` and `compile`.'''
        return Parser(self, source, name, filename).parse()

    
    def lex(self = None, source = None, name = None, filename = (None, None)):
        '''Lex the given sourcecode and return a generator that yields
        tokens as tuples in the form ``(lineno, token_type, value)``.
        This can be useful for :ref:`extension development <writing-extensions>`
        and debugging templates.

        This does not perform preprocessing.  If you want the preprocessing
        of the extensions to be applied you have to filter source through
        the :meth:`preprocess` method.
        '''
        source = str(source)
        
        try:
            return self.lexer.tokeniter(source, name, filename)
        except TemplateSyntaxError:
            self.handle_exception(source = source)
            return None


    
    def preprocess(self = None, source = None, name = None, filename = (None, None)):
        '''Preprocesses the source with all extensions.  This is automatically
        called for all parsing and compiling methods but *not* for :meth:`lex`
        because there you usually only want the actual source tokenized.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _tokenize(self = None, source = None, name = None, filename = (None, None), state = ('source', str, 'name', t.Optional[str], 'filename', t.Optional[str], 'state', t.Optional[str], 'return', TokenStream)):
        '''Called by the parser to do the preprocessing and filtering
        for all the extensions.  Returns a :class:`~jinja2.lexer.TokenStream`.
        '''
        source = self.preprocess(source, name, filename)
        stream = self.lexer.tokenize(source, name, filename, state)
        for ext in self.iter_extensions():
            stream = ext.filter_stream(stream)
            if not isinstance(stream, TokenStream):
                stream = TokenStream(stream, name, filename)
            return stream

    
    def _generate(self = None, source = None, name = None, filename = (False,), defer_init = ('source', nodes.Template, 'name', t.Optional[str], 'filename', t.Optional[str], 'defer_init', bool, 'return', str)):
        '''Internal hook that can be overridden to hook a different generate
        method in.

        .. versionadded:: 2.5
        '''
        return generate(source, self, name, filename, defer_init = defer_init, optimized = self.optimized)

    
    def _compile(self = None, source = None, filename = None):
        '''Internal hook that can be overridden to hook a different compile
        method in.

        .. versionadded:: 2.5
        '''
        return compile(source, filename, 'exec')

    compile = (lambda self, source = None, name = None, filename = typing.overload, raw = (None, None, False, False), defer_init = ('source', t.Union[(str, nodes.Template)], 'name', t.Optional[str], 'filename', t.Optional[str], 'raw', 'te.Literal[False]', 'defer_init', bool, 'return', CodeType): pass)()
    compile = (lambda self, source = None, name = None, filename = typing.overload, raw = (None, None, ..., False), defer_init = ('source', t.Union[(str, nodes.Template)], 'name', t.Optional[str], 'filename', t.Optional[str], 'raw', 'te.Literal[True]', 'defer_init', bool, 'return', str): pass)()
    compile = (lambda self, source = None, name = None, filename = internalcode, raw = (None, None, False, False), defer_init = ('source', t.Union[(str, nodes.Template)], 'name', t.Optional[str], 'filename', t.Optional[str], 'raw', bool, 'defer_init', bool, 'return', t.Union[(str, CodeType)]): source_hint = None# WARNING: Decompyle incomplete
)()
    
    def compile_expression(self = None, source = None, undefined_to_none = None):
        '''A handy helper method that returns a callable that accepts keyword
        arguments that appear as variables in the expression.  If called it
        returns the result of the expression.

        This is useful if applications want to use the same rules as Jinja
        in template "configuration files" or similar situations.

        Example usage:

        >>> env = Environment()
        >>> expr = env.compile_expression(\'foo == 42\')
        >>> expr(foo=23)
        False
        >>> expr(foo=42)
        True

        Per default the return value is converted to `None` if the
        expression returns an undefined value.  This can be changed
        by setting `undefined_to_none` to `False`.

        >>> env.compile_expression(\'var\')() is None
        True
        >>> env.compile_expression(\'var\', undefined_to_none=False)()
        Undefined

        .. versionadded:: 2.1
        '''
        parser = Parser(self, source, state = 'variable')
        
        try:
            expr = parser.parse_expression()
            if not parser.stream.eos:
                raise TemplateSyntaxError('chunk after expression', parser.stream.current.lineno, None, None)
            expr.set_environment(self)
        except TemplateSyntaxError:
            self.handle_exception(source = source)

        body = [
            nodes.Assign(nodes.Name('result', 'store'), expr, lineno = 1)]
        template = self.from_string(nodes.Template(body, lineno = 1))
        return TemplateExpression(template, undefined_to_none)

    
    def compile_templates(self, target, extensions = None, filter_func = None, zip = None, log_function = (None, None, 'deflated', None, True), ignore_errors = ('target', t.Union[(str, 'os.PathLike[str]')], 'extensions', t.Optional[t.Collection[str]], 'filter_func', t.Optional[t.Callable[([
        str], bool)]], 'zip', t.Optional[str], 'log_function', t.Optional[t.Callable[([
        str], None)]], 'ignore_errors', bool, 'return', None)):
        """Finds all the templates the loader can find, compiles them
        and stores them in `target`.  If `zip` is `None`, instead of in a
        zipfile, the templates will be stored in a directory.
        By default a deflate zip algorithm is used. To switch to
        the stored algorithm, `zip` can be set to ``'stored'``.

        `extensions` and `filter_func` are passed to :meth:`list_templates`.
        Each template returned will be compiled to the target folder or
        zipfile.

        By default template compilation errors are ignored.  In case a
        log function is provided, errors are logged.  If you want template
        syntax errors to abort the compilation you can set `ignore_errors`
        to `False` and you will get an exception on syntax errors.

        .. versionadded:: 2.4
        """
        pass
    # WARNING: Decompyle incomplete

    
    def list_templates(self = None, extensions = None, filter_func = None):
        """Returns a list of templates for this environment.  This requires
        that the loader supports the loader's
        :meth:`~BaseLoader.list_templates` method.

        If there are other files in the template folder besides the
        actual templates, the returned list can be filtered.  There are two
        ways: either `extensions` is set to a list of file extensions for
        templates, or a `filter_func` can be provided which is a callable that
        is passed a template name and should return `True` if it should end up
        in the result list.

        If the loader does not support that, a :exc:`TypeError` is raised.

        .. versionadded:: 2.4
        """
        pass
    # WARNING: Decompyle incomplete

    
    def handle_exception(self = None, source = None):
        '''Exception handling helper.  This is used internally to either raise
        rewritten exceptions or return a rendered traceback for the template.
        '''
        rewrite_traceback_stack = rewrite_traceback_stack
        import debug
        raise rewrite_traceback_stack(source = source)

    
    def join_path(self = None, template = None, parent = None):
        '''Join a template with the parent.  By default all the lookups are
        relative to the loader root so this method returns the `template`
        parameter unchanged, but if the paths should be relative to the
        parent template, this function can be used to calculate the real
        template name.

        Subclasses may override this method and implement template path
        joining here.
        '''
        return template

    _load_template = (lambda self = None, name = None, globals = internalcode: pass# WARNING: Decompyle incomplete
)()
    get_template = (lambda self = None, name = None, parent = internalcode, globals = (None, None): if isinstance(name, Template):
name# WARNING: Decompyle incomplete
)()
    select_template = (lambda self = None, names = None, parent = internalcode, globals = (None, None): if isinstance(names, Undefined):
names._fail_with_undefined_error()if not names:
raise TemplatesNotFound(message = 'Tried to select from an empty list of templates.')# WARNING: Decompyle incomplete
)()
    get_or_select_template = (lambda self = None, template_name_or_list = None, parent = internalcode, globals = (None, None): if isinstance(template_name_or_list, (str, Undefined)):
self.get_template(template_name_or_list, parent, globals)if None(template_name_or_list, Template):
template_name_or_listNone.select_template(template_name_or_list, parent, globals))()
    
    def from_string(self = None, source = None, globals = None, template_class = (None, None)):

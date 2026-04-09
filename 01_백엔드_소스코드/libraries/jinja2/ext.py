# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ext.pyc (Python 3.11)

'''Extension API for adding custom tags and behavior.'''
import pprint
import re
import typing as t
from markupsafe import Markup
from  import defaults
from  import nodes
from environment import Environment
from exceptions import TemplateAssertionError
from exceptions import TemplateSyntaxError
from runtime import concat
from runtime import Context
from runtime import Undefined
from utils import import_string
from utils import pass_context
if t.TYPE_CHECKING:
    import typing_extensions as te
    from lexer import Token
    from lexer import TokenStream
    from parser import Parser
    
    class _TranslationsBasic(te.Protocol):
        
        def gettext(self = None, message = None):
            pass

        
        def ngettext(self = None, singular = None, plural = None, n = ('singular', str, 'plural', str, 'n', int, 'return', str)):
            pass


    
    class _TranslationsContext(_TranslationsBasic):
        
        def pgettext(self = None, context = None, message = None):
            pass

        
        def npgettext(self, context = None, singular = None, plural = None, n = ('context', str, 'singular', str, 'plural', str, 'n', int, 'return', str)):
            pass


    _SupportedTranslations = t.Union[(_TranslationsBasic, _TranslationsContext)]
GETTEXT_FUNCTIONS: t.Tuple[(str, ...)] = ('_', 'gettext', 'ngettext', 'pgettext', 'npgettext')
_ws_re = re.compile('\\s*\\n\\s*')

class Extension:
    identifier: t.ClassVar[str] = 'Extensions can be used to add extra functionality to the Jinja template\n    system at the parser level.  Custom extensions are bound to an environment\n    but may not store environment specific data on `self`.  The reason for\n    this is that an extension can be bound to another environment (for\n    overlays) by creating a copy and reassigning the `environment` attribute.\n\n    As extensions are created by the environment they cannot accept any\n    arguments for configuration.  One may want to work around that by using\n    a factory function, but that is not possible as extensions are identified\n    by their import name.  The correct way to configure the extension is\n    storing the configuration values on the environment.  Because this way the\n    environment ends up acting as central configuration storage the\n    attributes may clash which is why extensions have to ensure that the names\n    they choose for configuration are not too generic.  ``prefix`` for example\n    is a terrible name, ``fragment_cache_prefix`` on the other hand is a good\n    name as includes the name of the extension (fragment cache).\n    '
    
    def __init_subclass__(cls = None):
        cls.identifier = f'''{cls.__module__}.{cls.__name__}'''

    tags: t.Set[str] = set()
    priority = 100
    
    def __init__(self = None, environment = None):
        self.environment = environment

    
    def bind(self = None, environment = None):
        '''Create a copy of this extension bound to another environment.'''
        rv = object.__new__(self.__class__)
        rv.__dict__.update(self.__dict__)
        rv.environment = environment
        return rv

    
    def preprocess(self = None, source = None, name = None, filename = (None,)):
        '''This method is called before the actual lexing and can be used to
        preprocess the source.  The `filename` is optional.  The return value
        must be the preprocessed source.
        '''
        return source

    
    def filter_stream(self = None, stream = None):
        """It's passed a :class:`~jinja2.lexer.TokenStream` that can be used
        to filter tokens returned.  This method has to return an iterable of
        :class:`~jinja2.lexer.Token`\\s, but it doesn't have to return a
        :class:`~jinja2.lexer.TokenStream`.
        """
        return stream

    
    def parse(self = None, parser = None):
        '''If any of the :attr:`tags` matched this method is called with the
        parser as first argument.  The token the parser stream is pointing at
        is the name token that matched.  This method has to return one or a
        list of multiple nodes.
        '''
        raise NotImplementedError()

    
    def attr(self = None, name = None, lineno = None):
        """Return an attribute node for the current extension.  This is useful
        to pass constants on extensions to generated template code.

        ::

            self.attr('_my_attribute', lineno=lineno)
        """
        return nodes.ExtensionAttribute(self.identifier, name, lineno = lineno)

    
    def call_method(self, name, args = None, kwargs = None, dyn_args = None, dyn_kwargs = (None, None, None, None, None), lineno = ('name', str, 'args', t.Optional[t.List[nodes.Expr]], 'kwargs', t.Optional[t.List[nodes.Keyword]], 'dyn_args', t.Optional[nodes.Expr], 'dyn_kwargs', t.Optional[nodes.Expr], 'lineno', t.Optional[int], 'return', nodes.Call)):
        '''Call a method of the extension.  This is a shortcut for
        :meth:`attr` + :class:`jinja2.nodes.Call`.
        '''
        pass
    # WARNING: Decompyle incomplete


_gettext_alias = (lambda __context = None: pass# WARNING: Decompyle incomplete
)()

def _make_new_gettext(func = None):
    pass
# WARNING: Decompyle incomplete


def _make_new_ngettext(func = None):
    pass
# WARNING: Decompyle incomplete


def _make_new_pgettext(func = None):
    pass
# WARNING: Decompyle incomplete


def _make_new_npgettext(func = None):
    pass
# WARNING: Decompyle incomplete


class InternationalizationExtension(Extension):
    pass
# WARNING: Decompyle incomplete


class ExprStmtExtension(Extension):
    """Adds a `do` tag to Jinja that works like the print statement just
    that it doesn't print the return value.
    """
    tags = {
        'do'}
    
    def parse(self = None, parser = None):
        node = nodes.ExprStmt(lineno = next(parser.stream).lineno)
        node.node = parser.parse_tuple()
        return node



class LoopControlExtension(Extension):
    '''Adds break and continue to the template engine.'''
    tags = {
        'break',
        'continue'}
    
    def parse(self = None, parser = None):
        token = next(parser.stream)
        if token.value == 'break':
            return nodes.Break(lineno = token.lineno)
        return None.Continue(lineno = token.lineno)



class DebugExtension(Extension):
    """A ``{% debug %}`` tag that dumps the available variables,
    filters, and tests.

    .. code-block:: html+jinja

        <pre>{% debug %}</pre>

    .. code-block:: text

        {'context': {'cycler': <class 'jinja2.utils.Cycler'>,
                     ...,
                     'namespace': <class 'jinja2.utils.Namespace'>},
         'filters': ['abs', 'attr', 'batch', 'capitalize', 'center', 'count', 'd',
                     ..., 'urlencode', 'urlize', 'wordcount', 'wordwrap', 'xmlattr'],
         'tests': ['!=', '<', '<=', '==', '>', '>=', 'callable', 'defined',
                   ..., 'odd', 'sameas', 'sequence', 'string', 'undefined', 'upper']}

    .. versionadded:: 2.11.0
    """
    tags = {
        'debug'}
    
    def parse(self = None, parser = None):
        lineno = parser.stream.expect('name:debug').lineno
        context = nodes.ContextReference()
        result = self.call_method('_render', [
            context], lineno = lineno)
        return nodes.Output([
            result], lineno = lineno)

    
    def _render(self = None, context = None):
        result = {
            'context': context.get_all(),
            'filters': sorted(self.environment.filters.keys()),
            'tests': sorted(self.environment.tests.keys()) }
        return pprint.pformat(result, depth = 3, compact = True)



def extract_from_ast(ast = None, gettext_functions = None, babel_style = None):
    '''Extract localizable strings from the given template node.  Per
    default this function returns matches in babel style that means non string
    parameters as well as keyword arguments are returned as `None`.  This
    allows Babel to figure out what you really meant if you are using
    gettext functions that allow keyword arguments for placeholder expansion.
    If you don\'t want that behavior set the `babel_style` parameter to `False`
    which causes only strings to be returned and parameters are always stored
    in tuples.  As a consequence invalid gettext calls (calls without a single
    string parameter or string parameters after non-string parameters) are
    skipped.

    This example explains the behavior:

    >>> from jinja2 import Environment
    >>> env = Environment()
    >>> node = env.parse(\'{{ (_("foo"), _(), ngettext("foo", "bar", 42)) }}\')
    >>> list(extract_from_ast(node))
    [(1, \'_\', \'foo\'), (1, \'_\', ()), (1, \'ngettext\', (\'foo\', \'bar\', None))]
    >>> list(extract_from_ast(node, babel_style=False))
    [(1, \'_\', (\'foo\',)), (1, \'ngettext\', (\'foo\', \'bar\'))]

    For every string found this function yields a ``(lineno, function,
    message)`` tuple, where:

    * ``lineno`` is the number of the line on which the string was found,
    * ``function`` is the name of the ``gettext`` function used (if the
      string was extracted from embedded Python code), and
    *   ``message`` is the string, or a tuple of strings for functions
         with multiple string arguments.

    This extraction function operates on the AST and is because of that unable
    to extract any comments.  For comment support you have to use the babel
    extraction interface or extract comments yourself.
    '''
    pass
# WARNING: Decompyle incomplete


class _CommentFinder:
    '''Helper class to find comments in a token stream.  Can only
    find comments for gettext calls forwards.  Once the comment
    from line 4 is found, a comment for line 1 will not return a
    usable value.
    '''
    
    def __init__(self = None, tokens = None, comment_tags = None):
        self.tokens = tokens
        self.comment_tags = comment_tags
        self.offset = 0
        self.last_lineno = 0

    
    def find_backwards(self = None, offset = None):
        
        try:
            for _, token_type, token_value in reversed(self.tokens[self.offset:offset]):
                if token_type in ('comment', 'linecomment'):
                    (prefix, comment) = token_value.split(None, 1)
                    
                    try:
                        pass
                    except ValueError:
                        
                        try:
                            continue
                            
                            try:
                                if prefix in self.comment_tags:
                                    
                                    return offset
                                offset = []
                                return None
                            except:
                                self.offset = offset





    
    def find_comments(self = None, lineno = None):
        if self.comment_tags or self.last_lineno > lineno:
            return []
        for token_lineno, _, _ in None(self.tokens[self.offset:]):
            if token_lineno > lineno:
                
                return None, self.find_backwards(self.offset + idx)
            return self.find_backwards(len(self.tokens))



def babel_extract(fileobj = None, keywords = None, comment_tags = None, options = ('fileobj', t.BinaryIO, 'keywords', t.Sequence[str], 'comment_tags', t.Sequence[str], 'options', t.Dict[(str, t.Any)], 'return', t.Iterator[t.Tuple[(int, str, t.Union[(t.Optional[str], t.Tuple[(t.Optional[str], ...)])], t.List[str])]])):
    '''Babel extraction method for Jinja templates.

    .. versionchanged:: 2.3
       Basic support for translation comments was added.  If `comment_tags`
       is now set to a list of keywords for extraction, the extractor will
       try to find the best preceding comment that begins with one of the
       keywords.  For best results, make sure to not have more than one
       gettext call in one line of code and the matching comment in the
       same line or the line before.

    .. versionchanged:: 2.5.1
       The `newstyle_gettext` flag can be set to `True` to enable newstyle
       gettext calls.

    .. versionchanged:: 2.7
       A `silent` option can now be provided.  If set to `False` template
       syntax errors are propagated instead of being ignored.

    :param fileobj: the file-like object the messages should be extracted from
    :param keywords: a list of keywords (i.e. function names) that should be
                     recognized as translation functions
    :param comment_tags: a list of translator tags to search for and include
                         in the results.
    :param options: a dictionary of additional options (optional)
    :return: an iterator over ``(lineno, funcname, message, comments)`` tuples.
             (comments will be empty currently)
    '''
    pass
# WARNING: Decompyle incomplete

i18n = InternationalizationExtension
do = ExprStmtExtension
loopcontrols = LoopControlExtension
debug = DebugExtension

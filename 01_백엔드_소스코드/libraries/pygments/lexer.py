# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: lexer.pyc (Python 3.11)

'''
    pygments.lexer
    ~~~~~~~~~~~~~~

    Base lexer classes.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
import re
import sys
import time
from pygments.filter import apply_filters, Filter
from pygments.filters import get_filter_by_name
from pygments.token import Error, Text, Other, Whitespace, _TokenType
from pygments.util import get_bool_opt, get_int_opt, get_list_opt, make_analysator, Future, guess_decode
from pygments.regexopt import regex_opt
__all__ = [
    'Lexer',
    'RegexLexer',
    'ExtendedRegexLexer',
    'DelegatingLexer',
    'LexerContext',
    'include',
    'inherit',
    'bygroups',
    'using',
    'this',
    'default',
    'words',
    'line_re']
line_re = re.compile('.*?\n')
_encoding_map = [
    (b'\xef\xbb\xbf', 'utf-8'),
    (b'\xff\xfe\x00\x00', 'utf-32'),
    (b'\x00\x00\xfe\xff', 'utf-32be'),
    (b'\xff\xfe', 'utf-16'),
    (b'\xfe\xff', 'utf-16be')]
_default_analyse = staticmethod((lambda x: 0))

class LexerMeta(type):
    '''
    This metaclass automagically converts ``analyse_text`` methods into
    static methods which always return float values.
    '''
    
    def __new__(mcs, name, bases, d):
        if 'analyse_text' in d:
            d['analyse_text'] = make_analysator(d['analyse_text'])
        return type.__new__(mcs, name, bases, d)



def Lexer():
    '''Lexer'''
    __doc__ = "\n    Lexer for a specific language.\n\n    See also :doc:`lexerdevelopment`, a high-level guide to writing\n    lexers.\n\n    Lexer classes have attributes used for choosing the most appropriate\n    lexer based on various criteria.\n\n    .. autoattribute:: name\n       :no-value:\n    .. autoattribute:: aliases\n       :no-value:\n    .. autoattribute:: filenames\n       :no-value:\n    .. autoattribute:: alias_filenames\n    .. autoattribute:: mimetypes\n       :no-value:\n    .. autoattribute:: priority\n\n    Lexers included in Pygments should have two additional attributes:\n\n    .. autoattribute:: url\n       :no-value:\n    .. autoattribute:: version_added\n       :no-value:\n\n    Lexers included in Pygments may have additional attributes:\n\n    .. autoattribute:: _example\n       :no-value:\n\n    You can pass options to the constructor. The basic options recognized\n    by all lexers and processed by the base `Lexer` class are:\n\n    ``stripnl``\n        Strip leading and trailing newlines from the input (default: True).\n    ``stripall``\n        Strip all leading and trailing whitespace from the input\n        (default: False).\n    ``ensurenl``\n        Make sure that the input ends with a newline (default: True).  This\n        is required for some lexers that consume input linewise.\n\n        .. versionadded:: 1.3\n\n    ``tabsize``\n        If given and greater than 0, expand tabs in the input (default: 0).\n    ``encoding``\n        If given, must be an encoding name. This encoding will be used to\n        convert the input string to Unicode, if it is not already a Unicode\n        string (default: ``'guess'``, which uses a simple UTF-8 / Locale /\n        Latin1 detection.  Can also be ``'chardet'`` to use the chardet\n        library, if it is installed.\n    ``inencoding``\n        Overrides the ``encoding`` if given.\n    "
    name = None
    aliases = []
    filenames = []
    alias_filenames = []
    mimetypes = []
    priority = 0
    url = None
    version_added = None
    _example = None
    
    def __init__(self, **options):
        """
        This constructor takes arbitrary options as keyword arguments.
        Every subclass must first process its own options and then call
        the `Lexer` constructor, since it processes the basic
        options like `stripnl`.

        An example looks like this:

        .. sourcecode:: python

           def __init__(self, **options):
               self.compress = options.get('compress', '')
               Lexer.__init__(self, **options)

        As these options must all be specifiable as strings (due to the
        command line usage), there are various utility functions
        available to help with that, see `Utilities`_.
        """
        self.options = options
        self.stripnl = get_bool_opt(options, 'stripnl', True)
        self.stripall = get_bool_opt(options, 'stripall', False)
        self.ensurenl = get_bool_opt(options, 'ensurenl', True)
        self.tabsize = get_int_opt(options, 'tabsize', 0)
        self.encoding = options.get('encoding', 'guess')
        if not options.get('inencoding'):
            self.encoding = self.encoding
            self.filters = []
            for filter_ in get_list_opt(options, 'filters', ()):
                self.add_filter(filter_)
                return None

    
    def __repr__(self):
        if self.options:
            return f'''<pygments.lexers.{self.__class__.__name__} with {self.options!r}>'''
        return f'''{self.__class__.__name__}>'''

    
    def add_filter(self, filter_, **options):
        '''
        Add a new stream filter to this lexer.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def analyse_text(text):
        """
        A static method which is called for lexer guessing.

        It should analyse the text and return a float in the range
        from ``0.0`` to ``1.0``.  If it returns ``0.0``, the lexer
        will not be selected as the most probable one, if it returns
        ``1.0``, it will be selected immediately.  This is used by
        `guess_lexer`.

        The `LexerMeta` metaclass automatically wraps this function so
        that it works like a static method (no ``self`` or ``cls``
        parameter) and the return value is automatically converted to
        `float`. If the return value is an object that is boolean `False`
        it's the same as if the return values was ``0.0``.
        """
        pass

    
    def _preprocess_lexer_input(self, text):
        '''Apply preprocessing such as decoding the input, removing BOM and normalizing newlines.'''
        pass
    # WARNING: Decompyle incomplete

    
    def get_tokens(self, text, unfiltered = (False,)):
        """
        This method is the basic interface of a lexer. It is called by
        the `highlight()` function. It must process the text and return an
        iterable of ``(tokentype, value)`` pairs from `text`.

        Normally, you don't need to override this method. The default
        implementation processes the options recognized by all lexers
        (`stripnl`, `stripall` and so on), and then yields all tokens
        from `get_tokens_unprocessed()`, with the ``index`` dropped.

        If `unfiltered` is set to `True`, the filtering mechanism is
        bypassed even if filters are defined.
        """
        pass
    # WARNING: Decompyle incomplete

    
    def get_tokens_unprocessed(self, text):
        '''
        This method should process the text and return an iterable of
        ``(index, tokentype, value)`` tuples where ``index`` is the starting
        position of the token within the input text.

        It must be overridden by subclasses. It is recommended to
        implement it as a generator to maximize effectiveness.
        '''
        raise NotImplementedError


Lexer = <NODE:27>(Lexer, 'Lexer', metaclass = LexerMeta)

class DelegatingLexer(Lexer):
    '''
    This lexer takes two lexer as arguments. A root lexer and
    a language lexer. First everything is scanned using the language
    lexer, afterwards all ``Other`` tokens are lexed using the root
    lexer.

    The lexers from the ``template`` lexer package use this base lexer.
    '''
    
    def __init__(self, _root_lexer, _language_lexer, _needle = (Other,), **options):
        pass
    # WARNING: Decompyle incomplete

    
    def get_tokens_unprocessed(self, text):
        buffered = ''
        insertions = []
        lng_buffer = []
        for i, t, v in self.language_lexer.get_tokens_unprocessed(text):
            if t is self.needle:
                if lng_buffer:
                    insertions.append((len(buffered), lng_buffer))
                    lng_buffer = []
                buffered += v
                continue
            lng_buffer.append((i, t, v))
            if lng_buffer:
                insertions.append((len(buffered), lng_buffer))
        return do_insertions(insertions, self.root_lexer.get_tokens_unprocessed(buffered))



class include(str):
    '''
    Indicates that a state should include rules from another state.
    '''
    pass


class _inherit:
    '''
    Indicates the a state should inherit from its superclass.
    '''
    
    def __repr__(self):
        return 'inherit'


inherit = _inherit()

class combined(tuple):
    '''
    Indicates a state combined from multiple states.
    '''
    
    def __new__(cls, *args):
        return tuple.__new__(cls, args)

    
    def __init__(self, *args):
        pass



class _PseudoMatch:
    '''
    A pseudo match object constructed from a string.
    '''
    
    def __init__(self, start, text):
        self._text = text
        self._start = start

    
    def start(self, arg = (None,)):
        return self._start

    
    def end(self, arg = (None,)):
        return self._start + len(self._text)

    
    def group(self, arg = (None,)):
        if arg:
            raise IndexError('No such group')
        return self._text

    
    def groups(self):
        return (self._text,)

    
    def groupdict(self):
        return { }



def bygroups(*args):
    '''
    Callback that yields multiple actions for each group in the match.
    '''
    pass
# WARNING: Decompyle incomplete


class _This:
    '''
    Special singleton used for indicating the caller class.
    Used by ``using``.
    '''
    pass

this = _This()

def using(_other, **kwargs):
    """
    Callback that processes the match with a different lexer.

    The keyword arguments are forwarded to the lexer, except `state` which
    is handled separately.

    `state` specifies the state that the new lexer will start in, and can
    be an enumerable such as ('root', 'inline', 'string') or a simple
    string which is assumed to be on top of the root state.

    Note: For that to work, `_other` must not be an `ExtendedRegexLexer`.
    """
    pass
# WARNING: Decompyle incomplete


class default:
    """
    Indicates a state or state action (e.g. #pop) to apply.
    For example default('#pop') is equivalent to ('', Token, '#pop')
    Note that state tuples may be used as well.

    .. versionadded:: 2.0
    """
    
    def __init__(self, state):
        self.state = state



class words(Future):
    '''
    Indicates a list of literal words that is transformed into an optimized
    regex that matches any of the words.

    .. versionadded:: 2.0
    '''
    
    def __init__(self, words, prefix, suffix = ('', '')):
        self.words = words
        self.prefix = prefix
        self.suffix = suffix

    
    def get(self):
        return regex_opt(self.words, prefix = self.prefix, suffix = self.suffix)



class RegexLexerMeta(LexerMeta):
    '''
    Metaclass for RegexLexer, creates the self._tokens attribute from
    self.tokens on the first instantiation.
    '''
    
    def _process_regex(cls, regex, rflags, state):
        '''Preprocess the regular expression component of a token definition.'''
        if isinstance(regex, Future):
            regex = regex.get()
        return re.compile(regex, rflags).match

    
    def _process_token(cls, token):
        '''Preprocess the token component of a token definition.'''
        pass
    # WARNING: Decompyle incomplete

    
    def _process_new_state(cls, new_state, unprocessed, processed):
        '''Preprocess the state transition action of a token definition.'''
        if isinstance(new_state, str):
            if new_state == '#pop':
                return -1
            if None in unprocessed:
                return (new_state,)
            if None == '#push':
                return new_state
            if None[:5] == '#pop:':
                return -int(new_state[5:])
            raise f'''unknown new state {new_state!r}'''()
    # WARNING: Decompyle incomplete

    
    def _process_state(cls, unprocessed, processed, state):
        '''Preprocess a single state definition.'''
        pass
    # WARNING: Decompyle incomplete

    
    def process_tokendef(cls, name, tokendefs = (None,)):
        '''Preprocess a dictionary of token definitions.'''
        processed = { }
        cls._all_tokens[name] = { }
        if not tokendefs:
            tokendefs = cls.tokens[name]
            for state in list(tokendefs):
                cls._process_state(tokendefs, processed, state)
                return processed

    
    def get_tokendefs(cls):
        '''
        Merge tokens from superclasses in MRO order, returning a single tokendef
        dictionary.

        Any state that is not defined by a subclass will be inherited
        automatically.  States that *are* defined by subclasses will, by
        default, override that state in the superclass.  If a subclass wishes to
        inherit definitions from a superclass, it can use the special value
        "inherit", which will cause the superclass\' state definition to be
        included at that point in the state.
        '''
        tokens = { }
        inheritable = { }
    # WARNING: Decompyle incomplete

    
    def __call__(cls, *args, **kwds):
        '''Instantiate cls after preprocessing its token definitions.'''
        if '_tokens' not in cls.__dict__:
            cls._all_tokens = { }
            cls._tmpname = 0
            if hasattr(cls, 'token_variants') and cls.token_variants:
                pass
            else:
                cls._tokens = cls.process_tokendef('', cls.get_tokendefs())
    # WARNING: Decompyle incomplete



def RegexLexer():
    '''RegexLexer'''
    __doc__ = '\n    Base for simple stateful regular expression-based lexers.\n    Simplifies the lexing process so that you need only\n    provide a list of states and regular expressions.\n    '
    flags = re.MULTILINE
    tokens = { }
    
    def get_tokens_unprocessed(self, text, stack = (('root',),)):
        """
        Split ``text`` into (tokentype, text) pairs.

        ``stack`` is the initial stack (default: ``['root']``)
        """
        pass
    # WARNING: Decompyle incomplete


RegexLexer = <NODE:27>(RegexLexer, 'RegexLexer', Lexer, metaclass = RegexLexerMeta)

class LexerContext:
    '''
    A helper object that holds lexer position data.
    '''
    
    def __init__(self, text, pos, stack, end = (None, None)):

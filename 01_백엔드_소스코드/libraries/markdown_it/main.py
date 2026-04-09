# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: main.pyc (Python 3.11)

from __future__ import annotations
from collections.abc import Callable, Generator, Iterable, Mapping, MutableMapping
from contextlib import contextmanager
from typing import Any, Literal, overload
from  import helpers, presets
from common import normalize_url, utils
from parser_block import ParserBlock
from parser_core import ParserCore
from parser_inline import ParserInline
from renderer import RendererHTML, RendererProtocol
from rules_core.state_core import StateCore
from token import Token
from utils import EnvType, OptionsDict, OptionsType, PresetType

try:
    import linkify_it
except ModuleNotFoundError:
    linkify_it = None

_PRESETS: 'dict[str, PresetType]' = {
    'default': presets.default.make(),
    'js-default': presets.js_default.make(),
    'zero': presets.zero.make(),
    'commonmark': presets.commonmark.make(),
    'gfm-like': presets.gfm_like.make() }

class MarkdownIt:
    
    def __init__(self = None, config = None, options_update = None, *, renderer_cls):
        '''Main parser class

        :param config: name of configuration to load or a pre-defined dictionary
        :param options_update: dictionary that will be merged into ``config["options"]``
        :param renderer_cls: the class to load as the renderer:
            ``self.renderer = renderer_cls(self)
        '''
        self.utils = utils
        self.helpers = helpers
        self.inline = ParserInline()
        self.block = ParserBlock()
        self.core = ParserCore()
        self.renderer = renderer_cls(self)
        self.linkify = linkify_it.LinkifyIt() if linkify_it else None
        if not options_update and isinstance(options_update, Mapping):
            raise TypeError(f'''options_update should be a mapping: {options_update}\n(Perhaps you intended this to be the renderer_cls?)''')
        self.configure(config, options_update = options_update)

    
    def __repr__(self = None):
        return f'''{self.__class__.__module__}.{self.__class__.__name__}()'''

    __getitem__ = (lambda self = None, name = None: pass)()
    __getitem__ = (lambda self = None, name = None: pass)()
    __getitem__ = (lambda self = None, name = None: pass)()
    __getitem__ = (lambda self = None, name = None: pass)()
    __getitem__ = (lambda self = None, name = None: pass)()
    
    def __getitem__(self = None, name = None):
        return {
            'inline': self.inline,
            'block': self.block,
            'core': self.core,
            'renderer': self.renderer }[name]

    
    def set(self = None, options = None):
        """Set parser options (in the same format as in constructor).
        Probably, you will never need it, but you can change options after constructor call.

        __Note:__ To achieve the best possible performance, don't modify a
        `markdown-it` instance options on the fly. If you need multiple configurations
        it's best to create multiple instances and initialize each with separate config.
        """
        self.options = OptionsDict(options)

    
    def configure(self = None, presets = None, options_update = None):
        '''Batch load of all options and component settings.
        This is an internal method, and you probably will not need it.
        But if you will - see available presets and data structure
        [here](https://github.com/markdown-it/markdown-it/tree/master/lib/presets)

        We strongly recommend to use presets instead of direct config loads.
        That will give better compatibility with next versions.
        '''
        if isinstance(presets, str):
            if presets not in _PRESETS:
                raise KeyError(f'''Wrong `markdown-it` preset \'{presets}\', check name''')
            config = _PRESETS[presets]
        else:
            config = presets
        if not config:
            raise ValueError("Wrong `markdown-it` config, can't be empty")
    # WARNING: Decompyle incomplete

    
    def get_all_rules(self = None):
        '''Return the names of all active rules.'''
        pass
    # WARNING: Decompyle incomplete

    
    def get_active_rules(self = None):
        '''Return the names of all active rules.'''
        pass
    # WARNING: Decompyle incomplete

    
    def enable(self = None, names = None, ignoreInvalid = None):
        """Enable list or rules. (chainable)

        :param names: rule name or list of rule names to enable.
        :param ignoreInvalid: set `true` to ignore errors when rule not found.

        It will automatically find appropriate components,
        containing rules with given names. If rule not found, and `ignoreInvalid`
        not set - throws exception.

        Example::

            md = MarkdownIt().enable(['sub', 'sup']).disable('smartquotes')

        """
        pass
    # WARNING: Decompyle incomplete

    
    def disable(self = None, names = None, ignoreInvalid = None):
        '''The same as [[MarkdownIt.enable]], but turn specified rules off. (chainable)

        :param names: rule name or list of rule names to disable.
        :param ignoreInvalid: set `true` to ignore errors when rule not found.

        '''
        pass
    # WARNING: Decompyle incomplete

    reset_rules = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    def add_render_rule(self = None, name = None, function = None, fmt = ('html',)):
        '''Add a rule for rendering a particular Token type.

        Only applied when ``renderer.__output__ == fmt``
        '''
        if self.renderer.__output__ == fmt:
            self.renderer.rules[name] = function.__get__(self.renderer)
            return None

    
    def use(self = None, plugin = None, *params, **options):
        """Load specified plugin with given params into current parser instance. (chainable)

        It's just a sugar to call `plugin(md, params)` with curring.

        Example::

            def func(tokens, idx):
                tokens[idx].content = tokens[idx].content.replace('foo', 'bar')
            md = MarkdownIt().use(plugin, 'foo_replace', 'text', func)

        """
        pass
    # WARNING: Decompyle incomplete

    
    def parse(self = None, src = None, env = None):
        '''Parse the source string to a token stream

        :param src: source string
        :param env: environment sandbox

        Parse input string and return list of block tokens (special token type
        "inline" will contain list of inline tokens).

        `env` is used to pass data between "distributed" rules and return additional
        metadata like reference info, needed for the renderer. It also can be used to
        inject data in specific cases. Usually, you will be ok to pass `{}`,
        and then pass updated object to renderer.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def render(self = None, src = None, env = None):
        '''Render markdown string into html. It does all magic for you :).

        :param src: source string
        :param env: environment sandbox
        :returns: The output of the loaded renderer

        `env` can be used to inject additional metadata (`{}` by default).
        But you will not need it with high probability. See also comment
        in [[MarkdownIt.parse]].
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def parseInline(self = None, src = None, env = None):
        '''The same as [[MarkdownIt.parse]] but skip all block rules.

        :param src: source string
        :param env: environment sandbox

        It returns the
        block tokens list with the single `inline` element, containing parsed inline
        tokens in `children` property. Also updates `env` object.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def renderInline(self = None, src = None, env = None):
        '''Similar to [[MarkdownIt.render]] but for single paragraph content.

        :param src: source string
        :param env: environment sandbox

        Similar to [[MarkdownIt.render]] but for single paragraph content. Result
        will NOT be wrapped into `<p>` tags.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def validateLink(self = None, url = None):
        """Validate if the URL link is allowed in output.

        This validator can prohibit more than really needed to prevent XSS.
        It's a tradeoff to keep code simple and to be secure by default.

        Note: the url should be normalized at this point, and existing entities decoded.
        """
        return normalize_url.validateLink(url)

    
    def normalizeLink(self = None, url = None):
        """Normalize destination URLs in links

        ::

            [label]:   destination   'title'
                    ^^^^^^^^^^^
        """
        return normalize_url.normalizeLink(url)

    
    def normalizeLinkText(self = None, link = None):
        '''Normalize autolink content

        ::

            <destination>
            ~~~~~~~~~~~
        '''
        return normalize_url.normalizeLinkText(link)

# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: runtime.pyc (Python 3.11)

'''The runtime functions and state used by compiled templates.'''
import functools
import sys
import typing as t
from collections import abc
from itertools import chain
from markupsafe import escape
from markupsafe import Markup
from markupsafe import soft_str
from async_utils import auto_aiter
from async_utils import auto_await
from exceptions import TemplateNotFound
from exceptions import TemplateRuntimeError
from exceptions import UndefinedError
from nodes import EvalContext
from utils import _PassArg
from utils import concat
from utils import internalcode
from utils import missing
from utils import Namespace
from utils import object_type_repr
from utils import pass_eval_context
V = t.TypeVar('V')
F = t.TypeVar('F', bound = t.Callable[(..., t.Any)])
if t.TYPE_CHECKING:
    import logging
    import typing_extensions as te
    from environment import Environment
    
    class LoopRenderFunc(te.Protocol):
        
        def __call__(self = None, reciter = None, loop_render_func = None, depth = (0,)):
            pass


exported = [
    'LoopContext',
    'TemplateReference',
    'Macro',
    'Markup',
    'TemplateRuntimeError',
    'missing',
    'escape',
    'markup_join',
    'str_join',
    'identity',
    'TemplateNotFound',
    'Namespace',
    'Undefined',
    'internalcode']
async_exported = [
    'AsyncLoopContext',
    'auto_aiter',
    'auto_await']

def identity(x = None):
    '''Returns its argument. Useful for certain things in the
    environment.
    '''
    return x


def markup_join(seq = None):
    '''Concatenation that escapes if necessary and converts to string.'''
    buf = []
    iterator = map(soft_str, seq)
    for arg in iterator:
        buf.append(arg)
        if hasattr(arg, '__html__'):
            
            return None, Markup('').join(chain(buf, iterator))
        return concat(buf)


def str_join(seq = None):
    '''Simple args to string conversion and concatenation.'''
    return concat(map(str, seq))


def new_context(environment, template_name, blocks = None, vars = None, shared = None, globals = (None, False, None, None), locals = ('environment', 'Environment', 'template_name', t.Optional[str], 'blocks', t.Dict[(str, t.Callable[([
    'Context'], t.Iterator[str])])], 'vars', t.Optional[t.Dict[(str, t.Any)]], 'shared', bool, 'globals', t.Optional[t.MutableMapping[(str, t.Any)]], 'locals', t.Optional[t.Mapping[(str, t.Any)]], 'return', 'Context')):
    '''Internal helper for context creation.'''
    pass
# WARNING: Decompyle incomplete


class TemplateReference:
    '''The `self` in templates.'''
    
    def __init__(self = None, context = None):
        self._TemplateReference__context = context

    
    def __getitem__(self = None, name = None):
        blocks = self._TemplateReference__context.blocks[name]
        return BlockReference(name, self._TemplateReference__context, blocks, 0)

    
    def __repr__(self = None):
        return f'''<{type(self).__name__} {self._TemplateReference__context.name!r}>'''



def _dict_method_all(dict_method = None):
    pass
# WARNING: Decompyle incomplete

Context = <NODE:12>()

class BlockReference:
    '''One block on a template reference.'''
    
    def __init__(self, name = None, context = None, stack = None, depth = ('name', str, 'context', 'Context', 'stack', t.List[t.Callable[([
        'Context'], t.Iterator[str])]], 'depth', int, 'return', None)):
        self.name = name
        self._context = context
        self._stack = stack
        self._depth = depth

    super = (lambda self = None: if self._depth + 1 >= len(self._stack):
self._context.environment.undefined(f'''there is no parent block called {self.name!r}.''', name = 'super')None(self.name, self._context, self._stack, self._depth + 1))()
    _async_call = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    __call__ = (lambda self = None: if self._context.environment.is_async:
self._async_call()rv = None._context.environment.concat(self._stack[self._depth](self._context))if self._context.eval_ctx.autoescape:
Markup(rv))()


class LoopContext:
    '''A wrapper iterable for dynamic ``for`` loops, with information
    about the loop and iteration.
    '''
    index0 = -1
    _length: t.Optional[int] = None
    _after: t.Any = missing
    _current: t.Any = missing
    _before: t.Any = missing
    _last_changed_value: t.Any = missing
    
    def __init__(self = None, iterable = None, undefined = None, recurse = (None, 0), depth0 = ('iterable', t.Iterable[V], 'undefined', t.Type['Undefined'], 'recurse', t.Optional['LoopRenderFunc'], 'depth0', int, 'return', None)):
        '''
        :param iterable: Iterable to wrap.
        :param undefined: :class:`Undefined` class to use for next and
            previous items.
        :param recurse: The function to render the loop body when the
            loop is marked recursive.
        :param depth0: Incremented when looping recursively.
        '''
        self._iterable = iterable
        self._iterator = self._to_iterator(iterable)
        self._undefined = undefined
        self._recurse = recurse
        self.depth0 = depth0

    _to_iterator = (lambda iterable = None: iter(iterable))()
    length = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    def __len__(self = None):
        return self.length

    depth = (lambda self = None: self.depth0 + 1)()
    index = (lambda self = None: self.index0 + 1)()
    revindex0 = (lambda self = None: self.length - self.index)()
    revindex = (lambda self = None: self.length - self.index0)()
    first = (lambda self = None: self.index0 == 0)()
    
    def _peek_next(self = None):
        '''Return the next element in the iterable, or :data:`missing`
        if the iterable is exhausted. Only peeks one item ahead, caching
        the result in :attr:`_last` for use in subsequent checks. The
        cache is reset when :meth:`__next__` is called.
        '''
        if self._after is not missing:
            return self._after
        self._after = None(self._iterator, missing)
        return self._after

    last = (lambda self = None: self._peek_next() is missing)()
    previtem = (lambda self = None: if self.first:
self._undefined('there is no previous item')None._before)()
    nextitem = (lambda self = None: rv = self._peek_next()if rv is missing:
self._undefined('there is no next item'))()
    
    def cycle(self = None, *args):
        '''Return a value from the given args, cycling through based on
        the current :attr:`index0`.

        :param args: One or more values to cycle through.
        '''
        if not args:
            raise TypeError('no items for cycling given')
        return args[self.index0 % len(args)]

    
    def changed(self = None, *value):
        '''Return ``True`` if previously called with a different value
        (including when called for the first time).

        :param value: One or more values to compare to the last call.
        '''
        if self._last_changed_value != value:
            self._last_changed_value = value
            return True

    
    def __iter__(self = None):
        return self

    
    def __next__(self = None):
        if self._after is not missing:
            rv = self._after
            self._after = missing
        else:
            rv = next(self._iterator)
        self._current = self, self.index0 += 1, .index0
        self._current = rv
        return (rv, self)

    __call__ = (lambda self = None, iterable = None: pass# WARNING: Decompyle incomplete
)()
    
    def __repr__(self = None):
        return f'''<{type(self).__name__} {self.index}/{self.length}>'''



class AsyncLoopContext(LoopContext):
    _iterator: t.AsyncIterator[t.Any] = 'AsyncLoopContext'
    _to_iterator = (lambda iterable = None: auto_aiter(iterable))()
    length = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    revindex0 = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    revindex = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    async def _peek_next(self = None):
        pass
    # WARNING: Decompyle incomplete

    last = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    nextitem = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    def __aiter__(self = None):
        return self

    
    async def __anext__(self = None):
        pass
    # WARNING: Decompyle incomplete



class Macro:
    '''Wraps a macro function.'''
    
    def __init__(self, environment, func, name, arguments = None, catch_kwargs = None, catch_varargs = None, caller = (None,), default_autoescape = ('environment', 'Environment', 'func', t.Callable[(..., str)], 'name', str, 'arguments', t.List[str], 'catch_kwargs', bool, 'catch_varargs', bool, 'caller', bool, 'default_autoescape', t.Optional[bool])):
        self._environment = environment
        self._func = func
        self._argument_count = len(arguments)
        self.name = name
        self.arguments = arguments
        self.catch_kwargs = catch_kwargs
        self.catch_varargs = catch_varargs
        self.caller = caller
        self.explicit_caller = 'caller' in arguments
    # WARNING: Decompyle incomplete

    __call__ = (lambda self = None: if args and isinstance(args[0], EvalContext):
autoescape = args[0].autoescapeargs = args[1:]else:
autoescape = self._default_autoescapearguments = list(args[:self._argument_count])off = len(arguments)found_caller = Falseif off != self._argument_count:
for name in self.arguments[len(arguments):]:
value = kwargs.pop(name)except KeyError:
value = missingif name == 'caller':
found_caller = Truearguments.append(value)continueelse:
found_caller = self.explicit_caller# WARNING: Decompyle incomplete
)()()
    
    async def _async_invoke(self = None, arguments = None, autoescape = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _invoke(self = None, arguments = None, autoescape = None):
        if self._environment.is_async:
            return self._async_invoke(arguments, autoescape)
    # WARNING: Decompyle incomplete

    
    def __repr__(self = None):
        pass
    # WARNING: Decompyle incomplete



class Undefined:
    """The default undefined type. This can be printed, iterated, and treated as
    a boolean. Any other operation will raise an :exc:`UndefinedError`.

    >>> foo = Undefined(name='foo')
    >>> str(foo)
    ''
    >>> not foo
    True
    >>> foo + 42
    Traceback (most recent call last):
      ...
    jinja2.exceptions.UndefinedError: 'foo' is undefined
    """
    __slots__ = ('_undefined_hint', '_undefined_obj', '_undefined_name', '_undefined_exception')
    
    def __init__(self = None, hint = None, obj = None, name = (None, missing, None, UndefinedError), exc = ('hint', t.Optional[str], 'obj', t.Any, 'name', t.Optional[str], 'exc', t.Type[TemplateRuntimeError], 'return', None)):
        self._undefined_hint = hint
        self._undefined_obj = obj
        self._undefined_name = name
        self._undefined_exception = exc

    _undefined_message = (lambda self = None: if self._undefined_hint:
self._undefined_hintif None._undefined_obj is missing:
f'''{self._undefined_name!r} is undefined'''if not None(self._undefined_name, str):
f'''{object_type_repr(self._undefined_obj)} has no element {self._undefined_name!r}'''f'''{None(self._undefined_obj)!r} has no attribute {self._undefined_name!r}''')()
    _fail_with_undefined_error = (lambda self = None: raise self._undefined_exception(self._undefined_message))()
    __getattr__ = (lambda self = None, name = None: if name[:2] == '__' and name[-2:] == '__':
raise AttributeError(name)self._fail_with_undefined_error())()
    __add__ = _fail_with_undefined_error
    __radd__ = _fail_with_undefined_error
    __sub__ = _fail_with_undefined_error
    __rsub__ = _fail_with_undefined_error
    __mul__ = _fail_with_undefined_error
    __rmul__ = _fail_with_undefined_error
    __div__ = _fail_with_undefined_error
    __rdiv__ = _fail_with_undefined_error
    __truediv__ = _fail_with_undefined_error
    __rtruediv__ = _fail_with_undefined_error
    __floordiv__ = _fail_with_undefined_error
    __rfloordiv__ = _fail_with_undefined_error
    __mod__ = _fail_with_undefined_error
    __rmod__ = _fail_with_undefined_error
    __pos__ = _fail_with_undefined_error
    __neg__ = _fail_with_undefined_error
    __call__ = _fail_with_undefined_error
    __getitem__ = _fail_with_undefined_error
    __lt__ = _fail_with_undefined_error
    __le__ = _fail_with_undefined_error
    __gt__ = _fail_with_undefined_error
    __ge__ = _fail_with_undefined_error
    __int__ = _fail_with_undefined_error
    __float__ = _fail_with_undefined_error
    __complex__ = _fail_with_undefined_error
    __pow__ = _fail_with_undefined_error
    __rpow__ = _fail_with_undefined_error
    
    def __eq__(self = None, other = None):
        return type(self) is type(other)

    
    def __ne__(self = None, other = None):
        return not self.__eq__(other)

    
    def __hash__(self = None):
        return id(type(self))

    
    def __str__(self = None):
        return ''

    
    def __len__(self = None):
        return 0

    
    def __iter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __aiter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __bool__(self = None):
        return False

    
    def __repr__(self = None):
        return 'Undefined'



def make_logging_undefined(logger = None, base = None):
    '''Given a logger object this returns a new undefined class that will
    log certain failures.  It will log iterations and printing.  If no
    logger is given a default logger is created.

    Example::

        logger = logging.getLogger(__name__)
        LoggingUndefined = make_logging_undefined(
            logger=logger,
            base=Undefined
        )

    .. versionadded:: 2.8

    :param logger: the logger to use.  If not provided, a default logger
                   is created.
    :param base: the base class to add logging functionality to.  This
                 defaults to :class:`Undefined`.
    '''
    pass
# WARNING: Decompyle incomplete


class ChainableUndefined(Undefined):
    """An undefined that is chainable, where both ``__getattr__`` and
    ``__getitem__`` return itself rather than raising an
    :exc:`UndefinedError`.

    >>> foo = ChainableUndefined(name='foo')
    >>> str(foo.bar['baz'])
    ''
    >>> foo.bar['baz'] + 42
    Traceback (most recent call last):
      ...
    jinja2.exceptions.UndefinedError: 'foo' is undefined

    .. versionadded:: 2.11.0
    """
    __slots__ = ()
    
    def __html__(self = None):
        return str(self)

    
    def __getattr__(self = None, name = None):
        if name[:2] == '__' and name[-2:] == '__':
            raise AttributeError(name)
        return self

    
    def __getitem__(self = None, _name = None):
        return self



class DebugUndefined(Undefined):
    """An undefined that returns the debug info when printed.

    >>> foo = DebugUndefined(name='foo')
    >>> str(foo)
    '{{ foo }}'
    >>> not foo
    True
    >>> foo + 42
    Traceback (most recent call last):
      ...
    jinja2.exceptions.UndefinedError: 'foo' is undefined
    """
    __slots__ = ()
    
    def __str__(self = None):
        if self._undefined_hint:
            message = f'''undefined value printed: {self._undefined_hint}'''
        elif self._undefined_obj is missing:
            message = self._undefined_name
        else:
            message = f'''no such element: {object_type_repr(self._undefined_obj)}[{self._undefined_name!r}]'''
        return f'''{{{{ {message} }}}}'''



class StrictUndefined(Undefined):
    """An undefined that barks on print and iteration as well as boolean
    tests and all kinds of comparisons.  In other words: you can do nothing
    with it except checking if it's defined using the `defined` test.

    >>> foo = StrictUndefined(name='foo')
    >>> str(foo)
    Traceback (most recent call last):
      ...
    jinja2.exceptions.UndefinedError: 'foo' is undefined
    >>> not foo
    Traceback (most recent call last):
      ...
    jinja2.exceptions.UndefinedError: 'foo' is undefined
    >>> foo + 42
    Traceback (most recent call last):
      ...
    jinja2.exceptions.UndefinedError: 'foo' is undefined
    """
    __slots__ = ()
    __iter__ = Undefined._fail_with_undefined_error
    __str__ = Undefined._fail_with_undefined_error
    __len__ = Undefined._fail_with_undefined_error
    __eq__ = Undefined._fail_with_undefined_error
    __ne__ = Undefined._fail_with_undefined_error
    __bool__ = Undefined._fail_with_undefined_error
    __hash__ = Undefined._fail_with_undefined_error
    __contains__ = Undefined._fail_with_undefined_error

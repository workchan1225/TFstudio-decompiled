# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: dispatcher.pyc (Python 3.11)

from __future__ import annotations
from warnings import warn
import inspect
from conflict import ordering, ambiguities, super_signature, AmbiguityWarning
from utils import expand_tuples
import itertools as itl

class MDNotImplementedError(NotImplementedError):
    ''' A NotImplementedError for multiple dispatch '''
    pass


def ambiguity_warn(dispatcher, ambiguities):
    ''' Raise warning when ambiguity is detected

    Parameters
    ----------
    dispatcher : Dispatcher
        The dispatcher on which the ambiguity was detected
    ambiguities : set
        Set of type signature pairs that are ambiguous within this dispatcher

    See Also:
        Dispatcher.add
        warning_text
    '''
    warn(warning_text(dispatcher.name, ambiguities), AmbiguityWarning)


class RaiseNotImplementedError:
    '''Raise ``NotImplementedError`` when called.'''
    
    def __init__(self, dispatcher):
        self.dispatcher = dispatcher

    
    def __call__(self, *args, **kwargs):
        types = (lambda .0: pass# WARNING: Decompyle incomplete
)(args())
        raise NotImplementedError(f'''Ambiguous signature for {self.dispatcher.name!s}: <{str_signature(types)!s}>''')



def ambiguity_register_error_ignore_dup(dispatcher, ambiguities):
    '''
    If super signature for ambiguous types is duplicate types, ignore it.
    Else, register instance of ``RaiseNotImplementedError`` for ambiguous types.

    Parameters
    ----------
    dispatcher : Dispatcher
        The dispatcher on which the ambiguity was detected
    ambiguities : set
        Set of type signature pairs that are ambiguous within this dispatcher

    See Also:
        Dispatcher.add
        ambiguity_warn
    '''
    for amb in ambiguities:
        signature = tuple(super_signature(amb))
        if len(set(signature)) == 1:
            continue
        dispatcher.add(signature, RaiseNotImplementedError(dispatcher), on_ambiguity = ambiguity_register_error_ignore_dup)
        return None

_unresolved_dispatchers: 'set[Dispatcher]' = set()
_resolve = [
    True]

def halt_ordering():
    _resolve[0] = False


def restart_ordering(on_ambiguity = (ambiguity_warn,)):
    _resolve[0] = True
# WARNING: Decompyle incomplete


class Dispatcher:
    ''' Dispatch methods based on type signature

    Use ``dispatch`` to add implementations

    Examples
    --------

    >>> from sympy.multipledispatch import dispatch
    >>> @dispatch(int)
    ... def f(x):
    ...     return x + 1

    >>> @dispatch(float)
    ... def f(x): # noqa: F811
    ...     return x - 1

    >>> f(3)
    4
    >>> f(3.0)
    2.0
    '''
    __slots__ = ('__name__', 'name', 'funcs', 'ordering', '_cache', 'doc')
    
    def __init__(self, name, doc = (None,)):
        self.name = name
        self.__name__ = name
        self.funcs = { }
        self._cache = { }
        self.ordering = []
        self.doc = doc

    
    def register(self, *types, **kwargs):
        """ Register dispatcher with new implementation

        >>> from sympy.multipledispatch.dispatcher import Dispatcher
        >>> f = Dispatcher('f')
        >>> @f.register(int)
        ... def inc(x):
        ...     return x + 1

        >>> @f.register(float)
        ... def dec(x):
        ...     return x - 1

        >>> @f.register(list)
        ... @f.register(tuple)
        ... def reverse(x):
        ...     return x[::-1]

        >>> f(1)
        2

        >>> f(1.0)
        0.0

        >>> f([1, 2, 3])
        [3, 2, 1]
        """
        pass
    # WARNING: Decompyle incomplete

    get_func_params = (lambda cls, func: if hasattr(inspect, 'signature'):
sig = inspect.signature(func)sig.parameters.values())()
    get_func_annotations = (lambda cls, func: pass# WARNING: Decompyle incomplete
)()
    
    def add(self, signature, func, on_ambiguity = (ambiguity_warn,)):
        """ Add new types/method pair to dispatcher

        >>> from sympy.multipledispatch import Dispatcher
        >>> D = Dispatcher('add')
        >>> D.add((int, int), lambda x, y: x + y)
        >>> D.add((float, float), lambda x, y: x + y)

        >>> D(1, 2)
        3
        >>> D(1, 2.0)
        Traceback (most recent call last):
        ...
        NotImplementedError: Could not find signature for add: <int, float>

        When ``add`` detects a warning it calls the ``on_ambiguity`` callback
        with a dispatcher/itself, and a set of ambiguous type signature pairs
        as inputs.  See ``ambiguity_warn`` for an example.
        """
        if not signature:
            annotations = self.get_func_annotations(func)
            if annotations:
                signature = annotations
        if (lambda .0: pass# WARNING: Decompyle incomplete
)(signature()):
            for typs in expand_tuples(signature):
                self.add(typs, func, on_ambiguity)
                return None
                for typ in signature:
                    if not isinstance(typ, type):
                        str_sig = (lambda .0: pass# WARNING: Decompyle incomplete
)(signature())
                        raise TypeError(f'''Tried to dispatch on non-type: {typ!s}\nIn signature: <{str_sig!s}>\nIn function: {self.name!s}''')
                    self.funcs[signature] = func
                    self.reorder(on_ambiguity = on_ambiguity)
                    self._cache.clear()
                    return None

    
    def reorder(self, on_ambiguity = (ambiguity_warn,)):
        if _resolve[0]:
            self.ordering = ordering(self.funcs)
            amb = ambiguities(self.funcs)
            if amb:
                on_ambiguity(self, amb)
                return None
            return None
        None.add(self)

    
    def __call__(self, *args, **kwargs):
        types = (lambda .0: [ type(arg) for arg in .0 ])(args())
    # WARNING: Decompyle incomplete

    
    def __str__(self):
        return '<dispatched %s>' % self.name

    __repr__ = __str__
    
    def dispatch(self, *types):
        ''' Deterimine appropriate implementation for this type signature

        This method is internal.  Users should call this object as a function.
        Implementation resolution occurs within the ``__call__`` method.

        >>> from sympy.multipledispatch import dispatch
        >>> @dispatch(int)
        ... def inc(x):
        ...     return x + 1

        >>> implementation = inc.dispatch(int)
        >>> implementation(3)
        4

        >>> print(inc.dispatch(float))
        None

        See Also:
            ``sympy.multipledispatch.conflict`` - module to determine resolution order
        '''
        if types in self.funcs:
            return self.funcs[types]
    # WARNING: Decompyle incomplete

    
    def dispatch_iter(self, *types):
        pass
    # WARNING: Decompyle incomplete

    
    def resolve(self, types):
        ''' Deterimine appropriate implementation for this type signature

        .. deprecated:: 0.4.4
            Use ``dispatch(*types)`` instead
        '''
        warn('resolve() is deprecated, use dispatch(*types)', DeprecationWarning)
    # WARNING: Decompyle incomplete

    
    def __getstate__(self):
        return {
            'name': self.name,
            'funcs': self.funcs }

    
    def __setstate__(self, d):
        self.name = d['name']
        self.funcs = d['funcs']
        self.ordering = ordering(self.funcs)
        self._cache = { }

    __doc__ = (lambda self: docs = [
'Multiply dispatched method: %s' % self.name]if self.doc:
docs.append(self.doc)other = []for sig in self.ordering[::-1]:
func = self.funcs[sig]if func.__doc__:
s = 'Inputs: <%s>\n' % str_signature(sig)s += '-' * len(s) + '\n's += func.__doc__.strip()docs.append(s)continueother.append(str_signature(sig))if other:
docs.append('Other signatures:\n    ' + '\n    '.join(other))'\n\n'.join(docs))()
    
    def _help(self, *args):
        pass
    # WARNING: Decompyle incomplete

    
    def help(self, *args, **kwargs):
        ''' Print docstring for the function corresponding to inputs '''
        pass
    # WARNING: Decompyle incomplete

    
    def _source(self, *args):
        pass
    # WARNING: Decompyle incomplete

    
    def source(self, *args, **kwargs):
        ''' Print source code for the function corresponding to inputs '''
        pass
    # WARNING: Decompyle incomplete



def source(func):
    s = 'File: %s\n\n' % inspect.getsourcefile(func)
    s = s + inspect.getsource(func)
    return s


class MethodDispatcher(Dispatcher):
    ''' Dispatch methods based on type signature

    See Also:
        Dispatcher
    '''
    get_func_params = (lambda cls, func: if hasattr(inspect, 'signature'):
sig = inspect.signature(func)itl.islice(sig.parameters.values(), 1, None))()
    
    def __get__(self, instance, owner):
        self.obj = instance
        self.cls = owner
        return self

    
    def __call__(self, *args, **kwargs):
        types = (lambda .0: [ type(arg) for arg in .0 ])(args())
    # WARNING: Decompyle incomplete



def str_signature(sig):
    """ String representation of type signature

    >>> from sympy.multipledispatch.dispatcher import str_signature
    >>> str_signature((int, float))
    'int, float'
    """
    return (lambda .0: pass# WARNING: Decompyle incomplete
)(sig())


def warning_text(name, amb):
    ''' The text for ambiguity warnings '''
    pass
# WARNING: Decompyle incomplete

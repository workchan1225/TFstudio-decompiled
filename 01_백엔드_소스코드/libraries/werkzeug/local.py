# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: local.pyc (Python 3.11)

from __future__ import annotations
import copy
import math
import operator
import typing as t
from contextvars import ContextVar
from functools import partial
from functools import update_wrapper
from operator import attrgetter
from wsgi import ClosingIterator
if t.TYPE_CHECKING:
    from _typeshed.wsgi import StartResponse
    from _typeshed.wsgi import WSGIApplication
    from _typeshed.wsgi import WSGIEnvironment
T = t.TypeVar('T')
F = t.TypeVar('F', bound = t.Callable[(..., t.Any)])

def release_local(local = None):
    '''Release the data for the current context in a :class:`Local` or
    :class:`LocalStack` without using a :class:`LocalManager`.

    This should not be needed for modern use cases, and may be removed
    in the future.

    .. versionadded:: 0.6.1
    '''
    local.__release_local__()


class Local:
    '''Create a namespace of context-local data. This wraps a
    :class:`ContextVar` containing a :class:`dict` value.

    This may incur a performance penalty compared to using individual
    context vars, as it has to copy data to avoid mutating the dict
    between nested contexts.

    :param context_var: The :class:`~contextvars.ContextVar` to use as
        storage for this local. If not given, one will be created.
        Context vars not created at the global scope may interfere with
        garbage collection.

    .. versionchanged:: 2.0
        Uses ``ContextVar`` instead of a custom storage implementation.
    '''
    __slots__ = ('__storage',)
    
    def __init__(self = None, context_var = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __iter__(self = None):
        return iter(self._Local__storage.get({ }).items())

    
    def __call__(self = None, name = None, *, unbound_message):
        """Create a :class:`LocalProxy` that access an attribute on this
        local namespace.

        :param name: Proxy this attribute.
        :param unbound_message: The error message that the proxy will
            show if the attribute isn't set.
        """
        return LocalProxy(self, name, unbound_message = unbound_message)

    
    def __release_local__(self = None):
        self._Local__storage.set({ })

    
    def __getattr__(self = None, name = None):
        values = self._Local__storage.get({ })
        if name in values:
            return values[name]
        raise None(name)

    
    def __setattr__(self = None, name = None, value = None):
        values = self._Local__storage.get({ }).copy()
        values[name] = value
        self._Local__storage.set(values)

    
    def __delattr__(self = None, name = None):
        values = self._Local__storage.get({ })
        if name in values:
            values = values.copy()
            del values[name]
            self._Local__storage.set(values)
            return None
        raise None(name)



def LocalStack():
    '''LocalStack'''
    __doc__ = 'Create a stack of context-local data. This wraps a\n    :class:`ContextVar` containing a :class:`list` value.\n\n    This may incur a performance penalty compared to using individual\n    context vars, as it has to copy data to avoid mutating the list\n    between nested contexts.\n\n    :param context_var: The :class:`~contextvars.ContextVar` to use as\n        storage for this local. If not given, one will be created.\n        Context vars not created at the global scope may interfere with\n        garbage collection.\n\n    .. versionchanged:: 2.0\n        Uses ``ContextVar`` instead of a custom storage implementation.\n\n    .. versionadded:: 0.6.1\n    '
    __slots__ = ('_storage',)
    
    def __init__(self = None, context_var = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __release_local__(self = None):
        self._storage.set([])

    
    def push(self = None, obj = None):
        '''Add a new item to the top of the stack.'''
        stack = self._storage.get([]).copy()
        stack.append(obj)
        self._storage.set(stack)
        return stack

    
    def pop(self = None):
        '''Remove the top item from the stack and return it. If the
        stack is empty, return ``None``.
        '''
        stack = self._storage.get([])
        if len(stack) == 0:
            return None
        rv = None[-1]
        self._storage.set(stack[:-1])
        return rv

    top = (lambda self = None: stack = self._storage.get([])if len(stack) == 0:
NoneNone[-1])()
    
    def __call__(self = None, name = None, *, unbound_message):
        '''Create a :class:`LocalProxy` that accesses the top of this
        local stack.

        :param name: If given, the proxy access this attribute of the
            top item, rather than the item itself.
        :param unbound_message: The error message that the proxy will
            show if the stack is empty.
        '''
        return LocalProxy(self, name, unbound_message = unbound_message)


LocalStack = <NODE:27>(LocalStack, 'LocalStack', t.Generic[T])

class LocalManager:
    '''Manage releasing the data for the current context in one or more
    :class:`Local` and :class:`LocalStack` objects.

    This should not be needed for modern use cases, and may be removed
    in the future.

    :param locals: A local or list of locals to manage.

    .. versionchanged:: 2.1
        The ``ident_func`` was removed.

    .. versionchanged:: 0.7
        The ``ident_func`` parameter was added.

    .. versionchanged:: 0.6.1
        The :func:`release_local` function can be used instead of a
        manager.
    '''
    __slots__ = ('locals',)
    
    def __init__(self = None, locals = None):
        pass
    # WARNING: Decompyle incomplete

    
    def cleanup(self = None):
        '''Release the data in the locals for this context. Call this at
        the end of each request or use :meth:`make_middleware`.
        '''
        for local in self.locals:
            release_local(local)
            return None

    
    def make_middleware(self = None, app = None):
        '''Wrap a WSGI application so that local data is released
        automatically after the response has been sent for a request.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def middleware(self = None, func = None):
        '''Like :meth:`make_middleware` but used as a decorator on the
        WSGI application function.

        .. code-block:: python

            @manager.middleware
            def application(environ, start_response):
                ...
        '''
        return update_wrapper(self.make_middleware(func), func)

    
    def __repr__(self = None):
        return f'''<{type(self).__name__} storages: {len(self.locals)}>'''



class _ProxyLookup:
    '''Descriptor that handles proxied attribute lookup for
    :class:`LocalProxy`.

    :param f: The built-in function this attribute is accessed through.
        Instead of looking up the special method, the function call
        is redone on the object.
    :param fallback: Return this function if the proxy is unbound
        instead of raising a :exc:`RuntimeError`.
    :param is_attr: This proxied name is an attribute, not a function.
        Call the fallback immediately to get the value.
    :param class_value: Value to return when accessed from the
        ``LocalProxy`` class directly. Used for ``__doc__`` so building
        docs still works.
    '''
    __slots__ = ('bind_f', 'fallback', 'is_attr', 'class_value', 'name')
    
    def __init__(self = None, f = None, fallback = None, class_value = (None, None, None, False), is_attr = ('f', 't.Callable[..., t.Any] | None', 'fallback', 't.Callable[[LocalProxy[t.Any]], t.Any] | None', 'class_value', 't.Any | None', 'is_attr', 'bool', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def __set_name__(self = None, owner = None, name = None):
        self.name = name

    
    def __get__(self = None, instance = None, owner = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self = None):
        return f'''proxy {self.name}'''

    
    def __call__(self = None, instance = None, *args, **kwargs):
        """Support calling unbound methods from the class. For example,
        this happens with ``copy.copy``, which does
        ``type(x).__copy__(x)``. ``type(x)`` can't be proxied, so it
        returns the proxy type and descriptor.
        """
        pass
    # WARNING: Decompyle incomplete



class _ProxyIOp(_ProxyLookup):
    pass
# WARNING: Decompyle incomplete


def _l_to_r_op(op = None):
    '''Swap the argument order to turn an l-op into an r-op.'''
    pass
# WARNING: Decompyle incomplete


def _identity(o = None):
    return o


def LocalProxy():
    '''LocalProxy'''
    __doc__ = 'A proxy to the object bound to a context-local object. All\n    operations on the proxy are forwarded to the bound object. If no\n    object is bound, a ``RuntimeError`` is raised.\n\n    :param local: The context-local object that provides the proxied\n        object.\n    :param name: Proxy this attribute from the proxied object.\n    :param unbound_message: The error message to show if the\n        context-local object is unbound.\n\n    Proxy a :class:`~contextvars.ContextVar` to make it easier to\n    access. Pass a name to proxy that attribute.\n\n    .. code-block:: python\n\n        _request_var = ContextVar("request")\n        request = LocalProxy(_request_var)\n        session = LocalProxy(_request_var, "session")\n\n    Proxy an attribute on a :class:`Local` namespace by calling the\n    local with the attribute name:\n\n    .. code-block:: python\n\n        data = Local()\n        user = data("user")\n\n    Proxy the top item on a :class:`LocalStack` by calling the local.\n    Pass a name to proxy that attribute.\n\n    .. code-block::\n\n        app_stack = LocalStack()\n        current_app = app_stack()\n        g = app_stack("g")\n\n    Pass a function to proxy the return value from that function. This\n    was previously used to access attributes of local objects before\n    that was supported directly.\n\n    .. code-block:: python\n\n        session = LocalProxy(lambda: request.session)\n\n    ``__repr__`` and ``__class__`` are proxied, so ``repr(x)`` and\n    ``isinstance(x, cls)`` will look like the proxied object. Use\n    ``issubclass(type(x), LocalProxy)`` to check if an object is a\n    proxy.\n\n    .. code-block:: python\n\n        repr(user)  # <User admin>\n        isinstance(user, User)  # True\n        issubclass(type(user), LocalProxy)  # True\n\n    .. versionchanged:: 2.2.2\n        ``__wrapped__`` is set when wrapping an object, not only when\n        wrapping a function, to prevent doctest from failing.\n\n    .. versionchanged:: 2.2\n        Can proxy a ``ContextVar`` or ``LocalStack`` directly.\n\n    .. versionchanged:: 2.2\n        The ``name`` parameter can be used with any proxied object, not\n        only ``Local``.\n\n    .. versionchanged:: 2.2\n        Added the ``unbound_message`` parameter.\n\n    .. versionchanged:: 2.0\n        Updated proxied attributes and methods to reflect the current\n        data model.\n\n    .. versionchanged:: 0.6.1\n        The class can be instantiated with a callable.\n    '
    _get_current_object: 't.Callable[[], T]' = ('__wrapped', '_get_current_object')
    
    def __init__(self = None, local = None, name = None, *, unbound_message):
        pass
    # WARNING: Decompyle incomplete

    __doc__ = _ProxyLookup(class_value = __doc__, fallback = (lambda self: type(self).__doc__), is_attr = True)
    __wrapped__ = _ProxyLookup(fallback = (lambda self: self._LocalProxy__wrapped), is_attr = True)
    __repr__ = _ProxyLookup(repr, fallback = (lambda self: f'''<{type(self).__name__} unbound>'''))
    __str__ = _ProxyLookup(str)
    __bytes__ = _ProxyLookup(bytes)
    __format__ = _ProxyLookup()
    __lt__ = _ProxyLookup(operator.lt)
    __le__ = _ProxyLookup(operator.le)
    __eq__ = _ProxyLookup(operator.eq)
    __ne__ = _ProxyLookup(operator.ne)
    __gt__ = _ProxyLookup(operator.gt)
    __ge__ = _ProxyLookup(operator.ge)
    __hash__ = _ProxyLookup(hash)
    __bool__ = _ProxyLookup(bool, fallback = (lambda self: False))
    __getattr__ = _ProxyLookup(getattr)
    __setattr__ = _ProxyLookup(setattr)
    __delattr__ = _ProxyLookup(delattr)
    __dir__ = _ProxyLookup(dir, fallback = (lambda self: []))
    __class__ = _ProxyLookup(fallback = (lambda self: type(self)), is_attr = True)
    __instancecheck__ = _ProxyLookup((lambda self, other: isinstance(other, self)))
    __subclasscheck__ = _ProxyLookup((lambda self, other: issubclass(other, self)))
    __call__ = _ProxyLookup((lambda self: pass# WARNING: Decompyle incomplete
))
    __len__ = _ProxyLookup(len)
    __length_hint__ = _ProxyLookup(operator.length_hint)
    __getitem__ = _ProxyLookup(operator.getitem)
    __setitem__ = _ProxyLookup(operator.setitem)
    __delitem__ = _ProxyLookup(operator.delitem)
    __iter__ = _ProxyLookup(iter)
    __next__ = _ProxyLookup(next)
    __reversed__ = _ProxyLookup(reversed)
    __contains__ = _ProxyLookup(operator.contains)
    __add__ = _ProxyLookup(operator.add)
    __sub__ = _ProxyLookup(operator.sub)
    __mul__ = _ProxyLookup(operator.mul)
    __matmul__ = _ProxyLookup(operator.matmul)
    __truediv__ = _ProxyLookup(operator.truediv)
    __floordiv__ = _ProxyLookup(operator.floordiv)
    __mod__ = _ProxyLookup(operator.mod)
    __divmod__ = _ProxyLookup(divmod)
    __pow__ = _ProxyLookup(pow)
    __lshift__ = _ProxyLookup(operator.lshift)
    __rshift__ = _ProxyLookup(operator.rshift)
    __and__ = _ProxyLookup(operator.and_)
    __xor__ = _ProxyLookup(operator.xor)
    __or__ = _ProxyLookup(operator.or_)
    __radd__ = _ProxyLookup(_l_to_r_op(operator.add))
    __rsub__ = _ProxyLookup(_l_to_r_op(operator.sub))
    __rmul__ = _ProxyLookup(_l_to_r_op(operator.mul))
    __rmatmul__ = _ProxyLookup(_l_to_r_op(operator.matmul))
    __rtruediv__ = _ProxyLookup(_l_to_r_op(operator.truediv))
    __rfloordiv__ = _ProxyLookup(_l_to_r_op(operator.floordiv))
    __rmod__ = _ProxyLookup(_l_to_r_op(operator.mod))
    __rdivmod__ = _ProxyLookup(_l_to_r_op(divmod))
    __rpow__ = _ProxyLookup(_l_to_r_op(pow))
    __rlshift__ = _ProxyLookup(_l_to_r_op(operator.lshift))
    __rrshift__ = _ProxyLookup(_l_to_r_op(operator.rshift))
    __rand__ = _ProxyLookup(_l_to_r_op(operator.and_))
    __rxor__ = _ProxyLookup(_l_to_r_op(operator.xor))
    __ror__ = _ProxyLookup(_l_to_r_op(operator.or_))
    __iadd__ = _ProxyIOp(operator.iadd)
    __isub__ = _ProxyIOp(operator.isub)
    __imul__ = _ProxyIOp(operator.imul)
    __imatmul__ = _ProxyIOp(operator.imatmul)
    __itruediv__ = _ProxyIOp(operator.itruediv)
    __ifloordiv__ = _ProxyIOp(operator.ifloordiv)
    __imod__ = _ProxyIOp(operator.imod)
    __ipow__ = _ProxyIOp(operator.ipow)
    __ilshift__ = _ProxyIOp(operator.ilshift)
    __irshift__ = _ProxyIOp(operator.irshift)
    __iand__ = _ProxyIOp(operator.iand)
    __ixor__ = _ProxyIOp(operator.ixor)
    __ior__ = _ProxyIOp(operator.ior)
    __neg__ = _ProxyLookup(operator.neg)
    __pos__ = _ProxyLookup(operator.pos)
    __abs__ = _ProxyLookup(abs)
    __invert__ = _ProxyLookup(operator.invert)
    __complex__ = _ProxyLookup(complex)
    __int__ = _ProxyLookup(int)
    __float__ = _ProxyLookup(float)
    __index__ = _ProxyLookup(operator.index)
    __round__ = _ProxyLookup(round)
    __trunc__ = _ProxyLookup(math.trunc)
    __floor__ = _ProxyLookup(math.floor)
    __ceil__ = _ProxyLookup(math.ceil)
    __enter__ = _ProxyLookup()
    __exit__ = _ProxyLookup()
    __await__ = _ProxyLookup()
    __aiter__ = _ProxyLookup()
    __anext__ = _ProxyLookup()
    __aenter__ = _ProxyLookup()
    __aexit__ = _ProxyLookup()
    __copy__ = _ProxyLookup(copy.copy)
    __deepcopy__ = _ProxyLookup(copy.deepcopy)

LocalProxy = <NODE:27>(LocalProxy, 'LocalProxy', t.Generic[T])

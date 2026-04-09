# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: headers.pyc (Python 3.11)

from __future__ import annotations
from collections.abc import abc as cabc
import re
import typing as t
from _internal import _missing
from exceptions import BadRequestKeyError
from mixins import ImmutableHeadersMixin
from structures import iter_multi_items
from structures import MultiDict
if t.TYPE_CHECKING:
    import typing_extensions as te
    from _typeshed.wsgi import WSGIEnvironment
T = t.TypeVar('T')

class Headers:
    """An object that stores some headers. It has a dict-like interface,
    but is ordered, can store the same key multiple times, and iterating
    yields ``(key, value)`` pairs instead of only keys.

    This data structure is useful if you want a nicer way to handle WSGI
    headers which are stored as tuples in a list.

    From Werkzeug 0.3 onwards, the :exc:`KeyError` raised by this class is
    also a subclass of the :class:`~exceptions.BadRequest` HTTP exception
    and will render a page for a ``400 BAD REQUEST`` if caught in a
    catch-all for HTTP exceptions.

    Headers is mostly compatible with the Python :class:`wsgiref.headers.Headers`
    class, with the exception of `__getitem__`.  :mod:`wsgiref` will return
    `None` for ``headers['missing']``, whereas :class:`Headers` will raise
    a :class:`KeyError`.

    To create a new ``Headers`` object, pass it a list, dict, or
    other ``Headers`` object with default values. These values are
    validated the same way values added later are.

    :param defaults: The list of default values for the :class:`Headers`.

    .. versionchanged:: 3.1
        Implement ``|`` and ``|=`` operators.

    .. versionchanged:: 2.1.0
        Default values are validated the same as values added later.

    .. versionchanged:: 0.9
       This data structure now stores unicode values similar to how the
       multi dicts do it.  The main difference is that bytes can be set as
       well which will automatically be latin1 decoded.

    .. versionchanged:: 0.9
       The :meth:`linked` function was removed without replacement as it
       was an API that does not support the changes to the encoding model.
    """
    
    def __init__(self = None, defaults = None):
        self._list = []
    # WARNING: Decompyle incomplete

    __getitem__ = (lambda self = None, key = None: pass)()
    __getitem__ = (lambda self = None, key = None: pass)()
    __getitem__ = (lambda self = None, key = None: pass)()
    
    def __getitem__(self = None, key = None):
        if isinstance(key, str):
            return self._get_key(key)
        if None(key, int):
            return self._list[key]
        return None.__class__(self._list[key])

    
    def _get_key(self = None, key = None):
        ikey = key.lower()
        for k, v in self._list:
            if k.lower() == ikey:
                
                return None, v
            raise BadRequestKeyError(key)

    
    def __eq__(self = None, other = None):
        if other.__class__ is not self.__class__:
            return NotImplemented
        
        def lowered(item = None):
            pass
        # WARNING: Decompyle incomplete

        return set(map(lowered, other._list)) == set(map(lowered, self._list))

    __hash__ = None
    get = (lambda self = None, key = None: pass)()
    get = (lambda self = None, key = None, default = t.overload: pass)()
    get = (lambda self = None, key = None, default = t.overload: pass)()
    get = (lambda self = None, key = None, type = t.overload: pass)()
    get = (lambda self = None, key = None, default = t.overload, type = ('key', 'str', 'default', 'T', 'type', 'cabc.Callable[[str], T]', 'return', 'T'): pass)()
    
    def get(self = None, key = None, default = None, type = (None, None)):
        """Return the default value if the requested data doesn't exist.
        If `type` is provided and is a callable it should convert the value,
        return it or raise a :exc:`ValueError` if that is not possible.  In
        this case the function will return the default as if the value was not
        found:

        >>> d = Headers([('Content-Length', '42')])
        >>> d.get('Content-Length', type=int)
        42

        :param key: The key to be looked up.
        :param default: The default value to be returned if the key can't
                        be looked up.  If not further specified `None` is
                        returned.
        :param type: A callable that is used to cast the value in the
                     :class:`Headers`.  If a :exc:`ValueError` is raised
                     by this callable the default value is returned.

        .. versionchanged:: 3.0
            The ``as_bytes`` parameter was removed.

        .. versionchanged:: 0.9
            The ``as_bytes`` parameter was added.
        """
        
        try:
            rv = self._get_key(key)
        except KeyError:
            return 

    # WARNING: Decompyle incomplete

    getlist = (lambda self = None, key = None: pass)()
    getlist = (lambda self = None, key = None, type = t.overload: pass)()
    
    def getlist(self = None, key = None, type = None):
        '''Return the list of items for a given key. If that key is not in the
        :class:`Headers`, the return value will be an empty list.  Just like
        :meth:`get`, :meth:`getlist` accepts a `type` parameter.  All items will
        be converted with the callable defined there.

        :param key: The key to be looked up.
        :param type: A callable that is used to cast the value in the
                     :class:`Headers`.  If a :exc:`ValueError` is raised
                     by this callable the value will be removed from the list.
        :return: a :class:`list` of all the values for the key.

        .. versionchanged:: 3.0
            The ``as_bytes`` parameter was removed.

        .. versionchanged:: 0.9
            The ``as_bytes`` parameter was added.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def get_all(self = None, name = None):
        '''Return a list of all the values for the named field.

        This method is compatible with the :mod:`wsgiref`
        :meth:`~wsgiref.headers.Headers.get_all` method.
        '''
        return self.getlist(name)

    
    def items(self = None, lower = None):
        pass
    # WARNING: Decompyle incomplete

    
    def keys(self = None, lower = None):
        pass
    # WARNING: Decompyle incomplete

    
    def values(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def extend(self = None, arg = None, **kwargs):
        '''Extend headers in this object with items from another object
        containing header items as well as keyword arguments.

        To replace existing keys instead of extending, use
        :meth:`update` instead.

        If provided, the first argument can be another :class:`Headers`
        object, a :class:`MultiDict`, :class:`dict`, or iterable of
        pairs.

        .. versionchanged:: 1.0
            Support :class:`MultiDict`. Allow passing ``kwargs``.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def __delitem__(self = None, key = None):
        if isinstance(key, str):
            self._del_key(key)
            return None
        del None._list[key]

    
    def _del_key(self = None, key = None):
        key = key.lower()
        new = []
        for k, v in self._list:
            if k.lower() != key:
                new.append((k, v))
            self._list[:] = new
            return None

    
    def remove(self = None, key = None):
        '''Remove a key.

        :param key: The key to be removed.
        '''
        return self._del_key(key)

    pop = (lambda self = None: pass)()
    pop = (lambda self = None, key = None: pass)()
    pop = (lambda self = None, key = None: pass)()
    pop = (lambda self = None, key = None, default = t.overload: pass)()
    pop = (lambda self = None, key = None, default = t.overload: pass)()
    
    def pop(self = None, key = None, default = None):
        """Removes and returns a key or index.

        :param key: The key to be popped.  If this is an integer the item at
                    that position is removed, if it's a string the value for
                    that key is.  If the key is omitted or `None` the last
                    item is removed.
        :return: an item.
        """
        pass
    # WARNING: Decompyle incomplete

    
    def popitem(self = None):
        '''Removes a key or index and returns a (key, value) item.'''
        return self._list.pop()

    
    def __contains__(self = None, key = None):
        '''Check if a key is present.'''
        
        try:
            self._get_key(key)
        except KeyError:
            return False

        return True

    
    def __iter__(self = None):
        '''Yield ``(key, value)`` tuples.'''
        return iter(self._list)

    
    def __len__(self = None):
        return len(self._list)

    
    def add(self = None, key = None, value = None, **kwargs):
        """Add a new header tuple to the list.

        Keyword arguments can specify additional parameters for the header
        value, with underscores converted to dashes::

        >>> d = Headers()
        >>> d.add('Content-Type', 'text/plain')
        >>> d.add('Content-Disposition', 'attachment', filename='foo.png')

        The keyword argument dumping uses :func:`dump_options_header`
        behind the scenes.

        .. versionchanged:: 0.4.1
            keyword arguments were added for :mod:`wsgiref` compatibility.
        """
        if kwargs:
            value = _options_header_vkw(value, kwargs)
        value_str = _str_header_value(value)
        self._list.append((key, value_str))

    
    def add_header(self = None, key = None, value = None, **kwargs):
        '''Add a new header tuple to the list.

        An alias for :meth:`add` for compatibility with the :mod:`wsgiref`
        :meth:`~wsgiref.headers.Headers.add_header` method.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def clear(self = None):
        '''Clears all headers.'''
        self._list.clear()

    
    def set(self = None, key = None, value = None, **kwargs):
        '''Remove all header tuples for `key` and add a new one.  The newly
        added key either appears at the end of the list if there was no
        entry or replaces the first one.

        Keyword arguments can specify additional parameters for the header
        value, with underscores converted to dashes.  See :meth:`add` for
        more information.

        .. versionchanged:: 0.6.1
           :meth:`set` now accepts the same arguments as :meth:`add`.

        :param key: The key to be inserted.
        :param value: The value to be inserted.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def setlist(self = None, key = None, values = None):
        '''Remove any existing values for a header and add new ones.

        :param key: The header key to set.
        :param values: An iterable of values to set for the key.

        .. versionadded:: 1.0
        '''
        if values:
            values_iter = iter(values)
            self.set(key, next(values_iter))
            for value in values_iter:
                self.add(key, value)
                return None
                self.remove(key)
                return None

    
    def setdefault(self = None, key = None, default = None):
        '''Return the first value for the key if it is in the headers,
        otherwise set the header to the value given by ``default`` and
        return that.

        :param key: The header key to get.
        :param default: The value to set for the key if it is not in the
            headers.
        '''
        
        try:
            return self._get_key(key)
        except KeyError:
            pass

        self.set(key, default)
        return self._get_key(key)

    
    def setlistdefault(self = None, key = None, default = None):
        '''Return the list of values for the key if it is in the
        headers, otherwise set the header to the list of values given
        by ``default`` and return that.

        Unlike :meth:`MultiDict.setlistdefault`, modifying the returned
        list will not affect the headers.

        :param key: The header key to get.
        :param default: An iterable of values to set for the key if it
            is not in the headers.

        .. versionadded:: 1.0
        '''
        if key not in self:
            self.setlist(key, default)
        return self.getlist(key)

    __setitem__ = (lambda self = None, key = None, value = t.overload: pass)()
    __setitem__ = (lambda self = None, key = None, value = t.overload: pass)()
    __setitem__ = (lambda self = None, key = None, value = t.overload: pass)()
    
    def __setitem__(self = None, key = None, value = None):

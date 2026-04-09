# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: url.pyc (Python 3.11)

'''Provides the :class:`~sqlalchemy.engine.url.URL` class which encapsulates
information about a database connection specification.

The URL object is created automatically when
:func:`~sqlalchemy.engine.create_engine` is called with a string
argument; alternatively, the URL is a public-facing construct which can
be used directly and is also accepted directly by ``create_engine()``.
'''
from __future__ import annotations
from collections.abc import abc as collections_abc
import re
from typing import Any
from typing import cast
from typing import Dict
from typing import Iterable
from typing import List
from typing import Mapping
from typing import NamedTuple
from typing import Optional
from typing import overload
from typing import Sequence
from typing import Tuple
from typing import Type
from typing import Union
from urllib.parse import parse_qsl
from urllib.parse import quote
from urllib.parse import quote_plus
from urllib.parse import unquote
from interfaces import Dialect
from  import exc
from  import util
from dialects import plugins
from dialects import registry

class URL(NamedTuple):
    query: 'util.immutabledict[str, Union[Tuple[str, ...], str]]' = "\n    Represent the components of a URL used to connect to a database.\n\n    URLs are typically constructed from a fully formatted URL string, where the\n    :func:`.make_url` function is used internally by the\n    :func:`_sa.create_engine` function in order to parse the URL string into\n    its individual components, which are then used to construct a new\n    :class:`.URL` object. When parsing from a formatted URL string, the parsing\n    format generally follows\n    `RFC-1738 <https://www.ietf.org/rfc/rfc1738.txt>`_, with some exceptions.\n\n    A :class:`_engine.URL` object may also be produced directly, either by\n    using the :func:`.make_url` function with a fully formed URL string, or\n    by using the :meth:`_engine.URL.create` constructor in order\n    to construct a :class:`_engine.URL` programmatically given individual\n    fields. The resulting :class:`.URL` object may be passed directly to\n    :func:`_sa.create_engine` in place of a string argument, which will bypass\n    the usage of :func:`.make_url` within the engine's creation process.\n\n    .. versionchanged:: 1.4\n\n        The :class:`_engine.URL` object is now an immutable object.  To\n        create a URL, use the :func:`_engine.make_url` or\n        :meth:`_engine.URL.create` function / method.  To modify\n        a :class:`_engine.URL`, use methods like\n        :meth:`_engine.URL.set` and\n        :meth:`_engine.URL.update_query_dict` to return a new\n        :class:`_engine.URL` object with modifications.   See notes for this\n        change at :ref:`change_5526`.\n\n    .. seealso::\n\n        :ref:`database_urls`\n\n    :class:`_engine.URL` contains the following attributes:\n\n    * :attr:`_engine.URL.drivername`: database backend and driver name, such as\n      ``postgresql+psycopg2``\n    * :attr:`_engine.URL.username`: username string\n    * :attr:`_engine.URL.password`: password string\n    * :attr:`_engine.URL.host`: string hostname\n    * :attr:`_engine.URL.port`: integer port number\n    * :attr:`_engine.URL.database`: string database name\n    * :attr:`_engine.URL.query`: an immutable mapping representing the query\n      string.  contains strings for keys and either strings or tuples of\n      strings for values.\n\n\n    "
    create = (lambda cls, drivername, username, password = None, host = None, port = classmethod, database = (None, None, None, None, None, util.EMPTY_DICT), query = ('drivername', 'str', 'username', 'Optional[str]', 'password', 'Optional[str]', 'host', 'Optional[str]', 'port', 'Optional[int]', 'database', 'Optional[str]', 'query', 'Mapping[str, Union[Sequence[str], str]]', 'return', 'URL'): cls(cls._assert_str(drivername, 'drivername'), cls._assert_none_str(username, 'username'), password, cls._assert_none_str(host, 'host'), cls._assert_port(port), cls._assert_none_str(database, 'database'), cls._str_dict(query)))()
    _assert_port = (lambda cls = None, port = None: pass# WARNING: Decompyle incomplete
)()
    _assert_str = (lambda cls = None, v = None, paramname = classmethod: if not isinstance(v, str):
raise TypeError('%s must be a string' % paramname)v)()
    _assert_none_str = (lambda cls = None, v = None, paramname = classmethod: pass# WARNING: Decompyle incomplete
)()
    _str_dict = (lambda cls = None, dict_ = None: pass# WARNING: Decompyle incomplete
)()
    
    def set(self, drivername, username, password = None, host = None, port = None, database = (None, None, None, None, None, None, None), query = ('drivername', 'Optional[str]', 'username', 'Optional[str]', 'password', 'Optional[str]', 'host', 'Optional[str]', 'port', 'Optional[int]', 'database', 'Optional[str]', 'query', 'Optional[Mapping[str, Union[Sequence[str], str]]]', 'return', 'URL')):
        '''return a new :class:`_engine.URL` object with modifications.

        Values are used if they are non-None.  To set a value to ``None``
        explicitly, use the :meth:`_engine.URL._replace` method adapted
        from ``namedtuple``.

        :param drivername: new drivername
        :param username: new username
        :param password: new password
        :param host: new hostname
        :param port: new port
        :param query: new query parameters, passed a dict of string keys
         referring to string or sequence of string values.  Fully
         replaces the previous list of arguments.

        :return: new :class:`_engine.URL` object.

        .. versionadded:: 1.4

        .. seealso::

            :meth:`_engine.URL.update_query_dict`

        '''
        kw = { }
    # WARNING: Decompyle incomplete

    
    def _assert_replace(self = None, **kw):
        '''argument checks before calling _replace()'''
        if 'drivername' in kw:
            self._assert_str(kw['drivername'], 'drivername')
        for name in ('username', 'host', 'database'):
            if name in kw:
                self._assert_none_str(kw[name], name)
        if 'port' in kw:
            self._assert_port(kw['port'])
        if 'query' in kw:
            kw['query'] = self._str_dict(kw['query'])
    # WARNING: Decompyle incomplete

    
    def update_query_string(self = None, query_string = None, append = None):
        '''Return a new :class:`_engine.URL` object with the :attr:`_engine.URL.query`
        parameter dictionary updated by the given query string.

        E.g.::

            >>> from sqlalchemy.engine import make_url
            >>> url = make_url("postgresql+psycopg2://user:pass@host/dbname")
            >>> url = url.update_query_string(
            ...     "alt_host=host1&alt_host=host2&ssl_cipher=%2Fpath%2Fto%2Fcrt"
            ... )
            >>> str(url)
            \'postgresql+psycopg2://user:pass@host/dbname?alt_host=host1&alt_host=host2&ssl_cipher=%2Fpath%2Fto%2Fcrt\'

        :param query_string: a URL escaped query string, not including the
         question mark.

        :param append: if True, parameters in the existing query string will
         not be removed; new parameters will be in addition to those present.
         If left at its default of False, keys present in the given query
         parameters will replace those of the existing query string.

        .. versionadded:: 1.4

        .. seealso::

            :attr:`_engine.URL.query`

            :meth:`_engine.URL.update_query_dict`

        '''
        return self.update_query_pairs(parse_qsl(query_string), append = append)

    
    def update_query_pairs(self = None, key_value_pairs = None, append = None):
        '''Return a new :class:`_engine.URL` object with the
        :attr:`_engine.URL.query`
        parameter dictionary updated by the given sequence of key/value pairs

        E.g.::

            >>> from sqlalchemy.engine import make_url
            >>> url = make_url("postgresql+psycopg2://user:pass@host/dbname")
            >>> url = url.update_query_pairs(
            ...     [
            ...         ("alt_host", "host1"),
            ...         ("alt_host", "host2"),
            ...         ("ssl_cipher", "/path/to/crt"),
            ...     ]
            ... )
            >>> str(url)
            \'postgresql+psycopg2://user:pass@host/dbname?alt_host=host1&alt_host=host2&ssl_cipher=%2Fpath%2Fto%2Fcrt\'

        :param key_value_pairs: A sequence of tuples containing two strings
         each.

        :param append: if True, parameters in the existing query string will
         not be removed; new parameters will be in addition to those present.
         If left at its default of False, keys present in the given query
         parameters will replace those of the existing query string.

        .. versionadded:: 1.4

        .. seealso::

            :attr:`_engine.URL.query`

            :meth:`_engine.URL.difference_update_query`

            :meth:`_engine.URL.set`

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def update_query_dict(self = None, query_parameters = None, append = None):
        '''Return a new :class:`_engine.URL` object with the
        :attr:`_engine.URL.query` parameter dictionary updated by the given
        dictionary.

        The dictionary typically contains string keys and string values.
        In order to represent a query parameter that is expressed multiple
        times, pass a sequence of string values.

        E.g.::


            >>> from sqlalchemy.engine import make_url
            >>> url = make_url("postgresql+psycopg2://user:pass@host/dbname")
            >>> url = url.update_query_dict(
            ...     {"alt_host": ["host1", "host2"], "ssl_cipher": "/path/to/crt"}
            ... )
            >>> str(url)
            \'postgresql+psycopg2://user:pass@host/dbname?alt_host=host1&alt_host=host2&ssl_cipher=%2Fpath%2Fto%2Fcrt\'


        :param query_parameters: A dictionary with string keys and values
         that are either strings, or sequences of strings.

        :param append: if True, parameters in the existing query string will
         not be removed; new parameters will be in addition to those present.
         If left at its default of False, keys present in the given query
         parameters will replace those of the existing query string.


        .. versionadded:: 1.4

        .. seealso::

            :attr:`_engine.URL.query`

            :meth:`_engine.URL.update_query_string`

            :meth:`_engine.URL.update_query_pairs`

            :meth:`_engine.URL.difference_update_query`

            :meth:`_engine.URL.set`

        '''
        return self.update_query_pairs(query_parameters.items(), append = append)

    
    def difference_update_query(self = None, names = None):
        '''
        Remove the given names from the :attr:`_engine.URL.query` dictionary,
        returning the new :class:`_engine.URL`.

        E.g.::

            url = url.difference_update_query(["foo", "bar"])

        Equivalent to using :meth:`_engine.URL.set` as follows::

            url = url.set(
                query={
                    key: url.query[key]
                    for key in set(url.query).difference(["foo", "bar"])
                }
            )

        .. versionadded:: 1.4

        .. seealso::

            :attr:`_engine.URL.query`

            :meth:`_engine.URL.update_query_dict`

            :meth:`_engine.URL.set`

        '''
        pass
    # WARNING: Decompyle incomplete

    normalized_query = (lambda self = None: (lambda .0: pass# WARNING: Decompyle incomplete
)(self.query.items()())
)()
    __to_string__ = (lambda self = None, hide_password = None: self.render_as_string(hide_password = hide_password))()
    
    def render_as_string(self = None, hide_password = None):
        '''Render this :class:`_engine.URL` object as a string.

        This method is used when the ``__str__()`` or ``__repr__()``
        methods are used.   The method directly includes additional options.

        :param hide_password: Defaults to True.   The password is not shown
         in the string unless this is set to False.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self = None):
        return self.render_as_string()

    
    def __copy__(self = None):
        return self.__class__.create(self.drivername, self.username, self.password, self.host, self.port, self.database, self.query)

    
    def __deepcopy__(self = None, memo = None):
        return self.__copy__()

    
    def __hash__(self = None):
        return hash(str(self))

    
    def __eq__(self = None, other = None):

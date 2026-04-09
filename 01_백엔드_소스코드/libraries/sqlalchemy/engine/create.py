# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: create.pyc (Python 3.11)

from __future__ import annotations
import inspect
import typing
from typing import Any
from typing import Callable
from typing import cast
from typing import Dict
from typing import List
from typing import Optional
from typing import overload
from typing import Type
from typing import Union
from  import base
from  import url as _url
from interfaces import DBAPIConnection
from mock import create_mock_engine
from  import event
from  import exc
from  import util
from pool import _AdhocProxiedConnection
from pool import ConnectionPoolEntry
from sql import compiler
from util import immutabledict
if typing.TYPE_CHECKING:
    from base import Engine
    from interfaces import _ExecuteOptions
    from interfaces import _ParamStyle
    from interfaces import IsolationLevel
    from url import URL
    from log import _EchoFlagType
    from pool import _CreatorFnType
    from pool import _CreatorWRecFnType
    from pool import _ResetStyleArgType
    from pool import Pool
    from util.typing import Literal
create_engine = (lambda url = None, *, connect_args: pass)()
create_engine = (lambda url = None: pass)()
create_engine = (lambda url = None: pass# WARNING: Decompyle incomplete
)()

def engine_from_config(configuration = None, prefix = None, **kwargs):
    '''Create a new Engine instance using a configuration dictionary.

    The dictionary is typically produced from a config file.

    The keys of interest to ``engine_from_config()`` should be prefixed, e.g.
    ``sqlalchemy.url``, ``sqlalchemy.echo``, etc.  The \'prefix\' argument
    indicates the prefix to be searched for.  Each matching key (after the
    prefix is stripped) is treated as though it were the corresponding keyword
    argument to a :func:`_sa.create_engine` call.

    The only required key is (assuming the default prefix) ``sqlalchemy.url``,
    which provides the :ref:`database URL <database_urls>`.

    A select set of keyword arguments will be "coerced" to their
    expected type based on string values.    The set of arguments
    is extensible per-dialect using the ``engine_config_types`` accessor.

    :param configuration: A dictionary (typically produced from a config file,
        but this is not a requirement).  Items whose keys start with the value
        of \'prefix\' will have that prefix stripped, and will then be passed to
        :func:`_sa.create_engine`.

    :param prefix: Prefix to match and then strip from keys
        in \'configuration\'.

    :param kwargs: Each keyword argument to ``engine_from_config()`` itself
        overrides the corresponding item taken from the \'configuration\'
        dictionary.  Keyword arguments should *not* be prefixed.

    '''
    pass
# WARNING: Decompyle incomplete

create_pool_from_url = (lambda url = None, *, poolclass: pass)()
create_pool_from_url = (lambda url = None: pass)()

def create_pool_from_url(url = None, **kwargs):
    '''Create a pool instance from the given url.

    If ``poolclass`` is not provided the pool class used
    is selected using the dialect specified in the URL.

    The arguments passed to :func:`_sa.create_pool_from_url` are
    identical to the pool argument passed to the :func:`_sa.create_engine`
    function.

    .. versionadded:: 2.0.10
    '''
    pass
# WARNING: Decompyle incomplete

_pool_translate_kwargs = immutabledict({
    'logging_name': 'pool_logging_name',
    'echo': 'echo_pool',
    'timeout': 'pool_timeout',
    'recycle': 'pool_recycle',
    'events': 'pool_events',
    'reset_on_return': 'pool_reset_on_return',
    'pre_ping': 'pool_pre_ping',
    'use_lifo': 'pool_use_lifo' })

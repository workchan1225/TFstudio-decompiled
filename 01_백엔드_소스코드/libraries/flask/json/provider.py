# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: provider.pyc (Python 3.11)

from __future__ import annotations
import dataclasses
import decimal
import json
import typing as t
import uuid
import weakref
from datetime import date
from werkzeug.http import http_date
if t.TYPE_CHECKING:
    from sansio.app import App
    from wrappers import Response

class JSONProvider:
    '''A standard set of JSON operations for an application. Subclasses
    of this can be used to customize JSON behavior or use different
    JSON libraries.

    To implement a provider for a specific library, subclass this base
    class and implement at least :meth:`dumps` and :meth:`loads`. All
    other methods have default implementations.

    To use a different provider, either subclass ``Flask`` and set
    :attr:`~flask.Flask.json_provider_class` to a provider class, or set
    :attr:`app.json <flask.Flask.json>` to an instance of the class.

    :param app: An application instance. This will be stored as a
        :class:`weakref.proxy` on the :attr:`_app` attribute.

    .. versionadded:: 2.2
    '''
    
    def __init__(self = None, app = None):
        self._app = weakref.proxy(app)

    
    def dumps(self = None, obj = None, **kwargs):
        '''Serialize data as JSON.

        :param obj: The data to serialize.
        :param kwargs: May be passed to the underlying JSON library.
        '''
        raise NotImplementedError

    
    def dump(self = None, obj = None, fp = None, **kwargs):
        '''Serialize data as JSON and write to a file.

        :param obj: The data to serialize.
        :param fp: A file opened for writing text. Should use the UTF-8
            encoding to be valid JSON.
        :param kwargs: May be passed to the underlying JSON library.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def loads(self = None, s = None, **kwargs):
        '''Deserialize data as JSON.

        :param s: Text or UTF-8 bytes.
        :param kwargs: May be passed to the underlying JSON library.
        '''
        raise NotImplementedError

    
    def load(self = None, fp = None, **kwargs):
        '''Deserialize data as JSON read from a file.

        :param fp: A file opened for reading text or UTF-8 bytes.
        :param kwargs: May be passed to the underlying JSON library.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _prepare_response_obj(self = None, args = None, kwargs = None):

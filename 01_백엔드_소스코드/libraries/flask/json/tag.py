# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tag.pyc (Python 3.11)

"""
Tagged JSON
~~~~~~~~~~~

A compact representation for lossless serialization of non-standard JSON
types. :class:`~flask.sessions.SecureCookieSessionInterface` uses this
to serialize the session data, but it may be useful in other places. It
can be extended to support other types.

.. autoclass:: TaggedJSONSerializer
    :members:

.. autoclass:: JSONTag
    :members:

Let's see an example that adds support for
:class:`~collections.OrderedDict`. Dicts don't have an order in JSON, so
to handle this we will dump the items as a list of ``[key, value]``
pairs. Subclass :class:`JSONTag` and give it the new key ``' od'`` to
identify the type. The session serializer processes dicts first, so
insert the new tag at the front of the order since ``OrderedDict`` must
be processed before ``dict``.

.. code-block:: python

    from flask.json.tag import JSONTag

    class TagOrderedDict(JSONTag):
        __slots__ = ('serializer',)
        key = ' od'

        def check(self, value):
            return isinstance(value, OrderedDict)

        def to_json(self, value):
            return [[k, self.serializer.tag(v)] for k, v in iteritems(value)]

        def to_python(self, value):
            return OrderedDict(value)

    app.session_interface.serializer.register(TagOrderedDict, index=0)
"""
from __future__ import annotations
import typing as t
from base64 import b64decode
from base64 import b64encode
from datetime import datetime
from uuid import UUID
from markupsafe import Markup
from werkzeug.http import http_date
from werkzeug.http import parse_date
from json import dumps
from json import loads

class JSONTag:
    '''Base class for defining type tags for :class:`TaggedJSONSerializer`.'''
    __slots__ = ('serializer',)
    key: 'str | None' = None
    
    def __init__(self = None, serializer = None):
        '''Create a tagger for the given serializer.'''
        self.serializer = serializer

    
    def check(self = None, value = None):
        '''Check if the given value should be tagged by this tag.'''
        raise NotImplementedError

    
    def to_json(self = None, value = None):
        '''Convert the Python object to an object that is a valid JSON type.
        The tag will be added later.'''
        raise NotImplementedError

    
    def to_python(self = None, value = None):
        '''Convert the JSON representation back to the correct type. The tag
        will already be removed.'''
        raise NotImplementedError

    
    def tag(self = None, value = None):
        '''Convert the value to a valid JSON type and add the tag structure
        around it.'''
        return {
            self.key: self.to_json(value) }



class TagDict(JSONTag):
    '''Tag for 1-item dicts whose only key matches a registered tag.

    Internally, the dict key is suffixed with `__`, and the suffix is removed
    when deserializing.
    '''
    __slots__ = ()
    key = ' di'
    
    def check(self = None, value = None):

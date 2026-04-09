# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _rest_streaming_base.pyc (Python 3.11)

'''Helpers for server-side streaming in REST.'''
from collections import deque
import string
from typing import Deque, Union
import types
import proto
import google.protobuf.message as google
from google.protobuf.json_format import Parse

class BaseResponseIterator:
    '''Base Iterator over REST API responses. This class should not be used directly.

    Args:
        response_message_cls (Union[proto.Message, google.protobuf.message.Message]): A response
        class expected to be returned from an API.

    Raises:
        ValueError: If `response_message_cls` is not a subclass of `proto.Message` or `google.protobuf.message.Message`.
    '''
    
    def __init__(self = None, response_message_cls = None):
        self._response_message_cls = response_message_cls
        self._ready_objs = deque()
        self._obj = ''
        self._level = 0
        self._in_string = False
        self._escape_next = False
        self._grab = types.MethodType(self._create_grab(), self)

    
    def _process_chunk(self = None, chunk = None):
        if self._level == 0 and chunk[0] != '[':
            raise ValueError('Can only parse array of JSON objects, instead got %s' % chunk)
        for char in chunk:
            if char == '{':
                if self._level == 1:
                    self._obj = ''
                if not self._in_string:
                    pass
            elif char == '}':
                if not self._in_string:
                    pass
                if self._in_string and self._level == 1:
                    self._ready_objs.append(self._obj)
                elif char == '"':
                    if not self._escape_next:
                        not (self._in_string) = self, self._level -= 1, ._level
                elif char in string.whitespace:
                    if self._in_string:
                        pass
                    elif char == '[':
                        if self._level == 0:
                            pass
                        
                    elif char == ']':
                        if self._level == 1:
                            pass
                        
                    
            not (self._escape_next) if char == '\\' else False = self, self._obj += char, ._obj
            return None

    
    def _create_grab(self):
        if issubclass(self._response_message_cls, proto.Message):
            
            def grab(this):
                return this._response_message_cls.from_json(this._ready_objs.popleft(), ignore_unknown_fields = True)

            return grab
        if None(self._response_message_cls, google.protobuf.message.Message):
            
            def grab(this):
                return Parse(this._ready_objs.popleft(), this._response_message_cls())

            return grab
        raise None('Response message class must be a subclass of proto.Message or google.protobuf.message.Message.')

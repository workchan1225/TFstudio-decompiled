# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: json_parser.pyc (Python 3.11)

from collections.abc import Callable
from typing import TYPE_CHECKING, Any, TextIO
from parse_array import parse_array as _parse_array
from parse_comment import parse_comment as _parse_comment
from parse_number import parse_number as _parse_number
from parse_object import parse_object as _parse_object
from parse_string import parse_string as _parse_string
from utils.constants import STRING_DELIMITERS, JSONReturnType
from utils.json_context import JsonContext
from utils.object_comparer import ObjectComparer
from utils.string_file_wrapper import StringFileWrapper
if TYPE_CHECKING:
    from schema_repair import SchemaRepairer

class JSONParser:
    
    def parse_array(self = None, schema = None, path = None):
        return _parse_array(self, schema, path)

    
    def parse_comment(self = None):
        return _parse_comment(self)

    
    def parse_number(self = None):
        return _parse_number(self)

    
    def parse_object(self = None, schema = None, path = None):
        return _parse_object(self, schema, path)

    
    def parse_string(self = None):
        return _parse_string(self)

    
    def __init__(self, json_str, json_fd = None, logging = None, json_fd_chunk_length = None, stream_stable = (0, False, False), strict = ('json_str', str | StringFileWrapper, 'json_fd', TextIO | None, 'logging', bool | None, 'json_fd_chunk_length', int, 'stream_stable', bool, 'strict', bool, 'return', None)):
        self.json_str = json_str
        if json_fd:
            self.json_str = StringFileWrapper(json_fd, json_fd_chunk_length)
        self.index = 0
        self.context = JsonContext()
        self.logging = logging
        self.logger = []
        if logging:
            self.log = self._log
        else:
            
            self.log = lambda *args, **kwargs: pass
        self.stream_stable = stream_stable
        self.strict = strict
        self.schema_repairer = None

    
    def parse(self = None):
        return self._parse_top_level(self.parse_json)

    
    def parse_with_schema(self = None, repairer = None, schema = None):
        '''Parse with schema guidance enabled for all nested values.'''
        pass
    # WARNING: Decompyle incomplete

    
    def _parse_top_level(self = None, parse_element = None):
        json = parse_element()
    # WARNING: Decompyle incomplete

    
    def parse_json(self = None, schema = None, path = None):
        '''Parse the next JSON value and, when configured, enforce schema constraints.'''
        pass
    # WARNING: Decompyle incomplete

    
    def get_char_at(self = None, count = None):
        
        try:
            return self.json_str[self.index + count]
        except IndexError:
            return None


    
    def skip_whitespaces(self = None):
        '''
        This function quickly iterates on whitespaces, moving the self.index forward
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def scroll_whitespaces(self = None, idx = None):
        """
        This function quickly iterates on whitespaces. Doesn't move the self.index and returns the offset from self.index
        """
        pass
    # WARNING: Decompyle incomplete

    
    def skip_to_character(self = None, character = None, idx = None):
        '''
        Advance from (self.index + idx) until we hit an *unescaped* target character.
        Returns the offset (idx) from self.index to that position, or the distance to the end if not found.
        '''
        targets = set(character) if isinstance(character, list) else {
            character}
        i = self.index + idx
        n = len(self.json_str)
        backslashes = 0
    # WARNING: Decompyle incomplete

    
    def _log(self = None, text = None):
        window = 10
        start = max(self.index - window, 0)
        end = min(self.index + window, len(self.json_str))
        context = self.json_str[start:end]
        self.logger.append({
            'text': text,
            'context': context })

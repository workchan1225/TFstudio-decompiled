# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: parser.pyc (Python 3.11)

__all__ = [
    'Parser',
    'ParserError']
from error import MarkedYAMLError
from tokens import *
from events import *
from scanner import *

class ParserError(MarkedYAMLError):
    pass


class Parser:
    DEFAULT_TAGS = {
        '!': '!',
        '!!': 'tag:yaml.org,2002:' }
    
    def __init__(self):
        self.current_event = None
        self.yaml_version = None
        self.tag_handles = { }
        self.states = []
        self.marks = []
        self.state = self.parse_stream_start

    
    def dispose(self):
        self.states = []
        self.state = None

    
    def check_event(self, *choices):
        pass
    # WARNING: Decompyle incomplete

    
    def peek_event(self):
        pass
    # WARNING: Decompyle incomplete

    
    def get_event(self):
        pass
    # WARNING: Decompyle incomplete

    
    def parse_stream_start(self):
        token = self.get_token()
        event = StreamStartEvent(token.start_mark, token.end_mark, encoding = token.encoding)
        self.state = self.parse_implicit_document_start
        return event

    
    def parse_implicit_document_start(self):
        if not self.check_token(DirectiveToken, DocumentStartToken, StreamEndToken):
            self.tag_handles = self.DEFAULT_TAGS
            token = self.peek_token()
            start_mark = token.start_mark
            end_mark = token.start_mark
            event = DocumentStartEvent(start_mark, end_mark, explicit = False)
            self.states.append(self.parse_document_end)
            self.state = self.parse_block_node
            return event
        return None.parse_document_start()

    
    def parse_document_start(self):
        pass
    # WARNING: Decompyle incomplete

    
    def parse_document_end(self):
        token = self.peek_token()
        start_mark = token.start_mark
        end_mark = token.start_mark
        explicit = False
        if self.check_token(DocumentEndToken):
            token = self.get_token()
            end_mark = token.end_mark
            explicit = True
        event = DocumentEndEvent(start_mark, end_mark, explicit = explicit)
        self.state = self.parse_document_start
        return event

    
    def parse_document_content(self):
        if self.check_token(DirectiveToken, DocumentStartToken, DocumentEndToken, StreamEndToken):
            event = self.process_empty_scalar(self.peek_token().start_mark)
            self.state = self.states.pop()
            return event
        return None.parse_block_node()

    
    def process_directives(self):
        self.yaml_version = None
        self.tag_handles = { }
    # WARNING: Decompyle incomplete

    
    def parse_block_node(self):
        return self.parse_node(block = True)

    
    def parse_flow_node(self):
        return self.parse_node()

    
    def parse_block_node_or_indentless_sequence(self):
        return self.parse_node(block = True, indentless_sequence = True)

    
    def parse_node(self, block, indentless_sequence = (False, False)):
        if self.check_token(AliasToken):
            token = self.get_token()
            event = AliasEvent(token.value, token.start_mark, token.end_mark)
            self.state = self.states.pop()
    # WARNING: Decompyle incomplete

    
    def parse_block_sequence_first_entry(self):
        token = self.get_token()
        self.marks.append(token.start_mark)
        return self.parse_block_sequence_entry()

    
    def parse_block_sequence_entry(self):
        if self.check_token(BlockEntryToken):
            token = self.get_token()
            if not self.check_token(BlockEntryToken, BlockEndToken):
                self.states.append(self.parse_block_sequence_entry)
                return self.parse_block_node()
            self.state = None.parse_block_sequence_entry
            return self.process_empty_scalar(token.end_mark)
        if not None.check_token(BlockEndToken):
            token = self.peek_token()
            raise ParserError('while parsing a block collection', self.marks[-1], 'expected <block end>, but found %r' % token.id, token.start_mark)
        token = self.get_token()
        event = SequenceEndEvent(token.start_mark, token.end_mark)
        self.state = self.states.pop()
        self.marks.pop()
        return event

    
    def parse_indentless_sequence_entry(self):
        if self.check_token(BlockEntryToken):
            token = self.get_token()
            if not self.check_token(BlockEntryToken, KeyToken, ValueToken, BlockEndToken):
                self.states.append(self.parse_indentless_sequence_entry)
                return self.parse_block_node()
            self.state = None.parse_indentless_sequence_entry
            return self.process_empty_scalar(token.end_mark)
        token = None.peek_token()
        event = SequenceEndEvent(token.start_mark, token.start_mark)
        self.state = self.states.pop()
        return event

    
    def parse_block_mapping_first_key(self):
        token = self.get_token()
        self.marks.append(token.start_mark)
        return self.parse_block_mapping_key()

    
    def parse_block_mapping_key(self):
        if self.check_token(KeyToken):
            token = self.get_token()
            if not self.check_token(KeyToken, ValueToken, BlockEndToken):
                self.states.append(self.parse_block_mapping_value)
                return self.parse_block_node_or_indentless_sequence()
            self.state = None.parse_block_mapping_value
            return self.process_empty_scalar(token.end_mark)
        if not None.check_token(BlockEndToken):
            token = self.peek_token()
            raise ParserError('while parsing a block mapping', self.marks[-1], 'expected <block end>, but found %r' % token.id, token.start_mark)
        token = self.get_token()
        event = MappingEndEvent(token.start_mark, token.end_mark)
        self.state = self.states.pop()
        self.marks.pop()
        return event

    
    def parse_block_mapping_value(self):
        if self.check_token(ValueToken):
            token = self.get_token()
            if not self.check_token(KeyToken, ValueToken, BlockEndToken):
                self.states.append(self.parse_block_mapping_key)
                return self.parse_block_node_or_indentless_sequence()
            self.state = None.parse_block_mapping_key
            return self.process_empty_scalar(token.end_mark)
        self.state = None.parse_block_mapping_key
        token = self.peek_token()
        return self.process_empty_scalar(token.start_mark)

    
    def parse_flow_sequence_first_entry(self):
        token = self.get_token()
        self.marks.append(token.start_mark)
        return self.parse_flow_sequence_entry(first = True)

    
    def parse_flow_sequence_entry(self, first = (False,)):

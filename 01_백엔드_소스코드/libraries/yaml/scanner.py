# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: scanner.pyc (Python 3.11)

__all__ = [
    'Scanner',
    'ScannerError']
from error import MarkedYAMLError
from tokens import *

class ScannerError(MarkedYAMLError):
    pass


class SimpleKey:
    
    def __init__(self, token_number, required, index, line, column, mark):
        self.token_number = token_number
        self.required = required
        self.index = index
        self.line = line
        self.column = column
        self.mark = mark



class Scanner:
    __module__ = __name__
    __qualname__ = 'Scanner'
    
    def __init__(self):
        '''Initialize the scanner.'''
        self.done = False
        self.flow_level = 0
        self.tokens = []
        self.fetch_stream_start()
        self.tokens_taken = 0
        self.indent = -1
        self.indents = []
        self.allow_simple_key = True
        self.possible_simple_keys = { }

    
    def check_token(self, *choices):
        pass
    # WARNING: Decompyle incomplete

    
    def peek_token(self):
        pass
    # WARNING: Decompyle incomplete

    
    def get_token(self):
        pass
    # WARNING: Decompyle incomplete

    
    def need_more_tokens(self):
        if self.done:
            return False
        if not None.tokens:
            return True
        None.stale_possible_simple_keys()
        if self.next_possible_simple_key() == self.tokens_taken:
            return True

    
    def fetch_more_tokens(self):
        self.scan_to_next_token()
        self.stale_possible_simple_keys()
        self.unwind_indent(self.column)
        ch = self.peek()
        if ch == '\x00':
            return self.fetch_stream_end()
        if None == '%' and self.check_directive():
            return self.fetch_directive()
        if None == '-' and self.check_document_start():
            return self.fetch_document_start()
        if None == '.' and self.check_document_end():
            return self.fetch_document_end()
        if None == '[':
            return self.fetch_flow_sequence_start()
        if None == '{':
            return self.fetch_flow_mapping_start()
        if None == ']':
            return self.fetch_flow_sequence_end()
        if None == '}':
            return self.fetch_flow_mapping_end()
        if None == ',':
            return self.fetch_flow_entry()
        if None == '-' and self.check_block_entry():
            return self.fetch_block_entry()
        if None == '?' and self.check_key():
            return self.fetch_key()
        if None == ':' and self.check_value():
            return self.fetch_value()
        if None == '*':
            return self.fetch_alias()
        if None == '&':
            return self.fetch_anchor()
        if None == '!':
            return self.fetch_tag()
        if not None == '|' and self.flow_level:
            return self.fetch_literal()
        if not None == '>' and self.flow_level:
            return self.fetch_folded()
        if None == "'":
            return self.fetch_single()
        if None == '"':
            return self.fetch_double()
        if None.check_plain():
            return self.fetch_plain()
        raise None('while scanning for the next token', None, 'found character %r that cannot start any token' % ch, self.get_mark())

    
    def next_possible_simple_key(self):
        min_token_number = None
    # WARNING: Decompyle incomplete

    
    def stale_possible_simple_keys(self):
        for level in list(self.possible_simple_keys):
            key = self.possible_simple_keys[level]
            if key.line != self.line or self.index - key.index > 1024:
                if key.required:
                    raise ScannerError('while scanning a simple key', key.mark, "could not find expected ':'", self.get_mark())
                del self.possible_simple_keys[level]
            return None

    
    def save_possible_simple_key(self):
        if not (self.flow_level):
            pass
        required = self.indent == self.column
        if self.allow_simple_key:
            self.remove_possible_simple_key()
            token_number = self.tokens_taken + len(self.tokens)
            key = SimpleKey(token_number, required, self.index, self.line, self.column, self.get_mark())
            self.possible_simple_keys[self.flow_level] = key
            return None

    
    def remove_possible_simple_key(self):
        if self.flow_level in self.possible_simple_keys:
            key = self.possible_simple_keys[self.flow_level]
            if key.required:
                raise ScannerError('while scanning a simple key', key.mark, "could not find expected ':'", self.get_mark())
            del self.possible_simple_keys[self.flow_level]
            return None

    
    def unwind_indent(self, column):
        if self.flow_level:
            return None
    # WARNING: Decompyle incomplete

    
    def add_indent(self, column):
        if self.indent < column:
            self.indents.append(self.indent)
            self.indent = column
            return True

    
    def fetch_stream_start(self):
        mark = self.get_mark()
        self.tokens.append(StreamStartToken(mark, mark, encoding = self.encoding))

    
    def fetch_stream_end(self):
        self.unwind_indent(-1)
        self.remove_possible_simple_key()
        self.allow_simple_key = False
        self.possible_simple_keys = { }
        mark = self.get_mark()
        self.tokens.append(StreamEndToken(mark, mark))
        self.done = True

    
    def fetch_directive(self):
        self.unwind_indent(-1)
        self.remove_possible_simple_key()
        self.allow_simple_key = False
        self.tokens.append(self.scan_directive())

    
    def fetch_document_start(self):
        self.fetch_document_indicator(DocumentStartToken)

    
    def fetch_document_end(self):
        self.fetch_document_indicator(DocumentEndToken)

    
    def fetch_document_indicator(self, TokenClass):
        self.unwind_indent(-1)
        self.remove_possible_simple_key()
        self.allow_simple_key = False
        start_mark = self.get_mark()
        self.forward(3)
        end_mark = self.get_mark()
        self.tokens.append(TokenClass(start_mark, end_mark))

    
    def fetch_flow_sequence_start(self):
        self.fetch_flow_collection_start(FlowSequenceStartToken)

    
    def fetch_flow_mapping_start(self):
        self.fetch_flow_collection_start(FlowMappingStartToken)

    
    def fetch_flow_collection_start(self, TokenClass):
        self.save_possible_simple_key()
        True = self, self.flow_level += 1, .flow_level
        start_mark = self.get_mark()
        self.forward()
        end_mark = self.get_mark()
        self.tokens.append(TokenClass(start_mark, end_mark))

    
    def fetch_flow_sequence_end(self):
        self.fetch_flow_collection_end(FlowSequenceEndToken)

    
    def fetch_flow_mapping_end(self):
        self.fetch_flow_collection_end(FlowMappingEndToken)

    
    def fetch_flow_collection_end(self, TokenClass):
        self.remove_possible_simple_key()
        False = self, self.flow_level -= 1, .flow_level
        start_mark = self.get_mark()
        self.forward()
        end_mark = self.get_mark()
        self.tokens.append(TokenClass(start_mark, end_mark))

    
    def fetch_flow_entry(self):
        self.allow_simple_key = True
        self.remove_possible_simple_key()
        start_mark = self.get_mark()
        self.forward()
        end_mark = self.get_mark()
        self.tokens.append(FlowEntryToken(start_mark, end_mark))

    
    def fetch_block_entry(self):
        if not self.flow_level:
            if not self.allow_simple_key:
                raise ScannerError(None, None, 'sequence entries are not allowed here', self.get_mark())
            if self.add_indent(self.column):
                mark = self.get_mark()
                self.tokens.append(BlockSequenceStartToken(mark, mark))
            
        self.allow_simple_key = True
        self.remove_possible_simple_key()
        start_mark = self.get_mark()
        self.forward()
        end_mark = self.get_mark()
        self.tokens.append(BlockEntryToken(start_mark, end_mark))

    
    def fetch_key(self):
        if not self.flow_level:
            if not self.allow_simple_key:
                raise ScannerError(None, None, 'mapping keys are not allowed here', self.get_mark())
            if self.add_indent(self.column):
                mark = self.get_mark()
                self.tokens.append(BlockMappingStartToken(mark, mark))
        self.allow_simple_key = not (self.flow_level)
        self.remove_possible_simple_key()
        start_mark = self.get_mark()
        self.forward()
        end_mark = self.get_mark()
        self.tokens.append(KeyToken(start_mark, end_mark))

    
    def fetch_value(self):
        if self.flow_level in self.possible_simple_keys:
            key = self.possible_simple_keys[self.flow_level]
            del self.possible_simple_keys[self.flow_level]
            self.tokens.insert(key.token_number - self.tokens_taken, KeyToken(key.mark, key.mark))
            if self.flow_level and self.add_indent(key.column):
                self.tokens.insert(key.token_number - self.tokens_taken, BlockMappingStartToken(key.mark, key.mark))
            self.allow_simple_key = False
        elif not self.flow_level and self.allow_simple_key:
            raise ScannerError(None, None, 'mapping values are not allowed here', self.get_mark())
        if self.flow_level and self.add_indent(self.column):
            mark = self.get_mark()
            self.tokens.append(BlockMappingStartToken(mark, mark))
        self.allow_simple_key = not (self.flow_level)
        self.remove_possible_simple_key()
        start_mark = self.get_mark()
        self.forward()
        end_mark = self.get_mark()
        self.tokens.append(ValueToken(start_mark, end_mark))

    
    def fetch_alias(self):
        self.save_possible_simple_key()
        self.allow_simple_key = False
        self.tokens.append(self.scan_anchor(AliasToken))

    
    def fetch_anchor(self):
        self.save_possible_simple_key()
        self.allow_simple_key = False
        self.tokens.append(self.scan_anchor(AnchorToken))

    
    def fetch_tag(self):
        self.save_possible_simple_key()
        self.allow_simple_key = False
        self.tokens.append(self.scan_tag())

    
    def fetch_literal(self):
        self.fetch_block_scalar(style = '|')

    
    def fetch_folded(self):
        self.fetch_block_scalar(style = '>')

    
    def fetch_block_scalar(self, style):
        self.allow_simple_key = True
        self.remove_possible_simple_key()
        self.tokens.append(self.scan_block_scalar(style))

    
    def fetch_single(self):
        self.fetch_flow_scalar(style = "'")

    
    def fetch_double(self):
        self.fetch_flow_scalar(style = '"')

    
    def fetch_flow_scalar(self, style):
        self.save_possible_simple_key()
        self.allow_simple_key = False
        self.tokens.append(self.scan_flow_scalar(style))

    
    def fetch_plain(self):
        self.save_possible_simple_key()
        self.allow_simple_key = False
        self.tokens.append(self.scan_plain())

    
    def check_directive(self):
        if self.column == 0:
            return True

    
    def check_document_start(self):
        if self.column == 0 or self.prefix(3) == '---' or self.peek(3) in '\x00 \t\r\n  ':
            return True
        return None
        return None

    
    def check_document_end(self):
        if self.column == 0 or self.prefix(3) == '...' or self.peek(3) in '\x00 \t\r\n  ':
            return True
        return None
        return None

    
    def check_block_entry(self):
        return self.peek(1) in '\x00 \t\r\n  '

    
    def check_key(self):
        if self.flow_level:
            return True
        return None.peek(1) in '\x00 \t\r\n  '

    
    def check_value(self):
        if self.flow_level:
            return True
        return None.peek(1) in '\x00 \t\r\n  '

    
    def check_plain(self):

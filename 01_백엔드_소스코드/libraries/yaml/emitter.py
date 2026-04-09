# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: emitter.pyc (Python 3.11)

__all__ = [
    'Emitter',
    'EmitterError']
from error import YAMLError
from events import *

class EmitterError(YAMLError):
    pass


class ScalarAnalysis:
    
    def __init__(self, scalar, empty, multiline, allow_flow_plain, allow_block_plain, allow_single_quoted, allow_double_quoted, allow_block):
        self.scalar = scalar
        self.empty = empty
        self.multiline = multiline
        self.allow_flow_plain = allow_flow_plain
        self.allow_block_plain = allow_block_plain
        self.allow_single_quoted = allow_single_quoted
        self.allow_double_quoted = allow_double_quoted
        self.allow_block = allow_block



class Emitter:
    DEFAULT_TAG_PREFIXES = {
        '!': '!',
        'tag:yaml.org,2002:': '!!' }
    
    def __init__(self, stream, canonical, indent, width, allow_unicode, line_break = (None, None, None, None, None)):
        self.stream = stream
        self.encoding = None
        self.states = []
        self.state = self.expect_stream_start
        self.events = []
        self.event = None
        self.indents = []
        self.indent = None
        self.flow_level = 0
        self.root_context = False
        self.sequence_context = False
        self.mapping_context = False
        self.simple_key_context = False
        self.line = 0
        self.column = 0
        self.whitespace = True
        self.indention = True
        self.open_ended = False
        self.canonical = canonical
        self.allow_unicode = allow_unicode
        self.best_indent = 2
        80 = None if indent else indent
        if width and width > self.best_indent * 2:
            self.best_width = width
        self.best_line_break = '\n'
        if line_break in ('\r', '\n', '\r\n'):
            self.best_line_break = line_break
        self.tag_prefixes = None
        self.prepared_anchor = None
        self.prepared_tag = None
        self.analysis = None
        self.style = None

    
    def dispose(self):
        self.states = []
        self.state = None

    
    def emit(self, event):
        self.events.append(event)
    # WARNING: Decompyle incomplete

    
    def need_more_events(self):
        if not self.events:
            return True
        event = None.events[0]
        if isinstance(event, DocumentStartEvent):
            return self.need_events(1)
        if None(event, SequenceStartEvent):
            return self.need_events(2)
        if None(event, MappingStartEvent):
            return self.need_events(3)

    
    def need_events(self, count):
        level = 0
        for event in self.events[1:]:
            if isinstance(event, (DocumentStartEvent, CollectionStartEvent)):
                level += 1
            elif isinstance(event, (DocumentEndEvent, CollectionEndEvent)):
                level -= 1
            elif isinstance(event, StreamEndEvent):
                level = -1
            if level < 0:
                return False
            return len(self.events) < count + 1

    
    def increase_indent(self, flow, indentless = (False, False)):
        self.indents.append(self.indent)
    # WARNING: Decompyle incomplete

    
    def expect_stream_start(self):
        if isinstance(self.event, StreamStartEvent):
            if not self.event.encoding and hasattr(self.stream, 'encoding'):
                self.encoding = self.event.encoding
            self.write_stream_start()
            self.state = self.expect_first_document_start
            return None
        raise None('expected StreamStartEvent, but got %s' % self.event)

    
    def expect_nothing(self):
        raise EmitterError('expected nothing, but got %s' % self.event)

    
    def expect_first_document_start(self):
        return self.expect_document_start(first = True)

    
    def expect_document_start(self, first = (False,)):
        if isinstance(self.event, DocumentStartEvent):
            if (self.event.version or self.event.tags) and self.open_ended:
                self.write_indicator('...', True)
                self.write_indent()
            if self.event.version:
                version_text = self.prepare_version(self.event.version)
                self.write_version_directive(version_text)
            self.tag_prefixes = self.DEFAULT_TAG_PREFIXES.copy()
            if self.event.tags:
                handles = sorted(self.event.tags.keys())
                for handle in handles:
                    prefix = self.event.tags[handle]
                    self.tag_prefixes[prefix] = handle
                    handle_text = self.prepare_tag_handle(handle)
                    prefix_text = self.prepare_tag_prefix(prefix)
                    self.write_tag_directive(handle_text, prefix_text)
                    if first:
                        if not (self.event.explicit):
                            if not (self.canonical):
                                if not (self.event.version):
                                    if not (self.event.tags):
                                        implicit = not self.check_empty_document()
                                        if not implicit:
                                            self.write_indent()
                                            self.write_indicator('---', True)
                                            if self.canonical:
                                                self.write_indent()
            self.state = self.expect_document_root
            return None
        if isinstance(self.event, StreamEndEvent):
            if self.open_ended:
                self.write_indicator('...', True)
                self.write_indent()
            self.write_stream_end()
            self.state = self.expect_nothing
            return None
        raise None('expected DocumentStartEvent, but got %s' % self.event)

    
    def expect_document_end(self):
        if isinstance(self.event, DocumentEndEvent):
            self.write_indent()
            if self.event.explicit:
                self.write_indicator('...', True)
                self.write_indent()
            self.flush_stream()
            self.state = self.expect_document_start
            return None
        raise None('expected DocumentEndEvent, but got %s' % self.event)

    
    def expect_document_root(self):
        self.states.append(self.expect_document_end)
        self.expect_node(root = True)

    
    def expect_node(self, root, sequence, mapping, simple_key = (False, False, False, False)):
        self.root_context = root
        self.sequence_context = sequence
        self.mapping_context = mapping
        self.simple_key_context = simple_key
        if isinstance(self.event, AliasEvent):
            self.expect_alias()
            return None
        if None(self.event, (ScalarEvent, CollectionStartEvent)):
            self.process_anchor('&')
            self.process_tag()
            if isinstance(self.event, ScalarEvent):
                self.expect_scalar()
                return None
            if None(self.event, SequenceStartEvent):
                if self.flow_level and self.canonical and self.event.flow_style or self.check_empty_sequence():
                    self.expect_flow_sequence()
                    return None
                None.expect_block_sequence()
                return None
            if None(self.event, MappingStartEvent):
                if self.flow_level and self.canonical and self.event.flow_style or self.check_empty_mapping():
                    self.expect_flow_mapping()
                    return None
                None.expect_block_mapping()
                return None
            return None
        raise None('expected NodeEvent, but got %s' % self.event)

    
    def expect_alias(self):
        pass
    # WARNING: Decompyle incomplete

    
    def expect_scalar(self):
        self.increase_indent(flow = True)
        self.process_scalar()
        self.indent = self.indents.pop()
        self.state = self.states.pop()

    
    def expect_flow_sequence(self):
        self.write_indicator('[', True, whitespace = True)
        self.increase_indent(flow = True)
        self.expect_first_flow_sequence_item = self, self.flow_level += 1, .flow_level

    
    def expect_first_flow_sequence_item(self):
        if isinstance(self.event, SequenceEndEvent):
            self.indent = self.indents.pop()
            self.write_indicator(']', False)
            self.states.pop() = self, self.flow_level -= 1, .flow_level
            return None
        if None.canonical or self.column > self.best_width:
            self.write_indent()
        self.states.append(self.expect_flow_sequence_item)
        self.expect_node(sequence = True)

    
    def expect_flow_sequence_item(self):
        if isinstance(self.event, SequenceEndEvent):
            self.indent = self.indents.pop()
            if self.canonical:
                self.write_indicator(',', False)
                self.write_indent()
            self.write_indicator(']', False)
            self.states.pop() = self, self.flow_level -= 1, .flow_level
            return None
        None.write_indicator(',', False)
        if self.canonical or self.column > self.best_width:
            self.write_indent()
        self.states.append(self.expect_flow_sequence_item)
        self.expect_node(sequence = True)

    
    def expect_flow_mapping(self):
        self.write_indicator('{', True, whitespace = True)
        self.increase_indent(flow = True)
        self.expect_first_flow_mapping_key = self, self.flow_level += 1, .flow_level

    
    def expect_first_flow_mapping_key(self):
        if isinstance(self.event, MappingEndEvent):
            self.indent = self.indents.pop()
            self.write_indicator('}', False)
            self.states.pop() = self, self.flow_level -= 1, .flow_level
            return None
        if None.canonical or self.column > self.best_width:
            self.write_indent()
        if self.canonical and self.check_simple_key():
            self.states.append(self.expect_flow_mapping_simple_value)
            self.expect_node(mapping = True, simple_key = True)
            return None
        None.write_indicator('?', True)
        self.states.append(self.expect_flow_mapping_value)
        self.expect_node(mapping = True)

    
    def expect_flow_mapping_key(self):
        if isinstance(self.event, MappingEndEvent):
            self.indent = self.indents.pop()
            if self.canonical:
                self.write_indicator(',', False)
                self.write_indent()
            self.write_indicator('}', False)
            self.states.pop() = self, self.flow_level -= 1, .flow_level
            return None
        None.write_indicator(',', False)
        if self.canonical or self.column > self.best_width:
            self.write_indent()
        if self.canonical and self.check_simple_key():
            self.states.append(self.expect_flow_mapping_simple_value)
            self.expect_node(mapping = True, simple_key = True)
            return None
        None.write_indicator('?', True)
        self.states.append(self.expect_flow_mapping_value)
        self.expect_node(mapping = True)

    
    def expect_flow_mapping_simple_value(self):
        self.write_indicator(':', False)
        self.states.append(self.expect_flow_mapping_key)
        self.expect_node(mapping = True)

    
    def expect_flow_mapping_value(self):
        if self.canonical or self.column > self.best_width:
            self.write_indent()
        self.write_indicator(':', True)
        self.states.append(self.expect_flow_mapping_key)
        self.expect_node(mapping = True)

    
    def expect_block_sequence(self):
